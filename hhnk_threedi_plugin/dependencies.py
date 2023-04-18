"""

@author: Wietse Gerwen & Daniel Tollenaar

Current requirements:
    - QGIS version must be 3.22
    - ThreeDiToolbox properly installed (for threedigrid and other deps).


How ensure_dependencies works:
    1. Adding ThreeDiToolbox.deps and hhnk_threedi_plugin.external-dependencies
       to path, so all installed modules can be found
    2. Checking if the current Python-environment includes all packages with
       versions as specified in hhnk_threedi_plugin.env.environment.yml
    3. If Python and/or package versions in current environment do not match
       hhnk_threedi_plugin.env.environment.yml, warn the user if this
       inconsistencies
    4. Installing all missing packages


Functions are heavily inspired by/ copied from:
    https://github.com/nens/ThreeDiToolbox/blob/master/dependencies.py
"""

import os
import sys
import pkg_resources
import logging
import subprocess
from pathlib import Path
import platform
import importlib
from collections import namedtuple
import yaml
from typing import List
from platform import python_version
import shutil

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressDialog
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox


CREATE_NO_WINDOW = 0x08000000
DETACHED_PROCESS = 0x00000008

# Globals
OUR_DIR = Path(__file__).parent
DEPENDENCY_DIR = OUR_DIR / "external-dependencies"
DEPENDENCY_DIR.mkdir(parents=True, exist_ok=True)
THREEDI_DEPENDENCY_DIR = OUR_DIR.parent / "ThreeDiToolbox" / "deps"

WHEEL_DIR = OUR_DIR / "wheels"
WHEEL_DIR.mkdir(parents=True, exist_ok=True)

YML_PATH = OUR_DIR.joinpath("env", "environment.yml")

LOG_DIR = OUR_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

PATCH_DIR = OUR_DIR / "patches"
PATCHES = {}

Dependency = namedtuple("Dependency", ["package", "version"])


# add logging + filehandler so we can log what we are doing
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


inconsist_deps_message = f"""
Installatie hhnk_threedi_plugin
<br><br>
De volgende depencendies in deze QGIS python-environment zijn niet compatible met geteste plugin environment: 
<br>
{{msg}}
<br><br>
Verwijder deze packages, of update de <a href='file:{YML_PATH}'>environment.yml</a> om deze melding te laten verdwijnen.
<br>
En test de plugin voor deze omgeving wanneer je de environment.yml update(!)
""" # noqa: E501

""" Helper functions for QGIS QProgressDialog and  QMessageBox """


restart_message = """
Installatie hhnk_threedi_plugin dependencies is voltooid.

Let op (!): QGIS herstarten om geinstalleerde modules te her-activeren.
"""


def _get_python_interpreter():
    """Return the path to the python3 interpreter.

    Under linux sys.executable is set to the python3 interpreter used by Qgis.
    However, under Windows/Mac this is not the case and sys.executable refers
    to the Qgis start-up script.
    """
    interpreter = None
    executable = sys.executable
    directory, _ = os.path.split(executable)
    if _is_windows():
        interpreter = os.path.join(directory, "python3.exe")
    elif platform.system().lower() == "darwin":
        interpreter = os.path.join(directory, "bin", "python3")
    else:
        interpreter = executable

    assert os.path.exists(interpreter)  # safety check
    return interpreter


def _is_windows():
    """Return whether we are starting from QGIS on Windows."""
    executable = sys.executable
    _, filename = os.path.split(executable)
    if "python3" in filename.lower():
        return False
    elif "qgis" in filename.lower():
        if platform.system().lower() == "darwin":
            return False
        else:
            return True


def _is_qgis():
    return any(
        (i in _get_python_interpreter().lower() for i in ["qgis", "3di"])
        )


def _create_progress_dialog(missing_dependencies, qgis=_is_qgis()):
    """Create a process dialog."""
    if _is_windows() and qgis:
        label = f"Start installatie: {len(missing_dependencies)} packages"
        dialog = QProgressDialog()
        dialog.setWindowTitle("HHNK 3Di plugin installatie")
        dialog.setLabelText(label)
        dialog.setWindowFlags(Qt.WindowStaysOnTopHint)
        bar = QProgressBar(dialog)
        bar.setTextVisible(True)
        bar.setValue(0)
        bar.setMaximum(100)
        dialog.setBar(bar)
        dialog.setMinimumWidth(500)
        dialog.update()
        dialog.setCancelButton(None)
        dialog.show()
        QApplication.processEvents()
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    else:
        dialog, bar, startupinfo = None, None, None
    return dialog, bar, startupinfo


def _update_dialog(dialog, dependency, qgis=_is_qgis()):
    """Update the label of the dialog."""
    if dialog and qgis:
        dialog.setLabelText(f"Installeren: {dependency.package}")
        QApplication.processEvents()


def _update_bar(bar, count, total, qgis=_is_qgis()):
    """Update the progress bar of the dialog."""
    if bar and qgis:
        bar.setValue(int((count / total) * 100))
        bar.update()
        QApplication.processEvents()


def _raise_inconsistency_warning(
    correct_python_version, inconsistent_dependencies, qgis=_is_qgis()
):
    """Raise an inconsistency warning if environment is not compatible with yml.""" # noqa: E501s

    msg = ""
    if not correct_python_version:
        msg = f"- python=={python_version()}<br>"

    msg += "<br>".join(
        [f"- {i.package}=={i.version} ({_package_location(i)})" for i in inconsistent_dependencies]
    )

    if msg:
        msg = inconsist_deps_message.format(msg=msg)
        logger.warning(msg)

        if qgis:
            msg_box = QMessageBox()
            msg_box.setTextFormat(Qt.RichText)
            msg_box.setWindowTitle("Inconsistente Python environment")
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText(msg)
            msg_box.setFixedWidth(1000)
            msg_box.exec_()

def _raise_restart_warning(qgis=_is_qgis()):
    """Raise restart warning after installation."""
    if qgis:
        QMessageBox.information(None, "Warning", restart_message)


""" Helper functions for logging file-handler."""


def _add_logger_file_handler(log_file=LOG_DIR / "ensure_dependencies.log"):
    """Add a logger file_handler."""
    fh = logging.FileHandler(log_file)
    fh.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
    )
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    return fh


def _remove_logger_file_handler(fh):
    """Remove a logger file_handler."""
    logger.removeHandler(fh)
    fh.close()


""" Helper functions for checking environment to environment.yml."""


def _yaml_to_dependencies(yaml_path: Path = YML_PATH) -> List[Dependency]:
    """
    Function to read the dependencies from an environment.yml path

    Args:
        yaml_path (Path): Path to the environment.yml file

    Returns:
        Dependency, List[Dependency]: Python version or List of dependencies

    """

    environment = yaml.safe_load(Path(yaml_path).read_text())
    deps = []
    python_dep = None

    # Extract package names and versions
    dependencies = environment.get("dependencies", [])
    for dependency in dependencies:
        if isinstance(dependency, str):
            # Extract package name from string
            splitted_dependency = dependency.lower().split("=")
            name = splitted_dependency[0]
            if len(splitted_dependency) > 1:
                version = splitted_dependency[1]
            else:
                version = None
            if name == "python":
                python_dep = Dependency(name, version)
            else:
                deps.append(Dependency(name, version))
        elif isinstance(dependency, dict):
            if "pip" in dependency.keys():
                for pip_dependency in dependency["pip"]:
                    splitted_dependency = pip_dependency.lower().split("==")
                    name = splitted_dependency[0]
                    if len(splitted_dependency) > 1:
                        version = splitted_dependency[1]
                    else:
                        version = None
                    deps.append(Dependency(name, version))

    return python_dep, deps


def _update_path(directories):
    """update path with directories."""
    for dir_path in directories:
        dir_path = Path(dir_path)
        if dir_path.exists():
            if str(dir_path) not in sys.path:
                sys.path.insert(0, str(dir_path))
                logger.info(f"{dir_path} added to sys.path")
        else:
            logger.warning(
                f"{dir_path} does not exist and is not added to sys.path"
                )
#%%
def _package_location(dependency):
    try:
        pkg = pkg_resources.get_distribution(dependency.package)
        location = Path(pkg.location) / dependency.package
        return f"<a href='file:{location.as_posix()}'>{location.as_posix()}</a>"
    except pkg_resources.DistributionNotFound:
        pass
#%%    

def _evaluate_environment(yml_path: Path = YML_PATH):
    """
    Evaluates run-environment to an environment.yml

    Args:
        yml_path (Path, optional): Path to the environment.yml.
        Defaults to YML_PATH.

    Returns:
        correct_python_version (bool): Python version matches environment
        inconsistent_dependencies (list[Dependency]): List of dependencies in
        environment with inconsistent version
        missing_dependencies (list[Dependency]): List of missing dependencies in
        environment

    """

    missing_dependencies = []
    inconsistent_dependencies = []

    python_dep, dependencies = _yaml_to_dependencies(yml_path)

    if python_dep is None:
        correct_python_version = True
    else:
        correct_python_version = python_dep.version == python_version()

    for dependency in dependencies:
        try:
            pkg = pkg_resources.get_distribution(dependency.package)
            if dependency.version is not None:
                if pkg.version != dependency.version:
                    inconsistent_dependencies.append(
                        Dependency(dependency.package, pkg.version)
                    )
        except pkg_resources.DistributionNotFound:
            missing_dependencies.append(dependency)

    return (
        correct_python_version,
        inconsistent_dependencies,
        missing_dependencies
        )


""" Installation of patches. Note (!) try to avoid patches!"""


def _install_patches(patches: dict = PATCHES, patch_dir: Path = PATCH_DIR):
    """
    Install patches in the QGIS environment to fix errors in (threedi) modules.

    Note (!) patches are not permanent fixes (!); please report issues in GitHub

    Args:
        patches (dict, optional): dictionary with patches in the form
          {file.ext:path/to/destination/file.ext}. Defaults to PATCHES.
        patch_dir (Path, optional): directory with path-files to be read.
        Defaults to PATCH_DIR.

    Returns:
        None.

    """
    for source, target in patches.items():
        source = patch_dir / source
        target = target
        if all((source.exists(), target.exists())):
            if not (source.read_bytes() == target.read_bytes()):
                logger.info(f"patching {target} with {source}")
                target.write_text(source.read_text())


""" Helper functions on maintaining the wheel directory """


def _delete_directory(directory, mkdir=True):
    directory = Path(directory)
    try:
        if directory.exists():
            shutil.rmtree(directory)
    except PermissionError:
        logger.warning(f"Failed to remove {directory}")

    if mkdir:
        directory.mkdir(parents=True, exist_ok=True)


def download_wheels(dependencies, directory=WHEEL_DIR, clean_dir=True):
    """Download the wheels into the wheel directory"""

    if clean_dir:
        _delete_directory(directory, mkdir=True)

    for dependency in dependencies:
        command = [
            _get_python_interpreter(),
            "-m",
            "pip",
            "download",
            "-d",
            str(directory),
        ]
        command.extend([f"{dependency.package}=={dependency.version}"])
        process = subprocess.Popen(command)
        output, error = process.communicate()
        exit_code = process.wait()
        if exit_code:
            logger.error(
                f"Downloading {dependency.package} failed with: {error} {output}" # noqa: E501
            )


""" Helper functions to install missing dependencies. """


def _refresh_python_import_mechanism():
    """Refresh the import mechanism.
    This is required when deps are dynamically installed/removed. The modules
    'importlib' and 'pkg_resources' need to update their internal data structures. 
    """ # noqa: E501
    # This function should be called if any modules are created/installed while your # noqa: E501
    # program is running to guarantee all finders will notice the new module’s existence. # noqa: E501
    importlib.invalidate_caches()

    # https://stackoverflow.com/questions/58612272/pkg-resources-get-distributionmymodule-version-not-updated-after-reload
    # Apparantely pkg_resources needs to be reloaded to be up-to-date with newly installed packages # noqa: E501
    importlib.reload(pkg_resources)


def _install_dependency(
        dependency: Dependency,
        dialog=None,
        startupinfo=None,
        fh=None
        ):
    """Install a dependency with pip"""

    command = [
        _get_python_interpreter(),
        "-m",
        "pip",
        "install",
        "--find-links",
        str(WHEEL_DIR),
    ]

    # if jupyter, we go for a full install in user-directory
    if dependency.package == "jupyter":
        command.extend(
            [
                "--user",
                "--upgrade",
                "--force-reinstall",
                "--no-cache-dir",
                "--no-warn-script-location",
            ]
        )
    else:  # if not we install it in the DEPENCENDY_DIR and ignore dependencies
        command.extend(["--target", str(DEPENDENCY_DIR), "--no-deps"])

    if dependency.version:
        command.extend([f"{dependency.package}=={dependency.version}"])
    else:
        command.extend([f"{dependency.package}"])

    logger.info(f"executing command {' '.join(command)}")
    process = subprocess.Popen(
        command,
        universal_newlines=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        startupinfo=startupinfo,
    )

    # The input/output/error stream handling is a bit involved, but it is
    # necessary because of a python bug on windows 7, see
    # https://bugs.python.org/issue3905 .
    i, o, e = (process.stdin, process.stdout, process.stderr)
    i.close()
    result = o.read() + e.read()
    o.close()
    e.close()
    exit_code = process.wait()

    if exit_code:
        try:  # if we can import the package now, we ignore the exit-code
            _refresh_python_import_mechanism()
            pkg_resources.get_distribution(dependency.package)
        except pkg_resources.DistributionNotFound as e:
            msg = f"""
            Installeren {dependency.package} is gefaald met error code: {exit_code} 

            Uitgevoerde command-line: {" ".join(command)}

            Resulterende command-logging: {result}

            Python-exception na import: {e}

            """ # noqa: E501

            logger.error(msg)

            if dialog:
                dialog.close()
            if fh:
                _remove_logger_file_handler(fh)

            raise RuntimeError(msg)


def _uninstall_dependency(dependency, startupinfo=None):
    """Uninstall a dependency with pip"""
    command = [
        _get_python_interpreter(),
        "-m",
        "pip",
        "uninstall",
        "--yes",
        (dependency.package)
        ]
    process = subprocess.Popen(
        command,
        universal_newlines=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        startupinfo=startupinfo,
    )
    # The input/output/error stream handling is a bit involved, but it is
    # necessary because of a python bug on windows 7, see
    # https://bugs.python.org/issue3905 .
    i, o, e = (process.stdin, process.stdout, process.stderr)
    i.close()
    o.close()
    e.close()
    exit_code = process.wait()
    if exit_code:
        logger.error(f"uninstalling package failed!: {dependency.package}")


def _clean_inconsistent_dependencies(inconsistent_dependencies, missing_dependencies):
    """Uninstall inconsistent_dependencies if installed in DEPENDENCY_DIR.
    If successfully uninstalled dependency will be added to missing_dependencies."""
    for dependency in inconsistent_dependencies:
        pkg = pkg_resources.get_distribution(dependency.package)
        if DEPENDENCY_DIR == Path(pkg.location):
            logger.info(f"uninstalling package: {dependency.package}")
            _uninstall_dependency(dependency)
            try:
                pkg = pkg_resources.get_distribution(dependency.package)
            except pkg_resources.DistributionNotFound:
                inconsistent_dependencies.pop(dependency)
                missing_dependencies.append(dependency)

    return inconsistent_dependencies, missing_dependencies


def ensure_dependencies(
    threedi_dependency_dir=THREEDI_DEPENDENCY_DIR,
    dependency_dir=DEPENDENCY_DIR,
    yml_path=YML_PATH,
):
    """
    Ensures all dependencies are installed

    Args:
        threedi_dependency_dir (Path, optional): Path to 3Di Toolbox dependencies
            dir Defaults to THREEDI_DEPENCENDCY_DIR.
        dependency_dir (Path, optional): path to hhnk_threedi_plugin dependencies
            dir Defaults to DEPENDENCY_DIR.
        yml_path (Path, optional): Path to environment.yml Defaults to YML_PATH.

    """ # noqa: E501
    # add log-file
    fh = _add_logger_file_handler()

    logger.info("start: ensuring dependencies")

    logger.info(
        f"python-interpreter {_get_python_interpreter()} is QGIS: {_is_qgis()}"
        )

    # make sure all currently installed modules are patched if necessary
    _install_patches()

    logger.info("adding paths")
    # add paths to dependency-dirs
    _update_path([threedi_dependency_dir, dependency_dir])
    logger.info(f"sys.path: {','.join(sys.path)}")

    # make sure all packages in path can be found
    _refresh_python_import_mechanism()

    logger.info("evaluating environment")
    # check if all is consistent and what is missing
    (
        correct_python_version,
        inconsistent_dependencies,
        missing_dependencies,
    ) = _evaluate_environment(yml_path)

    # try uninstalling inconsistent dependencies
    inconsistent_dependencies, missing_dependencies = _clean_inconsistent_dependencies(
        inconsistent_dependencies,
        missing_dependencies
        )

    # raise an inconsistency warning if environment is not consistent with tested plugin environment # noqa: E501
    if (not correct_python_version) or (inconsistent_dependencies):
        _raise_inconsistency_warning(
            correct_python_version,
            inconsistent_dependencies
            )

    if missing_dependencies:
        logger.info(
            f"missing dependencies: {' '.join([i.package for i in missing_dependencies])}" # noqa: E501
        )
        # create a QGIS progress dialog (if Windows)
        dialog, bar, startupinfo = _create_progress_dialog(
            missing_dependencies
            )

        # loop trough missing dependencies
        for count, dependency in enumerate(missing_dependencies):

            # update dialog label
            _update_dialog(dialog, dependency)

            # install dependency
            logger.info(f"installing: {dependency.package}")
            _install_dependency(
                dependency, startupinfo=startupinfo, dialog=dialog, fh=fh
            )

            # update progress bar
            _update_bar(bar, count, len(missing_dependencies))

        # make all modules available for import
        _refresh_python_import_mechanism()

        # close dialog
        if dialog:
            dialog.close()

        # restart warning: just to be sure...
        _raise_restart_warning()

    # make sure all newly installed modules are patched if necessary
    _install_patches()

    # remove log-file
    _remove_logger_file_handler(fh)


if __name__ == "__main__":
    ensure_dependencies()

# -*- coding: utf-8 -*-
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
       hhnk_threedi_plugin.env.environment.yml, enabling user to update
       hhnk_threedi_plugin.env.environment.yml to current environment
    4. Installing all missing packages

"""

import os
import sys
import pkg_resources
import logging
import subprocess
from pathlib import Path
import platform
from collections import namedtuple
import yaml
from typing import List
from platform import python_version

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
DEPENDENCY_DIR = str(DEPENDENCY_DIR)
THREEDI_DEPENCENDCY_DIR = OUR_DIR / "ThreeDiToolbox" / "deps"

WHEEL_DIR = OUR_DIR / "wheels"
WHEEL_DIR = str(WHEEL_DIR)
REQUIREMENTS_PATH = f"{WHEEL_DIR}/requirements.txt"

YML_PATH = OUR_DIR.joinpath("env", "environment.yml")

LOG_DIR = OUR_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

PATCH_DIR = OUR_DIR / "patches"
PATCHES = {"custom_types.py": THREEDI_DEPENCENDCY_DIR.joinpath("threedi_schema//domain//custom_types.py")}

Dependency = namedtuple("Dependency", ["package", "version"])


# add logging + filehandler so we can log what we are doing
logger = logging.getLogger(__name__)

# inconsistent_environment ="""Huidige python-omgeving is niet"""

""" Helper functions for QGIS QProgressDialog """


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


def _create_progress_dialog(missing_dependencies, qgis=True):
    """Create a process dialog."""
    if _is_windows() and qgis:
        missing_dependencies = " ".join(
            [i.package for i in missing_dependencies]
            )
        label = f"Start installatie: {missing_dependencies}"
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


def _update_dialog(dialog, dependency, qgis=True):
    """Update the label of the dialog."""
    if dialog and qgis:
        dialog.setLabelText(f"Installeren: {dependency.name}")
        QApplication.processEvents()


def _update_bar(bar, count, total, qgis=True):
    """Update the progress bar of the dialog."""
    if bar and qgis:
        bar.setValue(int((count / total) * 100))
        bar.update()
        QApplication.processEvents()

# def _update_environment_yml(correct_python_version, inconsistent_dependencies, qgis=True):
#     if not correct_python_version:
#         inconsistent_dependencies.insert(0, Dependency("python",python_version()))

#     if qgis:
#         msg = f"""De QGIS environment is niet consistent met de environment in 
#         {"\n".join([f"{i.package}=={i.version}" for i in inconsistent_dependencies])
        
        
#         """
#         QMessageBox.information(None,
#                                 "Warning"
#                                 msg)

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
                        Dependency(
                            dependency.package,
                            pkg.version)
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


""" Helper functions to install missing dependencies. """


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


def _install_dependency(dependency: Dependency, dialog=None, startupinfo=None, fh=None):
    """install pip in the main directory of qgis"""

    command = [_get_python_interpreter(), "-m", "pip", "install"]

    # if jupyter, we go for a full install in user-directory
    if dependency.package == "jupyter":
        command.extend(
            ["--user",
             "--upgrade",
             "--force-reinstall",
             "--no-cache-dir",
             "--no-warn-script-location"]
            )
    else:  # if not we install it in the DEPENCENDY_DIR and ignore dependencies
        command.extend(["--target", str(DEPENDENCY_DIR), "--no-deps"])

    if dependency.version:
        command.extend(f"{dependency.package}=={dependency.version}")
    else:
        command.extend("dependency.package")

    command.extend([dependency.package + dependency.constraint])

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
        try:
            pkg_resources.get_distribution(dependency.package)
        except pkg_resources.DistributionNotFound as e:
            msg = f"""
            Installeren {dependency.name} is gefaald met error code: {exit_code}

            Uitgevoerde command-line: {" ".join(command)}

            Resulterende command-logging: {result}

            Python-exception na import: {e}

            """

            logger.error(msg)

            if dialog:
                dialog.close()
            if fh:
                _remove_logger_file_handler(fh)

            raise RuntimeError(msg)


def ensure_dependencies(
        threedi_dependency_dir=THREEDI_DEPENCENDCY_DIR,
        dependency_dir=DEPENDENCY_DIR,
        yml_path=YML_PATH):
    """
    Ensures all dependencies are installed

    Args:
        threedi_dependency_dir (Path, optional): Path to 3Di Toolbox dependencies
            dir Defaults to THREEDI_DEPENCENDCY_DIR.
        dependency_dir (Path, optional): path to hhnk_threedi_plugin dependencies
            dir Defaults to DEPENDENCY_DIR.
        yml_path (Path, optional): Path to environment.yml Defaults to YML_PATH.

    """
    # add log-file
    fh = _add_logger_file_handler()

    # make sure all packages can be found
    for dir_path in (threedi_dependency_dir, dependency_dir):
        if dir_path.exists():
            if str(dir_path) not in sys.path:
                sys.path.insert(0, str(dir_path))
            logger.info(f"{dir_path} added to sys.path")
        else:
            logger.warning(f"{dir_path} does not exist and is not added to sys.path")
    
    # make sure all currently installed modules are patched if necessary
    _install_patches()
    
    logger.info("evaluating environment")
    correct_python_version, inconsistent_dependencies, missing_dependencies = _evaluate_environment(yml_path)
    
    if missing_dependencies:
        logger.info(
            f"missing dependencies: {' '.join([i.package for i in missing_dependencies])}"
            )
        # create a QGIS progress dialog (if Windows)
        dialog, bar, startupinfo = _create_progress_dialog(missing_dependencies)
    
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

    #close dialog
    if dialog:
        dialog.close()

    # make sure all newly installed modules are patched if necessary
    _install_patches()

    # remove log-file
    _remove_logger_file_handler(fh)


if __name__ == "__main__":
    ensure_dependencies()

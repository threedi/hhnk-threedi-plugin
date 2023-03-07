# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:19:30 2021

@author: chris.kerklaan

Current requirements:
    - The 3Di toolbox must be installed (for threedigrid and other deps).
    - QGIS version must be 3.22

How these dependencies are made:
    - Geopandas
    First the osgeo installer is used to copy the main dependencies of
    geopandas (wheels/geopandas). They are copied to external-dependencies.
    Geopandas 0.8.2 must be used (instead of 0.8.1.) for reading excel sheets.
    
    - Jupyter (flexible)
    Jupyter is installed in 'user' (roaming/python) due to constraints on
    the hhnk servers.
    
    - hhnk_research_tools / hhnk_threedi_tools 
    These deps are made flexible and are thus downloaded from the internet.
    Therefore we can change the version very simply here in the script.
    
    
    - Other
    All other dependencies are installed via wheels (/wheels/requirements.txt)
    in the external-dependencies folder.
    
    
All dependencies are installed and reloaded. The external-dependencies path is 
put at the top of sys.path so this is the first path that will be seen by
python.

"""

import os
import sys
import site
import shutil
import pkg_resources
import importlib
import logging
import subprocess
from pathlib import Path
import platform
from collections import namedtuple
import yaml
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressDialog
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QApplication


CREATE_NO_WINDOW = 0x08000000
DETACHED_PROCESS = 0x00000008

# Globals
OUR_DIR = Path(__file__).parent
DEPENDENCY_DIR = OUR_DIR / "external-dependencies"
DEPENDENCY_DIR.mkdir(parents=True, exist_ok=True)
DEPENDENCY_DIR = str(DEPENDENCY_DIR)

WHEEL_DIR = OUR_DIR / "wheels"
WHEEL_DIR = str(WHEEL_DIR)
REQUIREMENTS_PATH = f"{WHEEL_DIR}/requirements.txt"

YML_PATH = OUR_DIR / "environment.yml"

LOG_DIR = OUR_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

PATCH_DIR = OUR_DIR / "patches"

# list of depencies
""" folder can be set to "external-dependencies" to insstall in th plugin folder, it is loaded incorrectly 
the first time you update the plugin
"""

Dependency = namedtuple(
    "Dependency",
    [
        "name",
        "package",
        "version",
        "constraint",
        "no_dependecies",
        "folder",
        "enforce_version",
    ],
)

FLEXIBLE_DEPENDENCIES = [
    Dependency("jupyter", "jupyter", "1.0.0", "==1.0.0", False, "user", False),
    Dependency(
        "hhnk_research_tools",
        "hhnk_research_tools",
        "2023.1",
        "==2023.1",
        True,
        "external-dependencies",
        True,
    ),
    Dependency(
        "hhnk_threedi_tools",
        "hhnk_threedi_tools",
        "2023.1",
        "==2023.1",
        True,
        "external-dependencies",
        True,
    ),
    Dependency(
        "threedi_scenario_downloader",
        "threedi_scenario_downloader",
        "0.16",
        "==0.16",
        True,
        "external-dependencies",
        True,
    ),
    Dependency(
        "threedi_raster_edits",
        "threedi_raster_edits",
        "0.26",
        "==0.26",
        True,
        "external-dependencies",
        True,
    ),
    Dependency(
        "threedi-api-client",
        "threedi-api-client",
        "4.1.1",
        "==4.1.1",
        True,
        "external-dependencies",
        True,
    ),
]

package_module_map = {"python_dateutil": "dateutil",
                      "gdal": "osgeo",
                      "threedi-api-client": "threedi_api_client"}

patches = {"custom_types.py": r"threedi_schema//domain//custom_types.py"}

# add logging + filehandler so we can log what we are doing
logger = logging.getLogger(__name__)


def install_patches():
    deps_dir = _dependencies_target_dir()
    for source, target in patches.items():
        source = PATCH_DIR / source
        target = deps_dir / target
        if all((source.exists(), target.exists())):
            if not (source.read_bytes() == target.read_bytes()):
                logger.info(f"patching {target} with {source}")
                target.write_text(source.read_text())


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
    # else:
    #     raise EnvironmentError("Unexpected value for sys.executable: %s" % executable)


def _create_progress_dialog(progress, text):
    dialog = QProgressDialog()
    dialog.setWindowTitle("HHNK 3Di plugin installatie")
    dialog.setLabelText(text)
    dialog.setWindowFlags(Qt.WindowStaysOnTopHint)
    bar = QProgressBar(dialog)
    bar.setTextVisible(True)
    bar.setValue(progress)
    bar.setValue(0)
    bar.setMaximum(100)
    dialog.setBar(bar)
    dialog.setMinimumWidth(500)
    dialog.update()
    dialog.setCancelButton(None)
    dialog.show()
    return dialog, bar


def ensure_dependencies(
    requirements_path=REQUIREMENTS_PATH,
    flexible_dependencies=FLEXIBLE_DEPENDENCIES,
    only_path=False,
):
    """ensures dependencies by looking adding sys paths en looking into pip"""

    fh = logging.FileHandler(LOG_DIR / "ensure_dependencies.log")
    fh.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
    )
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    if DEPENDENCY_DIR not in sys.path:
        sys.path.insert(0, str(_dependencies_target_dir()))  # threedi
        sys.path.insert(0, DEPENDENCY_DIR)
        logger.info(f"Extended paths: {[i for i in sys.path]}")

    if not only_path:
        frozen_dependencies = _requirements_to_dependencies(REQUIREMENTS_PATH)
        dependencies = frozen_dependencies + flexible_dependencies

        # install patches over threeditoolbox
        install_patches()

        logger.info(f"Our dependencies: {[i.name for i in dependencies]}")
        dependencies = [i for i in dependencies if not _available(i)]
        logger.info(f"Our missing dependencies: {[i.name for i in dependencies]}")
        if dependencies:
            if _is_windows():
                dialog, bar = _create_progress_dialog(
                    0, f"Installeren: {dependencies[0].name}"
                )
                QApplication.processEvents()
                startupinfo = subprocess.STARTUPINFO()
                # Prevents terminal screens from popping up
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            else:
                dialog, bar, startupinfo = None, None, None

            for count, dependency in enumerate(dependencies):
                logger.info(f"checking {dependency.name}")
                # if not _available(dependency) or not _correct_version(dependency):
                    # to_be_installed.append(dependency)
                if dialog:
                    dialog.setLabelText(f"Installeren: {dependency.name}")
                    QApplication.processEvents()
                _install_dependency(
                    dependency, startupinfo=startupinfo, dialog=dialog
                )

                if bar:
                    bar.setValue(int((count / len(dependencies)) * 100))
                    bar.update()
                    QApplication.processEvents()
            if dialog:
                dialog.close()

    install_patches()
    logger.removeHandler(fh)
    fh.close()


def _dependencies_target_dir(our_dir=OUR_DIR, create=False) -> Path:
    """Return (and create) the desired deps folder
    This is the 'deps' subdirectory of the plugin home folder
    """
    target_dir = our_dir.parent / "ThreeDiToolbox" / "deps"
    if not target_dir.exists():
        print("Please install the threeditoolbox first!")

    return target_dir


def _can_import(package_name):
    try:
        importlib.import_module(package_name)
    except (ImportError, ModuleNotFoundError) as e:
        print(package_name, e)
        return False
    else:
        return True


def _available(dependency: Dependency, show=True, log=True):
    logger.info(f"checking availability of {dependency.package}")
    with open(LOG_DIR / "dependency_available.txt", "w+") as src:
        src.write(f"checking availability of {dependency.package}")
    if dependency.package == "jupyter":
        possible_import = _notebook_available("user")
    elif dependency.name in package_module_map.keys():
        possible_import = _can_import(package_module_map[dependency.name])
    else:
        possible_import = _can_import(dependency.name)

    if (not possible_import) and log:
        logger.info(f"{dependency.package} not available")

    return possible_import


def _correct_version(dependency: Dependency):
    """
    returns False if dependency is not available or has not correct version.
    returns True if correct version or if not enforcing dependency.
    """
    correct = False
    if _available(dependency, show=False):
        version = None
        # path is not yet added to pkg_resources, so manually
        if dependency.folder == "external-dependencies":
            for i in pkg_resources.find_distributions(DEPENDENCY_DIR):
                if i.project_name == dependency.name:
                    version = i.version

        if version is None:
            try:
                version = pkg_resources.get_distribution(dependency.name).version
            except pkg_resources.DistributionNotFound:
                return True

        correct = version in dependency.version
        if not correct:
            print(
                f"{dependency.name} hasn't a correct version ({version} not in {dependency.version})!"
            )

    if not dependency.enforce_version:
        return True
    else:
        return correct


def _notebook_available(location="osgeo"):
    """jupyters notebook is checked by looking at the executable
    instead of checking if it can be called in the cmd.
    In the cmd you'll open it immediately, instead of checking if it exists
    """
    if location == "osgeo":
        path = shutil.which("jupyter-notebook")
        notebook_exists = path is not None

        if notebook_exists and _can_import("jupyter"):
            return True
        else:
            return False
    elif location == "user":
        path = site.getusersitepackages().replace("site-packages", "Scripts")
        print("Looking for jupyter at", path + "/jupyter-notebook.exe")
        if os.path.exists(path + "/jupyter-notebook.exe"):
            return True
        else:
            return False


def _replace_patched_threedigrid(path=OUR_DIR):
    """threedigrid is patched in the toolbox it does not work with the current scripting"""
    try:
        plugin_dir = OUR_DIR.parent
        threedi_patch = str(
            plugin_dir / "ThreeDiToolbox" / "utils" / "patched_threedigrid.py"
        )
        our_patch = str(OUR_DIR / "utils" / "patched_threedigrid.py")
        print(our_patch, threedi_patch)
        shutil.copy(our_patch, threedi_patch)
    except Exception:
        print("Failed to replace the threedigrid_patch with our own.")
    else:
        print("Successfully replaced the threedigrid_patch with our own.")


def _get_python_interpreter(osgeo_shell=False):
    """Return the path to the python3 interpreter.

    Under linux sys.executable is set to the python3 interpreter used by Qgis.
    However, under Windows/Mac this is not the case and sys.executable refers to the
    Qgis start-up script.
    """
    interpreter = None
    executable = sys.executable
    directory, filename = os.path.split(executable)
    if "python" in filename and not osgeo_shell:
        if filename.lower() in ["python.exe", "python3.exe"]:
            interpreter = executable
        else:
            raise EnvironmentError(
                "Unexpected value for sys.executable: %s" % executable
            )
        assert os.path.exists(interpreter)  # safety check
        return "python", interpreter

    elif "qgis" in filename or "QGIS" in directory:
        # qgis python interpreter
        main_folder = str(Path(executable).parents[0])
        folder_files = os.listdir(main_folder)

        if "py3_env.bat" in folder_files:
            interpreter = main_folder + "/py3_env.bat"

        if "python-qgis-ltr.bat" in folder_files:
            interpreter = main_folder + "/python-qgis-ltr.bat"

        if not interpreter:
            raise EnvironmentError(
                "could not find qgis-python bat file in: %s" % main_folder
            )

        if osgeo_shell:
            interpreter = str(Path(executable).parents[1]) + "/OSGeo4W.bat"

        return "qgis", interpreter


def _install_dependency(
    dependency: Dependency, command_only=False, startupinfo=None, dialog=None
):
    """install pip in the main directory of qgis"""

    system, python_interpreter = _get_python_interpreter()

    command = [python_interpreter, "-m", "pip", "install"]

    if dependency.folder == "external-dependencies":
        command.extend(["--target", str(DEPENDENCY_DIR)])

    if dependency.no_dependecies:
        command.append("--no-deps")

    if dependency.folder == "user":
        command.append("--user")

    if dependency.package == "jupyter":
        command.extend(["--upgrade", "--force-reinstall",  "--no-cache-dir", "--no-warn-script-location"])
        # command.extend(["--upgrade"])

    command.extend([dependency.package + dependency.constraint])
    if command_only:
        return command

    logger.info(f"executing command {' '.join(command)}")
    process = subprocess.Popen(
        command,
        universal_newlines=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        startupinfo=startupinfo,
    )
    # output, error = process.communicate()

    # The input/output/error stream handling is a bit involved, but it is
    # necessary because of a python bug on windows 7, see
    # https://bugs.python.org/issue3905 .
    i, o, e = (process.stdin, process.stdout, process.stderr)
    i.close()
    result = o.read() + e.read()
    o.close()
    e.close()
    exit_code = process.wait()

    if exit_code and (not _available(dependency, log=False)):
        QApplication.processEvents()
        msg = f"Installeren {dependency.name} failed: ({' '.join(command)}) ({exit_code}) ({result})"
        try:
            if dependency.name in package_module_map.keys():
                module_name = package_module_map[dependency.name]
            else:
                module_name = dependency.name
            importlib.import_module(dependency.name)
        except (ImportError, ModuleNotFoundError) as e:
            msg + f"{(e)}"
            logger.error(msg)
            if dialog:
                dialog.close()
            raise RuntimeError(msg)
            

    # if dependency.package in sys.modules:
    #     print("Unloading old %s module" % dependency.package)
    #     del sys.modules[dependency.package]
    # if dependency.name in sys.modules:
    #     print("Unloading old %s module" % dependency.name)
    #     del sys.modules[dependency.name]

    return process.pid


def _install_multiple_dependencies(dependencies: [Dependency, Dependency]):
    """install pip in the main directory of qgis"""
    system, python_interpreter = _get_python_interpreter(True)

    complete_install = []
    for dependency in dependencies:
        command = _install_dependency(dependency, command_only=True)
        complete_install.append(" ".join(command))

    process = subprocess.Popen(
        python_interpreter,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        creationflags=DETACHED_PROCESS,
    )

    output, error = process.communicate("\n".join(complete_install))
    exit_code = process.wait()
    print(output)
    if exit_code:
        print("Installing failed")
    else:
        print("Install succes!")
        print(output)
        # print(f"Installing {dependency.package} failed with: {error} {output}")

    # if dependency.package in sys.modules:
    #    print("Unloading old %s module" % dependency.package)
    #    del sys.modules[dependency.package]

    return process.pid


def _download_wheels(dependency, directory=WHEEL_DIR):
    """Download the wheels into the wheel directory"""

    system, python_interpreter = _get_python_interpreter()
    command = [python_interpreter, "-m", "pip", "download", "-d", directory]
    command.extend([dependency.package + dependency.constraint])
    process = subprocess.Popen(command)
    output, error = process.communicate()
    exit_code = process.wait()
    if exit_code:
        print(f"Downloading {dependency.package} failed with: {error} {output}")


def _requirements_to_dependencies(requirements_path):
    with open(requirements_path) as f:
        lines = f.readlines()

    deps = []
    for l in lines:
        wheel = l.replace("\n", "")
        name = wheel.split("-")[0].lower()
        version = wheel.split("-")[0:2]
        deps.append(
            Dependency(
                name,
                WHEEL_DIR + "/" + wheel,
                version,
                "",
                True,
                "external-dependencies",
                True,
            )
        )
    return deps

def _yaml_to_dependencies(yaml_path: Path) -> List[Dependency]:
    """
    Function to read the dependencies from a yaml-path

    Args:
        yaml_path (Path): Path to the environment.yml file

    Returns:
        List[Dependency]: List of dependencies

    """

    environment = yaml.safe_load(YML_PATH.read_text())
    deps = []

    # Extract package names and versions
    dependencies = environment.get('dependencies', [])
    for dependency in dependencies:
        if isinstance(dependency, str):
            # Extract package name from string
            name = dependency.split('=')[0]
            constraint = dependency.replace(name, "", 1)
            if constraint:
                enforce_version = True
            else:
                enforce_version = False
            deps.append(
                Dependency(name,
                           name,
                           None,
                           constraint,
                           True,
                           None,
                           enforce_version
                           ))
    return deps


THREEDI_DIR = _dependencies_target_dir()


if __name__ == "__main__":
    ensure_dependencies()

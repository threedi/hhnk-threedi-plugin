# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:19:30 2021

@author: chris.kerklaan
Only works with modeller interface 3.16

#TODO:
    1. Check versioning of packages

Currently only jupyter is installed per user, due to the exectuable, others are installed in the osgeo directory, none in the external-dependecies folder.


"""


import sys
import site
import pathlib
import shutil

OUR_DIR = pathlib.Path(__file__).parent
DEPENDENCY_DIR = OUR_DIR / "external-dependencies"
DEPENDENCY_DIR.mkdir(parents=True, exist_ok=True)
DEPENDENCY_DIR = str(DEPENDENCY_DIR)

import os
import importlib
import logging
import subprocess
import pathlib
from collections import namedtuple

CREATE_NEW_PROCESS_GROUP = 0x00000200
DETACHED_PROCESS = 0x00000008

# list of depencies
""" folder can be set to "external-dependecies" to insstall in th plugin folder, it is loaded incorrectly 
the first time you update the plugin
"""
Dependency = namedtuple(
    "Dependency",
    ["name", "package", "constraint", "no_dependecies", "folder", "testpypi"],
)
DEPENDENCIES = [
    Dependency("Jupyter", "jupyter", "==1.0.0", False, "user", False), # upgrades get add layer
    Dependency("Rtree", "rtree", "==0.9.7", False, "qgis", False),
    Dependency("APScheduler", "apscheduler", "==3.8.1", False, "qgis", False),
    Dependency("ipyfilechooser", "ipyfilechooser", "==0.6.0", False, "qgis", False),
    Dependency("Scipy", "scipy", "==1.7.0", False, "qgis", False),
    Dependency("Descartes", "descartes", "==1.1.0", False, "qgis", False),
    Dependency(
        "threedi_scenario_downloader",
        "threedi_scenario_downloader",
        "==0.15",
        False,
        "qgis",
        False,
    ),
    Dependency(
        "threedi_api_client", "threedi_api_client", "==3.0.29", False, "qgis", False
    ),
    Dependency("xlrd", "xlrd", "==1.1.0", False, "qgis", False),
    Dependency("tqdm", "tqdm", "==4.40.2", False, "qgis", False),
    # test pypi
    Dependency(
        "hhnk_threedi_tools", "hhnk_threedi_tools", "==0.5.16", True, "qgis", True
    ),
    Dependency(
        "hhnk_research_tools", "hhnk_research_tools", "==0.4", True, "qgis", True
    ),
]

logger = logging.getLogger(__name__)


def ensure_dependencies(path=DEPENDENCY_DIR, dependencies=DEPENDENCIES):
    """ensures dependencies by looking adding sys paths en looking into pip"""
    sys.path.insert(0, str(_dependencies_target_dir()))  # threedi
    sys.path.insert(0, DEPENDENCY_DIR)

    print("`\nCheck if install is needed for HHNK-THREED-PLUGIN:\n")
    for dependency in dependencies:
        if not _available(dependency):
            _install_dependency(dependency)

    print("\nCurrent paths:\n")
    for path in sys.path:
        print(path)

    print("\nCheck if installed correctly:\n")
    for dependency in dependencies:
        _available(dependency)

    _replace_patched_threedigrid()


def _dependencies_target_dir(our_dir=OUR_DIR):
    """Return python dir inside our profile

    Return two dirs up if we're inside the plugins dir. If not, we have to
    import from qgis (which we don't really want in this file) and ask for our
    profile dir.

    """
    if "plugins" in str(our_dir).lower():
        # Looks like we're in the plugin dir. Return ../..
        return OUR_DIR.parent.parent
    # We're somewhere outside of the plugin directory. Perhaps a symlink?
    # Perhaps a development setup? We're forced to import qgis and ask for our
    # profile directory, something we'd rather not do at this stage. But ok.
    print("We're not in our plugins directory: %s" % our_dir)
    from qgis.core import QgsApplication

    python_dir = pathlib.Path(QgsApplication.qgisSettingsDirPath()) / "python"
    print("We've asked qgis for our python directory: %s" % python_dir)
    return python_dir

def _can_import(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        return False
    else:
        return True
        
def _available(dependency: Dependency):

    if dependency.name == "Jupyter":
        possible_import = notebook_available('user')
    else:
        possible_import = _can_import(dependency.package)

    if possible_import:
        print(f"{dependency.name} available!")
    else:
        print(f"{dependency.name} does not exists!")
    return possible_import
    
def notebook_available(location="osgeo"):
    """ jupyters notebook is checked by looking at the executable
        instead of checking if it can be called in the cmd.
        In the cmd you'll open it immediately, instead of checking if it exists
    """
    if location =='osgeo':
        path = shutil.which("jupyter-notebook")
        notebook_exists = path is not None
        
        if notebook_exists and _can_import("jupyter"):
            return True
        else:
            return False
    elif location == "user":
        path = site.getusersitepackages().replace("site-packages", "Scripts")
        print("Looking for jupyter at",path +"/jupyter-notebook.exe" )
        if os.path.exists(path +"/jupyter-notebook.exe"):
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
        print("Failed to replace the threedigrid_patch with our own")
    else:
        print("Successfully replaced the threedigrid_patch with our own")


def _get_python_interpreter():
    """Return the path to the python3 interpreter.

    Under linux sys.executable is set to the python3 interpreter used by Qgis.
    However, under Windows/Mac this is not the case and sys.executable refers to the
    Qgis start-up script.
    """
    interpreter = None
    executable = sys.executable
    directory, filename = os.path.split(executable)
    if "python" in filename:

        if filename.lower() in ["python.exe", "python3.exe"]:
            interpreter = executable
        else:
            raise EnvironmentError(
                "Unexpected value for sys.executable: %s" % executable
            )
        assert os.path.exists(interpreter)  # safety check
        return "python", interpreter

    elif "qgis" in filename:
        # qgis python interpreter
        main_folder = str(pathlib.Path(executable).parents[0])
        folder_files = os.listdir(main_folder)

        if "py3_env.bat" in folder_files:
            interpreter = main_folder + "/py3_env.bat"

        if "python-qgis-ltr.bat" in folder_files:
            interpreter = main_folder + "/python-qgis-ltr.bat"

        if not interpreter:
            raise EnvironmentError(
                "could not find qgis-python bat file in: %s" % main_folder
            )

        return "qgis", interpreter


def _install_dependency(dependency: Dependency):
    """install pip in the main directory of qgis"""
    system, python_interpreter = _get_python_interpreter()

    command = [python_interpreter, "-m", "pip", "install"]

    if dependency.folder == "external-dependecies":
        command = command + ["--target", str(DEPENDENCY_DIR)]

    if dependency.no_dependecies:
        command = command + ["--no-deps"]

    if dependency.testpypi:
        command = command + ["-i", "https://test.pypi.org/simple/"]
        
        
    if dependency.folder == "user":
        command = command + ["--user"]
        
    if dependency.name == "Jupyter":
        command = command + ["--upgrade", "--force-reinstall", "--no-cache-dir"]
       
    command = command + [dependency.package + dependency.constraint]
    print(command)
    process = subprocess.Popen(command)
    output, error = process.communicate()
    exit_code = process.wait()
    if exit_code:
        print(f"Installing {dependency.name} failed with: {error} {output}")

    if dependency.package in sys.modules:
        print("Unloading old %s module" % dependency.package)
        del sys.modules[dependency.package]

    return process.pid


THREEDI_DIR = _dependencies_target_dir()

if __name__ == "__main__":
    ensure_dependencies()

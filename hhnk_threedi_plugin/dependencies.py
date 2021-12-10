# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:19:30 2021

@author: chris.kerklaan
Only works with modeller interface 3.16

"""


import sys
import pathlib

OUR_DIR = pathlib.Path(__file__).parent
DEPENDENCY_DIR = str(OUR_DIR / "external-dependencies")

import os
import importlib
import logging
import subprocess
import pathlib
from collections import namedtuple

CREATE_NEW_PROCESS_GROUP = 0x00000200
DETACHED_PROCESS = 0x00000008

# list of depencies
Dependency = namedtuple("Dependency", ["name", "package", "constraint", "no_dependecies", "folder", "testpypi"])
DEPENDENCIES = [Dependency("Jupyter", "jupyter", "--upgrade --no-cache-dir --user", False, "qgis", False),
                Dependency("Rtree", "rtree", "==0.9.7", False,"external-dependecies", False),
                Dependency("APScheduler", "apscheduler", "==3.8.1", False, "external-dependecies", False),
                Dependency("ipyfilechooser", "ipyfilechooser", "==0.6.0", False, "external-dependecies", False),                
                Dependency("threedi_scenario_downloader", "threedi_scenario_downloader", "==0.15", False, "external-dependecies", False),
                Dependency("threedi_api_client", "threedi_api_client", "==3.0.29", False, "external-dependecies", False),
                Dependency("xlrd", "xlrd", "==1.1.0", False, "external-dependecies", False),
                Dependency("tqdm", "tqdm", "==4.40.2", False, "external-dependecies", False),
                
                # test pypi
                Dependency("hhnk_threedi_tools", "hhnk_threedi_tools", "==0.5", True, "external-dependecies", True),
                Dependency("hhnk_research_tools", "hhnk_research_tools", "==0.4", True, "external-dependecies", True)
                
                ]

logger = logging.getLogger(__name__)


def ensure_dependencies(path=DEPENDENCY_DIR, dependencies=DEPENDENCIES):
    """ensures dependencies by looking adding sys paths en looking into pip"""
    sys.path.insert(0, str(_dependencies_target_dir())) # threedi
    sys.path.insert(0, DEPENDENCY_DIR)

    for dependency in dependencies:
        if not _available(dependency):   
            _install_dependency(dependency)

    
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

def _available(dependency:Dependency):
    posssible_import = True
    try:
        importlib.import_module(dependency.package)
    except ImportError:
        posssible_import = False
        
    if posssible_import:
        print(f"{dependency.name} exists!")
    else:
        print(f"{dependency.name} does not exists!")
    return posssible_import

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

    command = [
        python_interpreter,
        "-m",
        "pip",
        "install"
        ]
    
    if dependency.folder == "external-dependecies":
        command = command + ["--target", str(DEPENDENCY_DIR)]
    
    if dependency.no_dependecies:
        command  = command + ["--no-deps"]
        
    command = command + [dependency.package + dependency.constraint]

    process = subprocess.Popen(
        command,
        shell=True,
        universal_newlines=True,
        stdin=None,
        stdout=None,
        stderr=None,
        close_fds=True,
        creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
    )
    print(f"Started processing with pid: {process.pid} and command {command}")
    return process.pid

THREEDI_DIR = _dependencies_target_dir()

if __name__ == "__main__":
    ensure_dependencies()
    
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
import pathlib
from collections import namedtuple
from distutils.dir_util import copy_tree


CREATE_NO_WINDOW = 0x08000000
DETACHED_PROCESS = 0x00000008

# Globals
OUR_DIR = pathlib.Path(__file__).parent
DEPENDENCY_DIR = OUR_DIR / "external-dependencies"
DEPENDENCY_DIR.mkdir(parents=True, exist_ok=True)
DEPENDENCY_DIR = str(DEPENDENCY_DIR)

WHEEL_DIR = OUR_DIR / "wheels"
WHEEL_DIR = str(WHEEL_DIR)
REQUIREMENTS_PATH = f"{WHEEL_DIR}/requirements.txt"

# list of depencies
""" folder can be set to "external-dependencies" to insstall in th plugin folder, it is loaded incorrectly 
the first time you update the plugin
"""

Dependency = namedtuple(
    "Dependency",
    ["name", "package", "version", "constraint", "no_dependecies", "folder", "enforce_version"],
)

FLEXIBLE_DEPENDENCIES = [
    Dependency("jupyter", "jupyter", "1.0.0", "==1.0.0", False, "user", False), 
    Dependency("hhnk_threedi_tools","hhnk_threedi_tools","0.9.2", "==0.9.2", True, "external-dependencies" , True),
    Dependency("hhnk_research_tools","hhnk_research_tools","0.8", "==0.8", True, "external-dependencies" , True), 
    Dependency("threedi_raster_edits","threedi_raster_edits","0.26", "==0.26", True, "external-dependencies" , True),  
    Dependency("threedi_scenario_downloader","threedi_scenario_downloader","0.16", "==0.16", True, "external-dependencies" , True),  
    Dependency("pytest","pytest", "7.1.2", "7.1.2", False, "external-dependencies" , False),  
]


logger = logging.getLogger(__name__)


def ensure_dependencies(requirements_path=REQUIREMENTS_PATH, flexible_dependencies=FLEXIBLE_DEPENDENCIES, only_path=False):
    """ensures dependencies by looking adding sys paths en looking into pip"""
    
    if DEPENDENCY_DIR not in sys.path:
        sys.path.insert(0, str(_dependencies_target_dir()))  # threedi
        sys.path.insert(0, DEPENDENCY_DIR)

    if not only_path:
        frozen_dependencies = _requirements_to_dependencies(REQUIREMENTS_PATH)
        dependencies = frozen_dependencies + flexible_dependencies

        print("\nExtended paths:\n")
        for path in sys.path:
            print(path)
        
        if not "fiona" in os.listdir(DEPENDENCY_DIR):
        
            print("\n Moving geopandas distribution to site-packages")
            copy_tree(WHEEL_DIR + "/geopandas", DEPENDENCY_DIR) 
        
        print("`\nInstalling frozen and flexible dependencies...:\n")
        to_be_installed = []
        for dependency in dependencies:
            if not _available(dependency) or not _correct_version(dependency):
                to_be_installed.append(dependency)
                _install_dependency(dependency)

        #_install_multiple_dependencies(to_be_installed)
        _replace_patched_threedigrid()
    
def _dependencies_target_dir(our_dir=OUR_DIR, create=False) -> pathlib.Path:
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
        
def _available(dependency: Dependency, show=True):

    if dependency.package == "jupyter":
        possible_import = _notebook_available('user')
    elif dependency.name == "python_dateutil":
        possible_import = _can_import('dateutil')
    elif dependency.name == "gdal":
        possible_import = _can_import('osgeo')    
    else:
        possible_import = _can_import(dependency.name)

    if possible_import:
        msg = f"{dependency.package} available!"
    else:
        msg = f"{dependency.package} does not exists!"
        
    if show:
        print(msg)
        
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
        if correct:
            print(f"{dependency.name} has correct version!")
        else:
            print(f"{dependency.name} has incorrect version: {version}")
    
    if not dependency.enforce_version:
        return True
    else:
        return correct

def _notebook_available(location="osgeo"):
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
            
        if osgeo_shell:
            interpreter = str(pathlib.Path(executable).parents[1]) + "/OSGeo4W.bat"

        return "qgis", interpreter


def _install_dependency(dependency: Dependency, command_only=False):
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
        #command.extend(["--upgrade", "--force-reinstall",  "--no-cache-dir", "--no-warn-script-location"])
        command.extend(["--upgrade"])
    
    command.extend([dependency.package + dependency.constraint])
    if command_only:
        return command
    
    process = subprocess.Popen(command)
    output, error = process.communicate()
    exit_code = process.wait()
    if exit_code:
       print(f"Installing {dependency.package} failed with: {error} {output}")
    else:
       print(f"Succesfully installed {dependency.name}!")
    
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
    
       
    process = subprocess.Popen(python_interpreter, 
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                creationflags=DETACHED_PROCESS
            )
            
    output, error = process.communicate("\n".join(complete_install))
    exit_code = process.wait()
    print(output)
    if exit_code:
        print("Installing failed")
    else:
        print("Install succes!")
        print(output)
        #print(f"Installing {dependency.package} failed with: {error} {output}")

    #if dependency.package in sys.modules:
    #    print("Unloading old %s module" % dependency.package)
    #    del sys.modules[dependency.package]

    return process.pid

def _download_wheels(dependency, directory= WHEEL_DIR):
    """ Download the wheels into the wheel directory"""
    
    system, python_interpreter = _get_python_interpreter()
    command = [python_interpreter, "-m", "pip", "download", "-d", directory]
    command.extend( [dependency.package + dependency.constraint])
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
        deps.append(Dependency(name, WHEEL_DIR + "/" + wheel,version, "", True, "external-dependencies", True))
    return deps
    
THREEDI_DIR = _dependencies_target_dir()


if __name__ == "__main__":
    ensure_dependencies()


# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:19:30 2021

@author: chris.kerklaan

Only works with modeller interface 3.16
"""


import sys
import pathlib
THIS_PATH = str(pathlib.Path(__file__).parent.absolute())
DEPENDENCY_PATH = THIS_PATH + "/external-dependencies"

def _ensure_dependencies(path=DEPENDENCY_PATH):
    sys.path.insert(0,DEPENDENCY_PATH)
    # later do with pip install
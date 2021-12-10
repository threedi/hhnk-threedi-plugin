# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:17:00 2021

@author: chris.kerklaan
"""
# First-party imports
import os
import pathlib

# Local imports
from hhnk_threedi_tools.utils.notebooks.run import open_notebook, open_server
from hhnk_threedi_tools.core.folders import Folders

# Globals
# __file__ = "C:/Users/chris.kerklaan/Documents/Github/hhnk-threedi-tests/hhnk_threedi_tools/tests/test_sqlite.py"
TEST_MODEL = str(pathlib.Path(__file__).parent.absolute()) + "/data/model_test/"


def test_run_notebook():
    open_notebook("02_calculation_gui.ipynb")


def test_open_server_mp():
    open_server()

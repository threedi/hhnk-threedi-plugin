# %%
"""
Test qgis_interaction.project functions.
Run this file in qgis.
"""
import importlib
import os
import sys

import hhnk_research_tools as hrt
import hhnk_threedi_tools as htt
import pandas as pd
from pathlib import Path
import pytest
from hhnk_threedi_tools.qgis import layer_structure
from hhnk_threedi_plugin.qgis_interaction.klimaatsommen_pdfs import load_print_layout
import hhnk_threedi_plugin.qgis_interaction.project as project

REPOS_DIR = os.getenv("REPOS_DIR")
assert REPOS_DIR is not None
REPOS_DIR = REPOS_DIR

# Removing the modules from sys.path is a bit slow, set to True on first run in new qgis instance.
if False:
    mods = sys.modules.copy()
    for x in mods:
        if "hhnk_threedi_plugin" in x:
            del sys.modules[x]
            # if 'hhnk_threedi_plugin.qgis_interaction.project' in sys.modules:
            # del sys.modules['hhnk_threedi_plugin.qgis_interaction.project']
    import hhnk_threedi_plugin.qgis_interaction.project as project
importlib.reload(project)
importlib.reload(layer_structure)


if project.__file__ != rf"{REPOS_DIR}\hhnk_threedi_plugin\hhnk_threedi_plugin\qgis_interaction\project.py":
    print(project.__file__)


#LAYER_STRUCTURE_PATH = r"d:\repositories\hhnk-threedi-tools\tests\data\layer_structure.csv"
LAYER_STRUCTURE_PATH = (
   rf"{REPOS_DIR}\hhnk-threedi-tools\hhnk_threedi_tools\resources\qgis_layer_structure.csv"
)


folder = htt.Folders(rf"{REPOS_DIR}\hhnk-threedi-tools\tests\data\model_test")
#folder = htt.Folders(r"E:\02.modellen\callantsoog")


revisions = layer_structure.SelectedRevisions(check_0d1d="BWN bwn_test #7 0d1d_test")
# revisions = layer_structure.SelectedRevisions(
#     check_0d1d="callantsoog #23 0d1d_test", klimaatsommen="callantsoog_referentie_v2"
# )


subjects = None
# subjects=None

# Generate structure

p = self = project.Project()
self.run(layer_structure_path=LAYER_STRUCTURE_PATH, subjects=subjects, revisions=revisions, folder=folder)

# self.set_themes(verbose=True)
# l_s = self.layers[0]
# l = project.QgisLayer(l_s)


# root = QgsProject.instance().layerTreeRoot()

# root.addLayer(l.layer)
# l.add_styles()
# l_s.qml_lst


# g = project.QgisAllGroups(settings=self.groups)
# g.create_groups()

#Add print layout and check if it was added.
load_print_layout()

assert self.layout.get_layout("wsa_kaarten1") is not None

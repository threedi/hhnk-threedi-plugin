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
import pytest
from hhnk_threedi_tools.qgis import layer_structure

plugindir_new = rf"E:\github\{os.getlogin()}\hhnk-threedi-plugin"
plugindir_old = r"C:\Users\wvangerwen\AppData\Roaming\3Di\QGIS3\profiles\default/python/plugins"
if plugindir_new not in sys.path:
    sys.path.insert(0, plugindir_new)
if plugindir_old in sys.path:
    sys.path.remove(plugindir_old)

import hhnk_threedi_plugin.qgis_interaction.project as project

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

if project.__file__ != r"E:\github\wvangerwen\hhnk-threedi-plugin\hhnk_threedi_plugin\qgis_interaction\project.py":
    print(project.__file__)


LAYER_STRUCTURE_PATH = r"E:\github\wvangerwen\hhnk-threedi-tools\tests\data\layer_structure.csv"
LAYER_STRUCTURE_PATH = (
    r"E:\github\wvangerwen\hhnk-threedi-plugin\hhnk_threedi_plugin\qgis_interaction\layer_structure\testprotocol.csv"
)


folder = htt.Folders(r"E:\github\wvangerwen\hhnk-threedi-tools\tests\data\model_test")
folder = htt.Folders(r"E:\02.modellen\callantsoog")


revisions = layer_structure.SelectedRevisions(check_0d1d="callantsoog #23 0d1d_test")
# revisions = layer_structure.SelectedRevisions(
#     check_0d1d="callantsoog #23 0d1d_test", klimaatsommen="callantsoog_referentie_v2"
# )


subjects = ["test_0d1d", "klimaatsommen"]
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

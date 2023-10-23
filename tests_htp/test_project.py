import sys
plugindir_new = fr"E:\github\{os.getlogin()}\hhnk-threedi-plugin"
plugindir_old = r"C:\Users\wvangerwen\AppData\Roaming\3Di\QGIS3\profiles\default/python/plugins"
if plugindir_new not in sys.path:
    sys.path.insert(0, plugindir_new)
if plugindir_old in sys.path:
    sys.path.remove(plugindir_old)
import importlib

import hhnk_threedi_plugin.qgis_interaction.project as project
if False:
    mods = sys.modules.copy()
    for x in mods:
        if "hhnk_threedi_plugin" in x:
            del sys.modules[x]
            #if 'hhnk_threedi_plugin.qgis_interaction.project' in sys.modules:
            #del sys.modules['hhnk_threedi_plugin.qgis_interaction.project']
    import hhnk_threedi_plugin.qgis_interaction.project as project
importlib.reload(project)

if project.__file__ != r"E:\github\wvangerwen\hhnk-threedi-plugin\hhnk_threedi_plugin\qgis_interaction\project.py":
    print(project.__file__)


import hhnk_research_tools as hrt
import pandas as pd
import os
from hhnk_threedi_tools.qgis import layer_structure
import pytest
import hhnk_threedi_tools as htt
importlib.reload(layer_structure)

import sys


LAYER_STRUCTURE_PATH = r"E:\github\wvangerwen\hhnk-threedi-tools\tests\data\layer_structure.csv"
LAYER_STRUCTURE_PATH = r"E:\github\wvangerwen\hhnk-threedi-plugin\hhnk_threedi_plugin\qgis_interaction\layer_structure\testprotocol.csv"


folder = htt.Folders(r"E:\github\wvangerwen\hhnk-threedi-tools\tests\data\model_test")
folder = htt.Folders(r"E:\02.modellen\callantsoog")


revisions = layer_structure.SelectedRevisions(check_0d1d="callantsoog #23 0d1d_test")
subjects=["test_0d1d"]

#Generate structure

p=self = project.Project()
self.run(layer_structure_path=LAYER_STRUCTURE_PATH,
                                    subjects=['test_0d1d'],
                                    revisions=revisions,
                                    folder=folder)


# l_s = self.layers[0]
# l = project.QgisLayer(l_s)



# root = QgsProject.instance().layerTreeRoot()

# root.addLayer(l.layer)
# l.add_styles()
# l_s.qml_lst


# g = project.QgisAllGroups(settings=self.groups)
# g.create_groups()

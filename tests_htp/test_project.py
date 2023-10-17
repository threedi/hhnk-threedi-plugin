import importlib
import hhnk_research_tools as hrt
import pandas as pd
import os
import hhnk_threedi_tools.qgis.layer_structure as layer_structure
import pytest
import hhnk_threedi_tools as htt
from hhnk_threedi_plugin.qgis_interaction.project import QgisLayer

LAYER_STRUCTURE_PATH = r"E:\github\wvangerwen\hhnk-threedi-tools\tests\data\layer_structure.csv"



folder = htt.Folders(r"E:\github\wvangerwen\hhnk-threedi-tools\tests\data\model_test")


#Generate structure
layer_struct = layer_structure.LayerStructure(layer_structure_path=LAYER_STRUCTURE_PATH,
                                    subjects=['test_0d1d'],
                                    folder=folder)
layer_struct.run()


print(layer_struct.df_full['layer'].iloc[0])
l = QgisLayer(layer_struct.df_full['layer'].iloc[0])


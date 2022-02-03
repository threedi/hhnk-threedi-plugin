# %%
f
# %%

import sys
from pathlib import Path
import os
sys.path.append(str(Path(os.getcwd()).parent.parent))
import hhnk_threedi_plugin.local_settings as local_settings
if local_settings.DEBUG:
    sys.path.insert(0, local_settings.hhnk_threedi_tools_path)
    import importlib, hhnk_threedi_tools
    hhnk_threedi_tools=importlib.reload(hhnk_threedi_tools)
    importlib.reload(hhnk_threedi_tools.core.folders)

from hhnk_threedi_tools.core.folders import Folders
class TestFolder():
    def __init__(self, path):
        self.fenv = Folders(path)

# qgis.utils.plugins['hhnk_threedi_plugin'].fenv.output
path = r'C:\Users\wvangerwen\Downloads\model_test_v2'
folder = Folders(path)
caller2 = TestFolder(path)

class Test():
    def __init__(self):
        self.caller = caller2

    def hh(self):
        print('hh')

self = Test()

folder.output.one_d_two_d['BWN_bwn_test_#5_1d2d_test']

# %%
# self.caller.fenv.source_data.polder_polygon.path

from hhnk_threedi_plugin.qgis_interaction.project import Layer, Project #TODO dependencies snappen waarom die een melding geeft

PDOK_LUCHTFOTO = "tileMatrixSet=EPSG:28992&crs=EPSG:28992&layers=Actueel_ortho25&styles=default&format=image/jpeg&url=https://service.pdok.nl/hwh/luchtfotorgb/wmts/v1_0"
SUBJECT = "Achtergrond"
STRUCTURE = {
    SUBJECT: [
        "Landgebruik (v1801c)",
        "Luchtfoto actueel (PDOK)",
        "Legger Waterlopen 2020",
    ]
}



layer = Layer(
        PDOK_LUCHTFOTO, "Luchtfoto actueel (PDOK)", "wms", subject=SUBJECT
        )
# %%




from hhnk_threedi_plugin.qgis_interaction.project import Layer, Project
project = Project(subject='Test')

layer_name='KZK'
group_name='Opmerkingen'

project.zoom_to_layer(layer_name=layer_name, group_name=group_name)

# project.remove_layer(layer_name, group_name)
'BWN_bwn_test_#6_1d2d_test'\Layers\1d2d_alle_stroming.gpkg

# project.instance.mapLayersByName()
# %%
from hhnk_threedi_plugin.qgis_interaction.layers_management.layers.get_layers_list import get_layers_list
from hhnk_threedi_tools.qgis.paths_functions import get_top_level_directories
from hhnk_threedi_tools.qgis.build_output_files_dict import build_output_files_dict


one_d_two_d_dict = build_output_files_dict(
                test_type=4,
                base_folder=self.one_d_two_d_output_path,
                revision_dir_name=self.one_d_two_d_selector.currentText(),
            )


one_d_two_d_layers = get_layers_list(
    test_type=4,
    plugin_dir=self.caller.plugin_dir,
    output_dict=one_d_two_d_dict,
    group_structure=layer_groups_structure,
    chosen_tests=None,
)

# TODO fix layers dict to list
one_d_two_d_layers = [
    one_d_two_d_layers[x] for x in one_d_two_d_layers
]

# Add tif layers created by regular expression
# one_d_two_d_layers = find_tif_layers_and_append(
#     input_folder=one_d_two_d_dict["layer_path"],
#     layers_list=.one_d_two_d_layers,
# )

# remove_layers(self.one_d_two_d_layers)  # Remove layers from project
# add_layers(
#     layers_list=self.one_d_two_d_layers,
#     group_structure=layer_groups_structure,
# )

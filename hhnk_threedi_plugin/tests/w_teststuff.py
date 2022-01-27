# %%

import sys
from pathlib import Path
import os
sys.path.append(str(Path(os.getcwd()).parent.parent))


# %%
from hhnk_threedi_tools import Folders

import qgis
# import hhnk_threedi_plugin.hhnk_toolbox




# %%


class TestFolder():
    def __init__(self, path):
        self.fenv = Folders(path)


path = r'C:\Users\wvangerwen\Downloads\model_test_v2'
folder = Folders(path)
caller2 = TestFolder(path)

class Test():
    def __init__(self):
        self.caller = caller2

    def hh(self):
        print('hh')

self = Test()

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

# %%

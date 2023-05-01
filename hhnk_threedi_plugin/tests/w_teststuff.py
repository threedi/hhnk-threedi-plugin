# %%
import matplotlib.pyplot as plt

a= """-9.85;0.15#0.15;0.15#0.151;0.136#0.152;0.122#0.153;0.108#0.154;0.094#0.155;0.08#0.156;0.066#0.157;0.052#0.158;0.038#0.159;0.024#0.16;0.01#0.161;-0.004#0.162;-0.018#0.163;-0.032#0.164;-0.046#0.165;-0.06#0.166;-0.074#0.167;-0.088#0.168;-0.102#0.169;-0.116#0.17;-0.13#0.171;-0.144#0.172;-0.158#0.173;-0.172#0.174;-0.186#0.175;-0.2#0.176;-0.214#0.177;-0.228#0.178;-0.242#0.179;-0.256#0.18;-0.27#0.181;-0.284#0.182;-0.298#0.183;-0.312#0.184;-0.326#0.185;-0.34#0.186;-0.354#0.187;-0.368#0.188;-0.382#0.189;-0.396#0.19;-0.41#10.15;-0.41"""
a="""-15.4;-5.4#-5.4;-5.4#-5.399;-5.419#-5.398;-5.438#-5.397;-5.457#-5.396;-5.476#-5.395;-5.495#-5.394;-5.514#-5.393;-5.533#-5.392;-5.552#-5.391;-5.571#-5.39;-5.59#-5.389;-5.609#-5.388;-5.628#-5.387;-5.647#-5.386;-5.666#-5.385;-5.685#-5.384;-5.704#-5.383;-5.723#-5.382;-5.742#-5.381;-5.761#-5.38;-5.78#-5.379;-5.799#-5.378;-5.818#-5.377;-5.837#-5.376;-5.856#-5.375;-5.875#-5.374;-5.894#-5.373;-5.913#-5.372;-5.932#-5.371;-5.951#-5.37;-5.97#-5.369;-5.989#-5.368;-6.008#-5.367;-6.027#-5.366;-6.046#-5.365;-6.065#-5.364;-6.084#-5.363;-6.103#-5.362;-6.122#-5.361;-6.141#4.6;-6.16"""
aa=a.split('#')

measure = [float(i.split(';')[0]) for i in aa][1:-1]
action = [float(i.split(';')[1]) for i in aa][1:-1]

plt.plot(measure,action)

# %%

import sys
from pathlib import Path
import os
sys.path.append(str(Path(os.getcwd()).parent.parent))
# import hhnk_threedi_plugin.local_settings as local_settings
# if local_settings.DEBUG:
#     sys.path.insert(0, local_settings.hhnk_threedi_tools_path)
#     import importlib, hhnk_threedi_tools
#     hhnk_threedi_tools=importlib.reload(hhnk_threedi_tools)
#     importlib.reload(hhnk_threedi_tools.core.folders)

from hhnk_threedi_tools.core.folders import Folders
class TestFolder():
    def __init__(self, path):
        self.fenv = Folders(path)

# qgis.utils.plugins['hhnk_threedi_plugin'].fenv.output
path = r'E:\02.modellen\model_test_v2'
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

from threedigrid_builder import make_gridadmin
import pandas as pd
from shapely import wkb
import geopandas as gpd

import hhnk_research_tools as hrt

sqlite_path = folder.model.sqlite_paths[0]
dem_path = folder.model.rasters.dem.path
out_path = "grid.gpkg"


create_grid_from_sqlite(sqlite_path, dem_path, output_folder)

a=make_gridadmin(sqlite_path, dem_path) #using output here results in error, so we use the returned dict

df = pd.DataFrame(a['cells'])
gdf_cells = hrt.df_convert_to_gdf(df, geom_col_type='wkb', src_crs='28992')


df = pd.DataFrame(a['lines'])
gdf_lines = hrt.df_convert_to_gdf(df, geom_col_type='wkb', src_crs='28992')

hrt.gdf_write_to_geopackage(gdf_cells, filepath = out_path_cells)
hrt.gdf_write_to_geopackage(gdf_lines, filepath = out_path_lines)


# %% check of ids doorkomen
import hhnk_research_tools as hrt
from hhnk_threedi_tools.utils.queries_general_checks import ModelCheck
queries_lst = [item for item in vars(ModelCheck()).values()]
for query in queries_lst:
    df = hrt.execute_sql_selection(query=query, database_path=folder.model.schema_base.database_path)
    if not df.empty:
        print(df)
        break

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

def f_a(x):
    print(x)

def f_b(x):
    print('b')

class Test():
    def __init__(self, func):
        self.i = True
        self.func = func


        self.func('hi')


try:
    print('start')
    print('errror')
    print('a')
except Exception as e:
    raise
finally:
    print('THE END')

# %%

from hhnk_threedi_plugin.qgis_interaction.project import Layer, Project
project = Project(subject='Test')

layer_name='KZK'
group_name='Opmerkingen'

project.zoom_to_layer(layer_name=layer_name, group_name=group_name)

# project.remove_layer(layer_name, group_name)
'BWN_bwn_test_#6_1d2d_test'\Layers\1d2d_alle_stroming.gpkg

# project.instance.mapLayersByName()


# %% Plugin data bekijken
import qgis
self = qgis.utils.plugins['hhnk_threedi_plugin']
print( self.dockwidget )

# %%

from ThreeDiToolbox.tool_result_selection.result_selection_view import ThreeDiResultSelectionWidget, add_spatialite_connection
from ThreeDiToolbox.tool_result_selection.models import TimeseriesDatasourceModel
from ThreeDiToolbox.tool_result_selection.result_selection import ThreeDiResultSelection





filepath=r"C:\Users\wvangerwen\Downloads\model_test_v2\02_Model\bwn_test.sqlite"

threeditoolbox = qgis.utils.plugins['ThreeDiToolbox']

threeditoolbox.result_selection_tool.run()
#threeditoolbox.result_selection_tool.dialog.select_model_spatialite_file()


self = threeditoolbox.result_selection_tool.dialog

settings = QSettings("3di", "qgisplugin")

try:
    init_path = settings.value("last_used_spatialite_path", type=str)
except TypeError:
    logger.debug(
        "Last used datasource path is no string, setting it to our home dir."
    )
    init_path = os.path.expanduser("~")

#filepath, __ = QFileDialog.getOpenFileName(
#    self, "Open 3Di model spatialite file", init_path, "Spatialite (*.sqlite)"
#)

filepath=r"C:\Users\wvangerwen\Downloads\model_test_v2\02_Model\bwn_test.sqlite"


self.ts_datasources.spatialite_filepath = filepath
index_nr = self.modelSpatialiteComboBox.findText(filepath)
if index_nr < 0:
    self.modelSpatialiteComboBox.addItem(filepath)
    index_nr = self.modelSpatialiteComboBox.findText(filepath)

self.modelSpatialiteComboBox.setCurrentIndex(index_nr)

add_spatialite_connection(filepath, self.iface)
settings.setValue("last_used_spatialite_path", os.path.dirname(filepath))



#threeditoolbox.result_selection_tool.dialog.close()

# %%

import sys
from pathlib import Path
import os
sys.path.append(str(Path(os.getcwd()).parent.parent))
try: 
    import hhnk_threedi_plugin.local_settings as local_settings
except ModuleNotFoundError:
    import hhnk_threedi_plugin.local_settings_default as local_settings
if local_settings.DEBUG:
    sys.path.insert(0, local_settings.hhnk_threedi_tools_path)
    import importlib, hhnk_threedi_tools
    hhnk_threedi_tools=importlib.reload(hhnk_threedi_tools)
    importlib.reload(hhnk_threedi_tools.core.folders)

from hhnk_threedi_tools.core.folders import Folders

from hhnk_threedi_tools.core.checks.bank_levels import BankLevelTest
import hhnk_threedi_tools.core.checks.bank_levels as bank_levels


path = r'E:\02.modellen\model_test_v3'
folder = Folders(path)

self = BankLevelTest(folder)

# self.import_data()

# %%
import hhnk_research_tools as hrt
model_path=None
datachecker_path=None

self.model_path = model_path
if model_path == None:
    self.model_path = self.fenv.model.schema_base.database.path

self.datachecker_path = datachecker_path
if self.datachecker_path == None:
    self.datachecker_path = self.fenv.source_data.datachecker.path


self.grid = hrt.threedi.grid.Grid(sqlite_path=self.fenv.model.schema_base.sqlite_paths[0],
                dem_path = self.fenv.model.schema_base.rasters.dem.path              
                )


self.fixeddrainage_layer = self.fenv.source_data.datachecker_fixed_drainage

self.imports = bank_levels.import_information(
    model_path=self.model_path,
    datachecker_path=self.datachecker_path,
    fixeddrainage_layer=self.fixeddrainage_layer,
    grid=self.grid,
)

#TODO grid.read_1d2d_lines werkt niet als alles op isolated staat.

# %%
self.line_intersections()
self.flowlines_1d2d()

# manholes
self.divergent_waterlevel_nodes()
self.manhole_information()
self.manholes_to_add_to_model()

self.cross_loc_new_filtered, self.cross_loc_new = bank_levels.new_cross_loc_bank_levels(
            self.line_intersects, self.imports["channels"], self.imports["cross_loc"]
        )
# %%
a, b = new_cross_loc_bank_levels(self.line_intersects, self.imports["channels"], self.imports["cross_loc"])

# %%
import geopandas as gpd
import numpy as np
from hhnk_threedi_tools.utils.queries import (
    manholes_query,
    channels_query,
    cross_section_location_query,
    conn_nodes_query,
)

from hhnk_threedi_tools.variables.database_aliases import (
    a_man_id,
    a_conn_node_id,
    df_geo_col,
    a_man_conn_id,
    a_cross_loc_id,
)
from hhnk_threedi_tools.variables.bank_levels import (
    one_d_node_id_col,
    node_id_col,
    node_type_col,
    connection_val,
    storage_area_col,
    levee_id_col,
    type_col,
    one_d_two_d_crosses_levee_val,
    drain_level_col,
    already_manhole_col,
    unknown_val,
    node_in_wrong_fixed_area,
    added_calc_val,
    node_geometry_col,
    one_d_two_d_crosses_fixed,
    levee_height_val,
    ref_plus_10_val,
    init_plus_10_val,
)

from hhnk_threedi_tools.variables.database_variables import (
    display_name_col,
    code_col,
    conn_node_id_col,
    shape_col,
    width_col,
    manhole_indicator_col,
    calculation_type_col,
    bottom_lvl_col,
    surface_lvl_col,
    zoom_cat_col,
    initial_waterlevel_col,
    reference_level_col,
)

# def new_cross_loc_bank_levels(intersect_1d2d_all, channel_line_geo, cross_loc):
#     try:
        # %%
        # intersect_1d2d_all = self.line_intersects
        # intersect_1d2d_all = intersect_1d2d_all[0:0]
        # channel_line_geo = self.imports["channels"]
        # cross_loc = self.imports["cross_loc"]


# %%
from osgeo import gdal
import os

def build_vrt(raster_folder, vrt_name='combined_rasters', bandlist=[1], bounds=None, overwrite=False):
    """create vrt from all rasters in a folder.
    bounds=(xmin, ymin, xmax, ymax)
    bandList doesnt work as expected."""
    output_path = os.path.join(raster_folder, f'{vrt_name}.vrt')
    
    if os.path.exists(output_path) and not overwrite:
        print(f'vrt already exists: {output_path}')
        return

    tifs_list = [os.path.join(raster_folder, i) for i in os.listdir(raster_folder) if i.endswith('.tif') or i.endswith('.tiff')]


    vrt_options = gdal.BuildVRTOptions(resolution='highest',
                                       separate=False,
                                       resampleAlg='nearest',
                                       addAlpha=True,
                                       outputBounds=bounds,
                                       bandList=bandlist,)
    ds = gdal.BuildVRT(output_path, tifs_list, options=vrt_options)
    ds.FlushCache()
    if not os.path.exists(output_path):
        print('Something went wrong, vrt not created.')


build_vrt(raster_folder=r'\\srv57d1\geo_info\02_Werkplaatsen\06_HYD\Projecten\HKC16015 Wateropgave 2.0\06. Afgeleide gegevens\01.Input\inundatie_ref_T10_corr3')
build_vrt(raster_folder=r'\\srv57d1\geo_info\02_Werkplaatsen\06_HYD\Projecten\HKC16015 Wateropgave 2.0\06. Afgeleide gegevens\01.Input\inundatie_ref_T100_corr3')
build_vrt(raster_folder=r'\\srv57d1\geo_info\02_Werkplaatsen\06_HYD\Projecten\HKC16015 Wateropgave 2.0\06. Afgeleide gegevens\01.Input\inundatie_ref_T1000_corr3')







# %%

import hhnk_threedi_tools


# %%
#CHECK PATHS BETWEEN QGIS AND VS CODE
q_p = ['E:\\github\\wvangerwen\\hhnk-threedi-tools', 'E:\\github\\wvangerwen\\hhnk-threedi-tools', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default\\python\\plugins\\hhnk_threedi_plugin\\external-dependencies', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default\\python\\plugins\\ThreeDiToolbox\\deps', 'C:/PROGRA~1/3DIMOD~1.22/apps/qgis-ltr/./python', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default/python', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default/python/plugins', 'C:/PROGRA~1/3DIMOD~1.22/apps/qgis-ltr/./python/plugins', 'C:\\PROGRA~1\\3DIMOD~1.22\\bin\\python39.zip', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\DLLs', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib', 'C:\\PROGRA~1\\3DIMOD~1.22\\bin', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\Python\\Python39\\site-packages', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\GDAL-3.4.3-py3.9-win-amd64.egg', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\win32', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\win32\\lib', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\Pythonwin', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default/python', '.', 'C:\\Program Files', 'C:\\', 'C:\\Program Files', 'C:\\', 'C:\\', 'C:\\Program Files', 'C:\\', 'C:\\']

vs_p = ['C:/Users/wvangerwen/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/hhnk_threedi_plugin/external-dependencies',
 'C:/Users/wvangerwen/AppData/Roaming/QGIS/QGIS3/profiles/default/python',
 'e:\\github\\wvangerwen\\hhnk-threedi-plugin\\hhnk_threedi_plugin\\tests',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\Scripts',
 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default\\python',
 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default\\python\\plugins\\hhnk_threedi_plugin\\external-dependencies',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\qgis-ltr\\python',
 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default\\python\\plugins\\ThreeDiToolbox\\deps',
 'C:\\Users\\wvangerwen\\AppData\\Roaming\\Python\\Python39',
 'C:\\Users\\wvangerwen\\AppData\\Roaming\\Python\\Python39\\Scripts',
 'c:\\PROGRA~1\\3DIMOD~1.22\\bin\\python39.zip',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\DLLs',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib',
 'c:\\PROGRA~1\\3DIMOD~1.22\\bin',
 '',
 'C:\\Users\\wvangerwen\\AppData\\Roaming\\Python\\Python39\\site-packages',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\GDAL-3.4.3-py3.9-win-amd64.egg',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\win32',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\win32\\lib',
 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\Pythonwin']

for i in q_p:
    if i not in vs_p:
        print(i)
# %%

sys.path
# %%
rm_list = ['C:/Users/wvangerwen/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/hhnk_threedi_plugin/external-dependencies', 'C:/Users/wvangerwen/AppData/Roaming/QGIS/QGIS3/profiles/default/python']
for i in rm_list:
    if i in sys.path:
        sys.path.remove(i)
        print(f'removed {i}')
# %%
if __name__ == '__main__':
    import sys
    from pathlib import Path
    import os
    sys.path.append(str(Path(os.getcwd()).parent.parent))
    import hhnk_threedi_plugin.local_settings as local_settings

    if local_settings.DEBUG:
        sys.path.insert(0, local_settings.hhnk_threedi_tools_path)
        import hhnk_threedi_tools as htt
        #Reload hhnk_threedi_tools and all modules within. Does not work with importlib.reload.
        for m in [i for i in sys.modules.keys() if i.startswith('hhnk_threedi_tools')]:
            del(sys.modules[m])
        import hhnk_threedi_tools as htt

import hhnk_threedi_tools.core.checks.one_d_two_d as htt_1d2d
import hhnk_threedi_tools.core.checks.grid_result_metadata as grid_result_metadata
from hhnk_threedi_plugin.qgis_interaction import load_layers_interaction
from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR
import os

from qgis.core import Qgis
from qgis.utils import QgsMessageLog

if __name__ == '__main__':
    path = r'C:\Users\wvangerwen\Downloads\model_test_v2'
    folder = htt.folders(path)
    revision='BWN bwn_test #5 1d2d_test'
    dem_path = folder.model.schema_base.rasters.dem.path
    
# %%

def task_one_d_two_d(folder, revision, dem_path):
# %%
    #Define file locations
    grid_result = folder.threedi_results.one_d_two_d[revision].grid
    output_file_flowline = folder.output.one_d_two_d[revision].stroming_1d2d_test.path
    output_file_node = folder.output.one_d_two_d[revision].grid_nodes_2d.path
    
    #Create folder
    folder.output.one_d_two_d[revision].create()

    #Initialize to get information from the netcdf
    rain, detected_rain, timestep, days_dry_start, days_dry_end, timestep_df = grid_result_metadata.construct_scenario(grid_result)

    #flowline results
    description = "flowlines levels en stroming bepalen"
    QgsMessageLog.logMessage(f"1d2d test - {description}", level=Qgis.Info)

    flowlines_df=htt_1d2d.run_flowline_stats(threedi_result=grid_result, 
                                timestep_df=timestep_df)

    flowlines_df.to_file(output_file_flowline, driver='GPKG', index=False)


    #Node results
    description = "uitlezen waterstanden op tijdstappen en locaties uit 3di resultaten"
    QgsMessageLog.logMessage(f"1d2d test - {description}", level=Qgis.Info)

    nodes_df=htt_1d2d.run_node_stats(grid_result=grid_result, 
                                timestep_df=timestep_df)
    nodes_df.to_file(output_file_node, driver='GPKG', index=False)


    #Raster results
    description = "waterstandraster per tijdstap genereren"
    QgsMessageLog.logMessage(f"1d2d test - {description}", level=Qgis.Info)
    htt_1d2d.run_levels_depths_at_timesteps(timestep_df=timestep_df, 
                                                dem_path=dem_path, 
                                                grid_result=grid_result, 
                                                folder=folder, 
                                                revision=revision)


    #Add layers to project
    df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')
    revisions={'0d1d_test':'',
                '1d2d_test':revision,
                'klimaatsommen':''}

    load_layers_interaction.load_layers(folder=folder, 
                                df_path=df_path, 
                                revisions=revisions, 
                                subjects=['test_1d2d'])

# %%

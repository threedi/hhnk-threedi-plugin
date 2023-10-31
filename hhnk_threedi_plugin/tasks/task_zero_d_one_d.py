# %%
if __name__ == '__main__':
    import sys
    from pathlib import Path
    import os
    sys.path.append(str(Path(os.getcwd()).parent.parent))


import hhnk_research_tools as hrt
import hhnk_threedi_tools.core.checks.zero_d_one_d as htt_0d1d
import hhnk_threedi_tools.core.checks.grid_result_metadata as grid_result_metadata
from hhnk_threedi_tools.qgis import layer_structure
import hhnk_threedi_plugin.qgis_interaction.project as project
from hhnk_threedi_plugin.dependencies import HHNK_THREEDI_PLUGIN_DIR
import os

from qgis.core import Qgis
from qgis.utils import QgsMessageLog

if __name__ == '__main__':
    import hhnk_threedi_tools as htt
    path = r'C:\Users\wvangerwen\Downloads\model_test_v2'
    folder = htt.folders(path)
    revision='BWN bwn_test #5 0d1d_test'
    
# %%

def task_zero_d_one_d(folder, revision):
# %%
    # grid_result = folder.threedi_results.zero_d_one_d[revision].grid

    output_file_node = folder.output.zero_d_one_d[revision].nodes_0d1d_test.path
    output_file_channels = folder.output.zero_d_one_d[revision].hydraulische_toets_watergangen.path
    output_file_structs = folder.output.zero_d_one_d[revision].hydraulische_toets_kunstwerken.path

    #Create folder
    folder.output.zero_d_one_d[revision].create()

    #Initialize to get information from the netcdf
    # rain, detected_rain, timestep, days_dry_start, days_dry_end, timestep_df = grid_result_metadata.construct_scenario(grid_result)

    zero_d_one_d_test = htt_0d1d.ZeroDOneDTest(folder=folder, revision=revision)

    #Hydraulische toets    
    QgsMessageLog.logMessage(f"0d1d test - Hydraulische toets", level=Qgis.Info)
    channels_gdf, structs_gdf = zero_d_one_d_test.run_hydraulic()
    channels_gdf.to_file(output_file_channels, driver='GPKG', index=False)
    structs_gdf.to_file(output_file_structs, driver='GPKG', index=False)

    #Waterlevels at nodes
    QgsMessageLog.logMessage(f"0d1d test - Waterlevel at nodes", level=Qgis.Info)
    gdf_node = zero_d_one_d_test.run()
    gdf_node.to_file(output_file_node, driver='GPKG', index=False)

    #Add layers to project
    df_path = hrt.get_pkg_resource_path(package_resource=htt.resources,
                                                    name="qgis_layer_structure.csv")
    revisions = layer_structure.SelectedRevisions(check_0d1d=revision)

    proj = project.Project()
    proj.run(layer_structure_path=df_path,
                subjects=['test_0d1d'],
                revisions=revisions,
                folder=folder)

# %%

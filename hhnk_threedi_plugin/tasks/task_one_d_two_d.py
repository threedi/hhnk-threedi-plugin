# %%
if __name__ == "__main__":
    import os
    import sys
    from pathlib import Path

    sys.path.append(str(Path(os.getcwd()).parent.parent))


import os

import hhnk_research_tools as hrt
import hhnk_threedi_tools as htt
from hhnk_threedi_tools.core.checks.one_d_two_d import OneDTwoDTest
from hhnk_threedi_tools.qgis import layer_structure
from qgis.core import Qgis
from qgis.utils import QgsMessageLog

import hhnk_threedi_plugin.qgis_interaction.project as project
from hhnk_threedi_plugin.dependencies import HHNK_THREEDI_PLUGIN_DIR


def task_one_d_two_d(folder, revision, dem_path):
    # Define file locations
    output_file_flowline = folder.output.one_d_two_d[revision].stroming_1d2d_test.path
    output_file_node = folder.output.one_d_two_d[revision].grid_nodes_2d.path

    # Create folder
    folder.output.one_d_two_d[revision].create()

    # Initialize test instance
    test_1d2d = OneDTwoDTest(folder=folder, revision=revision, dem_path=dem_path)

    # flowline results
    description = "flowlines levels en stroming bepalen"
    QgsMessageLog.logMessage(f"1d2d test - {description}", level=Qgis.Info)

    flowlines_df = test_1d2d.run_flowline_stats()
    flowlines_df.to_file(output_file_flowline, driver="GPKG", index=False)

    # Node results
    description = "uitlezen waterstanden op tijdstappen en locaties uit 3di resultaten"
    QgsMessageLog.logMessage(f"1d2d test - {description}", level=Qgis.Info)

    nodes_df = test_1d2d.run_node_stats()
    nodes_df.to_file(output_file_node, driver="GPKG", index=False)

    # Raster results
    description = "waterstandraster per tijdstap genereren"
    QgsMessageLog.logMessage(f"1d2d test - {description}", level=Qgis.Info)
    test_1d2d.run_wlvl_depth_at_timesteps(overwrite=False)

    # Add layers to project
    df_path = hrt.get_pkg_resource_path(package_resource=htt.resources, name="qgis_layer_structure.csv")
    revisions = layer_structure.SelectedRevisions(check_1d2d=revision)

    # Load layers
    proj = project.Project()
    proj.run(layer_structure_path=df_path, subjects=["test_1d2d"], revisions=revisions, folder=folder)


# %%
if __name__ == "__main__":
    path = r"C:\Users\wvangerwen\Downloads\model_test_v2"
    folder = htt.folders(path)
    revision = "BWN bwn_test #5 1d2d_test"
    dem_path = folder.model.schema_base.rasters.dem.path

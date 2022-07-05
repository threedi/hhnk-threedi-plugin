# %%
"""
Created on Fri Jan 28 13:45:01 2022

@author: wietse.vangerwen

This script combines input from a folder object folder.py with qgis layer
and essentially forms the configuration for klimaatsommen (qgis3_export_pdfs)
"""

if __name__ == '__main__':
    #add hhnk_threedi_plugin to path. 
    import pathlib, sys, os
    sys.path.append(str(pathlib.Path(os.path.abspath(__file__)).parents[2]))

# First-party imports
import os
import pathlib

# Third-party imports
import pandas as pd

# Local imports
import hhnk_research_tools as hrt
from hhnk_threedi_plugin.qgis_interaction.project import Layer, Project
# from hhnk_threedi_plugin.qgis_interaction.styling import path as PATH #TODO deze verwijderen uit init?
from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR
from hhnk_threedi_tools.core.folders import Folders

# globals
STYLING_DIR = pathlib.Path(__file__).parent / "styling"

def load_layers(folder: Folders, df_path, revisions=None, subjects=None, group_index=-1, remove_layer=False):
    """creates groups, loads layers in project and adds themes based on input df.
    """
    project = Project(df_path=df_path, subjects=subjects, revisions=revisions)

    project.generate_groups(group_index=group_index)

    for index, row in project.df.iterrows():
        #Evaluate row
        full_path, layer_name, filetype, qml_path, subject, \
            group_lst = project.get_layer_information_from_row(row=row, 
                                    folder=folder, 
                                    HHNK_THREEDI_PLUGIN_DIR=HHNK_THREEDI_PLUGIN_DIR)

        if remove_layer:
            project.remove_layer(layer_name=layer_name, group_lst=group_lst)

        #Dont add when layer already present.
        if not project.get_layer(layer_name=layer_name, group_lst=group_lst):
            #Tranlate to qgis layer instance and add to project.
            layer = Layer(full_path, layer_name, filetype, qml_path, subject)
            # print(layer, group_lst)
            project.add_layer(layer=layer, group_lst=group_lst)

    project.generate_themes()

    if "grid" in subjects:
        grid_path = folder.output.sqlite_tests.path
        for part in ["cells", "lines", "nodes"]:
            
            if not project.get_layer(layer_name=part, group_lst=['Grid']):
                grid_path = folder.output.sqlite_tests.pl / part
                qml = str(STYLING_DIR / "grid"/ part) + ".qml" 
                layer = Layer(str(grid_path) + ".gpkg" , part, "vector", qml, part)
                project.add_layer(layer=layer, group_lst=['Grid'])
        
def load_sqlite(filepath=r"C:\Users\wvangerwen\Downloads\model_test_v2\02_Model\bwn_test.sqlite"):
    """use the 3Di NenS plugin to load the sqlite into the project."""

    from ThreeDiToolbox.tool_result_selection.result_selection_view import ThreeDiResultSelectionWidget, add_spatialite_connection
    from ThreeDiToolbox.tool_result_selection.models import TimeseriesDatasourceModel
    from ThreeDiToolbox.tool_result_selection.result_selection import ThreeDiResultSelection
    import qgis
    from qgis.PyQt.QtCore import QSettings

    def select_model_spatialite_file_custom(dialog, filepath):
        """custom function to open 3Di toolbox and load spatialite into project.
        threeditoolbox.result_selection_tool.dialog.select_model_spatialite_file() in the file
        from ThreeDiToolbox.tool_result_selection.result_selection_view import ThreeDiResultSelectionWidget"""
        self = dialog

        settings = QSettings("3di", "qgisplugin")

        try:
            init_path = settings.value("last_used_spatialite_path", type=str)
        except TypeError:
            # logger.debug("Last used datasource path is no string, setting it to our home dir.")
            init_path = os.path.expanduser("~")

        #Disabled the popup and return for custom input.
        #filepath, __ = QFileDialog.getOpenFileName(
        #    self, "Open 3Di model spatialite file", init_path, "Spatialite (*.sqlite)"
        #)
        # if filepath == "":
        #     return False

        self.ts_datasources.spatialite_filepath = filepath
        index_nr = self.modelSpatialiteComboBox.findText(filepath)
        if index_nr < 0:
            self.modelSpatialiteComboBox.addItem(filepath)
            index_nr = self.modelSpatialiteComboBox.findText(filepath)

        self.modelSpatialiteComboBox.setCurrentIndex(index_nr)

        add_spatialite_connection(filepath, self.iface)
        settings.setValue("last_used_spatialite_path", os.path.dirname(filepath))


    #Main function
    threeditoolbox = qgis.utils.plugins['ThreeDiToolbox']

    threeditoolbox.result_selection_tool.run() #open result selection window of ThreediToolbox

    #Loading empty filepath and normal after that ensures to reload te sqlite.
    select_model_spatialite_file_custom(dialog=threeditoolbox.result_selection_tool.dialog, 
                                        filepath='')
    select_model_spatialite_file_custom(dialog=threeditoolbox.result_selection_tool.dialog, 
                                        filepath=filepath)

    threeditoolbox.result_selection_tool.dialog.close() #close the window when loading is done.

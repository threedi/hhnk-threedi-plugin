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
import hhnk_threedi_plugin.qgis_interaction.project as project

# from hhnk_threedi_plugin.qgis_interaction.styling import path as PATH #TODO deze verwijderen uit init?
from hhnk_threedi_plugin.dependencies import HHNK_THREEDI_PLUGIN_DIR
from hhnk_threedi_tools.core.folders import Folders
from hhnk_threedi_tools.qgis import layer_structure


# globals
STYLING_DIR = pathlib.Path(__file__).parent / "styling"


def load_sqlite(filepath):
    """use the 3Di NenS plugin to load the sqlite into the project.
    
    filepath (str): path to sqlite"""

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

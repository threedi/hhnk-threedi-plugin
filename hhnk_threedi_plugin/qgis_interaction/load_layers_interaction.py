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


from hhnk_threedi_plugin.qgis_interaction.project import Layer, Project
# from hhnk_threedi_plugin.qgis_interaction.styling import path as PATH #TODO deze verwijderen uit init?
from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR
from hhnk_threedi_tools.core.folders import Folders
import pandas as pd
import os


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





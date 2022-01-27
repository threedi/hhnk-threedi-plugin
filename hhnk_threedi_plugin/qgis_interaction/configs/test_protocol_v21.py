# %%
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:27:11 2021

@authors: chris.kerklaan, wietse.vangerwen

This script is the configuration for "test protocol v21"
 Structuur is opgebouwd als volgt:
     
Structure = {
    Group name: { Subgroup name: [(filename_layer1, Qgis layer name)]},
    
    }

LINKS = {
    Group name: poth to filenames
    } 
    
#TODO:
    Toevoegen van testlagen aan views

"""


if __name__ == '__main__':
    #add hhnk_threedi_plugin to path. 
    import pathlib, sys, os
    sys.path.append(str(pathlib.Path(os.path.abspath(__file__)).parents[3]))


from hhnk_threedi_plugin.qgis_interaction.project import Layer, Project
# from hhnk_threedi_plugin.qgis_interaction.styling import path as PATH #TODO deze verwijderen uit init?
from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR
from hhnk_threedi_tools import Folders
import pandas as pd
import os


SUBJECT = "test_protocol_v21"


def load_test_protocol_v21_layers(folder: Folders):
    """loads klimaatsommen layers
    Groups are created at the same time when layers are added to them
    """
    structure_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')

    df = pd.read_csv(structure_path, sep=';') #Read csv from file with configuration for the available layers.

    project = Project(df=df, subject=SUBJECT)

    for parent_group in df['parent_group'].unique():
        project.add_group(group_name=parent_group)
        
        df_parent = df.query(f"parent_group=='{parent_group}'")
        for child_group in df_parent['child_group'].unique():
            project.add_subgroup(group_name=child_group, parent_group_name=parent_group)

        for index, row in df_parent.iterrows():
            #Evaluate row
            full_path, layer_name, filetype, qml_path, subject, group_name = project.get_layer_information_from_row(row, folder, HHNK_THREEDI_PLUGIN_DIR)

            #Dont add when layer already present.
            if not project.get_layer(layer_name=layer_name, group_name=group_name):
                #Tranlate to qgis layer instance and add to project.
                layer = Layer(full_path, layer_name, filetype, qml_path, subject)
                project.add_layer(layer, group_name)

    project.generate_themes()


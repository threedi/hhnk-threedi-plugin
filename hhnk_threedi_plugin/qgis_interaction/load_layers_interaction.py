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


# def load_layers_klimaatsommen(folder: Folders, revision):
#     SUBJECT = "Klimaatsommen"

#     df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'klimaatsommen.csv')
#     # df = pd.read_csv(df_path, sep=';') #Read csv from file with configuration for the available layers.
#     # df['parent_group'].replace('Klimaatsommen', f'Klimaatsommen [{revision}]', inplace=True) #Add revision to parentgroup

#     load_layers(folder=folder, df_path=df_path, revision=revision, subjects=['klimaatsommen'])


# def load_layers_test_protocol(folder: Folders):
#     SUBJECT = "test_protocol_v21"

#     df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')
    

#     subjects=['test_protocol']
#     # df = pd.read_csv(df_path, sep=';') #Read csv from file with configuration for the available layers.

#     # df = df.query(f"subject=='test_protocol'")
#     load_layers(folder=folder, df_path=df_path, revision=None, subjects=subjects)


# def load_layers_achtergrond(folder: Folders):
#     SUBJECT = "Achtergrond"

#     df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')
#     df = pd.read_csv(df_path, sep=';') #Read csv from file with configuration for the available layers.

#     df = df.query(f"subject=='achtergrond'")
#     load_layers(folder=folder, df_path=df_path, revision=None, subject=SUBJECT, group_index=-1)


# def load_layers_0d1dtest(folder: Folders, revision):
#     SUBJECT = "Test 0d1d"

#     df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')
#     df = pd.read_csv(df_path, sep=';') #Read csv from file with configuration for the available layers.
#     df['parent_group'].replace('05. Hydraulische Toets en 0d1d tests', f'05. Hydraulische Toets en 0d1d tests [{revision}]', inplace=True) #Add revision to parentgroup

#     df = df.query(f"subject=='test_0d1d'")
#     load_layers(folder=folder, df_path=df_path, revision=revision, subject=SUBJECT)


# def load_layers_1d2dtest(folder: Folders, revision):
#     SUBJECT = "Test 1d2d"

#     df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')
#     df = pd.read_csv(df_path, sep=';') #Read csv from file with configuration for the available layers.
#     df['parent_group'].replace('07. Testprotocol 1d2d tests', f'07. Testprotocol 1d2d tests [{revision}]', inplace=True) #Add revision to parentgroup

#     df = df.query(f"subject=='test_1d2d'")
#     load_layers(folder=folder, df_path=df_path, revision=revision, subject=SUBJECT)


# def load_layers_test_sqlite(folder: Folders, remove_layer=False):
#     SUBJECT = "Test sqlite"

#     df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')
#     df = pd.read_csv(df_path, sep=';') #Read csv from file with configuration for the available layers.

#     df = df.query(f"subject=='test_sqlite'")
#     load_layers(folder=folder, df_path=df_path, subject=SUBJECT, remove_layer=remove_layer)








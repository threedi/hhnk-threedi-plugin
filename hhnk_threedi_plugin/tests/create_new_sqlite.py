# %%
import sys
from pathlib import Path
import os
sys.path.append(str(Path(os.getcwd()).parent.parent))
import hhnk_threedi_plugin.local_settings as local_settings
if local_settings.DEBUG:
    sys.path.insert(0, local_settings.hhnk_threedi_tools_path)
    import importlib, hhnk_threedi_tools
    hhnk_threedi_tools=importlib.reload(hhnk_threedi_tools)
    importlib.reload(hhnk_threedi_tools.core.folders)


from hhnk_threedi_tools.core.folders import Folders
import shutil
import hhnk_research_tools as hrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from hhnk_threedi_tools.core import folders

# qgis.utils.plugins['hhnk_threedi_plugin'].fenv.output
path = r'E:\02.modellen\model_test_v2'
folder = Folders(path)

settings_df = pd.read_excel(folder.model.settings.path)
settings_default_series = pd.read_excel(folder.model.settings_default.path).iloc[0] #Series, only has one row.


#Sanity check settings tables
inter = settings_df.keys().intersection(settings_default_series.keys())
if len(inter) > 0:
    print(f"""Er staan kolommen zowel in de defaut als in de andere modelsettings.
Dat lijkt me een slecht plan. Kolommen: {inter.values}""")

INFILTRATION_COLS = ["infiltration_rate",
"infiltration_rate_file",
"infiltration_surface_option",
"max_infiltration_capacity_file",
"display_name",
]

RASTER_FILES =  ['dem_file', 'frict_coef_file', 'infiltration_rate_file', 'max_infiltration_capacity_file']
# %%



# %%
overwrite=True

for index, row in settings_df.iterrows():
    if row['name'] != '1d2d_test':
        continue

    print(f"Create {row['name']}")

    #Add schematisation to folder structure
    schema_name = folder.model.add_modelpath(name=row['name'])

    # Copy the files that are in the global settings.
    # This menas rasters that are not defined are not added to the schematisation. 
    schema_base = folder.model.schema_base
    schema_new = getattr(folder.model, schema_name)

    
    #Write the sqlite and rasters to new folders.
    if overwrite:
        #Copy sqlite
        src=schema_base.database.path
        dst = os.path.join(schema_new.path, schema_base.database.pl.name)
        shutil.copyfile(src=src, dst=dst) 

        raster_path =  os.path.join(schema_new.path, 'rasters')
        if not os.path.exists(raster_path):
            os.mkdir(raster_path)

        #Copy rasters that are defined in the settings file
        for raster_file in RASTER_FILES:
            if not pd.isnull(row[raster_file]):
                src = os.path.join(schema_base.path, row[raster_file])
                if os.path.exists(src):
                    dst = os.path.join(schema_new.path, row[raster_file])
                    shutil.copyfile(src=src, dst=dst) 
                else:
                    print(f'Couldnt find raster:\t{row[raster_file]}')

    database_path_base = schema_base.database.path
    database_path_new = schema_new.database.path


    #Edit theSQLITE
    table_names=['v2_global_settings','v2_simple_infiltration']
    for table_name in table_names:
        print(f"\tUpdate {table_name}")

        #Set the id in the v2_simple_iniltration to the id defined in global settings.
        if table_name=='v2_simple_infiltration':
            row['id'] = row['simple_infiltration_settings_id']
        
        #Clear the table
        hrt.execute_sql_changes(query=f"""DELETE FROM {table_name}""",
                    database=database_path_new) 
        
        # Create new value and column pairs. The new values are used from the settings.xlsx file.
        if not pd.isnull(row['id']):
            df_table = hrt.sqlite_table_to_df(database_path=database_path_new, table_name=table_name)
            columns=[]
            values=[]
            for key in df_table.keys():
                columns.append(key)
                if key in row:
                    value = row[key]
                elif key in settings_default_series:
                    value = settings_default_series[key]
                else:
                    value=None
                    print(f'Column {key} not defined')
                if pd.isnull(value):
                    value=None

                #Exceptions
                #startdate is interpreted as timestamp by pandas but we only need YYYY-MM-DD format. 
                if key=='start_date': 
                    try:
                        value=str(value)[:10]
                    except:
                        pass
                values.append(value)

            #Make sure None is interpreted as NULL by sqlite.
            columns= tuple(columns)
            values = str(tuple(values)).replace('None', 'NULL') 
                
            #Prepare insert query
            query=f"""INSERT INTO {table_name} {columns}
            VALUES {values}"""

            #Insert new row
            hrt.execute_sql_changes(query, database=database_path_new)


    #Additional model changes for different model types
    if row['name'] == '0d1d_test':
        #Set every channel to isolated
        hrt.execute_sql_changes(query="UPDATE v2_channel SET calculation_type=101", database=database_path_new)

        #Set controlled weirs to 10x width because we dont use controlled strcutures in hyd test.
        #To get the weir with we use the base database, so we cant accidentally run this twice.
        controlled_weirs_selection_query = f"""
            SELECT
            v2_weir.cross_section_definition_id as cross_def_id,
            v2_weir.code as weir_code,
            v2_weir.id as id,
            v2_cross_section_definition.width as width
            FROM v2_weir
            INNER JOIN v2_cross_section_definition ON v2_weir.cross_section_definition_id = v2_cross_section_definition.id
            INNER JOIN v2_control_table ON v2_weir.id = v2_control_table.target_id
            """
        controlled_weirs_df = hrt.execute_sql_selection(controlled_weirs_selection_query, database_path=database_path_base)

        controlled_weirs_df.insert(controlled_weirs_df.columns.get_loc('width') + 1, 'width_new',
                        controlled_weirs_df['width'].apply(lambda x: round((float(x) * 10), 3))
                    )

        query = hrt.sql_create_update_case_statement(df=controlled_weirs_df,
            layer='v2_cross_section_definition',
            df_id_col='cross_def_id',
            db_id_col='id',
            old_val_col= 'width',
            new_val_col= 'width_new',)

        hrt.execute_sql_changes(query=query, database=database_path_new)




# %%
import temp_upload_model.upload as upload
importlib.reload(upload)




raster_names = {'dem_file':schema_new.rasters.dem.path_if_exists, 
                'frict_coef_file':schema_new.rasters.friction.path_if_exists, 
                'infiltration_rate_file':schema_new.rasters.infiltration.path_if_exists,
                'max_infiltration_capacity_file':schema_new.rasters.storage.path_if_exists}
# **** possible raster_names ****
# [ dem_file, equilibrium_infiltration_rate_file, frict_coef_file,
# initial_groundwater_level_file, initial_waterlevel_file, groundwater_hydro_connectivity_file,
# groundwater_impervious_layer_level_file, infiltration_decay_period_file, initial_infiltration_rate_file,
# leakage_file, phreatic_storage_capacity_file, hydraulic_conductivity_file, porosity_file, infiltration_rate_file,
# max_infiltration_capacity_file, interception_file ]
# ********************************

tags = ["modeltest_1d2dtest_hoekje"]
sqlite_path = schema_new.database.path
schematisation_name = "modeltest_1d2d_test_hoekje"
organisation_uuid="48dac75bef8a42ebbb52e8f89bbdb9f2"

upload.upload_and_process(schematisation_name=schematisation_name,
    sqlite_path=sqlite_path,
    raster_paths=raster_names,
    schematisation_create_tags=tags,
    commit_message='Test rev3')

# %%

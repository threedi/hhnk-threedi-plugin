from distutils.command.upload import upload
import os
import os.path
from pathlib import Path
from pyexpat import model
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsApplication, Qgis, QgsProject, QgsVectorLayer
from qgis.utils import showPluginHelp
from qgis.PyQt.QtWidgets import QAction, QListWidgetItem
# Initialize Qt resources from file resources.py
from hhnk_threedi_plugin.resources import *
import pandas as pd
import datetime
from typing import Union
from hhnk_threedi_plugin.gui.model_states.functions.api_calls.threedi_calls import ThreediCalls

# Import the code for the DockWidget

from hhnk_threedi_plugin.hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget
import os.path

try: 
    import hhnk_threedi_plugin.local_settings as local_settings
except:
    pass
from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal
from hhnk_threedi_plugin.gui.model_states import modelselection
#from hhnk_threedi_plugin.gui.model_states.functions.create_new_sqlite import create_schematisation
#from hhnk_threedi_plugin.tests.temp_upload_model import upload as upload_2
from pathlib import Path
from zipfile import ZipFile
from threedi_api_client.api import ThreediApi
from typing import Union, Dict, List
from threedi_models_and_simulations.api_calls.threedi_calls import ThreediCalls



class modelSplitterDialog(QtWidgets.QDialog):
    def __init__(self, caller, parent=None):
        # super().__init__()
        super(modelSplitterDialog, self).__init__(parent)

        uic.loadUi(os.path.join(os.path.dirname(__file__), "model_splitter_dialog.ui"),self)
        self.caller=caller
        self.dockwidget = parent
        model_settings =  r'\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\model_settings.xlsx'
        self.setWindowTitle('Modelsplitter')
        # self.pb__log_in.clicked.connect(self.get_api)     
        self.model_settings_path.fileChanged.connect(self.add_models)
        self.show() #FIXME remove after testing.
        self.model_settings_path.setFilePath(model_settings)
        self.listWidget3.addItem(str(datetime.datetime.now()) + "SETTINGS FOLDER: - " + model_settings)
        self.run_push_btn.clicked.connect(self.iterlist)
        self.model_settings_path.fileChanged.connect(self.add_location)
        self.upload_models_pbn.clicked.connect(self.upload_model)
        self.cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def add_location(self):
        folder_path = self.model_settings_path.filePath()
        self.listWidget3.addItem("")
        self.listWidget3.addItem(str(datetime.datetime.now() + "-----------------------------------------------------------------------------*"))
        self.listWidget3.addItem("CHANGED SETTINGS FOLDER INTO: - " + folder_path)     

    def get_api(self):
        modelselection.Example.get_api(self)


    def add_models(self):
        modelsettings_path = self.model_settings_path.filePath()
        #a = r'\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\model_settings.xlsx'
        if os.path.exists(modelsettings_path):
            try:
                self.settings_df = pd.read_excel(modelsettings_path)
                self.settings_df.set_index('name', drop=False, inplace=True)
                for index, row in self.settings_df.iterrows():
                    item_name = index
                    print(item_name)

                    if item_name not in self.get_lst_items(listwidget=self.listWidget2) and item_name not in self.get_lst_items(listwidget=self.listWidget1):
                        self.listWidget2.addItem(QListWidgetItem(item_name))
                        print ('Not selected Model' )
                        
            except Exception as e:
                raise e
                for item_name in self.get_lst_items(listwidget=self.listWidget2):
                    print (item_name)


    def get_lst_items(self, listwidget):
        items = []
        for x in range(listwidget.count()):
            items.append(listwidget.item(x).text())
        return items

    def show_version_list(self, Listwidget):
        items = []
        for x in range(Listwidget.count()):
            items.append(Listwidget.item(x).text())
        return items
        
    def iterlist(self):
        modelselection.Example.iterlist(self)
        self.listWidget3.addItem("")
        self.listWidget3.addItem(str(datetime.datetime.now()) + " -----------------------------------------------------------------------------*")
        self.listWidget3.addItem("Model versions enabled: " + str(self.show_version_list(Listwidget=self.listWidget2)))
        self.listWidget3.addItem("Model versions disabled: " + str(self.show_version_list(Listwidget=self.listWidget1)))
        self.listWidget3.addItem("Path: " + str(local_settings.project_path))
        self.listWidget3.addItem("Continue to upload the versions")


    def upload_model(self):   
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
        commit_message='testmodel')








        self.listWidget3.addItem(self.listwidget2.selectedItems())


        self.listWidget3.addItem(self.listwidget2())


        lst_items = self.get_lst_items(listwidget=self.dlg.listWidget2)
        for list_name in lst_items:
            row = self.settings_df.loc[list_name]


            try:                                  
                    create_schematisation(name=list_name, row=row)


            except Exception as e:
                 
                    raise e


    # def run(self):

    #     """Run method that performs all the real work"""
        
    #     self.add_models()
    #     self.add_location()
    #     self.localsave.setFilePath(r'\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\model_settings.xlsx')
    #     self.localsave.fileChanged.connect(self.add_models)
    #     # Create the dialog with elements (after translation) and keep reference
    #     # Only create GUI ONCE in callback, so that it will only load when the plugin is started
    #     # if self.first_start == True:
    #     #     self.first_start = False
        
    #     #     # self.add_models()
    #     #     self.add_location()
            

    #     # show the dialog
    #     # self.show()
        
    #     # Run the dialog event loop       
    #     # self.pb__log_in.clicked.connect(self.get_api)
    #     # self.localsave.fileChanged.connect(self.add_models)
    #     # self.localsave.setFilePath(r'\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\model_settings.xlsx')
    #     # self.run_push_btn.clicked.connect(self.iterlist)



###########################################################################################################################################


    # def upload_schematisation(self): 
    #     from threedi_api_client.api import ThreediApi
    #     from threedi_models_and_simulations.api_calls.threedi_calls import ThreediCalls
                       
    #     THREEDI_API_HOST = "https://api.3di.live"
    
    #     self.user= 'j.acostabarragan' #self.username.text()

    #     CONFIG = {
    #         "THREEDI_API_HOST": "https://api.3di.live", #THREEDI_API_HOST,
    #         "THREEDI_API_USERNAME":"j.acostabarragan", #self.user,
    #         "THREEDI_API_PASSWORD":"Camilo89" #self.password.text()
    #     }
    #     self.config=CONFIG
    #     self.threedi_api = ThreediApi(config=CONFIG, version='v3-beta')

    #     tc = ThreediCalls(self.threedi_api)
    #     user_profile = tc.fetch_current_user()
    #     self.user_full_name = f"{user_profile.first_name} {user_profile.last_name}"
    #     self.organisations = {org.unique_id: org for org in tc.fetch_organisations()}

    #     ThreediCalls.upload_schematisation_revision_sqlite(self, schematisation_pk=1, revision_pk=1, filename= r"\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\1d2d_bgs\bwn_test.sqlite")
      
    #     print('the button is working but is not uploading anything yet')

        
    #     sqlite_path = r"\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\1d2d_bgs\bwn_test.sqlite"
    #     revision = 1   
    # def upload_sqlite(self, schematisation, revision, sqlite_path):#: Union[str, Path]):
    #     # from typing import Union, Dict, List
    #     from pathlib import Path
    #     from zipfile import ZipFile
    #     from threedi_api_client.api import ThreediApi
    #     from typing import Union, Dict, List
    #     from threedi_models_and_simulations.api_calls.threedi_calls import ThreediCalls
    #     sqlite_path = r"\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\1d2d_bgs\bwn_test.sqlite"
    #     revision = 1

    #     THREEDI_API_HOST = "https://api.3di.live"
    
    #     self.user= 'j.acostabarragan' #self.username.text()

    #     CONFIG = {
    #         "THREEDI_API_HOST": "https://api.3di.live", #THREEDI_API_HOST,
    #         "THREEDI_API_USERNAME":"j.acostabarragan", #self.user,
    #         "THREEDI_API_PASSWORD":"Camilo89" #self.password.text()
    #     }
    #     self.config=CONFIG
    #     self.threedi_api = ThreediApi(config=CONFIG, version='v3-beta')

    #     tc = ThreediCalls(self.threedi_api)
    #     user_profile = tc.fetch_current_user()
    #     self.user_full_name = f"{user_profile.first_name} {user_profile.last_name}"
    #     self.organisations = {org.unique_id: org for org in tc.fetch_organisations()}


    #     sqlite_path = Path(sqlite_path)
    #     sqlite_zip_path = sqlite_path.with_suffix('.zip')
    #     print(f'sqlite_zip_path = {sqlite_zip_path}')
    #     ZipFile(sqlite_zip_path, mode='w').write(str(sqlite_path), arcname=str(sqlite_path.name))
    #     upload = THREEDI_API.schematisations_revisions_sqlite_upload(
    #         id=revision.id,
    #         schematisation_pk=schematisation.id,
    #         data={"filename": str(sqlite_zip_path.name)}
    #     )
    #     if upload.put_url is None:
    #         print(f"Sqlite '{sqlite_path.name}' already existed, skipping upload.")
    #     else:
    #         print(f"Uploading '{str(sqlite_path.name)}'...")
    #         upload_file(url=upload.put_url, file_path=sqlite_zip_path, timeout=UPLOAD_TIMEOUT)

    #     sqlite = upload_sqlite(self, schematisation, 1, r"\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\1d2d_bgs\bwn_test.sqlite")


    # def upload_and_process(self, schematisation_name =  'Juan_Test',  
    #     sqlite_path= r"\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\1d2d_bgs\bwn_test.sqlite",        
    #     raster_paths= Dict[str(r"\\E:\02.modellen\model_test_v2\02_Model\1d2d_bgs\rasters\dem_hoekje.tif"), str(r"E:\02.modellen\model_test_v2\02_Model\1d2d_bgs\rasters\friction_hoekje.tif") , str(r"E:\02.modellen\model_test_v2\02_Model\1d2d_bgs\rasters\infiltration_hoekje.tif")], 
    #     schematisation_create_tags: List[str('Juan_test')] = None, commit_message: str = "auto-commit"):

    #     THREEDI_API_HOST = "https://api.3di.live"

    #     self.user= 'j.acostabarragan' #self.username.text()

    #     CONFIG = {
    #         "THREEDI_API_HOST": "https://api.3di.live", #THREEDI_API_HOST,
    #         "THREEDI_API_USERNAME":"j.acostabarragan", #self.user,
    #         "THREEDI_API_PASSWORD":"Camilo89" #self.password.text()
    #     }
    #     self.config=CONFIG
    #     self.threedi_api = ThreediApi(config=CONFIG, version='v3-beta')

    #     tc = ThreediCalls(self.threedi_api)
    #     user_profile = tc.fetch_current_user()
    #     self.user_full_name = f"{user_profile.first_name} {user_profile.last_name}"
    #     self.organisations = {org.unique_id: org for org in tc.fetch_organisations()}

    #     schematisation = get_or_create_schematisation(schematisation_name, tags=schematisation_create_tags)

    #     # Nieuwe (lege) revisie aanmaken
    #     revision = THREEDI_API.schematisations_revisions_create(schematisation.id, data={"empty": True})

    #     # Data uploaden
    #     # # Spatialite
    #     sqlite_path = Path(sqlite_path)
    #     upload_sqlite(schematisation=schematisation, revision=revision, sqlite_path=sqlite_path)

    #     # # Rasters
    #     for raster_type, raster_path in raster_paths.items():
    #         print(raster_path)
    #         if raster_path is not None: #all rasters are passed but are not always used in every model. It is None when thats the case
    #             upload_raster(rev_id=revision.id, schema_id=schematisation.id, raster_type=raster_type, raster_path=raster_path)

    #     # Commit revision
    #     commit_revision(rev_id=revision.id, schema_id=schematisation.id, commit_message=commit_message)

    #     # 3Di model en simulation template genereren
    #     threedimodel = create_threedimodel(schematisation, revision)
    #     return threedimodel

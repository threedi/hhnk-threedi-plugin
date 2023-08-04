import os

from qgis.PyQt.QtWidgets import QAction, QListWidgetItem
from qgis.PyQt import QtGui, QtWidgets, uic

import pandas as pd
import datetime
from pathlib import Path


from hhnk_threedi_tools.core.checks import model_splitter
from hhnk_threedi_plugin.hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget
from hhnk_threedi_tools import MigrateSchema
import hhnk_threedi_tools.core.api.upload_model.upload as upload
#from hhnk_threedi_plugin.gui.model_states.functions.create_new_sqlite import create_schematisation


class modelSplitterDialog(QtWidgets.QDialog):
    def __init__(self, caller, parent=None):
        # super().__init__()
        super(modelSplitterDialog, self).__init__(parent)

        uic.loadUi(os.path.join(os.path.dirname(__file__), "model_splitter_dialog.ui"),self)
        self.caller=caller
        self.dockwidget = parent
        self.setWindowTitle('Modelsplitter')
        
        #Load setting
        self.dockwidget.model_splitter_btn.clicked.connect(self.migration_check)
        self.dockwidget.model_splitter_btn.clicked.connect(self.load_settings)
        self.model_settings_path.fileChanged.connect(self.load_settings)
        self.model_settings_path.fileChanged.connect(self.add_models_to_widget)

        # creating schematisations, revisions and enable the upload process          
        self.run_push_btn.clicked.connect(self.revision_check)
        self.run_push_btn.clicked.connect(self.create_schematisations)
        self.run_push_btn.clicked.connect(self.enable_upload)

        # upload the models
        self.upload_push_btn.clicked.connect(self.upload_schematisations)
        self.upload_push_btn.clicked.connect(self.disable_upload)

        # other stuff
        self.cancel.clicked.connect(self.close)            
        self.model_settings_path.setFilePath(self.caller.fenv.model.settings.path)

        

    def load_settings(self):
        """Load model settings and default settings. Thet are added as .settings_df and .settings_default_series"""
        self.model_settings_path.setFilePath(self.caller.fenv.model.settings.path)
        modelsettings_path = self.model_settings_path.filePath() 
        self.modelschematisations = model_splitter.ModelSchematisations(folder=self.caller.fenv, modelsettings_path=modelsettings_path)

        if self.modelschematisations.settings_loaded:
            #Add logging that file was changed 
            folder_path = self.model_settings_path.filePath()
            self.listWidget3.addItem("")
            self.listWidget3.addItem(f"{datetime.datetime.now()} -----------------------------------------------------------------------------*")
            self.listWidget3.addItem("Current model settings folder:")
            self.listWidget3.addItem("- " + folder_path)


    def enable_upload(self):
        self.upload_push_btn.setEnabled(True)
    
    def disable_upload(self):
        self.upload_push_btn.setEnabled(False)


    def add_models_to_widget(self):
        """Add models to the listwidgets"""
        #modelsettings_path = r'\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\model_settings.xlsx'
        if os.path.exists(self.model_settings_path.filePath()):
            for item_name, row in self.modelschematisations.settings_df.iterrows():

                if item_name not in self.get_lst_items(listwidget=self.listWidget2) and item_name not in self.get_lst_items(listwidget=self.listWidget1):
                    self.listWidget2.addItem(QListWidgetItem(item_name))


    def get_lst_items(self, listwidget) -> list:
        """Get items from widgets"""
        items = []
        for x in range(listwidget.count()):
            items.append(listwidget.item(x).text())
        return items

    def migration_check(self):
        migrate_schema = MigrateSchema(filename=self.caller.fenv.model.schema_base.sqlite_paths[0])
        migrate_schema.run()
        
    def create_schematisations(self):
        """Loop over the selected models in the list widget on the right
        Create individual schematisations for each"""
        
        lst_items = self.get_lst_items(listwidget=self.listWidget2)
        api_key = self.dockwidget.threedi_api_key_textbox.text()
        for list_name in lst_items:
            self.modelschematisations.create_schematisation(name=list_name)

        #Logging
        self.listWidget3.addItem("")
        # self.listWidget3.addItem(f"{datetime.datetime.now()} -----------------------------------------------------------------------------*")
        self.listWidget3.addItem("Model versions enabled: " + str(self.get_lst_items(listwidget=self.listWidget2)))
        self.listWidget3.addItem("Model versions disabled: " + str(self.get_lst_items(listwidget=self.listWidget1)))
        self.listWidget3.addItem("")
        self.listWidget3.addItem("Selected Organisation ID: " + self.dockwidget.uuid_comboBox.currentText())
        self.listWidget3.addItem("")
        self.listWidget3.addItem("Continue to upload the versions!")

        #create local split-revision
        self.modelschematisations.sqlite_revision(commit_message=str(" (local split revision)" ))

    def revision_check(self):
        api_key = self.dockwidget.threedi_api_key_textbox.text()
        lst_items = self.get_lst_items(listwidget=self.listWidget2)
        
        self.listWidget3.addItem("")
        self.listWidget3.addItem(f"{datetime.datetime.now()} -----------------------------------------------------------------------------*")
        self.listWidget3.addItem(self.modelschematisations.get_local_revision_info(name=lst_items[0], api_key=api_key))

        for list_name in lst_items:
            self.listWidget3.addItem(self.modelschematisations.get_model_revision_info(name=list_name, api_key=api_key))

        #Logging
        self.listWidget3.addItem("")
        self.listWidget3.addItem("Check revisions and continue to upload the versions")

    def upload_schematisations(self):   
        """Upload selected schematisations to the 3Di servers."""
        commit_message = self.textEdit.toPlainText()
        commit_message = commit_message.lower()
        commit_message = commit_message.replace('\n', ' ').replace('\r', ' ').replace("\\", '|')
        polders_dir = self.dockwidget.polders_map_selector.filePath()
        polder = self.dockwidget.polder_selector.currentText()
        path = Path(polders_dir) / polder

        #settings for upload
        api_key = self.dockwidget.threedi_api_key_textbox.text()
        organisation_uuid = upload.threedi.api.contracts_list(organisation__name=self.dockwidget.uuid_comboBox.currentText()).results
        for uuid in organisation_uuid: 
            uuid_slug = uuid.organisation 
        lst_items = self.get_lst_items(listwidget=self.listWidget2)
        print(lst_items)    
        
        #upload the schematisation                                          
        for list_name in lst_items:
             self.listWidget3.addItem("")
             self.listWidget3.addItem("Started uploading: " + list_name)
             self.modelschematisations.upload_schematisation(name=list_name, commit_message=commit_message, api_key=api_key, organisation_uuid=uuid_slug)
             self.listWidget3.addItem("Finished uploading: " + list_name)
             self.listWidget3.addItem("")


        #Logging
        self.listWidget3.addItem("")
        self.listWidget3.addItem(f"{datetime.datetime.now()} -----------------------------------------------------------------------------*")
        self.listWidget3.addItem("Model versions uploaded: " + str(self.get_lst_items(listwidget=self.listWidget2)))
        self.listWidget3.addItem("Path: " + str(path))
        
        #create local upload revision
        self.modelschematisations.sqlite_revision(commit_message = ("upload revision " + commit_message))



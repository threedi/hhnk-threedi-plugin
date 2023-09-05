import os

from qgis.PyQt.QtWidgets import QAction, QListWidgetItem
from qgis.PyQt import QtGui, QtWidgets, uic

import datetime
from pathlib import Path

import hhnk_threedi_tools as htt
from hhnk_threedi_tools import MigrateSchema
import hhnk_threedi_tools.core.schematisation.upload as upload


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
        self.dockwidget.model_splitter_btn.clicked.connect(self.init_widgets)
        self.model_settings_path.fileChanged.connect(self.init_widgets)
        #self.model_settings_path.fileChanged.connect(self.add_models_to_widget)

        # creating schematisations, revisions and enable the upload process          
        self.run_push_btn.clicked.connect(self.revision_check)
        self.run_push_btn.clicked.connect(self.create_schematisations)
        self.run_push_btn.clicked.connect(self.disable_buttons)

        # upload the models
        self.upload_push_btn.clicked.connect(self.upload_schematisations)
        self.upload_push_btn.clicked.connect(self.disable_buttons)

        # other stuff
        self.cancel.clicked.connect(self.close_widget)      
        self.model_settings_path.setFilePath(self.caller.fenv.model.settings.base)

        

    def init_widgets(self):
        """Load model settings and default settings. Thet are added as .settings_df and .settings_default_series"""
        self.model_settings_path.setFilePath(self.caller.fenv.model.settings.base)
        modelsettings_path = self.model_settings_path.filePath() 
        self.modelschematisations = htt.model_splitter.ModelSchematisations(folder=self.caller.fenv, modelsettings_path=modelsettings_path)
        self.add_models_to_widget()
        
        self.upload_push_btn.setEnabled(False)

        if self.modelschematisations.settings_loaded:
            #Add logging that file was changed 
            folder_path = self.model_settings_path.filePath()
            self.info_list.addItem("")
            self.info_list.addItem(f"{datetime.datetime.now()} -----------------------------------------------------------------------------*")
            self.info_list.addItem("Current model settings folder:")
            self.info_list.addItem("- " + folder_path)

    def enable_buttons(self):
        self.upload_push_btn.setEnabled(True)
        #self.cancel.setEnabled(True)
        self.run_push_btn.setEnabled(True)        

    def disable_buttons(self):
        self.upload_push_btn.setEnabled(False)
        self.cancel.setEnabled(False)
        #self.run_push_btn.setEnabled(False)        

    def close_widget(self):
        # clear all list-widgets
        self.info_list.clear()
        self.enabled_list.clear()
        self.disabled_list.clear()

        # enable all buttons for next time
        self.enable_buttons()

        # close the widget
        self.close()
        

    def add_models_to_widget(self):
        """Add models to the listwidgets"""
        if os.path.exists(self.model_settings_path.filePath()):
            for item_name in self.modelschematisations.settings_df.index:
                if item_name not in self.get_lst_items(listwidget=self.enabled_list) and item_name not in self.get_lst_items(listwidget=self.disabled_list):
                    self.enabled_list.addItem(QListWidgetItem(item_name))

    def get_lst_items(self, listwidget) -> list:
        """Get items from widgets"""
        items = []
        for x in range(listwidget.count()):
            items.append(listwidget.item(x).text())
        return items

    def migration_check(self):
        print(self.caller.fenv.model.schema_base.sqlite_paths[0])
        migrate_schema = MigrateSchema(filename=self.caller.fenv.model.schema_base.sqlite_paths[0])
        migrate_schema.run()
        
    def create_schematisations(self):
        """Loop over the selected models in the list widget on the right
        Create individual schematisations for each"""
        
        lst_items = self.get_lst_items(listwidget=self.enabled_list)
        api_key = self.dockwidget.threedi_api_key_textbox.text()
        for list_name in lst_items:
            try:
                self.modelschematisations.create_schematisation(name=list_name)
            except Exception as e:
                self.info_list.addItem(f"ERROR: {str(e)}")
                raise e

        #Logging
        self.info_list.addItem("")
        # self.info_list.addItem(f"{datetime.datetime.now()} -----------------------------------------------------------------------------*")
        self.info_list.addItem("Model versions enabled: " + str(self.get_lst_items(listwidget=self.enabled_list)))
        self.info_list.addItem("Model versions disabled: " + str(self.get_lst_items(listwidget=self.disabled_list)))
        self.info_list.addItem("")
        #create local split-revision
        response = self.modelschematisations.create_local_sqlite_revision(commit_message=str(" (local split revision)" ))
        self.info_list.addItem(response)
        self.info_list.addItem("")
        self.info_list.addItem("Selected Organisation ID: " + self.dockwidget.org_name_comboBox.currentText())
        self.info_list.addItem("")
        self.info_list.addItem("Continue to upload the versions!")
        self.enable_buttons()


    def revision_check(self):
        api_key = self.dockwidget.threedi_api_key_textbox.text()
        lst_items = self.get_lst_items(listwidget=self.enabled_list)
        
        self.info_list.addItem("")
        self.info_list.addItem(f"{datetime.datetime.now()} -----------------------------------------------------------------------------*")
        self.info_list.addItem(self.modelschematisations.get_latest_local_revision_str())

        for list_name in lst_items:
            self.info_list.addItem(self.modelschematisations.get_model_revision_info(name=list_name, api_key=api_key))

        #Logging
        self.info_list.addItem("")
        self.info_list.addItem("Check revisions and continue to upload the versions")

    def upload_schematisations(self):   
        """Upload selected schematisations to the 3Di servers."""
        commit_message = self.textEdit.toPlainText()
        commit_message = commit_message.lower()
        commit_message = commit_message.replace('\n', ' ').replace('\r', ' ').replace("\\", '|')
        polders_dir = self.dockwidget.polders_map_selector.filePath()
        polder = self.dockwidget.polder_selector.currentText()
        polder_path = Path(polders_dir) / polder

        #settings for upload
        api_key = self.dockwidget.threedi_api_key_textbox.text()
        organisations = upload.threedi.api.contracts_list(organisation__name=self.dockwidget.org_name_comboBox.currentText()).results
        for org in organisations: 
            uuid_slug = org.organisation 
        lst_items = self.get_lst_items(listwidget=self.enabled_list)
        print(lst_items)    
        
        #upload the schematisation                                          
        for list_name in lst_items:
             self.info_list.addItem("")
             self.info_list.addItem("Started uploading: " + list_name)
             self.modelschematisations.upload_schematisation(name=list_name, commit_message=commit_message, api_key=api_key, organisation_uuid=uuid_slug)
             self.info_list.addItem("Finished uploading: " + list_name)
             self.info_list.addItem("")


        #Logging
        self.info_list.addItem("")
        self.info_list.addItem(f"{datetime.datetime.now()} -----------------------------------------------------------------------------*")
        self.info_list.addItem(f"Model versions uploaded: {self.get_lst_items(listwidget=self.enabled_list)}")
        self.info_list.addItem(f"Path: {polder_path}")
        
        #create local upload revision
        response = self.modelschematisations.create_local_sqlite_revision(commit_message = ("upload revision " + commit_message))
        self.info_list.addItem(response)
        self.enable_buttons()

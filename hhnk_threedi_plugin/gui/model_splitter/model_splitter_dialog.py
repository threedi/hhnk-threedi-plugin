import os

from qgis.PyQt.QtWidgets import QListWidgetItem
from qgis.PyQt import QtWidgets, uic
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication

import datetime
from pathlib import Path
import re

import hhnk_threedi_tools as htt
from hhnk_threedi_tools import MigrateSchema
import hhnk_threedi_tools.core.schematisation.upload as upload

import hhnk_research_tools as hrt
from hhnk_threedi_plugin.tasks import generalChecksTask, checkSchematisationTask
from hhnk_threedi_plugin.gui.utility.widget_interaction import update_button_background


CHECK_PARAMETERS = ["kmax", "grid_space", "output_time_step"]
#%%
def strip_special_characters(input_string):
    # Replace all backslashes with forward slashes
    input_string = input_string.replace('\\', '/')
    
    # Remove all characters except alphanumeric, underscores, hyphens, and forward slashes
    return re.sub(r'[^a-zA-Z0-9-_\/. ]', '', input_string)

#%%

class modelSplitterDialog(QtWidgets.QDialog):
    def __init__(self, caller, parent=None):
        super(modelSplitterDialog, self).__init__(parent)

        uic.loadUi(os.path.join(os.path.dirname(__file__), "model_splitter_dialog.ui"),self)
        self.caller=caller
        self.dockwidget = parent
        self.setWindowTitle('Modelsplitter')
        self.api_key = self.dockwidget.threedi_api_key_textbox.text()
        self.sql_error = None
        self.model_splitted = False

        # init widget
        self.dockwidget.model_splitter_btn.clicked.connect(self.migration_check)
        self.dockwidget.model_splitter_btn.clicked.connect(self.init_widgets)
        self.model_settings_path.fileChanged.connect(self.init_widgets)

        # checking model-consistency
        self.enabled_list.itemChanged.connect(self.check_consistency_enabled_models)

        # creating schematisations, revisions and enable the upload process          
        self.run_splitter_btn.clicked.connect(self.revision_check)
        self.run_splitter_btn.clicked.connect(self.create_schematisations)
        self.check_push_btn.clicked.connect(self.sqlite_check)

        # upload the models
        self.commitMessage.textChanged.connect(lambda: self.verify_upload(verbose=False))
        self.upload_push_btn.clicked.connect(self.upload_schematisations)

        # other stuff
        self.rejected.connect(self.close_widget)
        self.close_btn.clicked.connect(self.close_widget)      
        self.model_settings_path.setFilePath(self.caller.fenv.model.settings.base)

    def init_widgets(self):
        """Load model settings and default settings. Thet are added as .settings_df and .settings_default_series"""
        self.model_settings_path.setFilePath(self.caller.fenv.model.settings.base)
        modelsettings_path = self.model_settings_path.filePath() 
        self.modelschematisations = htt.model_splitter.ModelSchematisations(folder=self.caller.fenv, modelsettings_path=modelsettings_path)
        self.add_models_to_widget()

        if self.modelschematisations.settings_loaded:
            # Add logging that file was changed 
            folder_path = self.model_settings_path.filePath()
            self.info_list.addItem("")
            self.add_list_item(self.info_list, f"-----------------------------------------------------------------------------*", addtime=True)
            self.info_list.addItem("Current model settings folder:")
            self.add_list_item(self.info_list, f"- {folder_path}")
  

    @property
    def enabled_lst(self):
        return self.get_lst_items(listwidget=self.enabled_list)


    def check_consistency_enabled_models(self):
        """Check settings_df if any of the CHECK_PARAMETERS columns have different values
        give this back as warning so user is aware of the differences."""
        if self.enabled_lst:
            if "" in self.enabled_lst:
                #itemChanged geeft als er meerdere items aan enabled toe worden gevoegd
                #een signaal af voor elk item. Met daarna lege entries. We hoeven alleen
                #check te draaien als alle items zijn toegevoegd aan enabled_list.
                return
            else:
                models_df = self.modelschematisations.settings_df.loc[self.enabled_lst]
                for parameter in CHECK_PARAMETERS:
                    if parameter in models_df.columns:
                        if models_df[parameter].nunique() != 1:
                            self.info_list.addItem(
                                f"WARNING: value of '{parameter}' is not unique: {models_df[parameter].to_dict()}"
                                )

        #Something changed in selected so we need to split again.
        self.model_splitted = False
        self.reset_buttons()


    def reset_buttons(self):
        self.upload_push_btn.setEnabled(False)
        if self.modelschematisations.settings_loaded:
            self.run_splitter_btn.setEnabled(True)
        else:
            self.run_splitter_btn.setEnabled(False)
        update_button_background(self.run_splitter_btn)
        update_button_background(self.upload_push_btn)


    def close_widget(self):
        # clear all list-widgets
        self.commitMessage.clear()
        self.info_list.clear()
        self.enabled_list.clear()
        self.disabled_list.clear()

        # enable all buttons for next time
        self.reset_buttons()
        
        #Reset styles
        update_button_background(self.check_push_btn)
        update_button_background(self.upload_push_btn)

        # close the widget
        self.close()
        

    def verify_upload(self, verbose=True):
        """Check if upload is ready; model is splitted and commit-message supplied."""
        self.upload_push_btn.setEnabled(False)
        cont = True

        #Error in sqlite
        if cont and self.sql_error is None:
            message = "Run Check Sqlite to continue"
            cont = False

        #Error in sqlite
        if cont and self.sql_error:
            message = "Model contains errors in sqlite database and cannot be uploaded. Run sqlite checks and fix errors."
            cont = False

        #Model not split
        if not self.model_splitted:
            message = "Split model to upload version(s)"
            cont = False

        #empty list
        if cont and not self.enabled_lst: 
            message = "Enable a schematisation and use splitter"
            cont = False      

        if cont and (len(self.get_commit_message()) <= 2):
            message = "Provide commit message (minimal 3 characters) to upload version(s)"
            cont = False

        if cont:
            message = "Continue to upload the version(s)!"
            self.upload_push_btn.setEnabled(True)

        if verbose:
            self.info_list.addItem(message)
            self.add_list_item(self.info_list, "")   

    def add_models_to_widget(self):
        """Add models to the listwidgets"""
        if os.path.exists(self.model_settings_path.filePath()):
            enabled_models = []
            for item_name in self.modelschematisations.settings_df.index:
                self.disabled_list.addItem(QListWidgetItem(item_name))
            self.check_consistency_enabled_models()
                    

    def get_lst_items(self, listwidget) -> list:
        """Get items from widgets"""
        items = []
        for x in range(listwidget.count()):
            items.append(listwidget.item(x).text())
        return items
    
   
    def get_commit_message(self):
        commit_message = self.commitMessage.toPlainText()
        cleaned_commit_message = strip_special_characters(commit_message)
        if commit_message != cleaned_commit_message:
            self.commitMessage.setPlainText(cleaned_commit_message)
            cursor = self.commitMessage.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.commitMessage.setTextCursor(cursor)
        return cleaned_commit_message

    def sqlite_check(self):
        """Check if sqlite is OK according to 3Di:schematisation_checker and HHNK general checks"""

        update_button_background(button=self.check_push_btn, color="orange")
        
        # init checks
        check_schematisation = checkSchematisationTask(folder=self.caller.fenv, add_to_project=True)
        check_general = generalChecksTask(folder=self.caller.fenv)
        
        # run checks
        check_schematisation.run()
        check_general.run()
        
        # check errors
        self.sql_error = any((check_schematisation.error, check_general.error))
        self.info_list.addItem("")

        if self.sql_error:
            update_button_background(button=self.check_push_btn, color="red")
        else:
            update_button_background(button=self.check_push_btn, color="green")
        self.verify_upload(verbose=True)


    def migration_check(self):
        """Migrate schema to newest version using htt.MigrateSchema"""
        print(self.caller.fenv.model.schema_base.sqlite_paths[0])
        migrate_schema = MigrateSchema(filename=self.caller.fenv.model.schema_base.sqlite_paths[0])
        migrate_schema.run()
        

    def create_schematisations(self):
        """Loop over the selected models in the list widget on the right
        Create individual schematisations for each"""
        
        update_button_background(button=self.run_splitter_btn, color="orange")

        for list_name in self.enabled_lst:
            try:
                self.modelschematisations.create_schematisation(name=list_name)
            except Exception as e:
                self.info_list.addItem(f"{type(e).__name__}: {str(e)} (view Python error log for more info)")
                update_button_background(button=self.run_splitter_btn, color="red")

                raise e

        # Logging
        self.info_list.addItem("")
        # self.info_list.addItem(f"{datetime.datetime.now()} -----------------------------------------------------------------------------*")
        self.info_list.addItem("Model versions enabled: " + str(self.enabled_lst))
        self.info_list.addItem("Model versions disabled: " + str(self.get_lst_items(listwidget=self.disabled_list)))
        self.info_list.addItem("")
        # create local split-revision
        response = self.modelschematisations.create_local_sqlite_revision(commit_message=str(" (local split revision)" ))
        self.info_list.addItem(response)
        self.info_list.addItem("")
        self.info_list.addItem("Selected Organisation ID: " + self.dockwidget.org_name_comboBox.currentText())
        self.info_list.addItem("")
        self.model_splitted = True
        update_button_background(button=self.run_splitter_btn, color="green")
        self.verify_upload(verbose=True)


    def revision_check(self):
        """Log latest revision."""
        
        self.info_list.addItem("")
        self.add_list_item(self.info_list, f"-----------------------------------------------------------------------------*", addtime=True)
        self.info_list.addItem(self.modelschematisations.get_latest_local_revision_str())

        for list_name in self.enabled_lst:
            self.info_list.addItem(self.modelschematisations.get_model_revision_info(name=list_name, api_key=self.api_key))

        # Logging
        self.info_list.addItem("")
        self.info_list.addItem("Check revisions and continue to upload the versions")


    def upload_schematisations(self):   
        """Upload selected schematisations to the 3Di servers."""
        try:
            update_button_background(self.upload_push_btn, color="orange")

            commit_message = self.get_commit_message()
            polders_dir = self.dockwidget.polders_map_selector.filePath()
            polder = self.dockwidget.polder_selector.currentText()
            polder_path = Path(polders_dir) / polder

            # settings for upload
            organisations = upload.threedi.api.contracts_list(organisation__name=self.dockwidget.org_name_comboBox.currentText()).results
            for org in organisations: 
                uuid_slug = org.organisation 
            
            # upload the schematisation                                          
            for list_name in self.enabled_lst:
                self.info_list.addItem("")
                self.add_list_item(self.info_list, f"Started uploading: {list_name}", addtime=True)

                self.modelschematisations.upload_schematisation(name=list_name, commit_message=commit_message, api_key=self.api_key, organisation_uuid=uuid_slug)
                self.add_list_item(self.info_list, f"Finished uploading: {list_name}", addtime=True)

            # Logging
            self.info_list.addItem("")
            self.add_list_item(self.info_list, f"-----------------------------------------------------------------------------*", addtime=True)
            self.info_list.addItem(f"Model versions uploaded: {self.enabled_lst}")
            self.info_list.addItem(f"Path: {polder_path}")
            
            # create local upload revision
            response = self.modelschematisations.create_local_sqlite_revision(commit_message = ("upload revision " + commit_message))
            self.add_list_item(self.info_list, response)
            self.model_splitted = False
            self.upload_push_btn.setEnabled(False)
            update_button_background(self.upload_push_btn, color="green")
        except Exception as e:
            update_button_background(self.upload_push_btn, color="red")
            raise e
        

    def add_list_item(self, lst_widget, text, addtime=False):
        """add item to info_list and scroll to botom"""
        if addtime:
            lst_widget.addItem(f"{hrt.current_time()} {text}")
        else:
            lst_widget.addItem(f"{text}")

        lst_widget.scrollToBottom()
        lst_widget.repaint() #update widgets
import os

from qgis.PyQt.QtWidgets import QAction, QListWidgetItem
from qgis.PyQt import QtGui, QtWidgets, uic

import pandas as pd
import datetime

from hhnk_threedi_tools.core.checks import model_splitter
#from hhnk_threedi_plugin.gui.model_states.functions.create_new_sqlite import create_schematisation


class modelSplitterDialog(QtWidgets.QDialog):
    def __init__(self, caller, parent=None):
        # super().__init__()
        super(modelSplitterDialog, self).__init__(parent)

        uic.loadUi(os.path.join(os.path.dirname(__file__), "model_splitter_dialog.ui"),self)
        self.caller=caller
        self.dockwidget = parent
        self.setWindowTitle('Modelsplitter')

        self.model_settings_path.fileChanged.connect(self.load_settings)
        self.model_settings_path.fileChanged.connect(self.add_models_to_widget)
        self.run_push_btn.clicked.connect(self.create_schematisations)
        self.upload_models_pbn.clicked.connect(self.upload_schematisations)
        self.cancel.clicked.connect(self.exit)

        self.model_settings_path.setFilePath(self.caller.fenv.model.settings)
        self.listWidget3.addItem(str(datetime.datetime.now()) + "SETTINGS FOLDER: - " + self.caller.fenv.model.settings)


    def exit(self):
        self.close()


    def load_settings(self):
        """Load model settings and default settings. Thet are added as .settings_df and .settings_default_series"""
        modelsettings_path = self.model_settings_path.filePath() 
        
        self.modelschematisations = model_splitter.ModelSchematisations(folder=self.caller.fenv, modelsettings_path=modelsettings_path)

        if self.modelschematisations.settings_loaded:
            #Add logging that file was changed 
            folder_path = self.model_settings_path.filePath()
            self.listWidget3.addItem("")
            self.listWidget3.addItem(str(datetime.datetime.now() + "-----------------------------------------------------------------------------*"))
            self.listWidget3.addItem("CHANGED SETTINGS FOLDER INTO: - " + folder_path)

        else:
            self.settings_df = None
            self.settings_default_series = None  


    def add_models_to_widget(self):
        """Add models to the listwidgets"""
        #modelsettings_path = r'\\corp.hhnk.nl\data\Hydrologen_data\Data\02.modellen\model_test_v2\02_Model\model_settings.xlsx'
        if os.path.exists(self.model_settings_path.filePath()):
            for item_name, row in self.settings_df.iterrows():

                if item_name not in self.get_lst_items(listwidget=self.listWidget2) and item_name not in self.get_lst_items(listwidget=self.listWidget1):
                    self.listWidget2.addItem(QListWidgetItem(item_name))


    def get_lst_items(self, listwidget) -> list:
        """Get items from widgets"""
        items = []
        for x in range(listwidget.count()):
            items.append(listwidget.item(x).text())
        return items


    def create_schematisations(self):
        """Loop over the selected models in the list widget on the right
        Create individual schematisations for each"""
        lst_items = self.get_lst_items(listwidget=self.listWidget2)
        for list_name in lst_items:
            self.modelschematisations.create_schematisation(name=list_name)

        #Logging
        self.listWidget3.addItem("")
        self.listWidget3.addItem(str(datetime.datetime.now()) + " -----------------------------------------------------------------------------*")
        self.listWidget3.addItem("Model versions enabled: " + str(self.get_lst_items(Listwidget=self.listWidget2)))
        self.listWidget3.addItem("Model versions disabled: " + str(self.get_lst_items(Listwidget=self.listWidget1)))
        self.listWidget3.addItem("Path: " + str(self.dockwidget.polder_selector.filePath()))
        self.listWidget3.addItem("Continue to upload the versions")


    def upload_schematisations(self):   

        lst_items = self.get_lst_items(listwidget=self.listWidget2)
        for list_name in lst_items:
            self.modelschematisations.upload_schematisation(name=list_name)

        #Logging
        self.listWidget3.addItem("")
        self.listWidget3.addItem(str(datetime.datetime.now()) + " -----------------------------------------------------------------------------*")
        self.listWidget3.addItem("Model versions uploaded: " + str(self.get_lst_items(Listwidget=self.listWidget2)))
        self.listWidget3.addItem("Path: " + str(self.dockwidget.polder_selector.filePath()))

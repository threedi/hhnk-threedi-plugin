import os
import pandas as pd
import shutil
import glob 

from PyQt5.QtWidgets import (
    QComboBox,
    QDialog,
    QVBoxLayout,
    QFileDialog,
    QLineEdit,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QPushButton,
    QMessageBox,
)
from PyQt5.QtCore import Qt, pyqtSignal
from qgis.utils import Qgis, iface
from ..gui.utility.file_widget import fileWidget
from ..error_messages.input_error_messages import (
    invalid_character_in_filename,
    folder_exists_already,
)
from hhnk_threedi_tools.core.folders import Folders



def setupUi(new_project_dialog):
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignTop)
    layout.setContentsMargins(25, 25, 25, 25)
    new_project_dialog.setWindowTitle("Nieuw project aanmaken")
    new_project_dialog.setMinimumWidth(275)
    
    # Creates items to be in widget
    new_project_dialog.folder_selector = fileWidget(
        file_dialog_title="Selecteer map waarin project wordt aangemaakt",
        file_mode=QFileDialog.Directory,
        select_text="Selecteer map:",
    )

    """" later gebruiken"""
    # new_project_dialog.reference_model_box = fileWidget(
    #     file_dialog_title="Kies referentie model:",
    #     file_mode=QFileDialog.Directory,
    #     select_text="Selecteer referentie polder map:",
    # )

    new_project_dialog.reference_model_label = QLabel("Geef referentie polder op:")
    new_project_dialog.reference_model_box = QComboBox()

    new_project_dialog.polder_name_label = QLabel("Geef project (polder) naam op:")
    new_project_dialog.polder_name_field = QLineEdit()

    new_project_dialog.create_project_btn = QPushButton("Project aanmaken")

    # Add items to layout
    layout.addWidget(new_project_dialog.folder_selector, alignment=Qt.AlignTop)
    layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    layout.addWidget(new_project_dialog.reference_model_label, alignment=Qt.AlignTop)
    layout.addWidget(new_project_dialog.reference_model_box, alignment=Qt.AlignTop)
    layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    layout.addWidget(new_project_dialog.polder_name_label, alignment=Qt.AlignTop)   
    layout.addWidget(new_project_dialog.polder_name_field, alignment=Qt.AlignTop)
    layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    layout.addWidget(new_project_dialog.create_project_btn, alignment=Qt.AlignTop)
    new_project_dialog.setLayout(layout)

    #set reference model
    base_path = r"E:\02.modellen"
    reference_models_paths = glob.glob(str(base_path + "\\cbt-[0-9]")) + glob.glob(str(base_path + "\\cbt-[0-9][0-9]"))
    new_project_dialog.reference_model_box.addItem("",)
    for paths in reference_models_paths:
        files = os.listdir(paths)
        for file in files:
            if file.endswith('.sqlite'):
                new_project_dialog.reference_model_box.addItem((os.path.splitext(file)[0]))
    
                
    new_project_dialog.reference_model_box.setStyleSheet("QComboBox { combobox-popup: 0; }")
    new_project_dialog.reference_model_box.setMaxVisibleItems(10)
    new_project_dialog.reference_model_box.setPlaceholderText(str('-Select Polder-'))
    new_project_dialog.reference_model_box.setCurrentIndex(-1)
    

class newProjectDialog(QDialog):
    """
    Creates a widget that allows a user to easily create a new project.
    Select a base folder and a name for the project, the basic structure is automatically set up
    and read-me files specifying the contents are added.

    Signals:

    project_folder_path(path)
    """

    project_folder_path = pyqtSignal(str)

    def __init__(self):
        super(newProjectDialog, self).__init__()
        setupUi(self)
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        self.create_project_btn.clicked.connect(self.verify_submit)
        self.full_path = ""

    def verify_submit(self):
        base_path = self.folder_selector.filePath()
        if not base_path:
            iface.messageBar().pushMessage(
                "Selecteer een map om nieuw project in aan te maken", Qgis.Critical
            )
              
        else:
            if not os.path.isdir(base_path):
                iface.messageBar().pushMessage(
                    "Selecteer een bestaande map om nieuw project in aan te maken",
                    Qgis.Critical,
                )  
            else:
                project_name = self.polder_name_field.text()
                if not project_name:
                    iface.messageBar().pushMessage(
                        "Geen projectnaam opgegeven", Qgis.Critical
                    )
                else:
                    full_path = os.path.join(base_path, project_name)
                    if os.path.isdir(full_path):
                        iface.messageBar().pushMessage(
                            folder_exists_already, Qgis.Critical
                        )
                           
                    else:
                        try:
                            print(full_path)
                            os.mkdir(full_path)
                            Folders(full_path, create=True)
                            print("succes1")
                            self.project_folder_path.emit(full_path)
                            self.accept()
                            QMessageBox.information(
                                None, "Create project", "Your folders are created!"
                            )
                            self.full_path = full_path                                

                        except Exception:
                            iface.messageBar().pushMessage(
                                invalid_character_in_filename, Qgis.Critical
                            )

                        else:
                            print(self.reference_model_box.currentText()==(""))
                            try:
                                self.copy_files()
                            except:
                                iface.messageBar().pushMessage(
                                "Settings, sqlite of rasters niet gekopieerd", Qgis.Info
                                    )  
                            else:
                                if self.reference_model_box.currentText() == (""):
                                    iface.messageBar().pushMessage(
                                                "Geen referentie model opgegeven", Qgis.Info
                                                )
                                pass


    def copy_files(self):
        #setting the paths
        base_path = self.folder_selector.filePath()
        project_name = self.polder_name_field.text()
        dst = Folders(os.path.join(base_path, project_name))
        
        reference_model_base = self.reference_model_box.currentText()
        reference_model = reference_model_base[4:]

        bwn_paths = glob.glob(str(base_path + "\\cbt-[0-9]")) + glob.glob(str(base_path + "\\cbt-[0-9][0-9]"))
        raster_paths = glob.glob(str(base_path + "\\cbt-[0-9]\\rasters")) + glob.glob(str(base_path + "\\cbt-[0-9][0-9]\\rasters"))      
       
        #adjust and copy model settings        
        if reference_model == (""):
            raw_model_settings = pd.read_excel("E:\\github\\jkaptein\\hhnk-threedi-plugin\\hhnk-threedi_plugin\\model_settings.xlsx", engine="openpyxl")
            new_model_settings = pd.DataFrame(raw_model_settings.replace(regex=['hoekje'], value="[--set raster name--]"))
            new_model_settings['name'] = (new_model_settings['name'] + str('_' + project_name))
            new_model_settings.to_excel(os.path.join(dst.model.base, "model_settings.xlsx"))
            
            #copy model settings default file
            model_settings_default = pd.read_excel("E:\\github\\jkaptein\\hhnk-threedi-plugin\\hhnk-threedi_plugin\\model_settings_default.xlsx", engine="openpyxl")
            model_settings_default.to_excel(os.path.join(dst.model.base, "model_settings_default.xlsx"))
        
        else:
            raw_model_settings = pd.read_excel("E:\\github\\jkaptein\\hhnk-threedi-plugin\\hhnk-threedi_plugin\\model_settings.xlsx", engine="openpyxl")
            new_model_settings = pd.DataFrame(raw_model_settings.replace(regex=['hoekje'], value=reference_model))
            new_model_settings['name'] = (new_model_settings['name'] + str('_' + project_name))       
            new_model_settings.to_excel(os.path.join(dst.model.base, "model_settings.xlsx"))

            #copy model settings default file
            model_settings_default = pd.read_excel("E:\\github\\jkaptein\\hhnk-threedi-plugin\\hhnk-threedi_plugin\\model_settings_default.xlsx", engine="openpyxl")
            model_settings_default.to_excel(os.path.join(dst.model.base, "model_settings_default.xlsx"))
            
            #searching sqlite file and copy to destination folder
            for paths in bwn_paths:
                files = os.listdir(paths)
                copy_sqlite = []
                for file in files:
                    if reference_model_base in file:
                        if file.endswith('.sqlite'):
                            copy_sqlite.append(os.path.join(paths, file))
                for files in copy_sqlite:
                    shutil.copy(files, os.path.join(dst.model.schema_base.path))       
            
            #searching raster files and copy to destination folder
            for paths in raster_paths:
                files = os.listdir(paths)
                copy_rasters = []
                for file in files:
                    if reference_model in file:
                            if file.endswith('.tif'):
                                copy_rasters.append(os.path.join(paths, file))
                for files in copy_rasters:
                    shutil.copy(files, os.path.join(dst.model.schema_base.rasters.path))

                        
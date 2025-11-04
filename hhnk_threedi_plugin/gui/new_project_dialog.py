#%%
import glob
import os
import shutil
from pathlib import Path

import hhnk_research_tools as hrt
import hhnk_threedi_tools as htt
import pandas as pd
from hhnk_threedi_tools.core.folders import Folders
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QComboBox,
    QDialog,
    QFileDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)
from qgis.utils import Qgis, iface

from hhnk_threedi_plugin.hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget

from ..error_messages.input_error_messages import (
    folder_exists_already,
    invalid_character_in_filename,
)


def setupUi(new_project_dialog):
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignTop)
    layout.setContentsMargins(25, 25, 25, 25)
    new_project_dialog.setWindowTitle("Nieuw project aanmaken")
    new_project_dialog.setMinimumWidth(275)

    # Creates items to be in widget
    new_project_dialog.reference_model_label = QLabel("Geef referentie polder op:")
    new_project_dialog.reference_model_box = QComboBox()

    new_project_dialog.polder_name_label = QLabel("Geef project (polder) naam op:")
    new_project_dialog.polder_name_field = QLineEdit()

    new_project_dialog.create_project_btn = QPushButton("Project aanmaken")

    # Add items to layout

    layout.addWidget(new_project_dialog.reference_model_label, alignment=Qt.AlignTop)
    layout.addWidget(new_project_dialog.reference_model_box, alignment=Qt.AlignTop)
    layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    layout.addWidget(new_project_dialog.polder_name_label, alignment=Qt.AlignTop)
    layout.addWidget(new_project_dialog.polder_name_field, alignment=Qt.AlignTop)
    layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    layout.addWidget(new_project_dialog.create_project_btn, alignment=Qt.AlignTop)
    new_project_dialog.setLayout(layout)

    # set reference model
    dockwidget = HHNK_toolboxDockWidget()
    base_path = Path(dockwidget.polders_map_selector.filePath())
    base_path = str(base_path.parent)
    print(base_path)
    if base_path == "." or "":
        base_path = r"E:\02.modellen"

    print(base_path)

    reference_models_paths = glob.glob(str(base_path + "\\cbt-[0-9]")) + glob.glob(str(base_path + "\\cbt-[0-9][0-9]"))
    new_project_dialog.reference_model_box.addItem(
        "",
    )
    for paths in reference_models_paths:
        files = os.listdir(paths)
        for file in files:
            if file.endswith(".sqlite"):
                new_project_dialog.reference_model_box.addItem((os.path.splitext(file)[0]))

    new_project_dialog.reference_model_box.setStyleSheet("QComboBox { combobox-popup: 0; }")
    new_project_dialog.reference_model_box.setMaxVisibleItems(10)
    new_project_dialog.reference_model_box.setPlaceholderText(str("-Select Polder-"))
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

    def __init__(self, base_path):
        super(newProjectDialog, self).__init__()
        setupUi(self)
        self.base_path = Path(base_path)
        self.polder_path = None

        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        self.create_project_btn.clicked.connect(self.make_folders)

    def make_folders(self):
        project_name = self.polder_name_field.text().replace(" ", "_")
        if not project_name:
            iface.messageBar().pushMessage("Geen projectnaam opgegeven", Qgis.Critical)
        else:
            polder_path = self.base_path / project_name
            if polder_path.is_dir():
                iface.messageBar().pushMessage(folder_exists_already, Qgis.Critical)
            else:
                try:
                    Folders(polder_path, create=True)
                    self.project_folder_path.emit(polder_path.as_posix())
                    self.accept()
                    self.polder_path = polder_path
                    QMessageBox.information(None, "Create project", "Your folders are created!")
                except Exception:
                    iface.messageBar().pushMessage(invalid_character_in_filename, Qgis.Critical)
                    pass

                else:
                    try:
                        full_path = ""

                        # os.mkdir(str(full_path))
                        # print("succes0")

                        # Folders(full_path, create=True)
                        # print("succes1")

                        # self.project_folder_path.emit(full_path)

                        # self.accept()
                        # QMessageBox.information(
                        #      None, "Create project", "Your folders are created!"
                        #  )
                        # self.full_path = full_path

                    except Exception:
                        iface.messageBar().pushMessage(invalid_character_in_filename, Qgis.Critical)

                    else:
                        print(self.reference_model_box.currentText() == (""))
                        try:
                            self.copy_files()
                        except:
                            iface.messageBar().pushMessage("Settings, sqlite of rasters niet gekopieerd", Qgis.Info)
                        else:
                            if self.reference_model_box.currentText() == (""):
                                iface.messageBar().pushMessage("Geen referentie model opgegeven", Qgis.Info)
                            pass

    def copy_files(self):
        # setting the paths
        dockwidget = HHNK_toolboxDockWidget()
        base_path = Path(dockwidget.polders_map_selector.filePath())
        base_path = str(base_path.parent)
        print(base_path + " copy_files")
        if not base_path == r"E:\02.modellen":
            base_path = r"E:\02.modellen"

        # base_path = self.folder_selector.filePath()
        project_name = self.polder_name_field.text()
        print(project_name)
        dst = Folders(os.path.join(str(base_path), str(project_name)))
        print(dst)

        reference_model_base = self.reference_model_box.currentText()
        reference_model = reference_model_base[4:]

        bwn_paths = glob.glob(str(base_path + "\\cbt-[0-9]")) + glob.glob(str(base_path + "\\cbt-[0-9][0-9]"))
        raster_paths = glob.glob(str(base_path + "\\cbt-[0-9]\\rasters")) + glob.glob(
            str(base_path + "\\cbt-[0-9][0-9]\\rasters")
        )

        # adjust and copy model settings
        if reference_model == (""):
            value = "[--set raster name--]"
        else:
            value = reference_model

        p = hrt.get_pkg_resource_path(package_resource=htt.resources, name="model_settings.xslx")
        raw_model_settings = pd.read_excel(p, engine="openpyxl")
        new_model_settings = pd.DataFrame(raw_model_settings.replace(regex=["callantsoog"], value=value))
        new_model_settings["name"] = new_model_settings["name"] + str("_" + project_name)
        new_model_settings.to_excel(dst.model.settings.base)

        # copy model settings default file
        p = hrt.get_pkg_resource_path(package_resource=htt.resources, name="model_settings_default.xslx")
        model_settings_default = pd.read_excel(p, engine="openpyxl")
        model_settings_default.to_excel(dst.model.settings_default.base)

        if reference_model != (""):
            # searching sqlite file and copy to destination folder
            for paths in bwn_paths:
                files = os.listdir(paths)
                copy_sqlite = []
                for file in files:
                    if reference_model_base in file:
                        if file.endswith(".sqlite"):
                            copy_sqlite.append(os.path.join(paths, file))
                for files in copy_sqlite:
                    shutil.copy(files, os.path.join(dst.model.schema_base.path))

            # searching raster files and copy to destination folder
            for paths in raster_paths:
                files = os.listdir(paths)
                copy_rasters = []
                for file in files:
                    if reference_model in file:
                        if file.endswith(".tif"):
                            copy_rasters.append(os.path.join(paths, file))
                for files in copy_rasters:
                    shutil.copy(files, os.path.join(dst.model.schema_base.rasters.path))

# %%

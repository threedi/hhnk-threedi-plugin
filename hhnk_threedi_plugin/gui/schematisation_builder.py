import os
from dataclasses import dataclass

import geopandas as gpd
import pandas as pd
from hhnk_threedi_tools.core.project import Project
from hhnk_threedi_tools.core.schematisation_builder.DAMO_exporter import DAMO_exporter
from osgeo import ogr
from PyQt5.QtWidgets import QMessageBox, QPlainTextEdit
from qgis.core import QgsLayerTreeGroup, QgsProject, QgsVectorLayer
from qgis.PyQt.QtCore import QObject

from hhnk_threedi_plugin.hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget

BASE_FOLDER = r"\\corp.hhnk.nl\data\Hydrologen_data\Data\09.modellen_speeltuin"
TABLE_NAMES = ["HYDROOBJECT"]


@dataclass
class SchematisationBuilder:
    """
    All actions in the schematisation_builder tab of the HHNK 3Di Toolbox.

    UI includes:
    - SelectProjectLabel : QLabel
    - SelectProjectComboBox : QComboBox
    - CreateProjectLabel : QLabel
    - CreateProjectPlainTextEdit : QPlainTextEdit
    - CreateProjectPushButton : QPushButton
    - SchematisationBuilderVerticalSpacer : Spacer
    - ProjectTabWidget : QTabWidget
        - tab_status_0 : QWidget
            - SelectPolderLabel : QLabel
            - SelectPolderFileWidget : QgsFileWidget
            - ExportDAMOandHyDAMOPushButton : QPushButton
        - tab_status_1 : QWidget
            - ValidatePushButton : QPushButton
    """

    dockwidget: HHNK_toolboxDockWidget
    prewritten_text_CreateProjectPlainTextEdit: str = "Enter project name here"

    def __post_init__(self):
        """Connect all callback-functions to widgets."""
        self._setup_callbacks()
        self._initialize_ui()

    def _setup_callbacks(self):
        """Setup all widget actions."""
        dock = self.dockwidget

        # Populate the combobox
        self.populate_combobox()

        # Top-level UI actions
        dock.SelectProjectComboBox.currentIndexChanged.connect(self.on_project_selected)
        dock.CreateProjectPlainTextEdit.focusInEvent = self.create_project_text_focus
        dock.CreateProjectPushButton.clicked.connect(self.create_project)

        # Tab 0 actions
        dock.ExportDAMOandHyDAMOPushButton.clicked.connect(self.export_damo_and_hydamo)

        # Tab 1 actions
        dock.ValidatePushButton.clicked.connect(self.validate_project)

    def _initialize_ui(self):
        """Initialize UI elements with default states."""
        self.dockwidget.CreateProjectPlainTextEdit.setPlainText(self.prewritten_text_CreateProjectPlainTextEdit)
        self.dockwidget.ProjectTabWidget.setCurrentIndex(0)
        self.dockwidget.ExportDAMOandHyDAMOPushButton.setEnabled(True)

    def populate_combobox(self):
        """Populate the combobox with folder names from the base folder."""
        if os.path.exists(BASE_FOLDER):
            folder_names = [f for f in os.listdir(BASE_FOLDER) if os.path.isdir(os.path.join(BASE_FOLDER, f))]
            self.dockwidget.SelectProjectComboBox.addItems(folder_names)
        else:
            QMessageBox.warning(None, "Error", f"Base folder not found: {BASE_FOLDER}")

    def update_tab_based_on_status(self):
        """Switch to the correct tab based on the project status."""
        if self.project_status in range(self.dockwidget.ProjectTabWidget.count()):
            self.dockwidget.ProjectTabWidget.setCurrentIndex(self.project_status)
        else:
            QMessageBox.warning(None, "Error", f"Invalid project status: {self.project_status}")

    def on_project_selected(self):
        """Handle project selection from the combo box."""
        selected_folder = self.dockwidget.SelectProjectComboBox.currentText()
        full_path = os.path.join(BASE_FOLDER, selected_folder)
        self.project = Project(full_path)
        self.project_status = self.project.retrieve_project_status()
        self.update_tab_based_on_status()

    def create_project(self):
        """Handle creation of a new project."""
        project_name = self.dockwidget.CreateProjectPlainTextEdit.toPlainText()
        if project_name.strip() and project_name != self.prewritten_text_CreateProjectPlainTextEdit:
            if project_name not in os.listdir(BASE_FOLDER):
                full_path = os.path.join(BASE_FOLDER, project_name)
                self.project = Project(full_path)
                self.dockwidget.SelectProjectComboBox.addItem(project_name)
                QMessageBox.information(None, "Project", f"Project created: {project_name}")
                self.dockwidget.SelectProjectComboBox.setCurrentText(project_name)
                self.project_status = self.project.retrieve_project_status()
                self.update_tab_based_on_status()
            else:
                QMessageBox.warning(None, "Error", "Project name already exists.")
        else:
            QMessageBox.warning(None, "Error", "Project name cannot be empty or default text.")

    def create_project_text_focus(self, event):
        """Clear the text in the plain text edit when it gains focus."""
        if self.dockwidget.CreateProjectPlainTextEdit.toPlainText() == self.prewritten_text_CreateProjectPlainTextEdit:
            self.dockwidget.CreateProjectPlainTextEdit.clear()
        QPlainTextEdit.focusInEvent(self.dockwidget.CreateProjectPlainTextEdit, event)

    def load_layers_from_geopackage(self, geopackage_path, group_name):
        """
        Load all layers from a GeoPackage into QGIS and group them under a specified group name.

        Args:
            geopackage_path (str): Path to the GeoPackage file.
            group_name (str): Name of the group under which to load the layers.
        """
        if not os.path.exists(geopackage_path):
            raise FileNotFoundError(f"GeoPackage not found: {geopackage_path}")

        # Get the QGIS project instance and create/retrieve the specified group
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        group = root.findGroup(group_name) or root.addGroup(group_name)

        # Use OGR to list layers in the GeoPackage
        data_source = ogr.Open(geopackage_path)
        if not data_source:
            raise ValueError(f"Unable to open GeoPackage: {geopackage_path}")

        for i in range(data_source.GetLayerCount()):
            layer_name = data_source.GetLayerByIndex(i).GetName()
            layer_path = f"{geopackage_path}|layername={layer_name}"
            layer = QgsVectorLayer(layer_path, layer_name, "ogr")

            if layer.isValid():
                project.addMapLayer(layer, addToLegend=False)
                group.addLayer(layer)
            else:
                raise ValueError(f"Failed to load layer: {layer_name}")

    def export_damo_and_hydamo(self):
        """Handle export of DAMO and HyDAMO."""
        file_path = self.dockwidget.SelectPolderFileWidget.filePath()
        damo_gpkg_path = os.path.join(self.project.project_folder, "01_source_data", "DAMO.gpkg")

        if file_path:
            # DAMO export
            gdf_polder = gpd.read_file(file_path)
            dict_gdfs_damo = DAMO_exporter(gdf_polder, TABLE_NAMES)

            for table_name, damo_gdf in dict_gdfs_damo.items():
                damo_gdf.to_file(damo_gpkg_path, layer=table_name, driver="GPKG")

            # Load GeoPackage layers into QGIS
            try:
                damo_gpkg_path = os.path.join(self.project.project_folder, "01_source_data", "DAMO.gpkg")
                self.load_layers_from_geopackage(geopackage_path=damo_gpkg_path, group_name="DAMO")
            except Exception as e:
                QMessageBox.warning(None, "Error", f"Failed to load DAMO layers: {e}")

            # Conversion to HyDAMO
            #
            #

            QMessageBox.information(
                None, "Export", f"DAMO exported for file: {file_path}"
            )  # TODO later rename to HyDAMO
            self.project_status = 1
            self.project.update_project_status(self.project_status)
            self.update_tab_based_on_status()
            self.dockwidget.ValidatePushButton.setEnabled(True)
        else:
            QMessageBox.warning(None, "Error", "No file selected for export.")

    def validate_project(self):
        """Handle validation of the project."""
        QMessageBox.information(None, "Validation", "Validation not implemented yet.")

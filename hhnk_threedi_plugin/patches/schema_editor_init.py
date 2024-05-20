# Copyright (C) 2023 by Lutra Consulting
import os.path

from qgis.core import QgsApplication, QgsProject
from qgis.PyQt.QtGui import QCursor, QIcon
from qgis.PyQt.QtWidgets import QAction, QDialog, QMenu

import threedi_schematisation_editor.data_models as dm
from threedi_schematisation_editor.communication import UICommunication
from threedi_schematisation_editor.conversion import ModelDataConverter
from threedi_schematisation_editor.custom_widgets import ImportStructuresDialog, LoadSchematisationDialog
from threedi_schematisation_editor.processing import ThreediSchematisationEditorProcessingProvider
from threedi_schematisation_editor.user_layer_manager import LayersManager
from threedi_schematisation_editor.utils import (
    ConversionError,
    add_gpkg_connection,
    add_settings_entry,
    can_write_in_dir,
    check_enable_macros_option,
    create_empty_model,
    ensure_valid_schema,
    get_filepath,
    is_gpkg_connection_exists,
    remove_user_layers,
)


def classFactory(iface):
    return ThreediSchematisationEditorPlugin(iface)


class ThreediSchematisationEditorPlugin:
    PLUGIN_NAME = "3Di Schematisation Editor"
    THREEDI_GPKG_VAR_NAME = "threedi_gpkg_var"

    def __init__(self, iface):
        self.iface = iface
        self.uc = UICommunication(self.iface, self.PLUGIN_NAME)
        self.action_open = None
        self.action_import = None
        self.action_export = None
        self.action_export_as = None
        self.action_remove = None
        self.action_import_culverts = None
        self.model_gpkg = None
        self.layer_manager = None
        self.form_factory = None
        self.provider = ThreediSchematisationEditorProcessingProvider()
        self.project = QgsProject.instance()
        self.project.removeAll.connect(self.on_project_close)
        self.project.readProject.connect(self.on_3di_project_read)
        self.project.projectSaved.connect(self.on_3di_project_save)

    def initGui(self):
        QgsApplication.processingRegistry().addProvider(self.provider)
        self.action_open = QAction("Open 3Di Geopackage", self.iface.mainWindow())
        self.action_open.triggered.connect(self.open_model_from_geopackage)
        self.action_import = QAction("Load from Spatialite", self.iface.mainWindow())
        self.action_import.triggered.connect(self.load_from_spatialite)
        self.action_export = QAction("Save to Spatialite", self.iface.mainWindow())
        self.action_export.triggered.connect(self.save_to_default)
        self.action_export_as = QAction("Save As", self.iface.mainWindow())
        self.action_export_as.triggered.connect(self.save_to_selected)
        self.action_remove = QAction("Remove 3Di model", self.iface.mainWindow())
        self.action_remove.triggered.connect(self.remove_model_from_project)
        import_culverts_icon_path = os.path.join(os.path.dirname(__file__), "import.png")
        import_actions_spec = [
            ("Culverts", self.import_external_culverts, None),
            ("Orifices", self.import_external_orifices, None),
            ("Weirs", self.import_external_weirs, None),
            ("Pipes", self.import_external_pipes, None),
            ("Manholes", self.import_external_manholes, None),
        ]
        self.action_import_culverts = self.add_multi_action_button(
            "Import schematisation objects", import_culverts_icon_path, import_actions_spec
        )
        self.iface.addToolBarIcon(self.action_open)
        self.iface.addToolBarIcon(self.action_import)
        self.iface.addToolBarIcon(self.action_export)
        self.iface.addToolBarIcon(self.action_export_as)
        self.iface.addToolBarIcon(self.action_remove)
        self.iface.addToolBarIcon(self.action_import_culverts)
        self.toggle_active_project_actions()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
        self.iface.removeToolBarIcon(self.action_open)
        del self.action_open
        self.iface.removeToolBarIcon(self.action_import)
        del self.action_import
        self.iface.removeToolBarIcon(self.action_export)
        del self.action_export
        self.iface.removeToolBarIcon(self.action_export_as)
        del self.action_export_as
        self.iface.removeToolBarIcon(self.action_remove)
        del self.action_remove
        self.iface.removeToolBarIcon(self.action_import_culverts)
        del self.action_import_culverts

    def add_multi_action_button(self, name, icon_path, actions_specification):
        parent_window = self.iface.mainWindow()
        action_arguments = [name, parent_window]
        if icon_path:
            icon = QIcon(icon_path)
            action_arguments.insert(0, icon)
        main_action = QAction(*action_arguments)
        menu = QMenu()
        for sub_action_name, sub_action_callback, sub_icon_path in actions_specification:
            sub_action_arguments = [sub_action_name, parent_window]
            if sub_icon_path:
                sub_icon = QIcon(sub_icon_path)
                sub_action_arguments.insert(0, sub_icon)
            sub_action = QAction(*sub_action_arguments)
            sub_action.triggered.connect(sub_action_callback)
            menu.addAction(sub_action)
        main_action.setMenu(menu)
        main_action.triggered.connect(lambda: menu.exec(QCursor.pos()))
        return main_action

    def toggle_active_project_actions(self):
        if self.model_gpkg is None:
            self.action_export.setDisabled(True)
            self.action_export_as.setDisabled(True)
            self.action_remove.setDisabled(True)
            self.action_import_culverts.setDisabled(True)
        else:
            self.action_export.setEnabled(True)
            self.action_export_as.setEnabled(True)
            self.action_remove.setEnabled(True)
            self.action_import_culverts.setEnabled(True)

    def check_macros_status(self):
        macros_status = check_enable_macros_option()
        if macros_status != "Always":
            msg = (
                f"Required 'Macros enabled' option is set to '{macros_status}'. "
                "Please change it to 'Always' before making edits (Settings -> Options -> General -> Enable macros)."
            )
            self.uc.bar_warn(msg, dur=10)

    def select_user_layers_geopackage(self):
        name_filter = "3Di User Layers (*.gpkg *.GPKG)"
        filename = get_filepath(self.iface.mainWindow(), extension_filter=name_filter, save=False)
        return filename

    def select_sqlite_database(self, title):
        name_filter = "Spatialite Database (*.sqlite)"
        filename = get_filepath(self.iface.mainWindow(), extension_filter=name_filter, save=False, dialog_title=title)
        return filename

    def on_3di_project_read(self):
        self.action_export.setDisabled(True)
        custom_vars = self.project.customVariables()
        try:
            self.model_gpkg = custom_vars[self.THREEDI_GPKG_VAR_NAME]
        except KeyError:
            self.model_gpkg = None
            self.toggle_active_project_actions()
            return
        self.layer_manager = LayersManager(self.iface, self.uc, self.model_gpkg)
        self.layer_manager.load_all_layers(from_project=True)
        self.uc.bar_info("3Di User Layers registered!")
        self.check_macros_status()
        self.toggle_active_project_actions()

    def on_3di_project_save(self):
        if self.model_gpkg is not None:
            self.project.setCustomVariables({self.THREEDI_GPKG_VAR_NAME: self.model_gpkg})

    def open_model_from_geopackage(self):
        model_gpkg = self.select_user_layers_geopackage()
        if not model_gpkg:
            return
        if self.layer_manager is not None:
            self.layer_manager.remove_groups()
            self.model_gpkg = None
            self.toggle_active_project_actions()
        self.model_gpkg = model_gpkg
        self.layer_manager = LayersManager(self.iface, self.uc, self.model_gpkg)
        self.layer_manager.load_all_layers()
        self.uc.bar_info("3Di User Layers registered!")
        self.check_macros_status()
        self.project.setCustomVariables({self.THREEDI_GPKG_VAR_NAME: self.model_gpkg})
        self.toggle_active_project_actions()
        if self.model_gpkg and not is_gpkg_connection_exists(self.model_gpkg):
            add_gpkg_connection(self.model_gpkg, self.iface)

    #FIXME WvG: added src_sqlite as variable so we can call this with a function.
    #FIXME start of edits
    # def load_from_spatialite(self):
    #     schematisation_loader = LoadSchematisationDialog(self.uc)
    #     result = schematisation_loader.exec_()
    #     if result != QDialog.Accepted:
    #         return
    #     src_sqlite = schematisation_loader.selected_schematisation_sqlite

    def load_from_spatialite(self, src_sqlite=None):
        if not src_sqlite:
            schematisation_loader = LoadSchematisationDialog(self.uc)
            result = schematisation_loader.exec_()
            if result != QDialog.Accepted:
                return
            src_sqlite = schematisation_loader.selected_schematisation_sqlite
        #FIXME end of edits


        if not can_write_in_dir(os.path.dirname(src_sqlite)):
            warn_msg = "You don't have required write permissions to load data from the selected spatialite."
            self.uc.show_warn(warn_msg)
            return
        schema_version = ModelDataConverter.spatialite_schema_version(src_sqlite)
        if schema_version is None:
            warn_msg = (
                "The selected spatialite cannot be used because its schema version information is missing. "
                "Please upgrade the 3Di Schematisation Editor and try again."
            )
            self.uc.show_warn(warn_msg)
            self.uc.bar_warn("Loading from the Spatialite aborted!")
            return
        if schema_version > ModelDataConverter.SUPPORTED_SCHEMA_VERSION:
            warn_msg = (
                "The selected spatialite cannot be used because its database schema version is newer than expected. "
                "Please upgrade the 3Di Schematisation Editor and try again."
            )
            self.uc.show_warn(warn_msg)
            self.uc.bar_warn("Loading from the Spatialite aborted!")
            return
        else:
            schema_is_valid = ensure_valid_schema(src_sqlite, self.uc)
            if schema_is_valid is False:
                self.uc.bar_warn("Loading from the Spatialite aborted!")
                return
        if self.layer_manager is not None:
            self.layer_manager.remove_groups()
            self.model_gpkg = None
            self.toggle_active_project_actions()
        dst_gpkg = src_sqlite.replace(".sqlite", ".gpkg")
        converter = ModelDataConverter(src_sqlite, dst_gpkg, user_communication=self.uc)
        known_epsg = converter.set_epsg_from_sqlite()
        if known_epsg is False:
            return
        try:
            converter.create_empty_user_layers()
            converter.import_all_model_data()
        except ConversionError:
            self.uc.bar_warn("Loading from the Spatialite failed!")
            return
        if converter.missing_source_settings is True:
            add_settings_entry(dst_gpkg, id=1, epsg_code=converter.epsg_code)
        self.model_gpkg = dst_gpkg
        self.layer_manager = LayersManager(self.iface, self.uc, self.model_gpkg)
        self.layer_manager.load_all_layers()
        self.uc.show_info("Loading from the Spatialite finished!")
        self.check_macros_status()
        self.project.setCustomVariables({self.THREEDI_GPKG_VAR_NAME: self.model_gpkg})
        self.toggle_active_project_actions()
        if self.model_gpkg and not is_gpkg_connection_exists(self.model_gpkg):
            add_gpkg_connection(self.model_gpkg, self.iface)


    def save_to_selected(self):
        self.save_to_spatialite()

    def save_to_default(self):
        self.save_to_spatialite(pick_destination=False)

    def save_to_spatialite(self, pick_destination=True):
        if not self.model_gpkg:
            return
        if self.layer_manager is None:
            return
        fixed_errors_msg, unsolved_errors_msg = self.layer_manager.validate_layers()
        if unsolved_errors_msg:
            warn_msg = (
                "Saving to Spatialite failed. "
                "The following features have cross sections with incorrect table inputs:\n"
            )
            warn_msg += unsolved_errors_msg
            self.uc.show_warn(warn_msg)
            return
        self.layer_manager.stop_model_editing()
        if pick_destination:
            dst_sqlite = self.select_sqlite_database(title="Select database to save features to")
        else:
            dst_sqlite = self.model_gpkg.replace(".gpkg", ".sqlite")
        if not dst_sqlite:
            return
        if not os.path.isfile(dst_sqlite):
            warn_msg = "Target spatialite file doesn't exist. Saving to spatialite canceled."
            self.uc.show_warn(warn_msg)
            return
        if not can_write_in_dir(os.path.dirname(dst_sqlite)):
            warn_msg = "You don't have required write permissions to save data into the selected spatialite."
            self.uc.show_warn(warn_msg)
            return
        schema_version = ModelDataConverter.spatialite_schema_version(dst_sqlite)
        if schema_version > ModelDataConverter.SUPPORTED_SCHEMA_VERSION:
            warn_msg = (
                "The selected spatialite cannot be used because its database schema version is newer than expected. "
                "Please upgrade the 3Di Schematisation Editor and try again."
            )
            self.uc.show_warn(warn_msg)
            return
        else:
            schema_is_valid = ensure_valid_schema(dst_sqlite, self.uc)
            if schema_is_valid is False:
                return
        converter = ModelDataConverter(dst_sqlite, self.model_gpkg, user_communication=self.uc)
        known_epsg = converter.set_epsg_from_gpkg()
        if known_epsg is False:
            return
        converter.trim_sqlite_targets()
        converter.report_conversion_errors()
        converter.export_all_model_data()
        self.uc.show_info("Saving to the Spatialite finished!")

    def save_to_spatialite_on_action(self):
        model_modified = self.layer_manager.model_modified()
        if model_modified:
            title = "Save to Spatialite?"
            question = "Would you like to save model to Spatialite before closing project?"
            answer = self.uc.ask(None, title, question)
            if answer is True:
                self.save_to_spatialite()

    def remove_model_from_project(self):
        if not self.model_gpkg:
            return
        if self.layer_manager is not None:
            self.save_to_spatialite_on_action()
            self.layer_manager.remove_groups()
            self.model_gpkg = None
        custom_vars = self.project.customVariables()
        if self.THREEDI_GPKG_VAR_NAME in custom_vars:
            del custom_vars[self.THREEDI_GPKG_VAR_NAME]
            self.project.setCustomVariables(custom_vars)
        self.toggle_active_project_actions()
        self.iface.mapCanvas().refresh()

    def import_external_culverts(self):
        if not self.model_gpkg:
            return
        import_culverts_dlg = ImportStructuresDialog(dm.Culvert, self.model_gpkg, self.layer_manager, self.uc)
        import_culverts_dlg.exec_()

    def import_external_orifices(self):
        if not self.model_gpkg:
            return
        import_orifices_dlg = ImportStructuresDialog(dm.Orifice, self.model_gpkg, self.layer_manager, self.uc)
        import_orifices_dlg.exec_()

    def import_external_weirs(self):
        if not self.model_gpkg:
            return
        import_weirs_dlg = ImportStructuresDialog(dm.Weir, self.model_gpkg, self.layer_manager, self.uc)
        import_weirs_dlg.exec_()

    def import_external_pipes(self):
        import_pipes_dlg = ImportStructuresDialog(dm.Pipe, self.model_gpkg, self.layer_manager, self.uc)
        import_pipes_dlg.exec_()

    def import_external_manholes(self):
        import_manholes_dlg = ImportStructuresDialog(dm.Manhole, self.model_gpkg, self.layer_manager, self.uc)
        import_manholes_dlg.exec_()

    def on_project_close(self):
        if self.layer_manager is None:
            return
        self.save_to_spatialite_on_action()
        self.layer_manager.remove_loaded_layers(dry_remove=True)
        self.layer_manager = None
        self.model_gpkg = None
        self.toggle_active_project_actions()

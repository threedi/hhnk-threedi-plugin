from hhnk_threedi_tools.core.checks.model_state import (
    collect_excluded,
    collect_manual_adjustments,
    get_all_update_queries,
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTabWidget


class modelChangesTabs(QTabWidget):
    collect_changes = pyqtSignal()

    def __init__(self, parent):
        super(modelChangesTabs, self).__init__(parent)
        self.global_settings = None
        self.bank_levels = None
        self.new_manholes = None
        self.update_manholes = None
        self.weirs = None
        self.channels = None
        self.excluded_ids = None
        self.manual_changes = None
        self.queries_list = []

    def collect_queries(self):
        """
        collects arguments to pass to collect_all_queries
        """
        arguments = {}
        if self.global_settings is not None:
            arguments["global_settings_df"] = self.global_settings.df
            arguments["global_settings_excluded"] = self.global_settings.protected_ids_list
            arguments["global_settings_to_add"] = self.global_settings.add_rows_ids
            arguments["global_settings_to_delete"] = self.global_settings.delete_rows_ids
        if self.bank_levels is not None:
            arguments["bank_levels_df"] = self.bank_levels.df
            arguments["bank_levels_excluded"] = self.bank_levels.protected_ids_list
        if self.new_manholes is not None:
            arguments["new_manholes_df"] = self.new_manholes.df
            arguments["new_manholes_excluded"] = self.new_manholes.protected_ids_list
        if self.update_manholes is not None:
            arguments["update_manholes_df"] = self.update_manholes.df
            arguments["update_manholes_excluded"] = self.update_manholes.protected_ids_list
        if self.weirs is not None:
            arguments["weir_width_df"] = self.weirs.df
            arguments["weir_width_excluded"] = self.weirs.protected_ids_list
        if self.channels is not None:
            arguments["channels_df"] = self.channels.df
            arguments["channels_excluded"] = self.channels.protected_ids_list
        queries = get_all_update_queries(**arguments)
        return queries

    def collect_exceptions_queries(self):
        """
        If a user can change values in a tab, we return these changes to them once the changes
        to the model have been executed.
        """
        skipped_arguments = {}
        manual_arguments = {}
        if self.global_settings is not None:
            skipped_arguments["global_settings_excluded"] = self.global_settings.protected_ids_list
            manual_arguments["global_settings_manual_df"] = self.global_settings.manual_changes_df
        if self.bank_levels is not None:
            skipped_arguments["bank_levels_excluded"] = self.bank_levels.protected_ids_list
            manual_arguments["bank_levels_manual_df"] = self.bank_levels.manual_changes_df
        if self.new_manholes is not None:
            skipped_arguments["new_manholes_excluded"] = self.new_manholes.protected_ids_list
        if self.update_manholes is not None:
            skipped_arguments["manhole_updates_excluded"] = self.update_manholes.protected_ids_list
            manual_arguments["manhole_update_manual_df"] = self.update_manholes.manual_changes_df
        if self.weirs is not None:
            skipped_arguments["weirs_heights_excluded"] = self.weirs.protected_ids_list
            manual_arguments["weir_widths_manual_df"] = self.weirs.manual_changes_df
        if self.channels is not None:
            skipped_arguments["weirs_heights_excluded"] = self.channels.protected_ids_list
            manual_arguments["channels_manual_df"] = self.channels.manual_changes_df
        skipped_rows = collect_excluded(**skipped_arguments)
        manual_changes = collect_manual_adjustments(**manual_arguments)
        return skipped_rows, manual_changes

    def add_global_settings_tab(self, new_widget, name="global settings"):
        self.global_settings = new_widget
        if new_widget:
            self.collect_changes.connect(self.global_settings.return_changed_value_rows)
            self.addTab(self.global_settings, name)

    def add_channels_tab(self, new_widget, name="watergangen"):
        self.channels = new_widget
        if new_widget:
            self.collect_changes.connect(self.channels.return_changed_value_rows)
            self.addTab(self.channels, name)

    def add_bank_levels_tab(self, new_widget, name="bank levels"):
        self.bank_levels = new_widget
        if new_widget:
            self.collect_changes.connect(self.bank_levels.return_changed_value_rows)
            self.addTab(self.bank_levels, name)

    def add_new_manholes_tab(self, new_widget, name="putten toevoegen"):
        self.new_manholes = new_widget
        if new_widget:
            self.collect_changes.connect(self.new_manholes.return_changed_value_rows)
            self.addTab(self.new_manholes, name)

    def add_update_manholes_tab(self, new_widget, name="putten aanpassen"):
        self.update_manholes = new_widget
        if new_widget:
            self.collect_changes.connect(self.update_manholes.return_changed_value_rows)
            self.addTab(self.update_manholes, name)

    def add_weir_widths_tab(self, new_widget, name="gestuurde stuwen"):
        self.weirs = new_widget
        if new_widget:
            self.collect_changes.connect(self.weirs.return_changed_value_rows)
            self.addTab(self.weirs, name)

    def add_manual_changes_tab(self, new_widget, name="Handmatige aanpassingen"):
        self.manual_changes = new_widget
        if new_widget:
            self.addTab(self.manual_changes, name)

    def add_excluded_ids_tab(self, new_widget, name="Uitgesloten rijen"):
        self.excluded_ids = new_widget
        if new_widget:
            self.addTab(self.excluded_ids, name)

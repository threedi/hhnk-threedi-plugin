from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QTextEdit
from PyQt5.QtCore import pyqtSignal
from qgis.utils import QgsMessageBar, Qgis
from hhnk_threedi_plugin.gui.checks.bank_levels_widgets.proposed_changes_tabs import modelChangesTabs
from hhnk_threedi_plugin.gui.checks.bank_levels_widgets.proposed_changes_exceptions import exceptionsWidget
from hhnk_threedi_plugin.tasks.execute_model_changes import executeModelChangesTask

# hhnk-threedi-tests
from hhnk_threedi_tools.variables.model_state import (
    one_d_two_d_from_calc,
    one_d_two_d_state,
)
from hhnk_threedi_tools.core.checks.model_backup import update_bank_levels_last_calc


class modelChangesDialog(QDialog):
    exceptions_collected = pyqtSignal(str, str)
    query_execution_task_created = pyqtSignal(object)

    def __init__(self, model_path, parent, to_state, one_d_two_d_source=None):
        super().__init__(parent)
        self.to_state = to_state
        self.one_d_two_d_source = one_d_two_d_source
        self.setMinimumWidth(300)
        self.setWindowTitle("Voorgestelde aanpassingen conversie model")
        self.model_path = model_path
        self.message_bar = QgsMessageBar()
        self.tabs = modelChangesTabs(self)
        self.no_changes_message = QLabel("Geen aanpassingen nodig")
        self.accept_button = QPushButton("Aanpassingen uitvoeren")
        self.accept_button.clicked.connect(self.submit_done)
        layout = QVBoxLayout()
        layout.addWidget(self.message_bar)
        layout.addWidget(self.tabs)
        layout.addWidget(self.accept_button)
        layout.addWidget(self.no_changes_message)
        self.setLayout(layout)

    def update_bank_levels_calculated(self):
        """
        Updates timestamp when bank levels were last calculated
        """
        if (
            self.to_state == one_d_two_d_state
            and self.one_d_two_d_source == one_d_two_d_from_calc
        ):
            update_bank_levels_last_calc(db=self.model_path)

    def handle_execution_result_success(self):
        """
        If model changes were executed successfully, we collect all skipped id's and manual changes
        and return them to the user. This function is executed regardless of whether or not actual changes were
        made to the model.
        """
        skipped_rows, manual_changes = self.tabs.collect_exceptions_queries()
        self.update_bank_levels_calculated()
        if skipped_rows or manual_changes:
            self.tabs.clear()
            if skipped_rows:
                excluded_widget = exceptionsWidget(skipped_rows)
                self.tabs.add_excluded_ids_tab(excluded_widget)
            if manual_changes:
                manual_widget = exceptionsWidget(manual_changes)
                self.tabs.add_manual_changes_tab(manual_widget)
            self.accept_button.setText("Sluiten")
            self.accept_button.clicked.disconnect(self.submit_done)
            self.accept_button.clicked.connect(self.accept)
            self.show()
        else:
            self.accept()

    def handle_execution_result_failed(self, error):
        self.message_bar.pushMessage(
            f"Model aanpassingen konden niet worden uitgevoerd: \n{str(error)}",
            Qgis.Critical,
        )

    def submit_done(self):
        """
        Collect excluded ids and manual changes
        compose queries and try to execute
        If successful, remove tabs and accept button, changes title to show
        manual changes and exceptions
        Else, show error
        """
        self.tabs.collect_changes.emit()
        queries = self.tabs.collect_queries()
        try:
            if self.model_path is None:
                raise Exception(
                    "No database has been specified (modelChangesDialog.model_path not set)"
                )
            if queries:
                model_changes_task = executeModelChangesTask(
                    model_path=self.model_path, query=queries
                )
                self.query_execution_task_created.emit(model_changes_task)
            else:
                self.handle_execution_result_success()
        except Exception as e:
            raise e from None

    def has_changes(self):
        """
        If there are no tabs, then nothing needs to be changed.
        We don't show changes but a message informing the user of this.

        If there are no proposed changes to bank levels, we set the last calculated
        time to now
        """
        changes_to_show = self.tabs.count() > 0
        # If there are no bank levels to change and no new manholes to be added,
        # we still consider the current bank levels and manholes state as 1d2d appropriate
        if self.tabs.bank_levels is None and self.tabs.new_manholes is None:
            self.update_bank_levels_calculated()
        self.tabs.setHidden(not changes_to_show)
        self.accept_button.setHidden(not changes_to_show)
        self.no_changes_message.setHidden(changes_to_show)

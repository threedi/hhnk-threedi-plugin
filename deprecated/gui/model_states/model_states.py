import os
from PyQt5.QtWidgets import (
    QDialog,
    QFileDialog,
    QVBoxLayout,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QComboBox,
    QGroupBox,
    QCheckBox,
    QDialogButtonBox,
)
from PyQt5.QtCore import Qt, pyqtSignal
from qgis.core import Qgis
from qgis.utils import QgsMessageBar
from ..utility.file_widget import fileWidget
from .verify_model_states_input import verify_input

# hhnk-threedi-tests

from hhnk_threedi_tools.qgis import modelConversionVariables
from hhnk_threedi_tools.qgis import testEnvironment
from hhnk_threedi_tools.variables.backups_table_names import BANK_LVLS_LAST_CALC
from hhnk_threedi_tools.variables.model_state import (
    one_d_two_d_from_calc,
    hydraulic_test_state,
    one_d_two_d_state,
    one_d_two_d_keep,
)
from hhnk_threedi_tools.utils.queries import bank_lvls_last_changed

import hhnk_research_tools as hrt
from hhnk_threedi_tools.qgis.build_threedi_paths_dict import (
    build_threedi_source_paths_dict,
)


def setup_ui(model_state_widget):
    model_state_widget.setMinimumWidth(400)
    # Creates items to be in widget
    model_state_widget.bar = QgsMessageBar()
    model_state_widget.model_selector = fileWidget(
        select_text="Selecteer model:",
        file_dialog_title="Selecteer een model ('.sqlite')",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.sqlite",
    )
    model_state_widget.current_state_label = QLabel("Huidige model staat:")
    model_state_widget.current_state_show = QLabel("Geen (geldig) model geselecteerd")
    model_state_widget.new_state_selector_label = QLabel("Selecteer nieuwe staat:")
    model_state_widget.new_state_selector = QComboBox()
    model_state_widget.new_state_selector.addItems(["Hydraulische toets", "1d2d toets"])
    model_state_widget.one_d_two_d_group = QGroupBox(title="1d2d staat informatie")
    model_state_widget.one_d_two_d_group.setEnabled(False)
    model_state_widget.one_d_two_d_info_group = QGroupBox(
        title="Bereken op basis van 3di resultaat"
    )
    model_state_widget.one_d_two_d_info_group.setCheckable(True)
    model_state_widget.one_d_two_d_info_group.setChecked(True)
    model_state_widget.result_selector = fileWidget(
        select_text="Selecteer 3di resultaat",
        file_dialog_title="Selecteer 3di revisie map " "(bevat .nc en .h5 files)",
        file_mode=QFileDialog.Directory,
    )
    model_state_widget.datachecker_selector = fileWidget(
        select_text="Selecteer datachecker output:",
        file_dialog_title="Selecteer datachecker output (.gdb)",
        file_mode=QFileDialog.Directory,
    )
    model_state_widget.keep_values = QCheckBox("Behoud laatst berekende waarden")
    model_state_widget.bank_levels_last_calculated_label = QLabel(
        "Bank levels laatst berekend:"
    )
    model_state_widget.bank_levels_last_calculated_show = QLabel("")
    model_state_widget.buttons = QDialogButtonBox(
        QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    )

    # Creates layout
    message_bar_layout = QVBoxLayout()
    model_selector_layout = QVBoxLayout()
    model_selector_layout.setAlignment(Qt.AlignTop)
    curr_model_state_layout = QVBoxLayout()
    curr_model_state_layout.setAlignment(Qt.AlignTop)
    new_model_state_layout = QVBoxLayout()
    new_model_state_layout.setAlignment(Qt.AlignTop)
    group_box_layout = QVBoxLayout()
    group_box_layout.setAlignment(Qt.AlignTop)
    file_selection_layout = QVBoxLayout()

    # Add widgets to layout
    message_bar_layout.addWidget(model_state_widget.bar)
    model_selector_layout.addWidget(model_state_widget.model_selector)
    curr_model_state_layout.addWidget(
        model_state_widget.current_state_label, alignment=Qt.AlignTop
    )
    curr_model_state_layout.addWidget(
        model_state_widget.current_state_show, alignment=Qt.AlignTop
    )
    new_model_state_layout.addWidget(
        model_state_widget.new_state_selector_label, alignment=Qt.AlignTop
    )
    new_model_state_layout.addWidget(
        model_state_widget.new_state_selector, alignment=Qt.AlignTop
    )
    file_selection_layout.addWidget(
        model_state_widget.result_selector, alignment=Qt.AlignTop
    )
    model_state_widget.one_d_two_d_info_group.setLayout(file_selection_layout)
    group_box_layout.addWidget(model_state_widget.one_d_two_d_info_group)
    group_box_layout.addWidget(model_state_widget.keep_values)
    group_box_layout.addWidget(model_state_widget.bank_levels_last_calculated_label)
    group_box_layout.addWidget(model_state_widget.bank_levels_last_calculated_show)
    model_state_widget.one_d_two_d_group.setLayout(group_box_layout)
    file_selection_layout.addWidget(model_state_widget.datachecker_selector)

    # Combine all sections into main layout
    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.addLayout(message_bar_layout)
    main_layout.addLayout(model_selector_layout)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    main_layout.addLayout(curr_model_state_layout)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    main_layout.addLayout(new_model_state_layout)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    main_layout.addWidget(model_state_widget.one_d_two_d_group)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    main_layout.addWidget(model_state_widget.buttons)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    model_state_widget.setLayout(main_layout)


class modelStateDialog(QDialog):
    """
    Initialization:
        modelStateDialog(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))
    Signals:
    start_conversion(object (test_env))
    """

    start_conversion = pyqtSignal(object)

    def __init__(self, caller, parent):
        super(modelStateDialog, self).__init__(parent)
        setup_ui(self)
        self.setWindowTitle("Model staat aanpassen")
        # ----------------------------------------------------------
        # Variables
        # ----------------------------------------------------------
        self.caller = caller
        self.from_state = None
        self.to_state = (
            hydraulic_test_state
            if self.new_state_selector.currentIndex() == 0
            else one_d_two_d_state
        )
        self.one_d_two_d_from = (
            one_d_two_d_from_calc
            if self.one_d_two_d_info_group.isChecked()
            else one_d_two_d_keep
        )
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        self.setup_main_paths_signals()
        # If the model changes, update the model state display
        self.model_selector.fileSelected.connect(self.model_changed)
        # Toggle the 1d2d information fields: we only need them to convert to 1d2d
        self.new_state_selector.currentIndexChanged.connect(self.toggle_1d2d_group)
        # If a user selects a source for conversion to 1d2d state, update the one_d_two_d_from variable
        self.keep_values.clicked.connect(self.toggle_checkboxes)
        self.one_d_two_d_info_group.clicked.connect(self.toggle_checkboxes)
        # Close on cancel
        self.buttons.rejected.connect(self.close)
        # Verify on accept
        self.buttons.accepted.connect(self.verify_submit)
        self.parent().model_splitter_btn.clicked.connect(self.model_changed)
        self.model_changed()

    def set_current_paths(self):
        """
        Sets current paths as known to main widget to this widget's fields
        """
        paths = self.caller.current_source_paths
        if paths is not None:
            self.model_selector.setFilePath(paths["model"])
            self.datachecker_selector.setFilePath(paths["datachecker"])
            self.current_state_show.setText(self.parent().model_state_show.text())

    def toggle_1d2d_group(self):
        """
        Enables the selection box associated with converting to 1d2d test state if
        converting to 1d2d is selected. Disables it if converting to hydraulic test state
        is selected.
        If current index is 0, hydraulic test is selected
        If current index is 1, 1d2d state is selected
        """
        current_index = self.new_state_selector.currentIndex()
        if current_index == 0:
            self.to_state = hydraulic_test_state
            self.one_d_two_d_group.setEnabled(False)
        elif current_index == 1:
            self.to_state = one_d_two_d_state
            self.one_d_two_d_group.setEnabled(True)

    def toggle_checkboxes(self):
        """
        Handles exclusivity within the one_d_two_d_group: only one of one_d_two_d_info_group and keep_values
        can be checked at any time
        """
        origin = self.sender()
        if origin == self.keep_values:
            if self.keep_values.isChecked():
                self.one_d_two_d_info_group.setChecked(False)
                self.one_d_two_d_from = one_d_two_d_keep
            else:
                if not self.one_d_two_d_info_group.isChecked():
                    self.keep_values.setChecked(True)
                    self.one_d_two_d_from = one_d_two_d_keep
        if origin == self.one_d_two_d_info_group:
            if self.one_d_two_d_info_group.isChecked():
                self.keep_values.setChecked(False)
                self.one_d_two_d_from = one_d_two_d_from_calc
            else:
                if not self.keep_values.isChecked():
                    self.one_d_two_d_info_group.setChecked(True)
                    self.one_d_two_d_from = one_d_two_d_from_calc

    def setup_main_paths_signals(self):
        """
        Connects changes in fields (for example the selection of a file) to the function
        that updates (and keeps track of) the current fields for the entire plugin
        """
        self.model_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(model=path)
        )
        self.datachecker_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(datachecker=path)
        )

    def model_changed(self):
        """
        If the model path changes, gets the new state as string from the main plugin's
        display of the state. Also checks whether bank levels were calculated before
        and if so, shows when this last happened
        """
        model_state = self.parent().model_state_show.text()
        self.current_state_show.setText(model_state)
        self.from_state = model_state
        model_path = self.model_selector.filePath()
        if os.path.exists(model_path):
            if hrt.sql_table_exists(
                database_path=model_path, table_name=BANK_LVLS_LAST_CALC
            ):
                try:
                    last_changed_df = hrt.execute_sql_selection(
                        query=bank_lvls_last_changed, database_path=model_path
                    )
                    self.bank_levels_last_calculated_show.setText(
                        last_changed_df["dt"][0]
                    )
                except:
                    self.bank_levels_last_calculated_show.setText(
                        "Geen tijdstip gevonden van eerdere berekening"
                    )
            else:
                self.bank_levels_last_calculated_show.setText(
                    "Bank levels niet eerder berekend"
                )

    def create_test_environment(self):
        """
        Gathers all information of gui needed to run the associated tests
        """
        base_paths = self.caller.current_source_paths.copy()
        threedi_paths = {}
        if (
            self.to_state == one_d_two_d_state
            and self.one_d_two_d_from == one_d_two_d_from_calc
        ):
            threedi_paths = build_threedi_source_paths_dict(
                revision_path=self.result_selector.filePath()
            )
        src_paths = {}
        src_paths.update(base_paths)
        src_paths.update(threedi_paths)

        conversion_vars = modelConversionVariables(
            from_state=self.from_state,
            to_state=self.to_state,
            one_d_two_d_source=self.one_d_two_d_from,
        )
        test_environment = testEnvironment(
            source_paths_dict=src_paths, conversion_vars=conversion_vars
        )
        test_environment.revision_path = self.result_selector.filePath()

        return test_environment

    def verify_submit(self):
        """
        Checks whether all fields are correctly filled
        """
        res, message = verify_input(
            model_path=self.model_selector.file_selected_edit.text(),
            from_state=self.from_state,
            to_state=self.to_state,
            one_d_two_d_from=self.one_d_two_d_from,
            threedi_result_folder=self.result_selector.filePath(),
            datachecker_path=self.datachecker_selector.filePath(),
        )
        if res:
            test_environment = self.create_test_environment()
            self.start_conversion.emit(test_environment)
            self.accept()
        else:
            self.bar.pushMessage(message, Qgis.Critical)
import os
from PyQt5.QtWidgets import (
    QPushButton,
    QFileDialog,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
    QWidget,
    QSpacerItem,
)
from ...general_objects import revisionsComboBox
from PyQt5.QtCore import Qt, pyqtSignal
from pathlib import Path
from qgis.core import Qgis
from ...utility.file_widget import fileWidget
from .verify_bank_levels_input import verify_input
from ....qgis_interaction.layers_management.layers.get_layers_list import (
    get_layers_list,
)
from ....gui.path_verification_functions import is_valid_results_folder
from ....qgis_interaction.layers_management.groups.layer_groups_structure import (
    QgisLayerStructure,
)


# old
# from hhnk_threedi_tools.folder_structure_and_paths.get_working_paths import get_working_paths
# from hhnk_threedi_tools.tests.test_environment import testEnvironment
# from hhnk_threedi_tools.folder_structure_and_paths.paths_functions import get_top_level_directories

# hhnk-threedi-tests
from hhnk_threedi_tools.qgis.get_working_paths import get_working_paths
from hhnk_threedi_tools.qgis.paths_functions import get_top_level_directories
from hhnk_threedi_tools.qgis.environment import testEnvironment


def setupUi(bank_levels_widget):
    # Create button to start tests
    bank_levels_widget.start_bank_levels_btn = QPushButton("Begin tests")

    # Create all file widgets
    bank_levels_widget.results_dir_selector = fileWidget(
        select_text="Selecteer 3di resultaat map:",
        file_dialog_title="Selecteer 3di resultaten map " "(bevat revisie mappen)",
        file_mode=QFileDialog.Directory,
    )
    bank_levels_widget.select_revision_box = revisionsComboBox()
    bank_levels_widget.select_revision_label = QLabel("Selecteer revisie:")
    bank_levels_widget.result_selected_show_label = QLabel("Geselecteerde revisie: ")
    bank_levels_widget.result_selected_show = QLabel("Geen revisie geselecteerd")
    bank_levels_widget.model_selector = fileWidget(
        select_text="Selecteer model:",
        file_dialog_title="Selecteer een model (.sqlite)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.sqlite",
    )
    bank_levels_widget.datachecker_selector = fileWidget(
        select_text="Selecteer datachecker output:",
        file_dialog_title="Selecteer datachecker output (.gdb)",
        file_mode=QFileDialog.Directory,
    )
    bank_levels_widget.output_selector = fileWidget(
        select_text="Selecteer output map:",
        file_dialog_title="Selecteer map om output in aan te maken",
        file_mode=QFileDialog.Directory,
    )

    # Main layout
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.addWidget(bank_levels_widget.results_dir_selector)
    main_layout.addWidget(bank_levels_widget.select_revision_label)
    main_layout.addWidget(bank_levels_widget.select_revision_box)
    main_layout.addWidget(bank_levels_widget.result_selected_show_label)
    main_layout.addWidget(bank_levels_widget.result_selected_show)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(bank_levels_widget.model_selector)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(bank_levels_widget.datachecker_selector)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(bank_levels_widget.output_selector)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(bank_levels_widget.start_bank_levels_btn)
    bank_levels_widget.setLayout(main_layout)


class bankLevelsWidget(QWidget):
    """
    Initialization:
        bankLevelsWidget(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))

    Signals:

    start_bank_levels_tests(object (test_env))
    """

    start_bank_levels_tests = pyqtSignal(object)

    def __init__(self, caller, parent=None):
        super(bankLevelsWidget, self).__init__(parent)
        setupUi(self)
        # ----------------------------------------------------------
        # Variables
        # ----------------------------------------------------------
        self.caller = caller
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        self.setup_main_paths_signals()
        self.start_bank_levels_btn.clicked.connect(self.verify_submit)
        self.select_revision_box.currentIndexChanged.connect(self.set_revision_text)
        # self.select_revision_box.aboutToShowPopup.connect(
        #     lambda: self.populate_revision_box(self.results_dir_selector.filePath())
        # )
        # self.results_dir_selector.fileSelected.connect(self.populate_revision_box)

    def set_revision_text(self):
        current_rev_text = self.select_revision_box.currentText()
        if not current_rev_text:
            current_rev_text = "Geen revisie geselecteerd"
        self.result_selected_show.setText(current_rev_text)

    def populate_revisions_combobox(self):
        """
        Accumulates a list of valid 3di results (directories) and populates the revision selection
        combobox from this list
        """
        revisions = self.caller.fenv.threedi_results.one_d_two_d.revisions
        if len(revisions) == 0:
            self.select_revision_box.setEnabled(False)
            return
        self.select_revision_box.clear()
        self.select_revision_box.addItem("")
        for revision in revisions:
            self.select_revision_box.addItem(revision)

    def create_test_environment(self):
        """Collect all needed variables to run tests"""
        src_paths, output_dict = get_working_paths(
            test_type=3,
            active_paths=self.caller.current_source_paths,
            base_folder_output=self.output_selector.filePath(),
            threedi_results_path=self.results_dir_selector.filePath(),
            threedi_revision_name=self.select_revision_box.currentText(),
        )
        layer_groups_structure = QgisLayerStructure()
        layers = get_layers_list(
            test_type=3,
            plugin_dir=self.caller.plugin_dir,
            output_dict=output_dict,
            group_structure=layer_groups_structure,
        )
        test_environment = testEnvironment(
            source_paths_dict=src_paths,
            output_vars_dict=output_dict,
            layers=layers,
            group_structure=layer_groups_structure,
        )

        test_environment.revision_path = (
            self.results_dir_selector.filePath()
            + "/"
            + self.select_revision_box.currentText()
        )

        return test_environment

    def verify_submit(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """
        res, message = verify_input(
            model_path=self.model_selector.filePath(),
            datachecker_path=self.datachecker_selector.filePath(),
            output_path=self.output_selector.filePath(),
            revision_selected=self.select_revision_box.currentText(),
        )
        if not res:
            self.caller.iface.messageBar().pushMessage(message, Qgis.Critical)
        else:
            test_environment = self.create_test_environment()
            self.start_bank_levels_tests.emit(test_environment)

    def setup_main_paths_signals(self):
        """
        Connects changes in fields (for example the selection of a file) to the function
        that updates (and keeps track of) the current fields for the entire plugin
        """
        self.datachecker_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(datachecker=path)
        )
        self.model_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(model=path)
        )
        self.output_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(bank_levels_output=path)
        )

    def set_current_paths(self):
        """
        Sets current paths as known to main widget to this widget's fields
        """
        paths = self.caller.current_source_paths
        if paths is not None:
            self.model_selector.setFilePath(paths["model"])
            self.datachecker_selector.setFilePath(paths["datachecker"])
            self.output_selector.setFilePath(paths["bank_levels_output"])
            self.results_dir_selector.setFilePath(paths["1d2d_results_dir"])
            self.populate_revisions_combobox()

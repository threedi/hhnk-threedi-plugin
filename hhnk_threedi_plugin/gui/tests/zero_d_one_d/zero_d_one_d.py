import os
from pathlib import Path
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QFileDialog,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QVBoxLayout,
)
from ...general_objects import revisionsComboBox
from qgis.core import Qgis
from PyQt5.QtCore import Qt, pyqtSignal
from ...utility.file_widget import fileWidget
from .verify_zero_d_one_d_ui import verify_input
from ....gui.path_verification_functions import is_valid_results_folder
from ....qgis_interaction.layers_management.layers.get_layers_list import (
    get_layers_list,
)
from ...utility_functions import get_revision
from ....qgis_interaction.layers_management.groups.layer_groups_structure import (
    QgisLayerStructure,
)

# hhnk-threedi-tests
from hhnk_threedi_tools.qgis.get_working_paths import get_working_paths
from hhnk_threedi_tools.qgis.environment import testEnvironment
from hhnk_threedi_tools.qgis.paths_functions import get_top_level_directories


def setupUi(zero_d_one_d_widget):
    # Create button to start tests
    zero_d_one_d_widget.start_0d1d_tests_btn = QPushButton("Begin tests")

    # Create all file widgets
    zero_d_one_d_widget.results_dir_selector = fileWidget(
        select_text="Selecteer 3di resultaat map:",
        file_dialog_title="Selecteer 3di revisie map " "(bevat .nc en .h5 files)",
        file_mode=QFileDialog.Directory,
    )
    zero_d_one_d_widget.select_revision_box = revisionsComboBox()
    zero_d_one_d_widget.select_revision_label = QLabel("Selecteer revisie:")
    zero_d_one_d_widget.result_selected_show_label = QLabel("Geselecteerde revisie: ")
    zero_d_one_d_widget.result_selected_show = QLabel("Geen revisie geselecteerd")
    zero_d_one_d_widget.output_selector = fileWidget(
        select_text="Selecteer output map:",
        file_dialog_title="Selecteer map om output in aan te maken",
        file_mode=QFileDialog.Directory,
    )

    # Main layout
    zero_d_one_d_widget.main_layout = QVBoxLayout(zero_d_one_d_widget)
    zero_d_one_d_widget.main_layout.setAlignment(Qt.AlignTop)
    zero_d_one_d_widget.main_layout.setContentsMargins(25, 25, 25, 25)
    zero_d_one_d_widget.main_layout.addWidget(zero_d_one_d_widget.results_dir_selector)
    zero_d_one_d_widget.main_layout.addWidget(zero_d_one_d_widget.select_revision_label)
    zero_d_one_d_widget.main_layout.addWidget(zero_d_one_d_widget.select_revision_box)
    zero_d_one_d_widget.main_layout.addSpacerItem(
        QSpacerItem(25, 5, QSizePolicy.Expanding)
    )
    zero_d_one_d_widget.main_layout.addWidget(
        zero_d_one_d_widget.result_selected_show_label
    )
    zero_d_one_d_widget.main_layout.addWidget(zero_d_one_d_widget.result_selected_show)
    zero_d_one_d_widget.main_layout.addSpacerItem(
        QSpacerItem(25, 5, QSizePolicy.Expanding)
    )
    zero_d_one_d_widget.main_layout.addWidget(zero_d_one_d_widget.output_selector)
    zero_d_one_d_widget.main_layout.addSpacerItem(
        QSpacerItem(25, 5, QSizePolicy.Expanding)
    )
    zero_d_one_d_widget.main_layout.addWidget(zero_d_one_d_widget.start_0d1d_tests_btn)


class zeroDOneDWidget(QWidget):
    """
    Initialization:
        zeroDOneDWidget(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))

    Signals:

    start_0d1d_tests(object (test_env))
    """

    start_0d1d_tests = pyqtSignal(object)

    def __init__(self, caller, parent=None):
        super(zeroDOneDWidget, self).__init__(parent)
        setupUi(self)
        # ----------------------------------------------------------
        # Variables
        # ----------------------------------------------------------
        self.caller = caller
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        # self.setup_main_paths_signals()
        # If the results directory changes, populate the combobox (to choose a revision)
        # self.results_dir_selector.fileSelected.connect(self.populate_revisions_combobox)
        # self.select_revision_box.aboutToShowPopup.connect(
        #     lambda: self.populate_revisions_combobox(
        #         self.results_dir_selector.filePath()
        #     )
        # )
        # Geef geselecteerde revisie weer
        self.select_revision_box.currentIndexChanged.connect(self.set_revision_text)
        self.start_0d1d_tests_btn.clicked.connect(self.verify_submit)
        self.select_revision_box.aboutToShowPopup.connect(
            self.populate_revisions_combobox
        )
    def create_test_environment(self):
        """
        Gathers all information needed to run the associated tests
        """
        src_paths, output_dict = get_working_paths(
            test_type=2,
            active_paths=self.caller.current_source_paths,
            base_folder_output=self.output_selector.filePath(),
            threedi_results_path=self.results_dir_selector.filePath(),
            threedi_revision_name=self.select_revision_box.currentText(),
        )
        layer_groups_structure = QgisLayerStructure(
            zero_d_revision=get_revision(self.select_revision_box.currentText())
        )
        layers = get_layers_list(
            test_type=2,
            plugin_dir=self.caller.plugin_dir,
            output_dict=output_dict,
            group_structure=layer_groups_structure,
        )  # TODO
        test_environment = testEnvironment(
            source_paths_dict=src_paths,
            output_vars_dict=output_dict,
            layers=layers,
            group_structure=layer_groups_structure,
        )
        return test_environment

    def verify_submit(self):
        """
        Checks whether all fields are correctly filled
        """
        res, message = verify_input(
            output_path=self.output_selector.filePath(),
            revision_selected=self.select_revision_box.currentText(),
        )
        if not res:
            self.caller.iface.messageBar().pushMessage(message, Qgis.Critical)
        else:
            test_environment = self.create_test_environment()
            self.start_0d1d_tests.emit(test_environment)

    def set_revision_text(self):
        current_rev_text = self.select_revision_box.currentText()
        if not current_rev_text:
            current_rev_text = "Geen revisie geselecteerd"
        self.result_selected_show.setText(current_rev_text)

    def setup_main_paths_signals(self):
        """
        Connects changes in fields (for example the selection of a file) to the function
        that updates (and keeps track of) the current fields for the entire plugin
        """
        self.results_dir_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(zero_d_results=path)
        )
        self.output_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(zero_d_output=path)
        )

    def set_current_paths(self):
        """
        Sets current paths as known to main widget to this widget's fields
        """
        paths = self.caller.current_source_paths
        if paths is not None:
            self.results_dir_selector.setFilePath(paths["0d1d_results_dir"])
            self.output_selector.setFilePath(paths["0d1d_output"])
            self.populate_revisions_combobox()

    def populate_revisions_combobox(self):
        """
        Accumulates a list of valid 3di results (directories) and populates the revision selection
        combobox from this list
        """
        revisions = self.caller.fenv.threedi_results.zero_d_one_d.revisions
        print("zero_d_one_d", revisions)
        #if len(revisions) == 0:
        #    self.select_revision_box.setEnabled(False)
        #    return
        self.select_revision_box.clear()
        self.select_revision_box.addItem("")
        for revision in revisions:
            self.select_revision_box.addItem(revision)

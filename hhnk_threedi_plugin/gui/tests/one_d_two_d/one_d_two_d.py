import os
from pathlib import Path
from PyQt5.QtWidgets import (
    QPushButton,
    QFileDialog,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from ...general_objects import revisionsComboBox
from PyQt5.QtCore import Qt, pyqtSignal
from qgis.core import Qgis
from ...utility.file_widget import fileWidget
from ....gui.path_verification_functions import is_valid_results_folder
from ....qgis_interaction.layers_management.layers.get_layers_list import (
    get_layers_list,
)
from .verify_one_d_two_d_ui import verify_input
from ...utility_functions import get_revision
from ....qgis_interaction.layers_management.groups.layer_groups_structure import (
    QgisLayerStructure,
)

# hhnk-research-tols

# hhnk-threedi-tests
from hhnk_threedi_tools.qgis.get_working_paths import get_working_paths
from hhnk_threedi_tools.qgis.paths_functions import get_top_level_directories
from hhnk_threedi_tools.qgis.environment import testEnvironment


def setupUi(one_d_two_d_widget):
    # Create button to start tests
    one_d_two_d_widget.start_1d2d_tests_btn = QPushButton("Begin tests")

    # Create all file widgets
    one_d_two_d_widget.results_dir_selector = fileWidget(
        select_text="Selecteer 3di resultaat map:",
        file_dialog_title="Selecteer 3di revisie map " "(bevat .nc en .h5 files)",
        file_mode=QFileDialog.Directory,
    )
    one_d_two_d_widget.select_revision_box = revisionsComboBox()
    one_d_two_d_widget.select_revision_label = QLabel("Selecteer revisie:")
    one_d_two_d_widget.result_selected_show_label = QLabel("Geselecteerde revisie: ")
    one_d_two_d_widget.result_selected_show = QLabel("Geen revisie geselecteerd")

    one_d_two_d_widget.dem_selector = fileWidget(
        select_text="Selecteer DEM raster",
        file_dialog_title="Selecteer DEM raster (.tif)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.tif",
    )
    one_d_two_d_widget.model_selector = fileWidget(
        select_text="Selecteer model:",
        file_dialog_title="Selecteer een model (.sqlite)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.sqlite",
    )
    one_d_two_d_widget.output_selector = fileWidget(
        select_text="Selecteer output map:",
        file_dialog_title="Selecteer map om output in aan te maken",
        file_mode=QFileDialog.Directory,
    )

    # Main layout
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.addWidget(one_d_two_d_widget.results_dir_selector)
    main_layout.addWidget(one_d_two_d_widget.select_revision_label)
    main_layout.addWidget(one_d_two_d_widget.select_revision_box)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(one_d_two_d_widget.result_selected_show_label)
    main_layout.addWidget(one_d_two_d_widget.result_selected_show)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(one_d_two_d_widget.dem_selector)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(one_d_two_d_widget.model_selector)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(one_d_two_d_widget.output_selector)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(one_d_two_d_widget.start_1d2d_tests_btn)
    one_d_two_d_widget.setLayout(main_layout)


class oneDTwoDWidget(QWidget):
    """
    Initialization:
        oneDTwoDWidget(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))

    Signals:

    start_1d2d_tests(object (test_env))
    """

    start_1d2d_tests = pyqtSignal(object)

    def __init__(self, caller, parent=None):
        super(oneDTwoDWidget, self).__init__(parent)
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
        #     lambda: self.populate_revisions_combobox(
        #         self.results_dir_selector.filePath()
        #     )
        # )
        # Geef geselecteerde revisie weer

        # self.select_revision_box.aboutToShowPopup.connect(self.populate_revisions_combobox)
        self.select_revision_box.currentIndexChanged.connect(self.set_revision_text)
        self.start_1d2d_tests_btn.clicked.connect(self.verify_submit)

    def create_test_environment(self):
        """Collect all needed variables to run tests"""
        src_paths, output_dict = get_working_paths(
            test_type=4,
            active_paths=self.caller.current_source_paths,
            base_folder_output=self.output_selector.filePath(),
            threedi_results_path=self.results_dir_selector.filePath(),
            threedi_revision_name=self.select_revision_box.currentText(),
        )
        layer_groups_structure = QgisLayerStructure(
            one_d_revision=get_revision(self.select_revision_box.currentText())
        )

        layers = get_layers_list(
            test_type=4,
            plugin_dir=self.caller.plugin_dir,
            output_dict=output_dict,
            group_structure=layer_groups_structure,
        )  # TODO revision
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
        test_environment.dem_path = self.dem_selector.filePath()
        test_environment.model_path = self.model_selector.filePath()
        test_environment.output_path = (
            self.output_selector.filePath()
            + "/"
            + get_revision(self.select_revision_box.currentText())
        )
        return test_environment

    def verify_submit(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """
        res, message = verify_input(
            revision_selected=self.select_revision_box.currentText(),
            dem_path=self.dem_selector.filePath(),
            model_path=self.model_selector.filePath(),
            output_path=self.output_selector.filePath(),
        )
        if not res:
            self.caller.iface.messageBar().pushMessage(message, Qgis.Critical)
        else:
            test_environment = self.create_test_environment()
            self.start_1d2d_tests.emit(test_environment)

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
        self.dem_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(dem=path)
        )
        self.model_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(model=path)
        )
        self.results_dir_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(one_d_results=path)
        )
        self.output_selector.fileSelected.connect(
            lambda path: self.caller.update_current_paths(one_d_results=path)
        )

    def set_current_paths(self):
        """
        Sets current paths as known to main widget to this widget's fields
        """
        paths = self.caller.current_source_paths
        if paths is not None:
            self.model_selector.setFilePath(paths["model"])
            self.dem_selector.setFilePath(paths["dem"])
            self.results_dir_selector.setFilePath(paths["1d2d_results_dir"])
            self.output_selector.setFilePath(paths["1d2d_output"])
            self.populate_revisions_combobox()

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

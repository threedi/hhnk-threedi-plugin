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
from hhnk_threedi_plugin.qgis_interaction.layers_management.layers.get_layers_list import (
    get_layers_list,
)
from ....gui.path_verification_functions import is_valid_results_folder
from hhnk_threedi_plugin.qgis_interaction.layers_management.groups.layer_groups_structure import (
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

    bank_levels_widget.model_selector = fileWidget(
        select_text="Selecteer model:",
        file_dialog_title="Selecteer een model (.sqlite)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.sqlite",
    )
    # Main layout
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(bank_levels_widget.model_selector)
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

        self.start_bank_levels_btn.clicked.connect(self.verify_submit)
       
    def verify_submit(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """
        res, message = verify_input(
            model_path=self.model_selector.filePath(),
        )
        if not res:
            self.caller.iface.messageBar().pushMessage(message, Qgis.Critical)
        else:
            #test_environment = self.create_test_environment()
            self.start_bank_levels_tests.emit(None)


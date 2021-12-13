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
    QPlainTextEdit,
    QLineEdit,
    QLabel,
    QMessageBox,
    QComboBox,
)
from PyQt5.Qt import QApplication, QClipboard
from ..general_objects import revisionsComboBox
from PyQt5.QtCore import Qt, pyqtSignal
from qgis.core import (
    Qgis,
    QgsProject,
    QgsLayoutExporter,
    QgsRenderContext,
    QgsPathResolver,
)
from ..utility.file_widget import fileWidget
from ...gui.path_verification_functions import is_valid_results_folder
from ...qgis_interaction.layers_management.layers.get_layers_list import get_layers_list
from .verify_klimaatsommen_ui import verify_input
from ..utility_functions import get_revision
from ...qgis_interaction.layers_management.groups.layer_groups_structure import (
    QgisLayerStructure,
)
import pandas as pd


from ...qgis_interaction.configs.klimaatsommen import load_klimaatsommen_layers
from ...qgis_interaction.klimaatsommen_pdfs import create_pdfs, load_print_layout
from ...dependencies import DEPENDENCY_DIR, THREEDI_DIR


from hhnk_threedi_tools import (
    open_server,
    copy_notebooks,
    write_notebook_json,
    copy_projects,
)
from hhnk_threedi_tools.utils.notebooks.run import create_command_bat_file


SUBJECT = "Klimaatsommen"


def setupUi(klimaatsommen_widget):

    klimaatsommen_widget.server_btn = QPushButton("Open Jupyter notebook server")
    klimaatsommen_widget.laad_layout_btn = QPushButton("Laad layout")
    klimaatsommen_widget.create_pdfs_btn = QPushButton("Maak pdfs")
    klimaatsommen_widget.lizard_api_key_label = QLabel("Lizard API Key:")
    klimaatsommen_widget.select_revision_label = QLabel("Selecteer revisie:")
    klimaatsommen_widget.select_revision_box = revisionsComboBox()

    klimaatsommen_widget.help_text = QPlainTextEdit(klimaatsommen_widget)
    text = """ Help: Probeer eerst de notebook te openen via 'Start Jupyter notebook server', lukt dit niet, open de notebooks dan los in je geselecteerde polder folder.
               
    """
    klimaatsommen_widget.help_text.insertPlainText(text)

    klimaatsommen_widget.lizard_api_key_textbox = QLineEdit(klimaatsommen_widget)

    # Main layout
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)

    main_layout.addWidget(klimaatsommen_widget.lizard_api_key_label)
    main_layout.addWidget(klimaatsommen_widget.lizard_api_key_textbox)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))

    main_layout.addWidget(klimaatsommen_widget.server_btn)
    main_layout.addWidget(klimaatsommen_widget.help_text)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))

    main_layout.addWidget(klimaatsommen_widget.select_revision_label)
    main_layout.addWidget(klimaatsommen_widget.select_revision_box)
    main_layout.addWidget(klimaatsommen_widget.laad_layout_btn)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))

    main_layout.addWidget(klimaatsommen_widget.create_pdfs_btn)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))

    # main_layout.addWidget(klimaatsommen_widget.result_selected_show_label)
    # main_layout.addWidget(klimaatsommen_widget.result_selected_show)
    # main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    # main_layout.addWidget(klimaatsommen_widget.dem_selector)
    # main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    # main_layout.addWidget(klimaatsommen_widget.model_selector)
    # main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    # main_layout.addWidget(klimaatsommen_widget.output_selector)
    # main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    klimaatsommen_widget.setLayout(main_layout)


class KlimaatSommenWidget(QWidget):
    """
    Initialization:
        oneDTwoDWidget(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))

    Signals:

    start_1d2d_tests(object (test_env))
    """

    # wordt niet geburikt
    klimaatsommen = pyqtSignal(object)

    def __init__(self, caller, parent=None):
        super(KlimaatSommenWidget, self).__init__(parent)
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
        # self.select_revision_box.aboutToShowPopup.connect(lambda: self.populate_revisions_combobox(
        #    self.results_dir_selector.filePath()))
        # Geef geselecteerde revisie weer
        # self.select_revision_box.currentIndexChanged.connect(self.set_revision_text)

        # set up the signals
        self.server_btn.clicked.connect(self.verify_submit_start_server)
        self.laad_layout_btn.clicked.connect(self.verify_submit_laad_layout)
        self.create_pdfs_btn.clicked.connect(self.verify_submit_create_pdfs)
        self.select_revision_box.aboutToShowPopup.connect(self.populate_combobox)

    def generate_notebook_folder(self):
        """retrieves the polder folder and loads the"""

        self.polder_folder = self.caller.polder_folder
        self.polder_notebooks = self.polder_folder + "/Notebooks"
        server_bat_file = self.polder_notebooks + "/start_server.bat"
        copy_notebooks(self.polder_notebooks)
        create_command_bat_file(server_bat_file, "user")
        write_notebook_json(
            self.polder_notebooks,
            {
                "polder_folder": self.polder_folder,
                "lizard_api_key": self.lizard_api_key_textbox.text(),
                "syspaths": [str(DEPENDENCY_DIR), str(THREEDI_DIR)],
            },
        )

    def verify_submit_start_server(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """
        # should make a verify
        if not self.generate_notebook_valid():
            return

        self.generate_notebook_folder()
        open_server(directory=self.polder_notebooks, location="user", use="run")

    def verify_submit_laad_layout(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """

        self.fenv = self.caller.fenv
        load_klimaatsommen_layers(self.fenv, self.select_revision_box.currentText())
        load_print_layout()

    def verify_submit_create_pdfs(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """
        QMessageBox.warning(
            None,
            SUBJECT,
            "De pdf's zullen aangemaakt worden met de huidige QGIS extent!",
        )

        load_print_layout()
        create_pdfs(self.caller.fenv, self.select_revision_box.currentText())

    def populate_combobox(self):
        revisions = self.caller.fenv.threedi_results.climate_results.revisions

        self.select_revision_box.clear()
        self.select_revision_box.addItem("")
        for revision in revisions:
            self.select_revision_box.addItem(revision)

    def generate_notebook_valid(self):
        if self.lizard_api_key_textbox.text() == "":
            QMessageBox.warning(
                None,
                SUBJECT,
                "Vul de lizard api key in, deze is niet ingevuld! Heb je deze niet? Ga naar: https://hhnk.lizard.net/management/#/personal_api_keys",
            )
            return False
        else:
            return True

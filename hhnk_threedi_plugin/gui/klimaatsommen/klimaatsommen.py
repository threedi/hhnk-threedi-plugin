import os

import hhnk_research_tools as hrt
import hhnk_threedi_tools as htt
from hhnk_threedi_tools.qgis import layer_structure
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QComboBox,
    QFileDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

import hhnk_threedi_plugin.qgis_interaction.project as project
from hhnk_threedi_plugin.dependencies import HHNK_THREEDI_PLUGIN_DIR
from hhnk_threedi_plugin.gui.utility.widget_interaction import update_button_background
from hhnk_threedi_plugin.qgis_interaction.klimaatsommen_pdfs import (
    create_pdfs,
    load_print_layout,
)

from ..general_objects import revisionsComboBox

SUBJECT = "Klimaatsommen"


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
        super().__init__()
        self.setupUi()

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
        self.laad_layout_btn.clicked.connect(self.verify_submit_laad_layout)
        self.create_pdfs_btn.clicked.connect(self.verify_submit_create_pdfs)
        self.create_clean_btn.clicked.connect(self.verify_submit_create_clean)
        self.select_revision_box.aboutToShowPopup.connect(self.populate_combobox)
        self.select_revision_box.currentTextChanged.connect(self.reset_buttons)

    @property
    def fenv(self):
        return self.caller.fenv

    def setupUi(self):
        self.select_revision_label = QLabel("Selecteer revisie:")
        self.select_revision_box = revisionsComboBox()

        self.laad_layout_btn = QPushButton("Laad layout")
        self.create_pdfs_btn = QPushButton("Maak pdfs")
        self.create_clean_btn = QPushButton("clean")

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(45, 45, 25, 25)
        main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))

        main_layout.addWidget(self.select_revision_label)
        main_layout.addWidget(self.select_revision_box)
        main_layout.addWidget(self.laad_layout_btn)
        main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))

        main_layout.addWidget(self.create_clean_btn)
        main_layout.addWidget(self.create_pdfs_btn)
        main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))

        self.setLayout(main_layout)

    def verify_submit_laad_layout(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """

        update_button_background(button=self.laad_layout_btn, color="orange")

        df_path = hrt.get_pkg_resource_path(package_resource=htt.resources, name="qgis_layer_structure.csv")

        revisions = layer_structure.SelectedRevisions(klimaatsommen=self.select_revision_box.currentText())

        # Load layers
        proj = project.Project()
        proj.run(
            layer_structure_path=df_path, subjects=["klimaatsommen"], revisions=revisions, folder=self.caller.fenv
        )

        load_print_layout()
        update_button_background(button=self.laad_layout_btn, color="green")

    def verify_submit_create_pdfs(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """
        QMessageBox.warning(
            None,
            SUBJECT,
            """
                Let op:
                - De pdf's worden aangemaakt met het huidige extent in de layout!
                - Laadt de achtergrond laag in.
                - Laadt de revisie laag in.
                - Extents verschillen per monitor. Werkt het niet? Pas 
                de extent aan in de layout manager. (project -> layouts -> wsa_kaarten)
            """,
        )

        # load_print_layout()
        create_pdfs(self.caller.fenv, self.select_revision_box.currentText())

    def populate_combobox(self):
        revisions = self.caller.fenv.threedi_results.climate_results.revisions_rev

        self.select_revision_box.clear()
        self.select_revision_box.addItem("")

        for rev in revisions:
            self.select_revision_box.addItem(rev.name)

    def verify_submit_create_clean(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("AL GOOD")
        msgBox.setWindowTitle("GOOD MESSAGE")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.buttonClicked.connect(self.verify_submit_create_clean)

    def reset_buttons(self):
        update_button_background(button=self.laad_layout_btn)

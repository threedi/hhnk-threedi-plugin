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
from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR


# from ...qgis_interaction.configs.klimaatsommen import load_klimaatsommen_layers
from hhnk_threedi_plugin.qgis_interaction import load_layers_interaction

from ...qgis_interaction.klimaatsommen_pdfs import create_pdfs, load_print_layout

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
        super(KlimaatSommenWidget, self).__init__(parent)
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

        self.fenv = self.caller.fenv

        df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'klimaatsommen.csv')
        revisions = {'klimaatsommen':self.select_revision_box.currentText()}
        subjects=['klimaatsommen']
        load_layers_interaction.load_layers(folder=self.caller.fenv, 
                                            df_path=df_path, 
                                            revisions=revisions, 
                                            subjects=subjects,
                                            remove_layer=True)

        load_print_layout()

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
                - De pdf's worden aangemaakt met het huidige extent!
                - Laadt de achtergrond laag in.
                - Laadt de revisie laag in.
                - Extents verschillen per monitor. Werkt het niet? Pas 
                de extent aan in de layout manager. (project -> layouts -> wsa_kaarten)
            """
        )

        # load_print_layout()
        create_pdfs(self.caller.fenv, self.select_revision_box.currentText())

    def populate_combobox(self):
        revisions = self.caller.fenv.threedi_results.climate_results.revisions

        self.select_revision_box.clear()
        self.select_revision_box.addItem("")
        for revision in revisions:
            self.select_revision_box.addItem(revision.name)

    def verify_submit_create_clean(self):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("AL GOOD")
            msgBox.setWindowTitle("GOOD MESSAGE")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.buttonClicked.connect(self.verify_submit_create_clean)
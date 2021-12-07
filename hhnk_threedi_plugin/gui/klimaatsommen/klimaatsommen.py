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

from hhnk_threedi_tools import (
    open_server,
    copy_notebooks,
    write_notebook_json,
    copy_projects,
)


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
        copy_notebooks(self.polder_notebooks)
        write_notebook_json(
            self.polder_notebooks,
            {
                "polder_folder": self.polder_folder,
                "lizard_api_key": self.lizard_api_key_textbox.text(),
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
        open_server(self.polder_notebooks)

    def verify_submit_laad_layout(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """

        self.fenv = self.caller.fenv
        load_klimaatsommen_layers(self.fenv, self.select_revision_box.currentText())

    def verify_submit_create_pdfs(self):
        """
        Checks if all input is legal, if so, creates test environment (variable container) and
        emits start tests signal to controller
        """
        create_pdfs()

    def populate_combobox(self):
        revisions = self.caller.fenv.threedi_results.climate_results.revisions
        if len(revisions) == 0:
            QMessageBox.warning(
                None, SUBJECT, "Geen revisies gevonden in batch results"
            )
            return

        self.select_revision_box.clear()
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


def create_pdfs():

    output_path = QgsProject.instance().readPath("./")  # same as qgis project loc

    polder_folder = output_path.split("/")[-3]  # 10.tHoekje
    polder = polder_folder.split(".")[1]
    if "rev" in output_path.split("/")[-1]:
        revisie = output_path.split("/")[-1].split("rev")[
            -1
        ]  # TODO: toevoegen controle of dit de revisie is..
    else:
        revisie = output_path.split("/")[-1].split("_")[
            -1
        ]  # TODO: toevoegen controle of dit de revisie is..

    subtitle = "Maatregel model {} (rev{})".format(polder, revisie)

    # Select print composer
    dic = {}
    # Schadekaarten
    dic[0] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_cw_schade_totaal.pdf".format(polder, revisie),
        "theme": "schade_totaal",
        "title": "Schade",
        "legenda": "legenda_schade",
    }
    dic[1] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_cw_schade_plas.pdf".format(polder, revisie),
        "theme": "schade_plas",
        "title": "Schade plasvorming",
        "legenda": "legenda_schade",
    }
    dic[2] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_cw_schade_overlast.pdf".format(polder, revisie),
        "theme": "schade_overlast",
        "title": "Schade watersysteem",
        "legenda": "legenda_schade",
    }

    # #Gecorrigeerde schadekaarten
    dic[3] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_cw_schade_totaal_corr.pdf".format(polder, revisie),
        "theme": "schade_totaal_corr",
        "title": "Schade",
        "legenda": "legenda_schade",
    }
    dic[4] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_cw_schade_plas_corr.pdf".format(polder, revisie),
        "theme": "schade_plas_corr",
        "title": "Schade plasvorming",
        "legenda": "legenda_schade",
    }
    dic[5] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_cw_schade_overlast_corr.pdf".format(polder, revisie),
        "theme": "schade_overlast_corr",
        "title": "Schade watersysteem",
        "legenda": "legenda_schade",
    }

    # Inundatiekaarten
    dic[6] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_inundatie_totaal.pdf".format(polder, revisie),
        "theme": "inundatie_totaal",
        "title": "Inundatie",
        "legenda": "legenda_inundatie",
    }
    dic[7] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_inundatie_plas.pdf".format(polder, revisie),
        "theme": "inundatie_plas",
        "title": "Inundatie plasvorming",
        "legenda": "legenda_inundatie",
    }
    dic[8] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_inundatie_overlast.pdf".format(polder, revisie),
        "theme": "inundatie_overlast",
        "title": "Inundatie watersysteem",
        "legenda": "legenda_inundatie",
    }

    # Ruimtekaart
    dic[9] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_ruimtekaart.pdf".format(polder, revisie),
        "theme": "ruimtekaart",
        "title": "Ruimtekaart",
        "legenda": "legenda_ruimtekaart",
    }

    # Landgebruik
    dic[10] = {
        "composer_name": "wsa_kaarten",
        "pdf_name": "{}_rev{}_landgebruik.pdf".format(polder, revisie),
        "theme": "landgebruik",
        "title": "Landgebruik",
        "legenda": "legenda_landgebruik",
    }

    # Set dict in dataframe that will be looped.
    df = pd.DataFrame(
        columns=["composer_name", "pdf_name", "theme", "title", "legenda"]
    )
    df = df.append([dic[a] for a in dic], ignore_index=True)

    df["pdf_path"] = df["pdf_name"].apply(lambda x: os.path.join(output_path, x))

    # legenda_ids = df['legenda'].unique().tolist()
    legenda_ids = [
        "legenda_schade",
        "legenda_inundatie",
        "legenda_ruimtekaart",
        "legenda_landgebruik",
    ]

    # Connect to project and al print composers
    projectInstance = QgsProject.instance()
    layoutmanager = projectInstance.layoutManager()

    def create_pdf_from_composer(
        composer_name,
        title,
        subtitle,
        legenda_ids,
        selected_legenda,
        theme,
        output_file,
    ):
        layout_item = layoutmanager.layoutByName(
            composer_name
        )  # test is the layout name

        # -------------------------------------------------------------------------------------
        # Change layout settings
        # -------------------------------------------------------------------------------------
        label_item = layout_item.itemById("titel")
        label_item.setText(title)

        label_item = layout_item.itemById("subtitel")
        label_item.setText(subtitle)

        # Hide all legend items, only show selected legend.
        for legenda_id in legenda_ids:
            legenda_item = layout_item.itemById(legenda_id)
            legenda_item.setVisibility(False)
            if legenda_id == selected_legenda:
                legenda_item.setVisibility(True)

        map = layout_item.referenceMap()
        map.setFollowVisibilityPresetName(theme)

        # Poging om extent goed te zetten, maar handmatig is beter.
        # layer = QgsProject.instance().mapLayersByName('schade_per_peilgebied')[0]
        # map.setExtent(layer.extent())
        # map.attemptResize(QgsLayoutSize(250,200,QgsUnitTypes.LayoutMillimeters))

        # -------------------------------------------------------------------------------------
        # Export
        # -------------------------------------------------------------------------------------
        pdf_settings = QgsLayoutExporter.PdfExportSettings()
        pdf_settings.textRenderFormat = (
            QgsRenderContext.TextFormatAlwaysText
        )  # If not changed the labels will be ugly in the pdf

        image_settings = QgsLayoutExporter.ImageExportSettings()

        export = QgsLayoutExporter(layout_item)
        result = export.exportToPdf(output_file, pdf_settings)
        if result == 0:
            print("pdf aangemaakt: {}".format(row["pdf_name"]))
        else:
            print("pdf niet gelukt: {}".format(row["pdf_name"]))
        return result

    for index, row in df.iterrows():
        result = create_pdf_from_composer(
            composer_name=row["composer_name"],
            title=row["title"],
            subtitle=subtitle,
            legenda_ids=legenda_ids,
            selected_legenda=row["legenda"],
            theme=row["theme"],
            output_file=row["pdf_path"],
        )

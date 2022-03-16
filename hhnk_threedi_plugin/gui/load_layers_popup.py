import os
from pathlib import Path
from re import S
from qgis.core import QgsVectorLayer
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
    QMessageBox,
)
from PyQt5.QtCore import Qt, pyqtSignal
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageBar, QgsMessageLog, iface

from .utility_functions import get_revision
from hhnk_threedi_plugin.qgis_interaction.layers_management.layers.get_layers_list import get_layers_list
# from hhnk_threedi_plugin.qgis_interaction.layers_management.adding_layers import (
#     add_layers,
#     find_tif_layers_and_append,
# )
from hhnk_threedi_plugin.qgis_interaction.layers_management.groups.layer_groups_structure import (
    QgisLayerStructure,
)
# from hhnk_threedi_plugin.qgis_interaction.layers_management.removing_layers import remove_layers

# new

from .general_objects import revisionsComboBox
from hhnk_threedi_plugin.qgis_interaction.project import Project
from hhnk_threedi_plugin.qgis_interaction import load_layers_interaction

# hhnk-threedi-tests
from hhnk_threedi_tools.qgis.paths_functions import get_top_level_directories
from hhnk_threedi_tools.qgis.build_output_files_dict import build_output_files_dict
from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR


def setup_ui(load_layers_popup):
    load_layers_popup.setMinimumWidth(400)
    # Creates items to be in widget
    load_layers_popup.bar = QgsMessageBar()
    load_layers_popup.zero_d_one_d_selector_label = QLabel(
        "Selecteer 0d1d test revisie:"
    )
    load_layers_popup.zero_d_one_d_selector = revisionsComboBox()
    load_layers_popup.one_d_two_d_selector_label = QLabel(
        "Selecteer 1d2d test revisie:"
    )
    load_layers_popup.one_d_two_d_selector = revisionsComboBox()

    load_layers_popup.klimaatsommen_selector_label = QLabel(
        "Selecteer klimaatsom revisie:"
    )
    load_layers_popup.klimaatsommen_selector = revisionsComboBox()

    load_layers_popup.sqlite_test_selector = QCheckBox("Sqlite testen")
    load_layers_popup.sqlite_test_selector.setChecked(False)

    load_layers_popup.test_protocol_selector = QCheckBox("Basis layout")
    load_layers_popup.test_protocol_selector.setChecked(True)

    load_layers_popup.achtergrond_selector = QCheckBox("Achtergrondkaarten")
    load_layers_popup.achtergrond_selector.setChecked(False)

    load_layers_popup.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

    # Creates layout
    message_bar_layout = QVBoxLayout()

    # Add widgets to layout
    message_bar_layout.addWidget(load_layers_popup.bar)

    # Combine all sections into main layout
    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.addLayout(message_bar_layout)

    main_layout.addWidget(load_layers_popup.zero_d_one_d_selector_label)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    main_layout.addWidget(load_layers_popup.zero_d_one_d_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.one_d_two_d_selector_label)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    main_layout.addWidget(load_layers_popup.one_d_two_d_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.klimaatsommen_selector_label)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    main_layout.addWidget(load_layers_popup.klimaatsommen_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.sqlite_test_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.test_protocol_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.achtergrond_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.buttons)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    load_layers_popup.setLayout(main_layout)


class loadLayersDialog(QDialog):
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
        super(loadLayersDialog, self).__init__(parent)
        setup_ui(self)
        self.setWindowTitle("Resultaten toevoegen aan project")
        # ----------------------------------------------------------
        # Variables
        # ----------------------------------------------------------
        self.caller = caller

        # load

        self.klimaatsommen_selector.aboutToShowPopup.connect(self.populate_klimaatsommen_combobox)
        self.one_d_two_d_selector.aboutToShowPopup.connect(self.populate_one_d_two_combobox)
        self.zero_d_one_d_selector.aboutToShowPopup.connect(self.populate_zero_d_one_d_combobox)
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        self.buttons.accepted.connect(self.load_layers)

        # Close on cancel
        self.buttons.rejected.connect(self.close)
        # Verify on accept
        # self.buttons.accepted.connect(self.verify_submit)
        
        

    def populate_one_d_two_combobox(self):
        """Add available revisions to dropdown"""
        revisions = self.caller.fenv.output.one_d_two_d.revisions
        if len(revisions) == 0:
            return

        self.one_d_two_d_selector.clear()
        self.one_d_two_d_selector.addItem("")
        for revision in revisions:
            self.one_d_two_d_selector.addItem(revision)

    def populate_zero_d_one_d_combobox(self):
        """Add available revisions to dropdown"""
        revisions = self.caller.fenv.output.zero_d_one_d.revisions

        if len(revisions) == 0:
            return

        self.zero_d_one_d_selector.clear()
        self.zero_d_one_d_selector.addItem("")
        for revision in revisions:
            self.zero_d_one_d_selector.addItem(revision)

    def populate_klimaatsommen_combobox(self):
        """Add available revisions to dropdown"""
        revisions = self.caller.fenv.threedi_results.climate_results.revisions
        if len(revisions) == 0:
            return

        self.klimaatsommen_selector.clear()
        self.klimaatsommen_selector.addItem("")
        for revision in revisions:
            self.klimaatsommen_selector.addItem(revision)

    def set_current_paths(self):
        """
        Sets current paths as known to main widget to this widget's fields
        """
        paths = self.caller.current_source_paths

        if paths is not None:
            self.sqlite_output_path = paths["sqlite_tests_output"]
            self.zero_d_one_d_output_path = paths["0d1d_output"]
            self.one_d_two_d_output_path = paths["1d2d_output"]
            
            # combobox
            self.populate_klimaatsommen_combobox()
            self.populate_zero_d_one_d_combobox()
            self.populate_one_d_two_combobox()
            

    def load_layers(self):

        iface.messageBar().pushMessage(f"Inladen van lagen gestart", level=Qgis.Info)
        
        # set map canvas
        project = Project()

        df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')
        subjects=[]
        revisions={'0d1d_test':'',
                    '1d2d_test':'',
                    'klimaatsommen':''}

        # Sqlite test
        if self.sqlite_test_selector.isChecked() == True:
            subjects.append('test_sqlite')

        # Test protocol
        if self.test_protocol_selector.isChecked() == True:
            subjects.append('test_protocol')

        # Achtergrond
        if self.achtergrond_selector.isChecked() == True: #Todo naam butten veranderen en andere achtergrond buttons weg.
            subjects.append('achtergrond')

        # 0d1d test
        if self.zero_d_one_d_selector.currentText() != "":
            subjects.append('test_0d1d')
            revisions['0d1d_test'] = self.zero_d_one_d_selector.currentText()

        # 1d2d test
        if self.one_d_two_d_selector.currentText() != "":
            subjects.append('test_1d2d')
            revisions['1d2d_test'] = self.one_d_two_d_selector.currentText()


        #Laad geselecteerde lagen.
        if subjects != []:
            load_layers_interaction.load_layers(folder=self.caller.fenv, 
                                                df_path=df_path, 
                                                revisions=revisions, 
                                                subjects=subjects)


        # Klimaatsommen #TODO staat nu in aparate csv. Zo houden voor de themes? Of juist samen nemen?
        if self.klimaatsommen_selector.currentText() != "":
            df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'klimaatsommen.csv')
            revisions = {'klimaatsommen':self.klimaatsommen_selector.currentText()}
            subjects=['klimaatsommen']
            load_layers_interaction.load_layers(folder=self.caller.fenv, 
                                                df_path=df_path, 
                                                revisions=revisions, 
                                                subjects=subjects)

        #TODO moet dit een keuze worden? 
        project.zoom_to_layer(layer_name='polder_polygon')


        self.accept()


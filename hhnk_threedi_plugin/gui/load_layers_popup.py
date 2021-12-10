import os
from pathlib import Path
from re import S
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
from qgis.utils import QgsMessageBar

from .utility_functions import get_revision
from ..qgis_interaction.layers_management.layers.get_layers_list import get_layers_list
from ..qgis_interaction.layers_management.adding_layers import (
    add_layers,
    find_tif_layers_and_append,
)
from ..qgis_interaction.layers_management.groups.layer_groups_structure import (
    QgisLayerStructure,
)
from ..qgis_interaction.layers_management.removing_layers import remove_layers

# new

from .general_objects import revisionsComboBox
from ..qgis_interaction.configs.test_protocol_v21 import load_test_protocol_v21_layers
from ..qgis_interaction.configs.klimaatsommen import load_klimaatsommen_layers
from ..qgis_interaction.configs.achtergrond import load_achtergrond_layers


# hhnk-threedi-tests
from hhnk_threedi_tools.qgis.paths_functions import get_top_level_directories
from hhnk_threedi_tools.qgis.build_output_files_dict import build_output_files_dict


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
    load_layers_popup.sqlite_test_selector.setChecked(True)

    load_layers_popup.test_protocol_v21_selector = QCheckBox("Layout test protocol v21")
    load_layers_popup.test_protocol_v21_selector.setChecked(True)

    load_layers_popup.achtergrond_landgebruik_selector = QCheckBox("Lizard landgebruik")
    load_layers_popup.achtergrond_landgebruik_selector.setChecked(True)

    load_layers_popup.achtergrond_luchtfoto_selector = QCheckBox(
        "PDOK luchtfoto actueel"
    )
    load_layers_popup.achtergrond_luchtfoto_selector.setChecked(True)

    load_layers_popup.achtergrond_waterlopen_2020_selector = QCheckBox(
        "HHNK waterlopen 2020 (legger)"
    )
    load_layers_popup.achtergrond_waterlopen_2020_selector.setChecked(True)

    load_layers_popup.buttons = QDialogButtonBox(
        QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    )

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

    main_layout.addWidget(load_layers_popup.test_protocol_v21_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.achtergrond_landgebruik_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.achtergrond_luchtfoto_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.achtergrond_waterlopen_2020_selector)
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

        self.klimaatsommen_selector.aboutToShowPopup.connect(
            self.populate_klimaatsommen_combobox
        )
        self.one_d_two_d_selector.aboutToShowPopup.connect(
            self.populate_one_d_two_combobox
        )
        self.zero_d_one_d_selector.aboutToShowPopup.connect(
            self.populate_zero_d_one_d_combobox
        )
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        self.buttons.accepted.connect(self.load_layers)

        # Close on cancel
        self.buttons.rejected.connect(self.close)
        # Verify on accept
        # self.buttons.accepted.connect(self.verify_submit)

    def populate_one_d_two_combobox(self):
        revisions = self.caller.fenv.output.one_d_two_d.revisions
        if len(revisions) == 0:
            return

        self.one_d_two_d_selector.clear()
        self.one_d_two_d_selector.addItem("")
        for revision in revisions:
            self.one_d_two_d_selector.addItem(revision)

    def populate_zero_d_one_d_combobox(self):
        revisions = self.caller.fenv.output.zero_d_one_d.revisions

        if len(revisions) == 0:
            return

        self.zero_d_one_d_selector.clear()
        self.zero_d_one_d_selector.addItem("")
        for revision in revisions:
            self.zero_d_one_d_selector.addItem(revision)

    def populate_klimaatsommen_combobox(self):
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

    def load_layers(self):

        # Resolve paths to layers
        self.sqlite_dict = build_output_files_dict(
            test_type=1, base_folder=self.sqlite_output_path, revision_dir_name=None
        )

        if self.zero_d_one_d_selector.currentText() != "":
            self.zero_d_one_d_dict = build_output_files_dict(
                test_type=2,
                base_folder=self.zero_d_one_d_output_path,
                revision_dir_name=self.zero_d_one_d_selector.currentText(),
            )
        else:
            self.zero_d_one_d_dict = False

        if self.one_d_two_d_selector.currentText() != "":
            self.one_d_two_d_dict = build_output_files_dict(
                test_type=4,
                base_folder=self.one_d_two_d_output_path,
                revision_dir_name=self.one_d_two_d_selector.currentText(),
            )
        else:
            self.one_d_two_d_dict = False

        # Create layer list
        layer_groups_structure = QgisLayerStructure(
            zero_d_revision=get_revision(self.zero_d_one_d_selector.currentText()),
            one_d_revision=get_revision(self.one_d_two_d_selector.currentText()),
        )

        if self.sqlite_test_selector.isChecked() == True:
            self.sqlite_layers = get_layers_list(
                test_type=1,
                plugin_dir=self.caller.plugin_dir,
                output_dict=self.sqlite_dict,
                group_structure=layer_groups_structure,
                chosen_tests=None,
            )

            # TODO fix layers dict to list
            self.sqlite_layers = [self.sqlite_layers[x] for x in self.sqlite_layers]

            remove_layers(self.sqlite_layers)  # Remove layers from project
            add_layers(
                layers_list=self.sqlite_layers, group_structure=layer_groups_structure
            )

        # 0d1d results
        if self.zero_d_one_d_dict:
            self.zero_d_one_d_layers = get_layers_list(
                test_type=2,
                plugin_dir=self.caller.plugin_dir,
                output_dict=self.zero_d_one_d_dict,
                group_structure=layer_groups_structure,
                chosen_tests=None,
            )

            # TODO fix layers dict to list
            self.zero_d_one_d_layers = [
                self.zero_d_one_d_layers[x] for x in self.zero_d_one_d_layers
            ]

            remove_layers(self.zero_d_one_d_layers)  # Remove layers from project
            add_layers(
                layers_list=self.zero_d_one_d_layers,
                group_structure=layer_groups_structure,
            )

        # 1d2d results
        if self.one_d_two_d_dict:
            self.one_d_two_d_layers = get_layers_list(
                test_type=4,
                plugin_dir=self.caller.plugin_dir,
                output_dict=self.one_d_two_d_dict,
                group_structure=layer_groups_structure,
                chosen_tests=None,
            )

            # TODO fix layers dict to list
            self.one_d_two_d_layers = [
                self.one_d_two_d_layers[x] for x in self.one_d_two_d_layers
            ]

            # Add tif layers created by regular expression
            self.one_d_two_d_layers = find_tif_layers_and_append(
                input_folder=self.one_d_two_d_dict["layer_path"],
                layers_list=self.one_d_two_d_layers,
            )

            remove_layers(self.one_d_two_d_layers)  # Remove layers from project
            add_layers(
                layers_list=self.one_d_two_d_layers,
                group_structure=layer_groups_structure,
            )

        if self.klimaatsommen_selector.currentText() != "":
            load_klimaatsommen_layers(
                self.caller.fenv, self.klimaatsommen_selector.currentText()
            )

        # test protocol v21
        if self.test_protocol_v21_selector.isChecked() == True:
            load_test_protocol_v21_layers(self.caller.fenv)

        # achtergrond
        load_achtergrond_layers(
            self.caller.fenv,
            landgebruik=self.achtergrond_landgebruik_selector.isChecked(),
            luchtfoto=self.achtergrond_luchtfoto_selector.isChecked(),
            waterlopen_2020=self.achtergrond_waterlopen_2020_selector.isChecked(),
        )

        self.accept()

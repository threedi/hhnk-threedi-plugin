import os

import hhnk_research_tools as hrt
import hhnk_threedi_tools as htt
from hhnk_threedi_tools import MigrateSchema, SqliteCheck
from hhnk_threedi_tools.qgis import layer_structure
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)
from qgis.core import Qgis
from qgis.utils import QgsMessageBar, iface

import hhnk_threedi_plugin.qgis_interaction.project as project

# hhnk-threedi-tests
from hhnk_threedi_plugin.dependencies import HHNK_THREEDI_PLUGIN_DIR
from hhnk_threedi_plugin.gui.utility.widget_interaction import update_button_background
from hhnk_threedi_plugin.qgis_interaction import load_layers_interaction

# get plugin-tasks
from hhnk_threedi_plugin.tasks import generateGridTask

# new
from .general_objects import revisionsComboBox


def setup_ui(load_layers_popup):
    load_layers_popup.setMinimumWidth(400)
    # Creates items to be in widget
    load_layers_popup.bar = QgsMessageBar()
    load_layers_popup.zero_d_one_d_selector_label = QLabel("Selecteer 0d1d test revisie:")
    load_layers_popup.zero_d_one_d_selector = revisionsComboBox()
    load_layers_popup.one_d_two_d_selector_label = QLabel("Selecteer 1d2d test revisie:")
    load_layers_popup.one_d_two_d_selector = revisionsComboBox()

    load_layers_popup.klimaatsommen_selector_label = QLabel("Selecteer klimaatsom revisie:")
    load_layers_popup.klimaatsommen_selector = revisionsComboBox()

    load_layers_popup.sqlite_selector = QCheckBox("Sqlite (3Di plugin)")
    load_layers_popup.sqlite_selector.setChecked(True)

    load_layers_popup.grid_selector = QCheckBox("Grid genereren")
    load_layers_popup.grid_selector.setChecked(False)

    load_layers_popup.sqlite_test_selector = QCheckBox("Sqlite testen")
    load_layers_popup.sqlite_test_selector.setChecked(False)

    load_layers_popup.banklevel_test_selector = QCheckBox("Banklevel test")
    load_layers_popup.banklevel_test_selector.setChecked(False)

    load_layers_popup.test_protocol_selector = QCheckBox("Basis layout")
    load_layers_popup.test_protocol_selector.setChecked(True)

    load_layers_popup.achtergrond_selector = QCheckBox("Achtergrondkaarten")
    load_layers_popup.achtergrond_selector.setChecked(True)

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

    main_layout.addWidget(load_layers_popup.sqlite_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.grid_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.sqlite_test_selector)
    main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))

    main_layout.addWidget(load_layers_popup.banklevel_test_selector)
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
        revisions = self.caller.fenv.output.one_d_two_d.revisions_rev

        self.one_d_two_d_selector.clear()
        self.one_d_two_d_selector.addItem("")
        for revision in revisions:
            self.one_d_two_d_selector.addItem(revision.name)

    def populate_zero_d_one_d_combobox(self):
        """Add available revisions to dropdown"""
        revisions = self.caller.fenv.output.zero_d_one_d.revisions_rev

        self.zero_d_one_d_selector.clear()
        self.zero_d_one_d_selector.addItem("")
        for revision in revisions:
            self.zero_d_one_d_selector.addItem(revision.name)

    def populate_klimaatsommen_combobox(self):
        """Add available revisions to dropdown"""
        revisions = self.caller.fenv.threedi_results.climate_results.revisions_rev

        self.klimaatsommen_selector.clear()
        self.klimaatsommen_selector.addItem("")
        for revision in revisions:
            self.klimaatsommen_selector.addItem(revision.name)

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
        update_button_background(button=self.buttons, color="orange")

        iface.messageBar().pushMessage("Inladen van lagen gestart", level=Qgis.Info)

        df_path = hrt.get_pkg_resource_path(package_resource=htt.resources, name="qgis_layer_structure.csv")
        subjects = []
        revisions = layer_structure.SelectedRevisions()

        if self.sqlite_selector.isChecked() == True:
            # Migrate sqlite to newest version
            migrate_schema = MigrateSchema(filename=self.caller.fenv.model.schema_base.sqlite_paths[0].as_posix())
            migrate_schema.run()

            # load in project
            load_layers_interaction.load_sqlite(filepath=self.caller.fenv.model.schema_base.sqlite_paths[0].as_posix())

        if self.grid_selector.isChecked() == True:
            iface.messageBar().pushMessage("genereer grid")
            grid_task = generateGridTask(self.caller.fenv)
            grid_task.run()
            # sqlite_test = SqliteCheck(self.caller.fenv)
            # sqlite_test.create_grid_from_sqlite(output_folder=self.caller.fenv.output.sqlite_tests.base)

            # subjects.append('grid')

        # Sqlite test
        if self.sqlite_test_selector.isChecked() == True:
            subjects.append("test_sqlite")

        if self.banklevel_test_selector.isChecked() == True:
            subjects.append("test_banklevels")

        # Test protocol
        if self.test_protocol_selector.isChecked() == True:
            # FIXME tijdelijke implementatie om gdb in gpkg om te zetten. Als dit in alle projectmappen staat kan het weer weg.
            for source in ["datachecker", "damo", "hdb"]:
                in_gdb = hrt.SpatialDatabase(getattr(self.caller.fenv.source_data, source).path.with_suffix(".gdb"))
                out_gpkg = getattr(self.caller.fenv.source_data, source)

                hrt.convert_gdb_to_gpkg(gdb=in_gdb, gpkg=out_gpkg, overwrite=False, verbose=False)

                if in_gdb.exists():
                    iface.messageBar().pushMessage(
                        f"{source}_gdb is omgezet in {source}_gpkg. {source}.gdb kan verwijderd worden.",
                        level=Qgis.Warning,
                    )

            subjects.append("test_protocol")

        # 0d1d test
        if self.zero_d_one_d_selector.currentText() != "":
            subjects.append("test_0d1d")
            revisions.check_0d1d = self.zero_d_one_d_selector.currentText()

        # 1d2d test
        if self.one_d_two_d_selector.currentText() != "":
            subjects.append("test_1d2d")
            revisions.check_1d2d = self.one_d_two_d_selector.currentText()

        # Achtergrond
        if (
            self.achtergrond_selector.isChecked() == True
        ):  # Todo naam button veranderen en andere achtergrond buttons weg.
            subjects.append("achtergrond")

        # Klimaatsommen
        if self.klimaatsommen_selector.currentText() != "":
            subjects.append("klimaatsommen")
            revisions.klimaatsommen = self.klimaatsommen_selector.currentText()

        # Laad geselecteerde lagen.
        if subjects != []:
            proj = project.Project()
            proj.run(layer_structure_path=df_path, subjects=subjects, revisions=revisions, folder=self.caller.fenv)

        # TODO moet dit een keuze worden?
        # project.zoom_to_layer(layer_name='polder_polygon')

        update_button_background(button=self.buttons)
        self.accept()

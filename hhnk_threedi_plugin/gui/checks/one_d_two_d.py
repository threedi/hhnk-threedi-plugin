import os
from pathlib import Path

import numpy as np
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QFileDialog,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
from qgis.core import Qgis

from hhnk_threedi_plugin.gui.general_objects import revisionsComboBox
from hhnk_threedi_plugin.gui.utility.widget_interaction import update_button_background
from hhnk_threedi_plugin.tasks import task_one_d_two_d


def setupUi(one_d_two_d_widget):
    one_d_two_d_widget.select_revision_label = QLabel("Selecteer revisie:")
    one_d_two_d_widget.select_revision_box = revisionsComboBox()
    one_d_two_d_widget.start_1d2d_tests_btn = QPushButton("Begin tests")

    # Main layout
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)

    # Revision selection
    main_layout.addWidget(one_d_two_d_widget.select_revision_label)
    main_layout.addWidget(one_d_two_d_widget.select_revision_box)

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
        self.select_revision_box.aboutToShowPopup.connect(self.populate_revisions_combobox)
        self.start_1d2d_tests_btn.clicked.connect(self.one_d_two_d_tests_execution)
        self.select_revision_box.currentTextChanged.connect(self.reset_buttons)

    def populate_revisions_combobox(self):
        """
        Accumulates a list of valid 3di results (directories) and populates the revision selection
        combobox from this list
        """
        revisions = self.caller.fenv.threedi_results.one_d_two_d.revisions_rev

        self.select_revision_box.clear()
        self.select_revision_box.addItem("")

        for rev in revisions:
            self.select_revision_box.addItem(rev.name)

    def one_d_two_d_tests_execution(self):
        try:
            update_button_background(button=self.start_1d2d_tests_btn, color="orange")

            task_one_d_two_d.task_one_d_two_d(
                folder=self.caller.fenv,
                revision=self.select_revision_box.currentText(),
                dem_path=self.caller.input_data_dialog.dem_selector.filePath(),
            )
            update_button_background(button=self.start_1d2d_tests_btn, color="green")

        except Exception as e:
            self.caller.iface.messageBar().pushMessage(str(e), Qgis.Critical)
            update_button_background(button=self.start_1d2d_tests_btn, color="red")
            pass

    def reset_buttons(self):
        update_button_background(button=self.start_1d2d_tests_btn)

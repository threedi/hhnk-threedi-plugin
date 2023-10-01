import os
import numpy as np
from pathlib import Path
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QFileDialog,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QVBoxLayout,
)
from hhnk_threedi_plugin.gui.general_objects import revisionsComboBox
from qgis.core import Qgis
from PyQt5.QtCore import Qt, pyqtSignal

from hhnk_threedi_plugin.tasks import task_zero_d_one_d
from hhnk_threedi_plugin.error_messages.input_error_messages import no_output_folder, no_result_selected


def setupUi(zero_d_one_d_widget):
    zero_d_one_d_widget.select_revision_label = QLabel("Selecteer revisie:")
    zero_d_one_d_widget.select_revision_box = revisionsComboBox()
    zero_d_one_d_widget.start_0d1d_tests_btn = QPushButton("Begin tests")

    # Main layout
    zero_d_one_d_widget.main_layout = QVBoxLayout(zero_d_one_d_widget)
    zero_d_one_d_widget.main_layout.setAlignment(Qt.AlignTop)
    zero_d_one_d_widget.main_layout.setContentsMargins(25, 25, 25, 25)

    #Revision selection
    zero_d_one_d_widget.main_layout.addWidget(zero_d_one_d_widget.select_revision_label)
    zero_d_one_d_widget.main_layout.addWidget(zero_d_one_d_widget.select_revision_box)

    #Start test
    zero_d_one_d_widget.main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    zero_d_one_d_widget.main_layout.addWidget(zero_d_one_d_widget.start_0d1d_tests_btn)


class zeroDOneDWidget(QWidget):
    """
    Initialization:
        zeroDOneDWidget(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))

    Signals:

    start_0d1d_tests(object (test_env))
    """

    start_0d1d_tests = pyqtSignal(object)

    def __init__(self, caller, parent=None):
        super(zeroDOneDWidget, self).__init__(parent)
        setupUi(self)
        # ----------------------------------------------------------
        # Variables
        # ----------------------------------------------------------
        self.caller = caller
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------

        # Geef geselecteerde revisie weer
        self.select_revision_box.aboutToShowPopup.connect(self.populate_revisions_combobox)
        self.start_0d1d_tests_btn.clicked.connect(self.verify_submit)


    def verify_submit(self):
        """
        Checks whether all fields are correctly filled
        """
        def verify_input(output_path, revision_selected):
            """
            return values: valid_input (bool), error_message (empty string if no error, else message to display)
            """
            if output_path is None or not output_path:
                return False, no_output_folder
            if revision_selected is None or not revision_selected:
                return False, no_result_selected
            return True, ""
        
        res, message = verify_input(
            output_path=self.caller.input_data_dialog.output_0d_1d__selector.filePath(),
            revision_selected=self.select_revision_box.currentText(),
        )
        if not res:
            self.caller.iface.messageBar().pushMessage(message, Qgis.Critical)
        else:
            # test_environment = self.create_test_environment()
            # self.start_0d1d_tests.emit(test_environment)
            self.zero_d_one_d_test_execution()


    def populate_revisions_combobox(self):
        """
        Accumulates a list of valid 3di results (directories) and populates the revision selection
        combobox from this list
        """
        revisions = self.caller.fenv.threedi_results.zero_d_one_d.revisions
        print("zero_d_one_d", revisions)
        # if len(revisions) == 0:
        #    self.select_revision_box.setEnabled(False)
        #    return
        self.select_revision_box.clear()
        self.select_revision_box.addItem("")

        revisions_sorted = np.take(revisions, np.argsort([rev.lstat().st_mtime for rev in revisions]))[::-1]
        for rev in revisions_sorted:
            self.select_revision_box.addItem(rev.name)


    def zero_d_one_d_test_execution(self):
        try:
            task_zero_d_one_d.task_zero_d_one_d(folder = self.caller.fenv, 
                                                revision = self.select_revision_box.currentText())
            
        except Exception as e:
            self.caller.iface.messageBar().pushMessage(str(e), Qgis.Critical)
            pass
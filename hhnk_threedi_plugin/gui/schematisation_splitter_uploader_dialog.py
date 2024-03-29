import pandas as pd
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QFileDialog,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)
from qgis.core import Qgis, QgsTask
from qgis.gui import QgsMessageBar
from qgis.utils import QgsMessageLog, iface

# from hhnk_threedi_plugin.gui.tests.verify_sqlite_tests_input import verify_input
from hhnk_threedi_plugin.gui.utility.file_widget import fileWidget


def setupUi(splitter_dialog):
    splitter_dialog.setWindowTitle("Schematisation splitter and uploader")
    splitter_dialog.setMinimumWidth(500)

    # Create message bar for error logging
    splitter_dialog.bar = QgsMessageBar()

    # Create button to start tests
    splitter_dialog.start_split_btn = QPushButton("Start split")
    splitter_dialog.start_upload_btn = QPushButton("Start upload")

    # Create quick tests checkboxes and group
    splitter_dialog.schema_label = {}
    splitter_dialog.schema_chk = {}
    splitter_dialog.upload_chk = {}

    for index, row in splitter_dialog.settings_df.iterrows():
        schema_name = row["name"]

        # Schematisation name labels
        splitter_dialog.schema_label[schema_name] = QLabel(f"{schema_name}")

        # Schematisation creation checkboxes
        splitter_dialog.schema_chk[schema_name] = QCheckBox("", width=20)
        splitter_dialog.schema_chk[schema_name].setObjectName(f"schema_{schema_name}_chk")

        # Upload checkboxes
        splitter_dialog.upload_chk[schema_name] = QCheckBox("")
        splitter_dialog.upload_chk[schema_name].setObjectName(f"upload_{schema_name}_chk")

    selection_label = QLabel("Selecteer schematisaties")
    selection_layout = QGridLayout()
    selection_layout.setAlignment(Qt.AlignTop)
    selection_layout.setHorizontalSpacing(25)
    # selection_layout.setVerticalSpacing(25)

    selection_layout.addWidget(QLabel("Schematisation name"), 0, 0)
    selection_layout.addWidget(QLabel("Split"), 0, 1)
    selection_layout.addWidget(QLabel("Upload"), 0, 2)

    rows = len(splitter_dialog.schema_chk)
    for index, row in splitter_dialog.settings_df.iterrows():
        schema_name = row["name"]
        selection_layout.addWidget(splitter_dialog.schema_label[schema_name], index + 1, 0)
        selection_layout.addWidget(splitter_dialog.schema_chk[schema_name], index + 1, 1)
        selection_layout.addWidget(splitter_dialog.upload_chk[schema_name], index + 1, 2)

    splitter_dialog.browse_btn = fileWidget(file_dialog_title="Blabla", file_mode=QFileDialog.Directory)

    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.addWidget(splitter_dialog.bar)
    main_layout.addWidget(selection_label)
    main_layout.addLayout(selection_layout)
    main_layout.addWidget(splitter_dialog.start_split_btn)
    main_layout.addWidget(splitter_dialog.start_upload_btn)
    main_layout.addWidget(splitter_dialog.browse_btn)

    splitter_dialog.setLayout(main_layout)


class schematisationDialog(QDialog):
    """
    Initialization:
        sqliteCheckDialog(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))

    Signals:

    start_sqlite_tests(object (test_env))
    """

    start_splitter = pyqtSignal(object)

    def __init__(self, caller, parent):
        super(schematisationDialog, self).__init__(parent)
        self.caller = caller
        self.setStyleSheet(
            """
            QCheckBox::indicator {
            width: 30px;
            height: 30px
            }"""
        )

    def set_current_paths(self):
        self.settings_df = pd.read_excel(self.caller.fenv.model.settings.path, engine="openpyxl")

        setupUi(self)


# %%

import os
from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFileDialog,
    QLineEdit,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QPushButton,
    QMessageBox,
)
from PyQt5.QtCore import Qt, pyqtSignal
from qgis.utils import Qgis, iface
from ..gui.utility.file_widget import fileWidget
from ..error_messages.input_error_messages import (
    invalid_character_in_filename,
    folder_exists_already,
)
from hhnk_threedi_tools import Folders


def setupUi(new_project_dialog):
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignTop)
    layout.setContentsMargins(25, 25, 25, 25)
    new_project_dialog.setWindowTitle("Nieuw project aanmaken")
    new_project_dialog.setMinimumWidth(275)
    # Creates items to be in widget
    new_project_dialog.folder_selector = fileWidget(
        file_dialog_title="Selecteer map waarin project wordt aangemaakt",
        file_mode=QFileDialog.Directory,
        select_text="Selecteer map:",
    )
    new_project_dialog.polder_name_label = QLabel("Geef project (polder) naam op:")
    new_project_dialog.polder_name_field = QLineEdit()
    new_project_dialog.create_project_btn = QPushButton("Project aanmaken")

    # Add items to layout
    layout.addWidget(new_project_dialog.folder_selector, alignment=Qt.AlignTop)
    layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    layout.addWidget(new_project_dialog.polder_name_label, alignment=Qt.AlignTop)
    layout.addWidget(new_project_dialog.polder_name_field, alignment=Qt.AlignTop)
    layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding))
    layout.addWidget(new_project_dialog.create_project_btn, alignment=Qt.AlignTop)
    new_project_dialog.setLayout(layout)


class newProjectDialog(QDialog):
    """
    Creates a widget that allows a user to easily create a new project.
    Select a base folder and a name for the project, the basic structure is automatically set up
    and read-me files specifying the contents are added.

    Signals:

    project_folder_path(path)
    """

    project_folder_path = pyqtSignal(str)

    def __init__(self):
        super(newProjectDialog, self).__init__()
        setupUi(self)
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        self.create_project_btn.clicked.connect(self.verify_submit)
        self.full_path = ""

    def verify_submit(self):
        base_path = self.folder_selector.filePath()
        if not base_path:
            iface.messageBar().pushMessage(
                "Selecteer een map om nieuw project in aan te maken", Qgis.Critical
            )
        else:
            if not os.path.isdir(base_path):
                iface.messageBar().pushMessage(
                    "Selecteer een bestaande map om nieuw project in aan te maken",
                    Qgis.Critical,
                )
            else:
                project_name = self.polder_name_field.text()
                if not project_name:
                    iface.messageBar().pushMessage(
                        "Geen projectnaam opgegeven", Qgis.Critical
                    )
                else:
                    full_path = os.path.join(base_path, project_name)
                    if os.path.isdir(full_path):
                        iface.messageBar().pushMessage(
                            folder_exists_already, Qgis.Critical
                        )
                    else:
                        try:
                            # os.mkdir(full_path)
                            Folders(full_path, create=True)
                            self.project_folder_path.emit(full_path)
                            self.accept()
                            QMessageBox.information(
                                None, "Create project", "Your folders are created!"
                            )
                            self.full_path = full_path
                        except Exception:
                            iface.messageBar().pushMessage(
                                invalid_character_in_filename, Qgis.Critical
                            )
                            pass

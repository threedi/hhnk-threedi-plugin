import csv

from PyQt5.Qt import QStandardItem, QStandardItemModel, pyqtSignal
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QComboBox,
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableView,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from qgis.core import QgsProject
from qgis.utils import iface


def create_layer_added_label():
    return QLabel("Laag toegevoegd aan project")


def create_no_errors_label():
    return QLabel("Geen fouten gevonden")


def find_layer(path):
    ly = None
    for layer in QgsProject.instance().mapLayers().values():
        if layer.source() == path:
            ly = layer
            break
    return ly


def create_view_layer_attributes_button(path):
    button = QPushButton()
    button.setText("Bekijk resultaat")

    def show_attributes():
        layer = find_layer(path)
        if layer is not None:
            iface.showAttributeTable(layer)

    button.clicked.connect(show_attributes)
    return button


def create_formatted_text_edit(text):
    return QTextEdit("<br>".join(text.splitlines()))


class CsvAsTable(QDialog):
    def __init__(self, csv_path):
        super(CsvAsTable, self).__init__()
        self.csv = csv_path
        self.model = QStandardItemModel(self)
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.layoutVertical = QVBoxLayout(self)
        self.layoutVertical.addWidget(self.table)
        self.populate_table()

        self.table.resizeColumnToContents(0)  # resize col1 so it shows all

    def populate_table(self):
        with open(file=self.csv, mode="r") as fileInput:
            for row in csv.reader(fileInput):
                items = [QStandardItem(field) for field in row]
                self.model.appendRow(items)


class revisionsComboBox(QComboBox):
    """
    Created so that whenever the user clicks on the combobox, we repopulate it before showing
    the dropdown. This is not possible with the normal QComboBox
    """

    aboutToShowPopup = pyqtSignal()

    def __init__(self):
        super(revisionsComboBox, self).__init__()

    def showPopup(self):
        self.aboutToShowPopup.emit()
        QComboBox.showPopup(self)


class fileWidget(QWidget):
    # TODO verplaatsen naar general_objects.py
    # TODO utility map daarna verwijderen.
    """
    Creates a file widget containing a label (to tell users what should be selected), a line edit (to show
    current path) and a button. Clicking this button opens a file browser to select a file.

    Everytime a path changes (because a user types in the line edit or because okay is clicked in the file browser),
    the new path is emitted.

    The last directory a user looked in is saved and set as the new default location
    """

    fileSelected = pyqtSignal(str)

    def __init__(self, file_dialog_title, file_mode, name_filter=None, select_text=None):
        super(fileWidget, self).__init__()
        # ----------------------------------------------------------
        # Widgets
        # ----------------------------------------------------------
        self.label = QLabel(select_text)
        self.file_selected_edit = QLineEdit("")
        self.select_file_btn = QPushButton("...")
        self.select_file_btn.setFixedWidth(28)
        self.file_dialog = QFileDialog()
        self.last_opened_dir = None
        self.file_dialog.setWindowTitle(file_dialog_title)
        self.file_dialog.setFileMode(file_mode)
        if name_filter is not None:
            self.file_dialog.setNameFilter(name_filter)
        # ----------------------------------------------------------
        # Variables
        # ----------------------------------------------------------
        self.cursor_position = self.file_selected_edit.cursorPosition()
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        # Launch file widget on button click
        self.select_file_btn.clicked.connect(self.file_dialog.exec)
        # Once a file is selected in the filedialog, set the new path to be shown and emit it
        self.file_dialog.fileSelected.connect(self.file_selected_edit.setText)
        self.file_dialog.fileSelected.connect(self.fileSelected.emit)
        # Whenever a path is altered (programmatically or by the user), we emit the fileSelected signal
        # To prevent the cursor jumping back to the end of the line while the user is typing, we save and
        # reset the cursor every time a character is typed
        self.file_selected_edit.textChanged.connect(self.save_cursor_position)
        self.file_selected_edit.textChanged.connect(lambda: self.fileSelected.emit(self.file_selected_edit.text()))
        self.file_selected_edit.textChanged.connect(self.set_cursor_position)
        # If a file is chosen with the file dialog, save the path to that directory and open the file dialog there
        # next time
        self.file_dialog.fileSelected.connect(lambda: self.file_dialog.setDirectory(self.file_dialog.directory()))

        # Handle layout
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.file_selected_edit)
        layout.addWidget(self.select_file_btn)
        if select_text is not None:
            outer_layout = QVBoxLayout()
            outer_layout.setContentsMargins(0, 0, 0, 0)
            outer_layout.addWidget(self.label)
            outer_layout.addLayout(layout)
            self.setLayout(outer_layout)
        else:
            self.setLayout(layout)

    def set_cursor_position(self):
        self.file_selected_edit.setCursorPosition(self.cursor_position)

    def save_cursor_position(self):
        self.cursor_position = self.file_selected_edit.cursorPosition()

    def setFilePath(self, path):
        self.file_selected_edit.setText(path)

    def filePath(self):
        return self.file_selected_edit.text()

    def setEnabled(self, state):
        self.file_selected_edit.setEnabled(state)
        self.select_file_btn.setEnabled(state)

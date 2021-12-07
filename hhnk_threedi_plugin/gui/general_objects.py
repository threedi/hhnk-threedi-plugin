import csv
from PyQt5.QtWidgets import (
    QPushButton,
    QTextEdit,
    QDialog,
    QTableView,
    QVBoxLayout,
    QLabel,
    QComboBox,
)
from PyQt5.Qt import QStandardItemModel, QStandardItem, pyqtSignal
from qgis.utils import iface
from qgis.core import QgsProject


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

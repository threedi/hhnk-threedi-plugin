import os

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget

from hhnk_threedi_plugin.gui.general_objects import CsvAsTable, create_no_errors_label

geometry_titel = "Geometrie"


class geometryWidget(QWidget):
    def __init__(self, csv_path):
        super(geometryWidget, self).__init__()
        self.table = CsvAsTable(csv_path=csv_path)
        self.table.setGeometry(100, 100, 900, 900)
        self.btn = QPushButton("Bekijk fouten in geometrie")
        self.btn.clicked.connect(self.table.show)
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        self.setLayout(layout)


def create_geometries_result_widget(csv_path):
    if not os.path.exists(csv_path):
        widget = QWidget()
        layout = QVBoxLayout()
        label = create_no_errors_label()
        layout.addWidget(label)
        widget.setLayout(layout)
    else:
        widget = geometryWidget(csv_path=csv_path)
    return geometry_titel, widget

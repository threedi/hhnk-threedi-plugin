from hhnk_threedi_plugin.gui.general_objects import CsvAsTable, create_no_errors_label
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

geometry_titel = "Geometrie"


class geometryWidget(QWidget):
    def __init__(self, csv_path):
        super(geometryWidget, self).__init__()
        self.table = CsvAsTable(csv_path=csv_path)
        self.btn = QPushButton("Bekijk fouten in geometrie")
        self.btn.clicked.connect(self.table.show)
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        self.setLayout(layout)


def create_geometries_result_widget(csv_path):
    if csv_path is None:
        widget = QWidget()
        layout = QVBoxLayout()
        label = create_no_errors_label()
        layout.addWidget(label)
        widget.setLayout(layout)
    else:
        widget = geometryWidget(csv_path=csv_path)
    return geometry_titel, widget

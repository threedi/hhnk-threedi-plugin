from ....general_objects import CsvAsTable
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from ....general_objects import create_no_errors_label

geometry_titel = "Algemene tests"


class generalChecksWidget(QWidget):
    def __init__(self, csv_path):
        super(generalChecksWidget, self).__init__()
        self.table = CsvAsTable(csv_path=csv_path)
        self.btn = QPushButton("Bekijk fouten in model")
        self.btn.clicked.connect(self.table.show)
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        self.setLayout(layout)


def create_general_checks_result_widget(csv_path):
    if csv_path is None:
        widget = QWidget()
        layout = QVBoxLayout()
        label = create_no_errors_label()
        layout.addWidget(label)
        widget.setLayout(layout)
    else:
        widget = generalChecksWidget(csv_path=csv_path)
    return geometry_titel, widget

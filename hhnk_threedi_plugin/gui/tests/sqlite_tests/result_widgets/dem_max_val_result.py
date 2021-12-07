from PyQt5.QtWidgets import QWidget, QVBoxLayout
from ....general_objects import create_formatted_text_edit

dem_max_val_title = "Maximale waarde DEM"


def create_dem_max_val_result_widget(result_text):
    widget = QWidget()
    layout = QVBoxLayout()
    result = create_formatted_text_edit(result_text)
    layout.addWidget(result)
    widget.setLayout(layout)
    return dem_max_val_title, widget

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from ....general_objects import create_formatted_text_edit

impervious_surface_title = "Ondoorlatend oppervlak"


def create_impervious_surface_widget(result_text):
    widget = QWidget()
    layout = QVBoxLayout()
    result = create_formatted_text_edit(result_text)
    layout.addWidget(result)
    widget.setLayout(layout)
    return impervious_surface_title, widget

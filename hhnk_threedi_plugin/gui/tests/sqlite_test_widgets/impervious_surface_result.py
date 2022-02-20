   
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from hhnk_threedi_plugin.gui.general_objects import create_formatted_text_edit

impervious_surface_title = "Ondoorlatend oppervlak"


def create_impervious_surface_widget(result_text):
    widget = QWidget()
    layout = QVBoxLayout()
    result =  QTextEdit("<br>".join(result_text.splitlines())) #was create_formatted_text_edit
    result.setMaximumHeight(60)
    layout.addWidget(result)
    widget.setLayout(layout)
    return impervious_surface_title, widget

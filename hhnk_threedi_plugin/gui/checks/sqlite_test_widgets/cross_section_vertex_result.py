from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from hhnk_threedi_plugin.gui.general_objects import (
    create_view_layer_attributes_button,
    create_layer_added_label,
)

cross_section_no_vertex_chk_title = "Cross-section op channel vertex"


def cross_section_vertex_result_widget(layer_source):
    widget = QWidget()
    layout = QVBoxLayout()
    label = create_layer_added_label()
    button = create_view_layer_attributes_button(layer_source)
    layout.addWidget(label)
    layout.addWidget(button)
    widget.setLayout(layout)
    return cross_section_no_vertex_chk_title, widget

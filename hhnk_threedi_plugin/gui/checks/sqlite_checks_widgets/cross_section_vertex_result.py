from pathlib import Path

from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from hhnk_threedi_plugin.gui.general_objects import (
    create_layer_added_label,
    create_view_layer_attributes_button,
)

cross_section_no_vertex_chk_title = "Cross-section op channel vertex"


def cross_section_no_vertex_widget(layer_source: Path):
    widget = QWidget()
    layout = QVBoxLayout()
    label = create_layer_added_label()
    button = create_view_layer_attributes_button(layer_source)
    layout.addWidget(label)
    layout.addWidget(button)
    widget.setLayout(layout)
    return cross_section_no_vertex_chk_title, widget

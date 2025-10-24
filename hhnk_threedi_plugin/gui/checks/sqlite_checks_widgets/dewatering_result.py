from pathlib import Path

from PyQt5.QtWidgets import QVBoxLayout, QWidget

from hhnk_threedi_plugin.gui.general_objects import (
    create_layer_added_label,
    create_view_layer_attributes_button,
)

dewatering_title = "Drooglegging"


def create_dewatering_result_widget(layer_source: Path):
    widget = QWidget()
    layout = QVBoxLayout()
    label = create_layer_added_label()
    button = create_view_layer_attributes_button(layer_source)
    layout.addWidget(label)
    layout.addWidget(button)
    widget.setLayout(layout)
    return dewatering_title, widget

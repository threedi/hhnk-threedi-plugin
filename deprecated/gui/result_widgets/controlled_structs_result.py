from PyQt5.QtWidgets import QWidget, QVBoxLayout
from hhnk_threedi_plugin.gui.general_objects import (
    create_view_layer_attributes_button,
    create_layer_added_label,
)

controlled_structs_titel = "Gestuurde kunstwerken"


def create_controlled_structs_widget(layer_source):
    widget = QWidget()
    layout = QVBoxLayout()
    label = create_layer_added_label()
    button = create_view_layer_attributes_button(layer_source)
    layout.addWidget(label)
    layout.addWidget(button)
    widget.setLayout(layout)
    return controlled_structs_titel, widget

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from ....general_objects import (
    create_view_layer_attributes_button,
    create_layer_added_label,
)

profiles_used_title = "Gebruikte profielen watergangen"


def create_profiles_used_widget(layer_source):
    widget = QWidget()
    layout = QVBoxLayout()
    label = create_layer_added_label()
    button = create_view_layer_attributes_button(layer_source)
    layout.addWidget(label)
    layout.addWidget(button)
    widget.setLayout(layout)
    return profiles_used_title, widget

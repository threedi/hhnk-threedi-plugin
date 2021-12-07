from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from ....general_objects import (
    create_view_layer_attributes_button,
    create_layer_added_label,
)

structs_channels_titel = "Bodemhoogte kunstwerken"


def create_structs_channels_result_widget(layer_source):
    """
    Creates a widget showing the results of structs channel levels test.
    If layer_source is None then there were no structs below ground level found.
    """
    widget = QWidget()
    layout = QVBoxLayout()
    if layer_source is None:
        label = QLabel("Geen kunstwerken met te laag referentie level gevonden")
        layout.addWidget(label)
    else:
        label = create_layer_added_label()
        button = create_view_layer_attributes_button(layer_source)
        layout.addWidget(label)
        layout.addWidget(button)
    widget.setLayout(layout)
    return structs_channels_titel, widget

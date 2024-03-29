from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from hhnk_threedi_plugin.gui.general_objects import (
    create_formatted_text_edit,
    create_layer_added_label,
    create_view_layer_attributes_button,
)

isolated_channels_title = "Geisoleerde watergangen"


def create_isolated_channels_result_widget(result_text, layer_source):
    """
    Creates a widget showing the results of isolated channels test.
    If layer_source is None then there were no isolated channels found.
    """
    widget = QWidget()
    layout = QVBoxLayout()
    result = create_formatted_text_edit(result_text)
    result.setMaximumHeight(60)
    if layer_source is None:
        label = QLabel("Geen geisoleerde watergangen gevonden")
        layout.addWidget(label)
        layout.addWidget(result)
    else:
        label = create_layer_added_label()
        button = create_view_layer_attributes_button(layer_source)
        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(result)
    widget.setLayout(layout)
    return isolated_channels_title, widget

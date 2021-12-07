from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from ....general_objects import (
    create_view_layer_attributes_button,
    create_formatted_text_edit,
    create_layer_added_label,
)

watersurface_area_title = "Oppervlaktewater"


def create_watersurface_area_result_widget(result_text, layer_source):
    """
    Creates a widget showing the results of isolated channels test.
    If layer_source is None then there were no isolated channels found.
    """
    widget = QWidget()
    layout = QVBoxLayout()
    result = create_formatted_text_edit(result_text)
    label = create_layer_added_label()
    button = create_view_layer_attributes_button(layer_source)
    layout.addWidget(label)
    layout.addWidget(button)
    layout.addWidget(result)
    widget.setLayout(layout)
    return watersurface_area_title, widget

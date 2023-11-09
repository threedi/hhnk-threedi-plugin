from PyQt5.QtWidgets import QVBoxLayout, QWidget

from hhnk_threedi_plugin.gui.general_objects import create_formatted_text_edit


class exceptionsWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        layout = QVBoxLayout()
        self.text_edit = create_formatted_text_edit(text)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

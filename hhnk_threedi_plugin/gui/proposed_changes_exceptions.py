from PyQt5.QtWidgets import QWidget, QVBoxLayout
from .general_objects import create_formatted_text_edit


class exceptionsWidget(QWidget):
    def __init__(self, text):
        super(exceptionsWidget, self).__init__()
        layout = QVBoxLayout()
        self.text_edit = create_formatted_text_edit(text)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

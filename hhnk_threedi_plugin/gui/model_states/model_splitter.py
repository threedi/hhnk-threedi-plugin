import os

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal


class modelSplitterDialog(QtWidgets.QDialog):
    def __init__(self, caller, parent=None):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "model_splitter_dialog.ui"),self)

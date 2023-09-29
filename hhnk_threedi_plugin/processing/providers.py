# See https://docs.qgis.org/3.10/en/docs/pyqgis_developer_cookbook/processing.html
from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon

from ThreeDiToolbox.processing.schematisation_algorithms import (
    CheckSchematisationAlgorithm
    )

import os


class HHNKProvider(QgsProcessingProvider):
    """Loads the Processing Toolbox algorithms for 3Di"""

    def loadAlgorithms(self, *args, **kwargs):
        self.addAlgorithm(CheckSchematisationAlgorithm())


    def id(self, *args, **kwargs):
        """The ID of your plugin, used for identifying the provider.

        This string should be a unique, short, character only string,
        eg "qgis" or "gdal". This string should not be localised.
        """
        return "hhnk"

    def name(self, *args, **kwargs):
        """The human friendly name of your plugin in Processing.

        This string should be as short as possible (e.g. "Lastools", not
        "Lastools version 1.0.1 64-bit") and localised.
        """
        return self.tr("HHNK")

    def icon(self):
        """Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "icons", "hhnk_logo.jpg")
        return QIcon(icon_path)

"""Test script for the qgis-buttons

Overview of QGIS objects

"""

# System imports
import os
import os.path as path
import pathlib
import unittest

# Add the correct path
__file__ = "C:/Users/chris.kerklaan/Documents/Github/hhnk_threedi_plugin/tests/test_ui.py"
import sys

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))

# qgis imports
from qgis.core import *
from qgis.core import QgsSettings

qgs = QgsApplication([], False)
qgs.initQgis()


from qgis.gui import QgisInterface
from qgis.PyQt.QtCore import QCoreApplication, QSettings, Qt, QTranslator

# Local imports
from hhnk_threedi_plugin.hhnk_toolbox import HHNK_toolbox

# Globals
TEST_DIRECTORY = pathlib.Path(__file__).parent / "data" / "test_ui"


QgsApplication.setPrefixPath("C:/OSGEO4~1/apps/qgis-ltr", True)


# dummy instance to replace qgis.utils.iface
class QgisInterfaceDummy(object):
    def __init__(self):
        self.settings = QSettings()
        self.settings.setValue("locale/userLocale", "en_NL")

    def __getattr__(self, name):
        # return an function that accepts any arguments and does nothing
        def dummy(*args, **kwargs):
            return None

        return dummy


# class ExamplePluginTest(unittest.TestCase):
#     def setUp(self):
#         # create a new application instance
#         self.app = app = QtGui.QApplication(sys.argv)

#         # create a map canvas widget
#         self.canvas = canvas = QgsMapCanvas()
#         canvas.setCanvasColor(QtGui.QColor('white'))
#         canvas.enableAntiAliasing(True)

#         # load a shapefile
#         #layer = QgsVectorLayer(shapefile_path, 'MasterMap', 'ogr')

#         # add the layer to the canvas and zoom to it
#         QgsProject.instance().addMapLayer(layer)
#         canvas.setLayerSet([QgsMapCanvasLayer(layer)])
#         canvas.setExtent(layer.extent())

#         # display the map canvas widget
#         #canvas.show()

#         iface = QgisInterfaceDummy()

#         # import the plugin to be tested
#         import myplugin
#         self.plugin = myplugin.classFactory(iface)
#         self.plugin.initGui()
#         self.dlg = self.plugin.dlg
#         #self.dlg.show()

#     def test_populated(self):
#         '''Are the combo boxes populated correctly?'''
#         self.assertEqual(self.dlg.ui.comboBox_raster.currentText(), '')
#         self.assertEqual(self.dlg.ui.comboBox_vector.currentText(), 'MasterMap')
#         self.assertEqual(self.dlg.ui.comboBox_all1.currentText(), '')
#         self.dlg.ui.comboBox_all1.setCurrentIndex(1)
#         self.assertEqual(self.dlg.ui.comboBox_all1.currentText(), 'MasterMap')

#     def test_dlg_name(self):
#         self.assertEqual(self.dlg.windowTitle(), 'Testing')

#     def test_click_widget(self):
#         '''The OK button should close the dialog'''
#         self.dlg.show()
#         self.assertEqual(self.dlg.isVisible(), True)
#         okWidget = self.dlg.ui.buttonBox.button(self.dlg.ui.buttonBox.Ok)
#         QtTest.QTest.mouseClick(okWidget, Qt.LeftButton)
#         self.assertEqual(self.dlg.isVisible(), False)

#     def tearDown(self):
#         self.plugin.unload()
#         del(self.plugin)
#         del(self.app) # do not forget this

if __name__ == "__main__":
    iface = QgisInterfaceDummy()
    test = HHNK_toolbox(iface)
    ui = test.dlg.ui

    s = QSettings(os.path.join(os.getenv("APPDATA"), r"3Di/QGIS3/profiles/default/QGIS/QGIS3.ini"))

from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QGroupBox,
    QGridLayout,
    QFileDialog,
    QLabel,
    QCheckBox,
    QFrame,
    QSpacerItem,
    QDialog,
    QSizePolicy,
    QHBoxLayout,
    QApplication,
)
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from PyQt5.QtCore import Qt, pyqtSignal
from qgis.gui import QgsMessageBar
# from hhnk_threedi_plugin.gui.tests.verify_sqlite_tests_input import verify_input
from hhnk_threedi_plugin.gui.utility.file_widget import fileWidget
from hhnk_threedi_plugin.qgis_interaction.layers_management.layers.get_layers_list import (
    get_layers_list)
from hhnk_threedi_plugin.qgis_interaction.layers_management.groups.layer_groups_structure import (
    QgisLayerStructure)
from hhnk_threedi_plugin.tasks.task_sqlite_tests_main import task_sqlite_tests_main
from hhnk_threedi_plugin.qgis_interaction import load_layers_interaction

from hhnk_threedi_tools.qgis.get_working_paths import get_working_paths
from hhnk_threedi_tools.qgis.environment import testEnvironment

def setupUi(input_data):
    input_data.setWindowTitle("Model sqlite checks")
    input_data.setMinimumWidth(500)

    # Create message bar for error logging
    input_data.bar = QgsMessageBar()

    # Create button to start tests
    input_data.start_sqlite_tests_btn = QPushButton("Start tests")

    # Create all file widgets
    input_data.polder_label = QLabel("Polder:")
    input_data.polder_selector = fileWidget(
        file_dialog_title="", file_mode=QFileDialog.Directory    )
    input_data.polder_selector.setEnabled(False)

    input_data.output_selector_label = QLabel("Selecteer output map:")
    input_data.output_selector = fileWidget(
        file_dialog_title="Selecteer map om output in aan te maken",
        file_mode=QFileDialog.Directory,    )
    input_data.output_selector.setEnabled(False)

    input_data.model_selector_label = QLabel("Selecteer model:")
    input_data.model_selector = fileWidget(
        file_dialog_title="Selecteer een model (.sqlite)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.sqlite",    )
    input_data.model_selector.setEnabled(False)

    input_data.dem_label = QLabel("Selecteer DEM raster")
    input_data.dem_selector = fileWidget(
        file_dialog_title="Selecteer DEM raster (.tif)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.tif",    )
    input_data.dem_selector.setEnabled(False)

    input_data.datachecker_label = QLabel("Selecteer datachecker output:")
    input_data.datachecker_selector = fileWidget(
        file_dialog_title="Selecteer datachecker output (.gdb)",
        file_mode=QFileDialog.Directory,    )
    input_data.datachecker_selector.setEnabled(False)

    input_data.channels_from_label = QLabel("Watergangen van profielen:")
    input_data.channel_from_profiles_selector = fileWidget(
        file_dialog_title="Selecteer channels from profile " "shapefile (.shp)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.shp",    )
    input_data.channel_from_profiles_selector.setEnabled(False)

    input_data.hdb_label = QLabel("HDB:")
    input_data.hdb_selector = fileWidget(
        file_dialog_title="Selecteer hydrologen database (.gdb)",
        file_mode=QFileDialog.Directory,    )
    input_data.hdb_selector.setEnabled(False)

    input_data.damo_label = QLabel("DAMO:")
    input_data.damo_selector = fileWidget(
        file_dialog_title="Selecteer DAMO database (.gdb)",
        file_mode=QFileDialog.Directory,    )
    input_data.damo_selector.setEnabled(False)

    input_data.polder_shape_label = QLabel("Polder shapefile:")
    input_data.polder_shape_selector = fileWidget(
        file_dialog_title="Selecteer polder shapefile (.shp)",
        file_mode=QFileDialog.ExistingFile,    )
    input_data.polder_shape_selector.setEnabled(False)
    
    # Layouts
    separator = QFrame()
    separator.setFrameShape(QFrame.HLine)
    separator.setFrameShadow(QFrame.Sunken)

# Create layout for file dialogs
    path_selection_layout = QGridLayout()
    path_selection_layout.setAlignment(Qt.AlignTop)
    path_selection_layout.setHorizontalSpacing(25)
    path_selection_layout.addWidget(separator, 0, 0, 1, 2)
    #path_selection_layout.addWidget(input_data.polder_label, 1, 0)
    #path_selection_layout.addWidget(input_data.polder_selector, 1, 1)
    path_selection_layout.addWidget(input_data.output_selector_label, 2, 0)
    path_selection_layout.addWidget(input_data.output_selector, 2, 1)
    path_selection_layout.addWidget(input_data.model_selector_label, 3, 0)
    path_selection_layout.addWidget(input_data.model_selector, 3, 1)
    path_selection_layout.addWidget(input_data.dem_label, 4, 0)
    path_selection_layout.addWidget(input_data.dem_selector, 4, 1)
    path_selection_layout.addWidget(input_data.datachecker_label, 5, 0)
    path_selection_layout.addWidget(input_data.datachecker_selector, 5, 1)
    path_selection_layout.addWidget(input_data.channels_from_label, 6, 0)
    path_selection_layout.addWidget(input_data.channel_from_profiles_selector, 6, 1)
    path_selection_layout.addWidget(input_data.hdb_label, 7, 0)
    path_selection_layout.addWidget(input_data.hdb_selector, 7, 1)
    path_selection_layout.addWidget(input_data.damo_label, 8, 0)
    path_selection_layout.addWidget(input_data.damo_selector, 8, 1)
    path_selection_layout.addWidget(input_data.polder_shape_label, 9, 0)
    path_selection_layout.addWidget(input_data.polder_shape_selector, 9, 1)

    # Main layout
    paths_selection = QLabel("Selecteer benodigde bestanden")
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.addWidget(input_data.bar)
    main_layout.addWidget(paths_selection)
    main_layout.addLayout(path_selection_layout)
    main_layout.addSpacerItem(QSpacerItem(10, 5, QSizePolicy.Expanding))
    # main_layout.addWidget(input_data.all_tests)
    main_layout.addSpacerItem(QSpacerItem(10, 5, QSizePolicy.Expanding))
    main_layout.addWidget(input_data.start_sqlite_tests_btn, alignment=Qt.AlignRight)
    input_data.setLayout(main_layout)

class inputDataDialog(QDialog):

    def __init__(self, caller, parent):
        super(inputDataDialog, self).__init__(parent)
        setupUi(self)
        self.caller = caller
        self.setup_main_paths_signals()
        
    def setup_main_paths_signals(self):
        """
        Connects changes in fields (for example the selection of a file) to the function
        that updates (and keeps track of) the current fields for the entire plugin
        """
        self.datachecker_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(datachecker=path))
        self.damo_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(damo=path))
        self.hdb_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(hdb=path))
        self.polder_shape_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(polder_shapefile=path))
        self.channel_from_profiles_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(channels_shapefile=path))
        self.model_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(model=path))
        self.dem_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(dem=path))
        self.output_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(sqlite_output=path))

    def set_current_paths(self):
        """
        Sets current paths as known to main widget to this widget's fields
        """
        paths = self.caller.current_source_paths
        if paths is not None:
            self.polder_selector.setFilePath(paths["polder_folder"])
            self.model_selector.setFilePath(paths["model"])
            self.dem_selector.setFilePath(paths["dem"])
            self.datachecker_selector.setFilePath(paths["datachecker"])
            self.channel_from_profiles_selector.setFilePath(paths["channels_shapefile"])
            self.hdb_selector.setFilePath(paths["hdb"])
            self.damo_selector.setFilePath(paths["damo"])
            self.polder_shape_selector.setFilePath(paths["polder_shapefile"])
            self.output_selector.setFilePath(paths["sqlite_tests_output"])
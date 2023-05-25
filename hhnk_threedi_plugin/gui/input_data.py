# %%
import os
from collections import OrderedDict
# %%
import pandas as pd
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
from PyQt5.QtCore import Qt, pyqtSignal
from qgis.gui import QgsMessageBar
# from hhnk_threedi_plugin.gui.tests.verify_sqlite_tests_input import verify_input
from hhnk_threedi_plugin.gui.utility.file_widget import fileWidget



def setupUi(input_data):
    #Color 

    
    
    
    input_data.setWindowTitle("Selecteer benodigde bestanden")
    input_data.setMinimumWidth(500)

    # Create message bar for error logging
    input_data.bar = QgsMessageBar()

    # Create button to start tests
    # input_data.start_sqlite_tests_btn = QPushButton("Start tests")

    # Create all file widgets
    input_data.polder_label = QLabel("Project Folder:")
    input_data.polders_map_selector = fileWidget(
        file_dialog_title="", file_mode=QFileDialog.Directory    )
    input_data.polders_map_selector.setEnabled(False)

    input_data.output_selector_label = QLabel("Selecteer output map:")
    input_data.output_selector_label.setStyleSheet("background-color: lightgreen;border: 1px solid black;")
    input_data.output_selector = fileWidget(
        file_dialog_title="Selecteer map om output in aan te maken",
        file_mode=QFileDialog.Directory,    )
    input_data.output_selector.setEnabled(False)

    input_data.model_selector_label = QLabel("Selecteer model:")
    input_data.model_selector = fileWidget(
        file_dialog_title="Selecteer een model (.sqlite)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.sqlite",    )
    input_data.model_selector.setEnabled(True)

    input_data.dem_label = QLabel("Selecteer DEM raster")
    input_data.dem_selector = fileWidget(
        file_dialog_title="Selecteer DEM raster (.tif)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.tif",    )
    input_data.dem_selector.setEnabled(True)
   

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


    input_data.output_0d_1d_label = QLabel("Selecteer output voor 0d_1d test:")
    input_data.output_0d_1d__selector = fileWidget(
        file_dialog_title="Selecteer map om output in aan te maken",
        file_mode=QFileDialog.Directory,    )
    input_data.output_0d_1d__selector.setEnabled(False)
    
    input_data.results_dir_selector_label = QLabel("Selecteer 3di resultaat map:")
    input_data.results_dir_selector = fileWidget(
        file_dialog_title="Selecteer 3di revisie map " "(bevat .nc en .h5 files)",
        file_mode=QFileDialog.Directory,    )
    input_data.results_dir_selector.setEnabled(False)

    # Layouts
    separator = QFrame()
    separator.setFrameShape(QFrame.HLine)
    separator.setFrameShadow(QFrame.Sunken)

# Create layout for file dialogs
    path_selection_layout = QGridLayout()
    path_selection_layout.setAlignment(Qt.AlignTop)
    path_selection_layout.setHorizontalSpacing(25)
    path_selection_layout.addWidget(separator, 0, 0, 1, 2)
    # path_selection_layout.addWidget(input_data.polder_label, 1, 0)
    # path_selection_layout.addWidget(input_data.polders_map_selector, 1, 1)
    # path_selection_layout.addWidget(input_data.output_selector_label, 2, 0)
    # path_selection_layout.addWidget(input_data.output_selector, 2, 1)
    path_selection_layout.addWidget(input_data.model_selector_label, 1, 0)
    path_selection_layout.addWidget(input_data.model_selector, 1, 1)
    path_selection_layout.addWidget(input_data.dem_label, 2, 0)
    path_selection_layout.addWidget(input_data.dem_selector, 2, 1)
    path_selection_layout.addWidget(input_data.datachecker_label, 3, 0)
    path_selection_layout.addWidget(input_data.datachecker_selector, 3, 1)
    path_selection_layout.addWidget(input_data.channels_from_label, 4, 0)
    path_selection_layout.addWidget(input_data.channel_from_profiles_selector, 4, 1)
    path_selection_layout.addWidget(input_data.hdb_label, 5, 0)
    path_selection_layout.addWidget(input_data.hdb_selector, 5, 1)
    path_selection_layout.addWidget(input_data.damo_label, 6, 0)
    path_selection_layout.addWidget(input_data.damo_selector, 6, 1)
    path_selection_layout.addWidget(input_data.polder_shape_label, 7, 0)
    path_selection_layout.addWidget(input_data.polder_shape_selector, 7, 1)
    # path_selection_layout.addWidget(input_data.output_0d_1d_label, 10, 0)
    # path_selection_layout.addWidget(input_data.output_0d_1d__selector, 10, 1)
    # path_selection_layout.addWidget(input_data.results_dir_selector_label, 11, 0)
    # path_selection_layout.addWidget(input_data.results_dir_selector, 11, 1)

    # Main layout
    # paths_selection = QLabel("Selecteer benodigde bestanden")
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.addWidget(input_data.polder_label)
    main_layout.addWidget( input_data.polders_map_selector)
    main_layout.addWidget(input_data.bar)
    # main_layout.addWidget(paths_selection)
    main_layout.addLayout(path_selection_layout)
    main_layout.addSpacerItem(QSpacerItem(10, 5, QSizePolicy.Expanding))
    # main_layout.addWidget(input_data.all_tests)
    main_layout.addSpacerItem(QSpacerItem(10, 5, QSizePolicy.Expanding))
    # main_layout.addWidget(input_data.start_sqlite_tests_btn, alignment=Qt.AlignRight)
    input_data.setLayout(main_layout)



class inputDataDialog(QDialog):

    def __init__(self, caller, parent):
        super(inputDataDialog, self).__init__(parent)
        setupUi(self)
        self.caller = caller
        self.setup_main_paths_signals()
        self.model_selector.fileSelected.connect(self.caller.reset_ui)


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
        # self.output_selector_sqlite.fileSelected.connect(lambda path: self.caller.update_current_paths(sqlite_output=path))
        # self.result_selector_1d2d.fileSelected.connect(lambda path: self.caller.update_current_paths(one_d_results=path))
        self.output_0d_1d__selector.fileSelected.connect(lambda path: self.caller.update_current_paths(zero_d_output=path))
        self.results_dir_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(zero_d_output=path))


    def set_current_paths(self):
        """
        Sets current paths as known to main widget to this widget's fields
        """

        paths = self.caller.current_source_paths
        if paths is not None:

            widgets = OrderedDict({"polders_map_selector":"polder_folder","model_selector":"model",
            "dem_selector":"dem", "datachecker_selector":"datachecker", "channel_from_profiles_selector":"channels_shapefile",
            "hdb_selector":"hdb", "damo_selector":"damo", "polder_shape_selector":"polder_shapefile"})

            for key, value in widgets.items():
                widgt = getattr(self, key)
                
                filepath = paths[value] #Get filepath from current source paths
                name=filepath

                #Remove first part of path
                try:
                    if key != "polders_map_selector":
                        name = filepath(self.polders_map_selector.filePath())[-1]
                        # name = filepath.split(self.polders_map_selector.filePath())[-1]
                except:
                    pass
                widgt.setFilePath(name)

                if filepath is not None:
                    if os.path.exists(filepath):
                        widgt.setStyleSheet("background-color: lightgreen;border: 1px solid black")
                    else: 
                        widgt.setStyleSheet("background-color: orange; border: 1px solid black")
                else: 
                    widgt.setStyleSheet("background-color: blue; border: 1px solid black")


            # self.polders_map_selector.setFilePath(paths["polder_folder"])


            # self.polders_map_selector.setFilePath(paths["polder_folder"])
            # self.model_selector.setFilePath(paths["model"].split(self.polders_map_selector.filePath())[-1])
            # self.dem_selector.setFilePath(paths["dem"])
            # self.datachecker_selector.setFilePath(paths["datachecker"].split(self.polders_map_selector.filePath())[-1])
            # self.channel_from_profiles_selector.setFilePath(paths["channels_shapefile"].split(self.polders_map_selector.filePath())[-1])
            # self.hdb_selector.setFilePath(paths["hdb"].split(self.polders_map_selector.filePath())[-1])
            # self.damo_selector.setFilePath(paths["damo"].split(self.polders_map_selector.filePath())[-1])
            # self.polder_shape_selector.setFilePath(paths["polder_shapefile"].split(self.polders_map_selector.filePath())[-1])
            # self.output_selector.setFilePath(paths["sqlite_tests_output"].split(self.polders_map_selector.filePath())[-1])
            self.output_0d_1d__selector.setFilePath(paths["0d1d_output"])
            # self.one_d_two_d.dem_selector.setFilePath(paths["dem"])
            
        #Loop over widgets, check if name is None, color the box accordingly
            # if (pd.isnull(widgt.filePath())) or (widgt.filePath()==''):
            #     widgt.setStyleSheet("background-color: Blue; border: 1px solid black;")
            # else: 
            #     widgt.setStyleSheet("background-color: lightgreen;border: 1px solid black;")

            # self.output_selector.setFilePath(paths["sqlite_tests_output"])


    # def set_current_paths_1d_2d(self):
    #     """
    #     Sets current paths as known to main widget to this widget's fields
    #     """
    #     paths = self.caller.current_source_paths
    #     if paths is not None:
    #         self.model_selector.setFilePath(paths["model"])
    #         self.dem_selector.setFilePath(paths["dem"])
    #         self.results_dir_selector.setFilePath(paths["1d2d_results_dir"])
    #         self.output_selector.setFilePath(paths["1d2d_output"])
    #         #         E:\02.modellen\model_test_v2_juan
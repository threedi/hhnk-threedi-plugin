from msilib.schema import CheckBox
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
from hhnk_threedi_plugin.tasks.task_sqlite_tests_main import task_sqlite_tests_main
from hhnk_threedi_plugin.qgis_interaction import load_layers_interaction




def setupUi(sqlite_dialog):
    sqlite_dialog.setWindowTitle("Model sqlite checks")
    sqlite_dialog.setMinimumWidth(500)

    # Create message bar for error logging
    sqlite_dialog.bar = QgsMessageBar()

    # Create button to start tests
    sqlite_dialog.start_sqlite_tests_btn = QPushButton("Start tests")

#     # Create all file widgets
#     sqlite_dialog.polder_label = QLabel("Polder:")
#     sqlite_dialog.polders_map_selector = fileWidget(
#         file_dialog_title="", file_mode=QFileDialog.Directory    )
#     sqlite_dialog.polders_map_selector.setEnabled(False)

#     sqlite_dialog.output_selector_label = QLabel("Selecteer output map:")
#     sqlite_dialog.output_selector = fileWidget(
#         file_dialog_title="Selecteer map om output in aan te maken",
#         file_mode=QFileDialog.Directory,    )
#     sqlite_dialog.output_selector.setEnabled(False)

#     sqlite_dialog.model_selector_label = QLabel("Selecteer model:")
#     sqlite_dialog.model_selector = fileWidget(
#         file_dialog_title="Selecteer een model (.sqlite)",
#         file_mode=QFileDialog.ExistingFile,
#         name_filter="*.sqlite",    )
#     sqlite_dialog.model_selector.setEnabled(False)

#     sqlite_dialog.dem_label = QLabel("Selecteer DEM raster")
#     sqlite_dialog.dem_selector = fileWidget(
#         file_dialog_title="Selecteer DEM raster (.tif)",
#         file_mode=QFileDialog.ExistingFile,
#         name_filter="*.tif",    )
#     sqlite_dialog.dem_selector.setEnabled(False)

#     sqlite_dialog.datachecker_label = QLabel("Selecteer datachecker output:")
#     sqlite_dialog.datachecker_selector = fileWidget(
#         file_dialog_title="Selecteer datachecker output (.gdb)",
#         file_mode=QFileDialog.Directory,    )
#     sqlite_dialog.datachecker_selector.setEnabled(False)

#     sqlite_dialog.channels_from_label = QLabel("Watergangen van profielen:")
#     sqlite_dialog.channel_from_profiles_selector = fileWidget(
#         file_dialog_title="Selecteer channels from profile " "shapefile (.shp)",
#         file_mode=QFileDialog.ExistingFile,
#         name_filter="*.shp",    )
#     sqlite_dialog.channel_from_profiles_selector.setEnabled(False)

#     sqlite_dialog.hdb_label = QLabel("HDB:")
#     sqlite_dialog.hdb_selector = fileWidget(
#         file_dialog_title="Selecteer hydrologen database (.gdb)",
#         file_mode=QFileDialog.Directory,    )
#     sqlite_dialog.hdb_selector.setEnabled(False)

#     sqlite_dialog.damo_label = QLabel("DAMO:")
#     sqlite_dialog.damo_selector = fileWidget(
#         file_dialog_title="Selecteer DAMO database (.gdb)",
#         file_mode=QFileDialog.Directory,    )
#     sqlite_dialog.damo_selector.setEnabled(False)

#     sqlite_dialog.polder_shape_label = QLabel("Polder shapefile:")
#     sqlite_dialog.polder_shape_selector = fileWidget(
#         file_dialog_title="Selecteer polder shapefile (.shp)",
#         file_mode=QFileDialog.ExistingFile,    )
#     sqlite_dialog.polder_shape_selector.setEnabled(False)

    # Create all checkboxes group
    sqlite_dialog.all_tests = QGroupBox("Selecteer tests")

    # Create quick tests checkboxes and group
    sqlite_dialog.data_verification = QGroupBox("Data verificatie", sqlite_dialog.all_tests)
    sqlite_dialog.data_verification.setCheckable(True)
    sqlite_dialog.data_verification.setChecked(True)
    sqlite_dialog.impervious_surface_chk = QCheckBox("Ondoorlatend oppervlak")
    sqlite_dialog.impervious_surface_chk.setObjectName("impervious_surface_chk")
    sqlite_dialog.profiles_used_chk = QCheckBox("Gebruikte profielen")
    sqlite_dialog.profiles_used_chk.setObjectName("profiles_used_chk")
    sqlite_dialog.controlled_structs_chk = QCheckBox("Gestuurde kunstwerken")
    sqlite_dialog.controlled_structs_chk.setObjectName("controlled_structs_chk")
    sqlite_dialog.weir_height_chk = QCheckBox("Bodemhoogte stuw")
    sqlite_dialog.weir_height_chk.setObjectName("weir_height_chk")
    sqlite_dialog.geometry_chk = QCheckBox("Geometrie")
    sqlite_dialog.geometry_chk.setObjectName("geometry_chk")
    sqlite_dialog.structs_channel_chk = QCheckBox("Bodemhoogte kunstwerken")
    sqlite_dialog.structs_channel_chk.setObjectName("structs_channel_chk")
    sqlite_dialog.general_tests_chk = QCheckBox("Algemene tests")
    sqlite_dialog.general_tests_chk.setObjectName("general_tests_chk")
    sqlite_dialog.isolated_channels_chk = QCheckBox("Geisoleerde watergangen")
    sqlite_dialog.isolated_channels_chk.setObjectName("isolated_channels_chk")
    sqlite_dialog.grid_chk = QCheckBox("Genereer grid")
    sqlite_dialog.grid_chk.setObjectName("grid_chk")
    sqlite_dialog.cross_section_chk = QCheckBox("Profile controle")
    sqlite_dialog.cross_section_chk.setObjectName("cross_section_chk")
    sqlite_dialog.cross_section_intersection_chk = QCheckBox("Profiel snijpunt in vertex")
    sqlite_dialog.cross_section_intersection_chk.setObjectName("cross_section_intersection_chk")



    # Create slow tests checkboxes and group
    sqlite_dialog.one_time_checks = QGroupBox("Eenmalige tests", sqlite_dialog.all_tests)
    sqlite_dialog.one_time_checks.setCheckable(True)
    sqlite_dialog.max_dem_chk = QCheckBox(text="Maximale waarde DEM")
    sqlite_dialog.max_dem_chk.setObjectName("max_dem_chk")
    sqlite_dialog.dewatering_depth_chk = QCheckBox(text="Ontwateringsdiepte")
    sqlite_dialog.dewatering_depth_chk.setObjectName("dewatering_depth_chk")
    sqlite_dialog.watersurface_area_chk = QCheckBox("Oppervlaktewater")
    sqlite_dialog.watersurface_area_chk.setObjectName("watersurface_area_chk")

    # Layouts
    separator = QFrame()
    separator.setFrameShape(QFrame.HLine)
    separator.setFrameShadow(QFrame.Sunken)

    # Create layout for file dialogs
                        # path_selection_layout = QGridLayout()
                        # path_selection_layout.setAlignment(Qt.AlignTop)
                        # path_selection_layout.setHorizontalSpacing(25)
                        # path_selection_layout.addWidget(separator, 0, 0, 1, 2)
                        # path_selection_layout.addWidget(sqlite_dialog.polder_label, 1, 0)
                        # path_selection_layout.addWidget(sqlite_dialog.polders_map_selector, 1, 1)
                        # path_selection_layout.addWidget(sqlite_dialog.output_selector_label, 2, 0)
                        # path_selection_layout.addWidget(sqlite_dialog.output_selector, 2, 1)
                        # path_selection_layout.addWidget(sqlite_dialog.model_selector_label, 3, 0)
                        # path_selection_layout.addWidget(sqlite_dialog.model_selector, 3, 1)
                        # path_selection_layout.addWidget(sqlite_dialog.dem_label, 4, 0)
                        # path_selection_layout.addWidget(sqlite_dialog.dem_selector, 4, 1)
                        # path_selection_layout.addWidget(sqlite_dialog.datachecker_label, 5, 0)
                        # path_selection_layout.addWidget(sqlite_dialog.datachecker_selector, 5, 1)
                        # path_selection_layout.addWidget(sqlite_dialog.channels_from_label, 6, 0)
                        # path_selection_layout.addWidget(sqlite_dialog.channel_from_profiles_selector, 6, 1)
                        # path_selection_layout.addWidget(sqlite_dialog.hdb_label, 7, 0)
                        # path_selection_layout.addWidget(sqlite_dialog.hdb_selector, 7, 1)
                        # path_selection_layout.addWidget(sqlite_dialog.damo_label, 8, 0)
                        # path_selection_layout.addWidget(sqlite_dialog.damo_selector, 8, 1)
                        # path_selection_layout.addWidget(sqlite_dialog.polder_shape_label, 9, 0)
                        # path_selection_layout.addWidget(sqlite_dialog.polder_shape_selector, 9, 1)

    # Create checkboxes layout
    # quick checks
    verif_layout = QVBoxLayout()
    verif_layout.setAlignment(Qt.AlignTop)
    verif_layout.addWidget(sqlite_dialog.impervious_surface_chk)
    verif_layout.addWidget(sqlite_dialog.profiles_used_chk)
    verif_layout.addWidget(sqlite_dialog.controlled_structs_chk)
    verif_layout.addWidget(sqlite_dialog.weir_height_chk)
    verif_layout.addWidget(sqlite_dialog.geometry_chk)
    verif_layout.addWidget(sqlite_dialog.structs_channel_chk)
    verif_layout.addWidget(sqlite_dialog.general_tests_chk)
    verif_layout.addWidget(sqlite_dialog.isolated_channels_chk)
    verif_layout.addWidget(sqlite_dialog.grid_chk)
    verif_layout.addWidget(sqlite_dialog.cross_section_chk)
    verif_layout.addWidget(sqlite_dialog.cross_section_intersection_chk)
    sqlite_dialog.data_verification.setLayout(verif_layout)

    # Slow tests
    one_time_layout = QVBoxLayout()
    one_time_layout.setAlignment(Qt.AlignTop)
    one_time_layout.addWidget(sqlite_dialog.max_dem_chk)
    one_time_layout.addWidget(sqlite_dialog.dewatering_depth_chk)
    one_time_layout.addWidget(sqlite_dialog.watersurface_area_chk)
    sqlite_dialog.one_time_checks.setLayout(one_time_layout)

    # Combined
    checkboxes_layout = QHBoxLayout()
    checkboxes_layout.addWidget(sqlite_dialog.data_verification)
    checkboxes_layout.addWidget(sqlite_dialog.one_time_checks)
    sqlite_dialog.all_tests.setLayout(checkboxes_layout)


    # Main layout
    paths_selection = QLabel("Selecteer benodigde bestanden")
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.addWidget(sqlite_dialog.bar)
    main_layout.addWidget(paths_selection)
    #main_layout.addLayout(path_selection_layout)
    main_layout.addSpacerItem(QSpacerItem(10, 5, QSizePolicy.Expanding))
    main_layout.addWidget(sqlite_dialog.all_tests)
    main_layout.addSpacerItem(QSpacerItem(10, 5, QSizePolicy.Expanding))
    main_layout.addWidget(sqlite_dialog.start_sqlite_tests_btn, alignment=Qt.AlignRight)
    sqlite_dialog.setLayout(main_layout)

class sqliteCheckDialog(QDialog):
    """
    Initialization:
        sqliteCheckDialog(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))

    Signals:

    start_sqlite_tests(object (test_env))
    """

    start_sqlite_tests = pyqtSignal(object)

    def __init__(self, caller, parent):
        super(sqliteCheckDialog, self).__init__(parent)
        setupUi(self)
        self.caller = caller
        # self.setup_main_paths_signals()
        self.data_verification.clicked.connect(self.group_clicked)
        self.one_time_checks.clicked.connect(self.group_clicked)
        self.start_sqlite_tests_btn.clicked.connect(self.verify_submit)
        
        for child in self.data_verification.findChildren(QCheckBox):
            child.setChecked(True)

    def group_clicked(self):
        """
        When a user holds control and click the top-level checkbox, that toggles all its
        children according to the state of the top-level checkbox
        """
        if QApplication.keyboardModifiers() == Qt.ControlModifier:
            if self.sender() == self.one_time_checks:
                state = self.one_time_checks.isChecked()
                for child in self.one_time_checks.findChildren(QCheckBox):
                    child.setChecked(state)
            elif self.sender() == self.data_verification:
                state = self.data_verification.isChecked()
                for child in self.data_verification.findChildren(QCheckBox):
                    child.setChecked(state)

    def construct_chosen_tests_list(self):
        """Checks every checkbox. If one is enabled and checked, it is added
        to the list of selected tests"""
        lst = []
        for child in self.data_verification.findChildren(QCheckBox):
            if child.isEnabled() and child.isChecked():
                lst.append(child.objectName())
        for child in self.one_time_checks.findChildren(QCheckBox):
            if child.isEnabled() and child.isChecked():
                lst.append(child.objectName())
        return lst

    # TODO rewrite
    # def create_test_environment(self, chosen_tests):
    #     """
    #     Gathers all information needed to run the associated tests
    #     """
    #     src_path, output_dict = get_working_paths(
    #         test_type=1,
    #         active_paths=self.caller.current_source_paths,
    #         base_folder_output=self.output_selector.filePath(),
    #     )
    #     layer_groups_structure = QgisLayerStructure()
    #     layers_list = get_layers_list(
    #         test_type=1,
    #         plugin_dir=self.caller.plugin_dir,
    #         output_dict=output_dict,
    #         chosen_tests=chosen_tests,
    #         group_structure=layer_groups_structure,
    #     )
    #     test_environment = testEnvironment(
    #         source_paths_dict=src_path,
    #         output_vars_dict=output_dict,
    #         layers=layers_list,
    #         selected_tests=chosen_tests,
    #         group_structure=layer_groups_structure,
    #     )

    #     test_environment.file_dict = {}
    #     test_environment.file_dict["model_path"] = self.model_selector.filePath()
    #     test_environment.file_dict["damo_path"] = self.damo_selector.filePath()
    #     test_environment.file_dict["hdb_path"] = self.hdb_selector.filePath()
    #     test_environment.file_dict["polder_polygon_path"] = self.polder_shape_selector.filePath()
    #     test_environment.file_dict["channels_from_profiles_path"] = self.channel_from_profiles_selector.filePath()
    #     test_environment.file_dict["dem_path"] = self.dem_selector.filePath()
    #     # test_environment.file_dict['output_path'] = self.output_selector.filePath() #TODO waarom staat dit uit?
    #     test_environment.file_dict["datachecker_path"] = self.datachecker_selector.filePath()

    #     return test_environment

    def verify_submit(self):
        """
        Checks whether all fields are correctly filled
        """
        self.selected_tests = self.construct_chosen_tests_list()
        # res, message = verify_input(
        #     chosen_tests_list=chosen_tests,
        #     output_path=self.output_selector.filePath(),
        #     model_path=self.model_selector.filePath(),
        #     dem_path=self.dem_selector.filePath(),
        #     datachecker_path=self.datachecker_selector.filePath(),
        #     channel_shapefile=self.channel_from_profiles_selector.filePath(),
        #     hdb_path=self.hdb_selector.filePath(),
        #     damo_path=self.damo_selector.filePath(),
        #     polder_shapefile=self.polder_shape_selector.filePath(),
        # )
        # if not res:
        #     self.bar.pushMessage(message, Qgis.Critical)
        # else:
        # test_environment = self.create_test_environment(chosen_tests)
        self.start_sqlite_tests.emit(self.selected_tests)
        self.accept()
        # self.sqlite_tests_execution()


                # def setup_main_paths_signals(self):
                #     """
                #     Connects changes in fields (for example the selection of a file) to the function
                #     that updates (and keeps track of) the current fields for the entire plugin
                #     """
                #     self.datachecker_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(datachecker=path))
                #     self.damo_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(damo=path))
                #     self.hdb_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(hdb=path))
                #     self.polder_shape_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(polder_shapefile=path))
                #     self.channel_from_profiles_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(channels_shapefile=path))
                #     self.model_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(model=path))
                #     self.dem_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(dem=path))
                #     self.output_selector.fileSelected.connect(lambda path: self.caller.update_current_paths(sqlite_output=path))

    def set_current_paths(self):
        """
        Sets current paths as known to main widget to this widget's fields
        """
        paths = self.caller.current_source_paths
        # if paths is not None:
        #     self.polders_map_selector.setFilePath(paths["polder_folder"])
        #     self.model_selector.setFilePath(paths["model"])
        #     self.dem_selector.setFilePath(paths["dem"])
        #     self.datachecker_selector.setFilePath(paths["datachecker"])
        #     self.channel_from_profiles_selector.setFilePath(paths["channels_shapefile"])
        #     self.hdb_selector.setFilePath(paths["hdb"])
        #     self.damo_selector.setFilePath(paths["damo"])
        #     self.polder_shape_selector.setFilePath(paths["polder_shapefile"])
        #     self.output_selector.setFilePath(paths["sqlite_tests_output"])


    # def sqlite_tests_execution(self):
    #     try:
    #         #Execute tasks
    #         task_sqlite_tests_main(parent_widget=self.caller.sqlite_results_widget, folder=self.caller.fenv, selected_tests=self.selected_tests)

    #         #Load results in project.

    #         QgsMessageLog.logMessage(
    #         f"ALL DONE ON POPUP", level=Qgis.Info
    #         )
    #         # load_layers_interaction.load_layers_test_sqlite(folder=self.caller.fenv)

    #     except Exception as e:
    #         self.caller.iface.messageBar().pushMessage(str(e), Qgis.Critical)
    #         pass


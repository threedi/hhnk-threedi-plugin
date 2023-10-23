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
from hhnk_threedi_plugin.gui.utility.widget_interaction import update_button_background




def setupUi(sqlite_dialog):
    sqlite_dialog.setWindowTitle("Model sqlite checks")
    sqlite_dialog.setMinimumWidth(500)

    # Create message bar for error logging
    sqlite_dialog.bar = QgsMessageBar()

    # Create button to start tests
    sqlite_dialog.start_sqlite_tests_btn = QPushButton("Start tests")

    # Create all checkboxes group
    sqlite_dialog.all_tests = QGroupBox("Selecteer tests")

    # Create quick tests checkboxes and group
    sqlite_dialog.data_verification = QCheckBox("Data verificatie")
    sqlite_dialog.data_verification.setCheckable(True)
    sqlite_dialog.data_verification.setChecked(True)
    
    ## versie met check-boxes per test
    # sqlite_dialog.impervious_surface_chk = QCheckBox("Ondoorlatend oppervlak")
    # sqlite_dialog.impervious_surface_chk.setObjectName("impervious_surface_chk")
    # sqlite_dialog.profiles_used_chk = QCheckBox("Gebruikte profielen")
    # sqlite_dialog.profiles_used_chk.setObjectName("profiles_used_chk")
    # sqlite_dialog.controlled_structs_chk = QCheckBox("Gestuurde kunstwerken")
    # sqlite_dialog.controlled_structs_chk.setObjectName("controlled_structs_chk")
    # sqlite_dialog.weir_height_chk = QCheckBox("Bodemhoogte stuw")
    # sqlite_dialog.weir_height_chk.setObjectName("weir_height_chk")
    # sqlite_dialog.geometry_chk = QCheckBox("Geometrie")
    # sqlite_dialog.geometry_chk.setObjectName("geometry_chk")
    # sqlite_dialog.structs_channel_chk = QCheckBox("Bodemhoogte kunstwerken")
    # sqlite_dialog.structs_channel_chk.setObjectName("structs_channel_chk")
    # sqlite_dialog.general_tests_chk = QCheckBox("Algemene tests")
    # sqlite_dialog.general_tests_chk.setObjectName("general_tests_chk")
    # sqlite_dialog.isolated_channels_chk = QCheckBox("Geisoleerde watergangen")
    # sqlite_dialog.isolated_channels_chk.setObjectName("isolated_channels_chk")
    # sqlite_dialog.grid_chk = QCheckBox("Genereer grid")
    # sqlite_dialog.grid_chk.setObjectName("grid_chk")
    # sqlite_dialog.cross_section_duplicate_chk = QCheckBox("Dubbele cross-sections")
    # sqlite_dialog.cross_section_duplicate_chk.setObjectName("cross_section_duplicate_chk")
    # sqlite_dialog.cross_section_no_vertex_chk = QCheckBox("Cross-section niet op channel vertex")
    # sqlite_dialog.cross_section_no_vertex_chk.setObjectName("cross_section_no_vertex_chk")



    # Create slow tests checkboxes and group
    sqlite_dialog.one_time_checks = QCheckBox("Eenmalige tests", sqlite_dialog.all_tests)
    sqlite_dialog.one_time_checks.setCheckable(True)
    sqlite_dialog.one_time_checks.setChecked(False)
    
    ## versie met check-boxes per test
    # sqlite_dialog.max_dem_chk = QCheckBox(text="Maximale waarde DEM")
    # sqlite_dialog.max_dem_chk.setObjectName("max_dem_chk")
    # sqlite_dialog.dewatering_depth_chk = QCheckBox(text="Ontwateringsdiepte")
    # sqlite_dialog.dewatering_depth_chk.setObjectName("dewatering_depth_chk")
    # sqlite_dialog.watersurface_area_chk = QCheckBox("Oppervlaktewater")
    # sqlite_dialog.watersurface_area_chk.setObjectName("watersurface_area_chk")

    # Layouts
    #separator = QFrame()
    #separator.setFrameShape(QFrame.HLine)
    #separator.setFrameShadow(QFrame.Sunken)

    # Create checkboxes layout
    # quick checks
    # verif_layout = QVBoxLayout()
    # verif_layout.setAlignment(Qt.AlignTop)
    # verif_layout.addWidget(sqlite_dialog.impervious_surface_chk)
    # verif_layout.addWidget(sqlite_dialog.profiles_used_chk)
    # verif_layout.addWidget(sqlite_dialog.controlled_structs_chk)
    # verif_layout.addWidget(sqlite_dialog.weir_height_chk)
    # verif_layout.addWidget(sqlite_dialog.geometry_chk)
    # verif_layout.addWidget(sqlite_dialog.structs_channel_chk)
    # verif_layout.addWidget(sqlite_dialog.general_tests_chk)
    # verif_layout.addWidget(sqlite_dialog.isolated_channels_chk)
    # verif_layout.addWidget(sqlite_dialog.grid_chk)
    # verif_layout.addWidget(sqlite_dialog.cross_section_duplicate_chk)
    # verif_layout.addWidget(sqlite_dialog.cross_section_no_vertex_chk)
    # sqlite_dialog.data_verification.setLayout(verif_layout)

    # Slow tests
    # one_time_layout = QVBoxLayout()
    # one_time_layout.setAlignment(Qt.AlignTop)
    # one_time_layout.addWidget(sqlite_dialog.max_dem_chk)
    # one_time_layout.addWidget(sqlite_dialog.dewatering_depth_chk)
    # one_time_layout.addWidget(sqlite_dialog.watersurface_area_chk)
    # sqlite_dialog.one_time_checks.setLayout(one_time_layout)

    # Combined
    checkboxes_layout = QVBoxLayout()
    checkboxes_layout.addWidget(sqlite_dialog.data_verification)
    checkboxes_layout.addWidget(sqlite_dialog.one_time_checks)
    sqlite_dialog.all_tests.setLayout(checkboxes_layout)

    # Main layout
    #paths_selection = QLabel("Selecteer benodigde bestanden")
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.addWidget(sqlite_dialog.bar)
    #main_layout.addWidget(paths_selection)
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
        
        ## versie met check-boxes per test
        # for child in self.data_verification.findChildren(QCheckBox):
        #     if child.isEnabled() and child.isChecked():
        #         lst.append(child.objectName())
        # for child in self.one_time_checks.findChildren(QCheckBox):
        #     if child.isEnabled() and child.isChecked():
        #         lst.append(child.objectName())
        if self.data_verification.isChecked():
            lst += [
                "impervious_surface_chk",
                "profiles_used_chk",
                "controlled_structs_chk",
                "weir_height_chk",
                "geometry_chk",
                "structs_channel_chk",
                "general_tests_chk",
                "isolated_channels_chk",
                "grid_chk",
                "cross_section_duplicate_chk",
                "cross_section_no_vertex_chk",
                ]
        if self.one_time_checks.isChecked():
            lst += [
                "max_dem_chk",
                "dewatering_depth_chk",
                "watersurface_area_chk"
                ]
        
        return lst

    def verify_submit(self):
        """
        Checks whether all fields are correctly filled
        """
        update_button_background(button=self.start_sqlite_tests_btn, color="orange")
        self.selected_tests = self.construct_chosen_tests_list()

        self.start_sqlite_tests.emit(self.selected_tests)
        self.accept()
        update_button_background(button=self.start_sqlite_tests_btn, color="green")


    def set_current_paths(self):
        """
        Sets current paths as known to main widget to this widget's fields
        """
        paths = self.caller.current_source_paths

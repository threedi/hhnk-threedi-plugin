# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HHNK_toolbox
                                 A QGIS plugin
 Plugin voor watersystemen analyse
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-04-02
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Laure Ravier, HHNK
        email                : L.Ravier@hhnk.nl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsApplication, Qgis, QgsProject
from qgis.utils import showPluginHelp

# Initialize Qt resources from file resources.py
from .resources import *

# Import the code for the DockWidget
from .hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget
import os.path


# Import the code for the plugin content
# GUI
from .gui.load_layers_popup import loadLayersDialog
from .gui.tests.sqlite_tests.sqlite_check_popup import sqliteCheckDialog
from .gui.tests.one_d_two_d.one_d_two_d import oneDTwoDWidget
from .gui.model_states.model_states import modelStateDialog
from .gui.tests.zero_d_one_d.zero_d_one_d import zeroDOneDWidget
from .gui.tests.sqlite_tests.result_widgets.main_result_widget import collapsibleTree
from .gui.tests.bank_levels.bank_levels import bankLevelsWidget
from .gui.klimaatsommen.klimaatsommen import KlimaatSommenWidget

from .gui.new_project_dialog import newProjectDialog

# Functions
from hhnk_threedi_tools import Folders
from hhnk_threedi_tools.core.checks.model_state import detect_model_states

# Variables
from hhnk_threedi_tools.variables.model_state import invalid_path

# Test controllers
from .functionality_controllers.test_controllers.run_sqlite_tests import (
    run_sqlite_tests,
)
from .functionality_controllers.model_states_conversion import (
    run_model_states_conversion,
)
from .functionality_controllers.test_controllers.run_bank_levels_test import (
    run_bank_levels_test,
)
from .functionality_controllers.test_controllers.run_hydraulic_tests import (
    run_hydraulic_tests,
)
from .functionality_controllers.test_controllers.run_1d2d_tests import run_1d2d_tests


# docs
import webbrowser

DOCS_LINK = "https://hhnk-toolbox-user-docs.readthedocs.io/nl/latest/"


class HHNK_toolbox:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        self.help_address = "https://hhnk-toolbox-user-docs.readthedocs.io/nl/latest/"

        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        locale_path = os.path.join(
            self.plugin_dir, "i18n", "HHNK_threedi_toolbox_{}.qm".format(locale)
        )

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u"&HHNK threedi toolbox")
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u"HHNK_threedi_toolbox")
        self.toolbar.setObjectName(u"HHNK_threedi_toolbox")

        # print "** INITIALIZING HHNK_toolbox"

        self.pluginIsActive = False
        self.dockwidget = None

        # Program specific variables
        self.sqlite_tests_dialog = None
        self.sqlite_results_widget = None
        self.model_states_dialog = None
        self.model_states_results_widget = None
        self.zero_d_one_d = None
        self.bank_levels = None
        self.bank_levels_results_widget = None
        self.one_d_two_d = None
        self.polder_folder = None
        self.current_source_paths = None
        # Keep tracks of last chosen source paths over the entire toolbox

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate("HHNK_threedi_toolbox", message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None,
    ):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ":/plugins/hhnk_toolbox/hhnk_logo.jpg"
        help_path = ":/plugins/hhnk_toolbox/help_icon.png"
        self.add_action(
            icon_path,
            text=self.tr(u"HHNK threedi Toolbox"),
            callback=self.run,
            parent=self.iface.mainWindow(),
        )
        self.add_action(
            help_path,
            text="Help",
            callback=self.open_help,
            parent=self.iface.mainWindow(),
            add_to_toolbar=False,
        )

    # --------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        # print "** CLOSING HHNK_toolbox"

        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)
        # remove this statement if dockwidget is to remain
        # for reuse if plugin is reopened
        # Commented next statement since it causes QGIS crashe
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        # print "** UNLOAD HHNK_toolbox"
        for action in self.actions:
            self.iface.removePluginMenu(self.tr(u"&HHNK threedi toolbox"), action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    # --------------------------------------------------------------------------
    # Program specific functions
    def reset_ui(self, polder=None, model=None):
        """
        If we select a new polder folder we have to reset all result showing items
        """
        if polder is not None or model is not None:
            if (
                self.model_states_results_widget is not None
                and self.model_states_results_widget
                and self.model_states_results_widget.isVisible()
            ):
                self.model_states_results_widget.close()
            if (
                self.bank_levels_results_widget is not None
                and self.bank_levels_results_widget
                and self.bank_levels_results_widget.isVisible()
            ):
                self.bank_levels_results_widget.close()

    def polder_folder_changed(self):
        """
        If a new polder is selected, based on validity of provided path:
        reset the current active paths
        enable or disable toolbox
        """
        path = self.dockwidget.polder_selector.filePath()
        if not os.path.exists(os.path.join(path, "01_Source_data")):
            QMessageBox.warning(None, "Loading polder", "Incorrect folder!")
            return

        print("Found polder folder", path)
        self.reset_ui(polder=path)
        if path is not None and os.path.exists(path):
            folder = Folders(path)
            self.fenv = folder
            self.polder_folder = path
            self.current_source_paths = folder.to_file_dict()
            self.initialize_current_paths()
            self.dockwidget.model_state_btn.setEnabled(True)
            self.dockwidget.tests_toolbox.setEnabled(True)
        else:
            self.polder_folder = None
            if self.current_source_paths is not None:
                for key, value in self.current_source_paths.items():
                    self.current_source_paths[key] = None
                self.initialize_current_paths()
            self.dockwidget.model_state_btn.setEnabled(False)
            self.dockwidget.tests_toolbox.setEnabled(False)

    def initialize_current_paths(self):
        """
        When we create the default paths dict, set values to all widgets
        """
        self.load_layers_dialog.set_current_paths()
        self.model_states_dialog.set_current_paths()
        self.sqlite_tests_dialog.set_current_paths()
        self.zero_d_one_d.set_current_paths()
        self.bank_levels.set_current_paths()
        self.one_d_two_d.set_current_paths()

    def update_model_state(self):
        if self.current_source_paths is not None:
            current_state = detect_model_states(self.current_source_paths["model"])
            self.dockwidget.model_state_show.setText(current_state)
        else:
            self.dockwidget.model_state_show.setText(invalid_path)

    def update_current_paths(
        self,
        datachecker=None,
        damo=None,
        hdb=None,
        polder_shapefile=None,
        channels_shapefile=None,
        model=None,
        dem=None,
        zero_d_results=None,
        one_d_results=None,
        sqlite_output=None,
        zero_d_output=None,
        bank_levels_output=None,
        one_d_output=None,
    ):
        """
        Function is called if a path changes within a widget that is needed in other tests.
        This way we keep track of last specified paths. We immediately update all other paths too.
        """
        if self.current_source_paths is not None:
            if datachecker is not None:
                self.current_source_paths["datachecker"] = datachecker
                self.model_states_dialog.datachecker_selector.setFilePath(datachecker)
                self.sqlite_tests_dialog.datachecker_selector.setFilePath(datachecker)
                self.bank_levels.datachecker_selector.setFilePath(datachecker)
            if damo is not None:
                self.current_source_paths["damo"] = damo
            if hdb is not None:
                self.current_source_paths["hdb"] = hdb
            if polder_shapefile is not None:
                self.current_source_paths["polder_shapefile"] = polder_shapefile
            if channels_shapefile is not None:
                self.current_source_paths["channels_shapefile"] = channels_shapefile
            if model is not None:
                self.reset_ui(model=model)
                self.current_source_paths["model"] = model
                self.update_model_state()
                self.model_states_dialog.model_selector.setFilePath(model)
                self.model_states_dialog.model_changed()
                self.sqlite_tests_dialog.model_selector.setFilePath(model)
                self.bank_levels.model_selector.setFilePath(model)
                self.one_d_two_d.model_selector.setFilePath(model)
            if dem is not None:
                self.current_source_paths["dem"] = dem
                self.sqlite_tests_dialog.dem_selector.setFilePath(dem)
                self.one_d_two_d.dem_selector.setFilePath(dem)
            if zero_d_results is not None:
                self.current_source_paths["0d1d_results_dir"] = zero_d_results
            if one_d_results is not None:
                self.current_source_paths["1d2d_results_dir"] = one_d_results
            if sqlite_output is not None:
                self.current_source_paths["sqlite_tests_output"] = sqlite_output
            if zero_d_output is not None:
                self.current_source_paths["0d1d_output"] = zero_d_output
            if bank_levels_output is not None:
                self.current_source_paths["bank_levels_output"] = bank_levels_output
            if one_d_output is not None:
                self.current_source_paths["1d2d_output"] = one_d_output

    # --------------------------------------------------------------------------
    # Start tests and conversions
    # --------------------------------------------------------------------------

    def model_states_execution(self, test_env):
        try:
            if (
                self.model_states_results_widget is not None
                and self.model_states_results_widget
                and self.model_states_results_widget.isVisible()
            ):
                self.model_states_results_widget.close()

            # add the polder folder to the environment
            test_env.polder_folder = self.polder_folder

            self.model_states_results_widget = run_model_states_conversion(
                test_env=test_env,
                parent=self.dockwidget,
                on_succes=self.update_current_paths,
            )
        except Exception as e:
            self.iface.messageBar().pushMessage(str(e), Qgis.Critical)
            pass

    def sqlite_tests_execution(self, test_env):
        try:
            test_env.polder_folder = self.polder_folder
            run_sqlite_tests(
                results_widget=self.sqlite_results_widget, test_env=test_env
            )
        except Exception as e:
            self.iface.messageBar().pushMessage(str(e), Qgis.Critical)
            pass

    def zero_d_one_d_tests_execution(self, test_env):
        try:
            test_env.polder_folder = self.polder_folder
            run_hydraulic_tests(test_env=test_env)
        except Exception as e:
            self.iface.messageBar().pushMessage(str(e), Qgis.Critical)
            pass

    def bank_levels_execution(self, test_env):
        try:
            if (
                self.bank_levels_results_widget is not None
                and self.bank_levels_results_widget
                and self.bank_levels_results_widget.isVisible()
            ):
                self.bank_levels_results_widget.close()

            test_env.polder_folder = self.polder_folder
            self.bank_levels_results_widget = run_bank_levels_test(
                test_env=test_env, parent=self.dockwidget
            )
        except Exception as e:
            self.iface.messageBar().pushMessage(str(e), Qgis.Critical)
            pass

    def one_d_two_d_tests_execution(self, test_env):
        try:
            test_env.polder_folder = self.polder_folder
            run_1d2d_tests(test_env=test_env)
        except Exception as e:
            self.iface.messageBar().pushMessage(str(e), Qgis.Critical)
            pass

    def new_project_folder_execute(self):
        dialog = newProjectDialog()
        dialog.project_folder_path.connect(Folders)
        dialog.exec()
        QMessageBox.information(None, "Create project", "Your folders are created!")

    def open_documentatie_link(self):
        webbrowser.open(DOCS_LINK, new=2)

    def open_help(self):
        os.startfile(self.help_address)

    def run(self):
        """Run method that loads and starts the plugin"""

        if not self.pluginIsActive:
            self.pluginIsActive = True

            # print "** STARTING HHNK_toolbox"

            # dockwidget may not exist if:
            #    first run of plugin
            #    removed on close (see self.onClosePlugin method)
            if self.dockwidget == None:
                # Create the dockwidget (after translation) and keep reference
                self.dockwidget = HHNK_toolboxDockWidget()
                self.load_layers_dialog = loadLayersDialog(
                    caller=self, parent=self.dockwidget
                )
                self.sqlite_tests_dialog = sqliteCheckDialog(
                    caller=self, parent=self.dockwidget
                )
                self.model_states_dialog = modelStateDialog(
                    caller=self, parent=self.dockwidget
                )
                self.klimaatsommen = KlimaatSommenWidget(
                    caller=self, parent=self.dockwidget
                )
                self.zero_d_one_d = zeroDOneDWidget(caller=self, parent=self.dockwidget)
                self.bank_levels = bankLevelsWidget(caller=self, parent=self.dockwidget)
                self.one_d_two_d = oneDTwoDWidget(caller=self, parent=self.dockwidget)

                # If a polder folder is selected
                self.dockwidget.polder_selector.fileChanged.connect(
                    self.polder_folder_changed
                )
                # Controls widgets showing results
                self.sqlite_results_widget = collapsibleTree(
                    self.dockwidget.sqlite_tests
                )
                self.dockwidget.sqlite_tests.layout().addWidget(
                    self.sqlite_results_widget
                )
                # Add tabs to the main toolbox

                self.dockwidget.tests_toolbox.addItem(
                    self.klimaatsommen, "Klimaatsommen"
                )
                self.dockwidget.tests_toolbox.addItem(self.zero_d_one_d, "0d1d tests")
                self.dockwidget.tests_toolbox.addItem(self.bank_levels, "Bank levels")
                self.dockwidget.tests_toolbox.addItem(self.one_d_two_d, "1d2d tests")
                # Connect popups to buttons that prompt them
                self.dockwidget.load_layers_btn.clicked.connect(
                    self.load_layers_dialog.set_current_paths
                )
                self.dockwidget.load_layers_btn.clicked.connect(
                    self.load_layers_dialog.exec
                )  # exec dwingt af dat je 1 window open kan hebben.
                self.dockwidget.start_sqlite_check.clicked.connect(
                    self.sqlite_tests_dialog.set_current_paths
                )
                self.dockwidget.start_sqlite_check.clicked.connect(
                    self.sqlite_tests_dialog.show
                )
                self.dockwidget.model_state_btn.clicked.connect(
                    self.model_states_dialog.set_current_paths
                )
                self.dockwidget.model_state_btn.clicked.connect(
                    self.model_states_dialog.show
                )
                self.dockwidget.create_new_project_btn.clicked.connect(
                    self.new_project_folder_execute
                )

                self.dockwidget.documentatie_button.clicked.connect(
                    self.open_documentatie_link
                )

                # Connect start buttons to appropriate function calls
                self.model_states_dialog.start_conversion.connect(
                    self.model_states_execution
                )
                self.sqlite_tests_dialog.start_sqlite_tests.connect(
                    self.sqlite_tests_execution
                )
                self.zero_d_one_d.start_0d1d_tests.connect(
                    self.zero_d_one_d_tests_execution
                )
                self.bank_levels.start_bank_levels_tests.connect(
                    self.bank_levels_execution
                )
                self.one_d_two_d.start_1d2d_tests.connect(
                    self.one_d_two_d_tests_execution
                )

                # note that for 'klimaatsommen' functions are run from the widget

            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)

            # show the dockwidget
            # TODO: fix to allow choice of dock location
            self.iface.addTabifiedDockWidget(
                Qt.RightDockWidgetArea, self.dockwidget, raiseTab=True
            )
            self.dockwidget.show()

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
import os.path
from pathlib import Path
from pyexpat import model
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsApplication, Qgis, QgsProject, QgsVectorLayer
from qgis.utils import QgsMessageLog, showPluginHelp
import datetime

# Initialize Qt resources from file resources.py
from hhnk_threedi_plugin.resources import *
# Import the code for the DockWidget
# %%
try: 
    import hhnk_threedi_plugin.local_settings as local_settings
except ModuleNotFoundError:
    import hhnk_threedi_plugin.local_settings_default as local_settings

# Import the code for the plugin content
# GUI
from hhnk_threedi_plugin.hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget
from hhnk_threedi_plugin.gui.load_layers_popup import loadLayersDialog
# from hhnk_threedi_plugin.gui.schematisation_splitter_uploader_dialog import schematisationDialog
from hhnk_threedi_plugin.gui.checks.sqlite_check_popup import sqliteCheckDialog
from hhnk_threedi_plugin.gui.checks.zero_d_one_d import zeroDOneDWidget
from hhnk_threedi_plugin.gui.checks.one_d_two_d import oneDTwoDWidget
#from hhnk_threedi_plugin.gui.model_states.model_states import modelStateDialog
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.main_result_widget import collapsibleTree
from hhnk_threedi_plugin.gui.checks.bank_levels import bankLevelsWidget
from hhnk_threedi_plugin.gui.klimaatsommen.klimaatsommen import KlimaatSommenWidget
from hhnk_threedi_plugin.qgis_interaction.project import Project
from hhnk_threedi_plugin.gui.new_project_dialog import newProjectDialog
from hhnk_threedi_plugin.gui.input_data import inputDataDialog
from hhnk_threedi_plugin.qgis_interaction.open_notebook import NotebookWidget

from hhnk_threedi_plugin.gui.modelbuilder import ModelBuilder


# %%
# Functions
from hhnk_threedi_tools.core.folders import Folder, Folders
# from hhnk_threedi_tools.core.checks.model_state import detect_model_states

# Variables
from hhnk_threedi_tools.variables.model_state import invalid_path

import hhnk_threedi_tools.core.schematisation.upload as upload

from hhnk_threedi_plugin.tasks.task_sqlite_tests_main import task_sqlite_tests_main

import os

from hhnk_threedi_plugin.gui.model_splitter.model_splitter_dialog import modelSplitterDialog
import hhnk_research_tools as hrt


# docs

import webbrowser

DOCS_LINK = "https://threedi.github.io/hhnk-threedi-plugin/"

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
        self.help_address = "https://threedi.github.io/hhnk-threedi-plugin/"

        # initialize locale
        locale = QSettings().value("locale/userLocale")
        if locale is not None:
            locale_path = os.path.join(
                self.plugin_dir, "i18n", "HHNK_threedi_toolbox_{}.qm".format(locale[0:2])
            )
    
            if os.path.exists(locale_path):
                self.translator = QTranslator()
                self.translator.load(locale_path)
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u"&HHNK threedi toolbox")
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u"hhnk_threedi_plugin")
        self.toolbar.setObjectName(u"hhnk_threedi_plugin")

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
        self.one_d_two_d = None
        self.polder_folder = None
        self.current_source_paths = None
        self.modelbuilder = None

        self.debug = local_settings.DEBUG
    
    @property
    def polders_path(self):
        if self.dockwidget.polders_map_selector.filePath():
            return Path(self.dockwidget.polders_map_selector.filePath())

    def enable_buttons(self, enabled):
        self.dockwidget.model_splitter_btn.setEnabled(enabled)
        self.dockwidget.tests_toolbox.setEnabled(enabled)
        self.dockwidget.server_btn.setEnabled(enabled)
        self.dockwidget.input_btn.setEnabled(enabled)
        self.dockwidget.create_new_project_btn.setEnabled(enabled)
        self.dockwidget.load_layers_btn.setEnabled(enabled)

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
        return QCoreApplication.translate("hhnk_threedi_plugin", message)

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

        icon_path = os.path.join(self.plugin_dir, "icons/hhnk_logo.jpg")
        help_path = os.path.join(self.plugin_dir, "icons/help_icon.png") #":/plugins/hhnk_toolbox/icons/help_icon.png"
        self.add_action(
            icon_path,
            text=self.tr(u"HHNK Threedi Plugin"),
            callback=self.run,
            parent=self.iface.mainWindow(),
        )
        self.add_action(
            help_path,
            text="Help",
            callback=self.open_help,
            parent=self.iface.mainWindow(),
            add_to_toolbar=True,
        )
        
        self.initProcessing()

    def initProcessing(self):
        """Create the Qgis Processing Toolbox provider and its algorithms"""
        self.provider = HHNKProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)
    # --------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        # print("** CLOSING HHNK_toolbox")

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
                self.bank_levels is not None
                and self.bank_levels
                and self.bank_levels.isVisible()
            ):
                self.bank_levels.close()       

    # Select from the dockwidget the path where the polder is located. If the path is not correct or if it is empty I will not enabled the buttons 
    def polders_folder_changed(self):
        """
        Updates polder_selector from the contents of the path in polders_map_selector
        """
        if self.debug:
            self.add_message("polders_folder_changed start")
        items = []
        # get the contents of the folder in polders_map_selector
        path = self.dockwidget.polders_map_selector.filePath()

        if path is not None:
            if (path != "") and Path(path).exists():
                folder = Folder(path)

                # clean the contents (only accept valid Folders directories)
                items = [i.name for i in folder.content if Folders.is_valid(Path(path)/i)]

            
        # add items to the polder_selector
        self.dockwidget.polder_selector.clear()
        if items:
            self.dockwidget.polder_selector.addItems(items)
            self.dockwidget.polder_selector.setEnabled(True)
        else:
            self.dockwidget.polder_selector.setDisabled(False)

        if self.debug:
            self.add_message("polders_folder_changed end")


    def polder_changed(self):
        """
        If a new polder is selected, based on validity of provided path:
        reset the current active paths
        enable or disable toolbox
        """
        if self.debug:
            self.add_message("polder_changed start")

        polders_dir = self.dockwidget.polders_map_selector.filePath()
        polder = self.dockwidget.polder_selector.currentText()
        path = Path(polders_dir) / polder

        print("Found folder", path)
        self.reset_ui(polder=polder)
        if (polder != "") and path.exists():
            folder = Folders(path)
            self.fenv = folder #FIXME replace with self.folder in all scripts.
            self.folder = folder
            self.polder_folder = path.as_posix()
            self.current_source_paths = folder.to_file_dict()
            self.enable_buttons(True)
            if not os.path.exists(os.path.join(path, "01_Source_data")):
                QMessageBox.warning(None, "Loading polder", "Incorrect folders!")
                return
            else:
                self.initialize_current_paths()
        else:
            self.fenv=None
            self.folder = None
            self.polder_folder = None
            # TODO: verify if deleting the commented block with self.current_source_paths = None is a good idea
            self.current_source_paths = None
            # if self.current_source_paths is not None:
            #     for key, value in self.current_source_paths.items():
            #         self.current_source_paths[key] = None
            #     self.initialize_current_paths()

            self.enable_buttons(False)
            # self.dockwidget.load_layers_btn.setEnabled(True)

        if self.debug:
            self.add_message("polder_changed end")



    def initialize_current_paths(self):
        """
        When we create the default paths dict, set values to all widgets
        """
        self.load_layers_dialog.set_current_paths()
        #self.model_states_dialog.set_current_paths()
        # self.sqlite_tests_dialog.set_current_paths()
        # self.zero_d_one_d.set_current_paths()
        # self.one_d_two_d.set_current_paths()
        # self.schematisation_dialog.set_current_paths()
        self.input_data_dialog.set_current_paths()

    # def update_model_state(self):
    #     if self.current_source_paths is not None:
    #         current_state = detect_model_states(self.current_source_paths["model"])
    #         self.dockwidget.model_state_show.setText(current_state)
    #     else:
    #         self.dockwidget.model_state_show.setText(invalid_path)

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
                # self.input_data_dialog.datachecker_selector.setFilePath(datachecker)
                # self.sqlite_tests_dialog.datachecker_selector.setFilePath(datachecker)
                # self.sqlite_tests_dialog.datachecker_selector.setFilePath(datachecker)
                # self.bank_levels.datachecker_selector.setFilePath(datachecker)
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
                # self.update_model_state()
                # self.input_data_dialog.model_selector.setFilePath(model)
                # self.bank_levels.model_selector.setFilePath(model)
                # self.one_d_two_d.model_selector.setFilePath(model)

            if dem is not None:
                self.current_source_paths["dem"] = dem
                #self.sqlite_tests_dialog.dem_selector.setFilePath(dem)
                # self.input_data_dialog.dem_selector.setFilePath(dem)
                # self.one_d_two_d.dem_selector.setFilePath(dem)

            if zero_d_results is not None:
                self.current_source_paths["0d1d_results_dir"] = zero_d_results

            if one_d_results is not None:
                self.current_source_paths["1d2d_results_dir"] = one_d_results
                # self.input_data_dialog.results_dir_selector.setFilePath(one_d_results)
                # self.one_d_two_d.results_dir_selector.setFilePath(one_d_results)

            if sqlite_output is not None:
                self.current_source_paths["sqlite_tests_output"] = sqlite_output
            
            if zero_d_output is not None:
                self.current_source_paths["0d1d_output"] = zero_d_output
            if bank_levels_output is not None:
                self.current_source_paths["bank_levels_output"] = bank_levels_output

            if one_d_output is not None:
                self.current_source_paths["1d2d_output"] = one_d_output
                # self.input_data_dialog.output_selector.setFilePath(one_d_output)
                # self.one_d_two_d.output_selector.setFilePath(one_d_output)


    # --------------------------------------------------------------------------
    # Start tests and conversions
    # --------------------------------------------------------------------------
    def sqlite_tests_execution(self, selected_tests):
        try:
            # test_env.polder_folder = self.polder_folder
            task_sqlite_tests_main(parent_widget=self.sqlite_results_widget, folder=self.fenv, selected_tests=selected_tests)

        except Exception as e:
            self.iface.messageBar().pushMessage(str(e), Qgis.Critical)
            pass


    def new_project_folder_execute(self):
        dialog = newProjectDialog(self.polders_path)
        result = dialog.exec()
        if result:
            if dialog.polder_path is not None:
                self.dockwidget.polder_selector.addItem(dialog.polder_path.name)
                self.dockwidget.polder_selector.setCurrentText(
                    dialog.polder_path.name
                    )
      

    def open_model_splitter_dialog(self):
        if not hasattr(self, 'model_splitter_dialog'):
            self.model_splitter_dialog = modelSplitterDialog(caller=self, parent=self.dockwidget)
        self.model_splitter_dialog.show()


    def open_documentatie_link(self):
        webbrowser.open(DOCS_LINK, new=2)

    def open_help(self):
        os.startfile(self.help_address)

    def hide_apikeys_lizard(self):
        getattr(self.dockwidget, f'lizard_api_key_textbox').setEchoMode(2) #password echo mode

    def hide_apikeys_threedi(self):
        #TODO kan connect input meegeven zodat deze samen kan met lizard?
        getattr(self.dockwidget, f'threedi_api_key_textbox').setEchoMode(2) #password echo mode

    def get_org_names(self):

        if self.debug:
            self.add_message("org names start")

        api_key = getattr(self.dockwidget, f'threedi_api_key_textbox').text()
        self.dockwidget.org_name_comboBox.clear()
        try:
            organisation_names = upload.get_organisation_names(api_key)
            for i in organisation_names:
                self.dockwidget.org_name_comboBox.addItem(str(i))
        except:
            self.iface.messageBar().pushMessage(
                    'no organisation names available - check 3Di api_key and permissions', 
                    level=Qgis.Warning
                )
            
        if self.debug:
            self.add_message("org names done")

    def run(self):
        """Run method that loads and starts the plugin"""

        if not self.pluginIsActive:
            self.pluginIsActive = True

            # print "** STARTING HHNK_toolbox"

            # dockwidget may not exist if:
            #    first run of plugin
            #    removed on close (see self.onClosePlugin method)
            if self.dockwidget is None:
                # Create the dockwidget (after translation) and keep reference

                if self.debug:
                    self.add_message("starting plugin")

                self.dockwidget = HHNK_toolboxDockWidget()

                # disable predefined buttons    
                self.enable_buttons(False)
                # self.dockwidget.load_layers_btn.setEnabled(False)


                self.dockwidget.lizard_api_key_textbox.textChanged.connect(self.hide_apikeys_lizard)
                self.dockwidget.threedi_api_key_textbox.textChanged.connect(self.hide_apikeys_threedi)
                self.dockwidget.threedi_api_key_textbox.textChanged.connect(self.get_org_names)


                self.load_layers_dialog = loadLayersDialog(caller=self, parent=self.dockwidget)
                self.sqlite_tests_dialog = sqliteCheckDialog(caller=self, parent=self.dockwidget)

                # self.model_states_dialog = modelStateDialog(caller=self, parent=self.dockwidget) #TODO remove
                # self.schematisation_dialog = schematisationDialog(caller=self, parent=self.dockwidget) #TODO remove
                self.input_data_dialog = inputDataDialog(caller=self, parent=self.dockwidget)

                self.zero_d_one_d = zeroDOneDWidget(caller=self, parent=self.dockwidget)
                self.bank_levels = bankLevelsWidget(caller=self, parent=self.dockwidget)
                self.one_d_two_d = oneDTwoDWidget(caller=self, parent=self.dockwidget)
                self.klimaatsommen = KlimaatSommenWidget(caller=self, parent=self.dockwidget)
                self.notebook_widget = NotebookWidget(caller=self, parent=self.dockwidget)
                

                # If a polder folder is selected
                self.dockwidget.polders_map_selector.fileChanged.connect(self.polders_folder_changed)
                self.dockwidget.polder_selector.currentTextChanged.connect(self.polder_changed)
                # Controls widgets showing results
                self.sqlite_results_widget = collapsibleTree(self.dockwidget.sqlite_tests)
                self.dockwidget.sqlite_tests.layout().addWidget(self.sqlite_results_widget)
                # Add tabs to the main toolbox
                self.dockwidget.tests_toolbox.addItem(self.zero_d_one_d, "0d1d tests")
                self.dockwidget.tests_toolbox.addItem(self.bank_levels, "Bank levels")
                self.dockwidget.tests_toolbox.addItem(self.one_d_two_d, "1d2d tests")
                self.dockwidget.tests_toolbox.addItem(self.klimaatsommen, "Klimaatsommen")

                # Connect popups to buttons that prompt them
                self.dockwidget.load_layers_btn.clicked.connect(self.load_layers_dialog.set_current_paths)
                self.dockwidget.load_layers_btn.clicked.connect(self.load_layers_dialog.exec)  # exec dwingt af dat je 1 window open kan hebben.
                self.dockwidget.start_sqlite_check.clicked.connect(self.sqlite_tests_dialog.set_current_paths)
                self.dockwidget.start_sqlite_check.clicked.connect(self.sqlite_tests_dialog.show)

                self.dockwidget.input_btn.clicked.connect(self.input_data_dialog.set_current_paths)
                self.dockwidget.input_btn.clicked.connect(self.input_data_dialog.show)
                self.dockwidget.model_splitter_btn.clicked.connect(self.open_model_splitter_dialog)
                self.dockwidget.create_new_project_btn.clicked.connect(self.new_project_folder_execute)
               
                # self.dockwidget.documentatie_button.clicked.connect(self.open_documentatie_link)
                self.dockwidget.server_btn.clicked.connect(self.notebook_widget.start_server)
                

                # Connect start buttons to appropriate function calls

                self.sqlite_tests_dialog.start_sqlite_tests.connect(self.sqlite_tests_execution)
                # self.zero_d_one_d.start_0d1d_tests.connect(self.zero_d_one_d_tests_execution)
                # self.bank_levels.start_bank_levels_tests.connect(self.bank_levels_execution)

                # define modelbuilder. Note, all callbacks and functions you can find in ModelBuilder class
                self.modelbuilder = ModelBuilder(dockwidget=self.dockwidget)
            
                # note that for 'klimaatsomme
                # n' functions are run from the widget
            # self.dlg = modelSplitterDialog(caller=self)
            
            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)

            # show the dockwidget
            # TODO: fix to allow choice of dock location
            self.iface.addTabifiedDockWidget(Qt.RightDockWidgetArea, self.dockwidget, raiseTab=True)
            self.dockwidget.show()

            #set project_path from local_settings.
            try:
                self.dockwidget.polders_map_selector.setFilePath(local_settings.project_path)
            except:
                pass

    #TODO centraal ergens zetten?
    def add_message(self, message):
        message = f"{hrt.current_time()}: {message}"
        # QgsMessageLog.logMessage(message, level=level)
        print(message)

            
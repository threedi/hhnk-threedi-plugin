from email.mime import base
from pyexpat import model
from argon2 import PasswordHasher
from click import echo
from matplotlib.ft2font import LOAD_IGNORE_GLOBAL_ADVANCE_WIDTH
from hhnk_threedi_plugin.gui import model_states
from qgis.PyQt import uic
from threedi_api_client import ThreediApiClient
from traitlets import Unicode
import logging
from functools import wraps
from time import sleep
from threedi_api_client.openapi import ApiException
import os
from sqlite3 import Row
from pathlib import Path
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (
    QDialog,
    QFileDialog,
    QVBoxLayout,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QComboBox,
    QGroupBox,
    QCheckBox,
    QPushButton,
    QDialogButtonBox,
    QLineEdit,
    QFrame,
)
import ipywidgets as widgets
from qgis.PyQt import QtWidgets

from PyQt5.QtCore import Qt, pyqtSignal
from qgis.core import Qgis
from qgis.utils import QgsMessageBar
from ..utility.file_widget import fileWidget
from .verify_model_states_input import verify_input

# hhnk-threedi-tests

from hhnk_threedi_tools.qgis import modelConversionVariables
# from JuanTry1.modelselection.modelselection_dialog_base import 
from hhnk_threedi_tools.qgis import testEnvironment
from hhnk_threedi_tools.variables.backups_table_names import BANK_LVLS_LAST_CALC
from hhnk_threedi_tools.variables.model_state import (
    one_d_two_d_from_calc,
    hydraulic_test_state,
    one_d_two_d_state,
    one_d_two_d_keep,
)
from hhnk_threedi_tools.utils.queries import bank_lvls_last_changed

import hhnk_research_tools as hrt
from hhnk_threedi_tools.qgis.build_threedi_paths_dict import (
    build_threedi_source_paths_dict,
)

base_dir = os.path.dirname(os.path.dirname(__file__))

# uicls, basecls = uic.loadUiType(os.path.join(base_dir,"model_states", "model_states.py"))

logger = logging.getLogger(__name__)

def setup_ui(model_state_widget):
    # model_state_widget.Ui_ModelSelectionDialogBase(object)
    model_state_widget.setWindowTitle("Log in")
    model_state_widget.setMinimumWidth(500)
    separator = QFrame()
    separator.setFrameShape(QFrame.HLine)
    separator.setFrameShadow(QFrame.Sunken)
    # Creates items to be in widget
    
    model_state_widget.log_in_lbl =  QLabel('User Name:')
    model_state_widget.username = QLineEdit()
    model_state_widget.log_in_txt_psw =  QLabel('Password:')
    model_state_widget.log_in_psw = QLineEdit()
    model_state_widget.log_in_psw.EchoMode = 'Password'
    model_state_widget.log_in_btn = QPushButton('Log in')

    # Creates layout
    log_in_layout = QVBoxLayout()
    log_in_layout.setAlignment(Qt.AlignTop)
    log_in_layout.setContentsMargins(25, 25, 25, 25)

    # Add widgets to layout
    log_in_layout.addWidget(model_state_widget.log_in_lbl)
    log_in_layout.addWidget(model_state_widget.username)
    log_in_layout.addWidget(model_state_widget.log_in_txt_psw)
    log_in_layout.addWidget(model_state_widget.log_in_psw)
    log_in_layout.addWidget(model_state_widget.log_in_btn, alignment=Qt.AlignHCenter)
    model_state_widget.setLayout(log_in_layout)

def api_client_required(fn):
    """Decorator for limiting functionality access to logged-in user (with option to log in)."""

    @wraps(fn)
    def wrapper(self):
        if hasattr(self, "plugin_dock"):
            plugin_dock = getattr(self, "plugin_dock")
        else:
            plugin_dock = self
        threedi_api = getattr(plugin_dock, "threedi_api", None)
        if threedi_api is None:
            plugin_dock.communication.bar_info("Action reserved for logged in users. Please log-in before proceeding.")
            log_in_dialog = modelStateDialog(plugin_dock)
            accepted = log_in_dialog.exec_()
            if accepted:
                plugin_dock.threedi_api = log_in_dialog.threedi_api
                plugin_dock.current_user = log_in_dialog.user
                plugin_dock.current_user_full_name = log_in_dialog.user_full_name
                plugin_dock.organisations = log_in_dialog.organisations
                plugin_dock.initialize_authorized_view()
            else:
                plugin_dock.communication.bar_warn("Logging-in canceled. Action aborted!")
                return

        return fn(self)

    return wrapper

class modelStateDialog(QDialog):
    """
    Initialization:
        modelStateDialog(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))

    Signals:

    start_conversion(object (test_env))
    """

    def __init__(self, plugin_dock, parent=None):
        super(modelStateDialog, self).__init__(parent)
        setup_ui(self)
        self.plugin_dock = plugin_dock
        # self.communication = self.plugin_dock.communication
        self.user = None
        self.user_full_name = None
        self.threedi_api = None
        self.organisations = {}
        self.log_in_btn.clicked.connect(self.log_in_threedi)


    def log_in_threedi(self):
            """Method which runs all logging widgets methods and setting up needed variables."""
            username = self.username()
            password = self.password.text()
            api_url = self.plugin_dock.plugin_settings.api_url
            api_url_error_message = (
                f"Error: Invalid Base API URL '{api_url}'. "
                f"The 3Di API expects that the version is not included. "
                f"Please change the Base API URL in the 3Di Models and Simulations plugin settings."
            )#%%
            try:

                self.fetch_msg.hide()
                self.done_msg.hide()
                self.username.setText("")
                self.password.setText("")
                self.log_pbar.setValue(25)
                self.threedi_api = get_api_client(username, password, api_url)
                tc = ThreediCalls(self.threedi_api)
                user_profile = tc.fetch_current_user()
                self.user = username
                self.user_full_name = f"{user_profile.first_name} {user_profile.last_name}"
                self.log_pbar.setValue(75)
                self.fetch_msg.show()
                self.organisations = {org.unique_id: org for org in tc.fetch_organisations()}
                self.done_msg.show()
                self.wait_widget.update()
                self.log_pbar.setValue(100)
                sleep(1)
                super().accept()
            except ApiException as e:
                self.close()
                if e.status == 404:
                    error_msg = api_url_error_message
                else:
                    error_body = e.body
                    error_details = error_body["details"] if "details" in error_body else error_body
                    error_msg = f"Error: {error_details}"
                self.communication.show_error(error_msg)
            except Exception as e:
                if "THREEDI_API_HOST" in str(e):
                    error_msg = api_url_error_message
                else:
                    error_msg = f"Error: {e}"
                self.close()
                self.communication.show_error(error_msg)

    
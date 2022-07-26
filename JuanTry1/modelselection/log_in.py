#%%
import logging
import os
from functools import wraps
from time import sleep
from qgis.PyQt import uic
from threedi_api_client.openapi import ApiException
#from ..api_calls.threedi_calls import get_api_client, ThreediCalls
#%%
base_dir = os.path.dirname(os.path.dirname(__file__))
#%%
uicls, basecls = uic.loadUiType(os.path.join(base_dir,"modelselecction", "modelselection_dialog_base.ui"))

logger = logging.getLogger(__name__)

#%%
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
            log_in_dialog = LogInDialog(plugin_dock)
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
#%%

class LogInDialog(uicls, basecls):
    """Dialog with widgets and methods used in logging process."""

    def __init__(self, plugin_dock, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.plugin_dock = plugin_dock
        self.communication = self.plugin_dock.communication
        self.user = None
        self.user_full_name = None
        self.threedi_api = None
        self.organisations = {}
        self.log_in_widget.show()
        self.pb__log_in.clicked.connect(self.log_in_threedi)
        self.resize(500, 250)
        self.show_log_widget()

    def show_log_widget(self):
        """Showing logging form widget."""
        self.log_in_widget.show()
        self.setWindowTitle("HHNK")

    def log_in_threedi(self):
        """Method which runs all logging widgets methods and setting up needed variables."""
        username = self.username.text()
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



# #%%

#%%
import os 
from qgis.PyQt import uic
import ipywidgets as widgets
from qgis.PyQt import QtWidgets
from threedi_api_client import ThreediApiClient
from traitlets import Unicode



def item_layout(width="95%", grid_area="", **kwargs):
        return widgets.Layout(
            # width=width, grid_area=grid_area, **kwargs
        )
#%%
login_label = widgets.HTML(
    "<b>1. Login with 3Di account</b>", layout=item_layout(grid_area="login_label")
    )

    # Username widget
username_widget = widgets.Text(
        description="username:", layout=item_layout(width="261px", grid_area="username")
    )
#%%
    # Password widget
    class PasswordWidget(widgets.Text):
        _view_name = Unicode("password").tag(sync=True)

    password_widget = PasswordWidget(
        description="password:", layout=item_layout(width="261px", grid_area="password")
    )

    # Login button, after login create threedi api client
    login_button = widgets.Button(
        description="Login", layout=item_layout(height="30px", grid_area="login_button")
    )
#%%
    @login_button.on_click
    def login(action):
        global sim

        sim = Simulation(username_widget.value, password_widget.value)
        
        try:
            sim.logged_in
            # Login success
            login_button.style.button_color = "lightgreen"
            login_button.description = "Logged in"
            logout_button.disabled = False
        except:
            # Login failed
            login_button.style.button_color = "red"
            login_button.description = "Try again"
            logout_button.disabled = True

    logout_button = widgets.Button(
        description="Logout",
        layout=item_layout(height="30px", grid_area="logout_button"),
        disabled=True,
    )

    @logout_button.on_click
    def logout(action):
        global sim

        username_widget.value = ""
        password_widget.value = ""
        sim = None

        login_button.style.button_color = None
        login_button.description = "Login"
        logout_button.disabled = True

# %%

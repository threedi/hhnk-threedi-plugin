from dataclasses import dataclass

import requests
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QTextBrowser, QVBoxLayout
from requests.exceptions import ConnectionError

from hhnk_threedi_plugin.hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget

class LogDialog(QDialog):
    """Dialog used to display datachecker.log and schematisation_builder.log in QGIS."""

    def __init__(self, path, title, parent=None):
        super(LogDialog, self).__init__(parent)

        # Path to resource
        self.path = path
        self.setWindowTitle(title)
        # Create a QTextBrowser widget
        self.text_browser = QTextBrowser(self)
        self.text_browser.setReadOnly(True)
        self.text_browser.setMinimumWidth(800)
        self.text_browser.setMinimumHeight(800)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_browser)
        self.setLayout(layout)

    def clear(self):
        self.text_browser.clear()

    def show_log(self, url):
        # Add some text to the QTextBrowser
        self.clear()
        response = requests.get(f"{url}{self.path}")
        if response.ok:
            self.text_browser.append(response.text)
            self.show()


@dataclass
class SchematisationBuilder:
    """All actions in the schematisation_builder tab of the HHNK 3Di Toolbox."""

    dockwidget: HHNK_toolboxDockWidget

    tab_label: str = "Schematisation Builder"
    timer: QTimer = QTimer()
    status: dict = None
    _online: bool = None

    schematisation_builder_log: LogDialog = LogDialog(path=r"/schematisation_builder/log", title="SchematisationBuilder log")

    def __post_init__(self):
        """Connect all callback-functions to widgets."""

        self.dockwidget.input_dir_select.setFilePath(
            r"//corp.hhnk.nl/data/Hydrologen_data/Data/modelbuilder/data/input/"
        )
        self.dockwidget.output_dir_select.setFilePath(
            r"//corp.hhnk.nl/data/Hydrologen_data/Data/modelbuilder/data/output/"
        )

        self.timer.timeout.connect(self.check_available)
        self.dockwidget.tabWidget.currentChanged.connect(self.change_tab)
        self.dockwidget.select_server_box.currentTextChanged.connect(self.connect_schematisation_builder)
        self.dockwidget.schematisation_builder_log_btn.clicked.connect(self.show_schematisation_builder_log)
        self.dockwidget.start_schematisation_builder_btn.clicked.connect(self.start_schematisation_builder)

        # we check if we are in SchematisationBuilder.
        self.change_tab()

    def _request_status(self):
        try:
            response = requests.get(f"{self.url}/status", timeout=1)
            self._online = response.ok
            if self._online:
                self.status = response.json()
        except ConnectionError:
            self._online = False

    @property
    def online(self):
        """Server online, returns True or False."""
        if self._online is None:
            self._request_status()
        return self._online

    @property
    def available(self):
        status = self.get_status()
        if status is not None:
            return all(status.values())
        else:
            return False

    def get_status(self):
        """Server available (to start modelbuilder or datachecker), returns True or False."""
        if self.online:
            self._request_status()
        return self.status

    @property
    def url(self):
        """Server url."""
        return self.dockwidget.select_server_box.currentText()

    def start_timer(self, interval_milisecs=5000):
        """Start availability timer at interval."""
        self.timer.start(interval_milisecs)  # 5 seconds

    def stop_timer(self):
        """Stop availability timer if still active"""
        if self.timer.isActive():
            self.timer.stop()

    def set_select_server_label(self):
        """Set the select_server_label text and styling."""
        if self.online:
            self.dockwidget.select_server_label.setText("Server (online):")
            self.dockwidget.select_server_label.setStyleSheet("color: green; font: bold")
        else:
            self.dockwidget.select_server_label.setText("Server (offline):")
            self.dockwidget.select_server_label.setStyleSheet("color: red; font: bold")

    def set_modules_labels(self):
        self.get_status()
        for module in self.status.keys():
            label = getattr(self.dockwidget, f"{module}_label")
            if self.status[module]:
                label.setText(f"{module} (beschikbaar):")
                label.setStyleSheet("color: green; font: bold")
            else:
                label.setText(f"{module} (bezig):")
                label.setStyleSheet("color: orange; font: bold")

    def set_active_buttons(self, available):
        """Enable the correct buttons depending on online or available server."""
        self.dockwidget.start_schematisation_btn.setEnabled(available)
        self.dockwidget.polder_id_box.setEnabled(available)
        self.dockwidget.poldernaam_textbox.setEnabled(available)
        self.dockwidget.schematisation_builder_log_btn.setEnabled(self.online)

    def start_schematisation_builder(self):
        """Start the schematisation_builder."""
        self.get_status()
        polder_id = str(self.dockwidget.polder_id_box.value())
        polder_name = self.dockwidget.poldernaam_textbox.text()
        if polder_id and polder_name and self.status["schematisation_builder"]:
            response = requests.post(
                url=f"{self.url}/schematisation_builder/start", data={"polder_id": polder_id, "polder_name": polder_name}
            )
            if response.ok:
                self.set_unavailable()

    def show_schematisation_builder_log(self):
        """show schematisation_builder log."""
        self.schematisation_builder_log.show_log(self.url)

    def change_tab(self):
        """check if we are in or out schematisation_builder plugin tab."""
        tab_widget = self.dockwidget.tabWidget
        if tab_widget.tabText(tab_widget.currentIndex()) == self.tab_label:
            print("we are in schematisation_builder")
            self.connect_schematisation_builder()
        else:
            print("we are not in schematisation_builder")
            self.stop_timer()

    def connect_schematisation_builder(self):
        """connect to a datachecker server and check availability."""

        # check if server is online and set label
        self._online = None  # forces next line to check for status
        self.set_select_server_label()

        # check if server is available and set buttons active
        if self.status is not None:
            available = all(self.status.values())
        else:
            available = False
        self.set_active_buttons(available)

        # if online, but not available, start availability timer. Else stop timer (if running). # NOQA
        if self.online:
            if not available:
                self.set_unavailable()
            else:
                self.set_modules_labels()
        else:
            self.stop_timer()

    def check_available(self):
        """check if server is still unavailable."""
        available = self.available
        self.set_active_buttons(available=available)
        if available:
            self.set_modules_labels()
            self.stop_timer()

    def set_unavailable(self):
        """set the server to unavailable and start availability timer."""
        self.set_active_buttons(available=False)
        self.set_modules_labels()
        self.start_timer()

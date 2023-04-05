from dataclasses import dataclass
import requests
from requests.exceptions import ConnectionError
from PyQt5.QtWidgets import QDialog, QTextBrowser, QVBoxLayout
from PyQt5.QtCore import QTimer
from hhnk_threedi_plugin.hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget


class LogDialog(QDialog):
    """Dialog used to display datachecker.log and modelbuilder.log in QGIS."""

    def __init__(self, path, title, parent=None):
        super(LogDialog, self).__init__(parent)

        # Path to resource
        self.path = path
        self.setWindowTitle(title)
        # Create a QTextBrowser widget
        self.text_browser = QTextBrowser(self)
        self.text_browser.setReadOnly(True)
        self.text_browser.setMinimumWidth(500)

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
class ModelBuilder:
    """All actions in the modelbuilder tab of the HHNK 3Di Toolbox."""

    dockwidget: HHNK_toolboxDockWidget

    tab_label: str = "Modelbouw"
    timer: QTimer = QTimer()
    _online: bool = None

    datachecker_log: LogDialog = LogDialog(
        path=r"/datachecker/log",
        title="Datachecker log"
        )
    modelbuilder_log: LogDialog = LogDialog(
        path=r"/modelbuilder/log",
        title="Modelbuilder log"
        )

    def __post_init__(self):
        """Connect all callback-functions to widgets."""
        self.timer.timeout.connect(self.check_available)
        self.dockwidget.tabWidget.currentChanged.connect(self.change_tab)
        self.dockwidget.select_server_box.currentTextChanged.connect(
            self.connect_modelbuilder
            )
        self.dockwidget.datachecker_log_btn.clicked.connect(self.show_datachecker_log)
        self.dockwidget.modelbuilder_log_btn.clicked.connect(self.show_modelbuilder_log)
        self.dockwidget.start_datachecker_btn.clicked.connect(self.start_datachecker)
        self.dockwidget.start_modelbuilder_btn.clicked.connect(self.start_modelbuilder)

        # we check if we are in Modelbuilder.
        self.change_tab()

    @property
    def online(self):
        """Server online, returns True or False."""
        if self._online is None:
            try:
                response = requests.get(self.url, timeout=1)
                self._online = response.ok
            except ConnectionError:
                self._online = False
        return self._online

    @property
    def available(self):
        """Server available (to start modelbuilder or datachecker), returns True or False."""
        available = False
        if self.online:
            response = requests.get(f"{self.url}/status")
            if response.ok and (response.text == "available"):
                available = True
        return available

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
            self.dockwidget.select_server_label.setStyleSheet(
                "color: green; font: bold"
                )
        else:
            self.dockwidget.select_server_label.setText("Server (offline):")
            self.dockwidget.select_server_label.setStyleSheet(
                "color: red; font: bold"
                )

    def set_active_buttons(self, available):
        """Enable the correct buttons depending on online or available server."""
        self.dockwidget.start_datachecker_btn.setEnabled(available)
        self.dockwidget.start_modelbuilder_btn.setEnabled(available)
        self.dockwidget.polder_id_box.setEnabled(available)
        self.dockwidget.poldernaam_textbox.setEnabled(available)
        self.dockwidget.datachecker_log_btn.setEnabled(self.online)
        self.dockwidget.modelbuilder_log_btn.setEnabled(self.online)

    def start_datachecker(self):
        """Start the datachecker."""
        if self.available:
            response = requests.post(f"{self.url}/datachecker/start")
            if response.ok:
                self.set_unavailable()

    def start_modelbuilder(self):
        """Start the modelbuilder."""
        polder_id = str(self.dockwidget.polder_id_box.value())
        polder_name = self.dockwidget.poldernaam_textbox.text()
        if polder_id and polder_name and self.available:
            response = requests.post(
                url=f"{self.url}/modelbuilder/start",
                data={"polder_id": polder_id, "polder_name": polder_name}
                )
            if response.ok:
                self.set_unavailable()

    def show_datachecker_log(self):
        """show datachecker log."""
        self.datachecker_log.show_log(self.url)

    def show_modelbuilder_log(self):
        """show modelbuilder log."""
        self.modelbuilder_log.show_log(self.url)

    def change_tab(self):
        """check if we are in or out modelbuilder plugin tab."""
        tab_widget = self.dockwidget.tabWidget
        if tab_widget.tabText(tab_widget.currentIndex()) == self.tab_label:
            print("we are in modelbuilder")
            self.connect_modelbuilder()
        else:
            print("we are not in modelbuilder")
            self.stop_timer()

    def connect_modelbuilder(self):
        """connect to a datachecker server and check availability."""

        # check if server is online and set label
        self._online = None
        self.set_select_server_label()

        # check if server is available and set buttons active
        available = self.available
        self.set_active_buttons(available)

        # if online, but not available, start availability timer. Else stop timer (if running). # NOQA
        if self.online and (not available):
            print("unavailable; start timer?")
            self.set_unavailable()
        else:
            self.stop_timer()

    def check_available(self):
        """check if server is still unavailable."""
        available = self.available
        print(f"server available: {available}")
        self.set_active_buttons(available=available)
        if available:
            self.stop_timer()

    def set_unavailable(self):
        """set the server to unavailable and start availability timer."""
        self.set_active_buttons(available=False)
        self.start_timer()

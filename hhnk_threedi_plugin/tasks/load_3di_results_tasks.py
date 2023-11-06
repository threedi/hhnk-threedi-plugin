from copy import copy

from hhnk_research_tools.threedi.construct_rain_scenario import construct_scenario
from hhnk_research_tools.threedi.construct_rain_scenario_dataframe import (
    create_results_dataframe,
)
from hhnk_research_tools.threedi.variables.variables_container import ThreediInformation
from PyQt5.QtCore import pyqtSignal
from qgis.core import Qgis, QgsTask
from qgis.utils import QgsMessageLog, iface

from ..gui.threedi.confirm_rain_scenario_loaded import ConfirmScenario
from ..gui.threedi.construct_rain_scenario_plot import create_results_plot

load_description = "Laden 3di resultaten"


class load3diResultsTask(QgsTask):
    """
    Loads 3di results and constructs rain scenario based on it
    """

    results_loaded = pyqtSignal(object)

    def __init__(self, test_env, confirm_scenario=False):
        super().__init__(load_description, QgsTask.CanCancel)
        self.description = load_description
        self.exception = None
        self.test_env = copy(test_env)
        self.confirm_scenario = confirm_scenario
        self.result = None
        self.df = None
        self.rain = None
        self.detected_rain = None
        self.timestep = None
        self.days_dry_start = None
        self.days_dry_end = None
        self.plotting_args = None

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            (
                self.result,
                self.rain,
                self.detected_rain,
                self.timestep,
                self.days_dry_start,
                self.days_dry_end,
            ) = construct_scenario(test_env=self.test_env)
            self.df = create_results_dataframe(self.timestep, self.days_dry_start, self.days_dry_end)
            if self.confirm_scenario:
                self.plotting_args = create_results_plot(
                    rain=self.rain,
                    detected_rain=self.detected_rain,
                    days_dry_start=self.days_dry_start,
                    days_dry_end=self.days_dry_end,
                    timestep=self.timestep,
                )
            return True
        except Exception as e:
            self.exception = e
            return False

    def finished(self, result):
        """
        If result is False, either an exception occured or the task was cancelled.
        If the task completed succesfully, we create the output files, add layers to
        QGIS (if needed) and create the output widget to add to the toolbox
        """
        if not result:
            if self.exception is None:
                iface.messageBar().pushMessage(f"Taak {self.description} onderbroken", level=Qgis.Warning)
            else:
                iface.messageBar().pushMessage(
                    f"Taak {self.description} mislukt: zie Message Log",
                    level=Qgis.Critical,
                )
                QgsMessageLog.logMessage(
                    '"{name}" Exception: {exception}'.format(name=self.description, exception=self.exception),
                    level=Qgis.Critical,
                )
                raise self.exception
        else:
            # On succesful run
            threedi_vars = ThreediInformation(result=self.result, df=self.df)
            iface.messageBar().pushMessage(f"Taak {self.description} succesvol uitgevoerd", level=Qgis.Info)
            if self.confirm_scenario:
                confirm_dialog = ConfirmScenario(**self.plotting_args)
                res = confirm_dialog.exec()
                if res == 1:
                    self.results_loaded.emit(threedi_vars)
            else:
                self.results_loaded.emit(threedi_vars)

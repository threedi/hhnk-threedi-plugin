import copy
from PyQt5.QtCore import pyqtSignal
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.dem_max_val_result import (
    create_dem_max_val_result_widget,
)

description = "maximale waarde DEM bepalen"

# hhnk-threedi-tests
from hhnk_threedi_tools import SqliteTest


class demMaxValTask(QgsTask):
    result_widget_created = pyqtSignal(str, object)

    def __init__(self, test_env):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.test_env = copy.copy(test_env)
        self.result_str = None

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            sqlite_test = SqliteTest.from_path(
                self.test_env.polder_folder, **self.test_env.file_dict
            )
            self.result_str = sqlite_test.run_dem_max_value()
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
                iface.messageBar().pushMessage(
                    f"Taak {self.description} onderbroken", level=Qgis.Warning
                )
            else:
                iface.messageBar().pushMessage(
                    f"Taak {self.description} mislukt: zie Message Log",
                    level=Qgis.Critical,
                )
                QgsMessageLog.logMessage(
                    '"{name}" Exception: {exception}'.format(
                        name=self.description, exception=self.exception
                    ),
                    level=Qgis.Critical,
                )
                raise self.exception
        else:
            # On succesful run
            iface.messageBar().pushMessage(
                f"Taak {self.description} succesvol uitgevoerd", level=Qgis.Info
            )
            try:
                title, widget = create_dem_max_val_result_widget(
                    result_text=self.result_str
                )
                self.result_widget_created.emit(title, widget)
            except Exception as e:
                raise e from None

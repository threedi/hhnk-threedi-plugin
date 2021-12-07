import copy
from PyQt5.QtCore import pyqtSignal
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
import hhnk_research_tools as hrt
from ....gui.tests.sqlite_tests.result_widgets.general_checks_result import (
    create_general_checks_result_widget,
)


description = "algemene model checks"

# hhnk-threedi-tests
from hhnk_threedi_tools import SqliteTest


class generalChecksTask(QgsTask):
    result_widget_created = pyqtSignal(str, object)
    os_error = pyqtSignal(object, object, Exception)

    def __init__(self, test_env, mutex, wait_cond):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.test_env = copy.copy(test_env)
        self.csv_path = None
        self.gdf = None
        self.os_retry = None
        self.mutex = mutex
        self.wait_cond = wait_cond

    def set_result(self, res):
        self.os_retry = res

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            if self.os_retry is None:
                sqlite_test = SqliteTest.from_path(
                    self.test_env.polder_folder, **self.test_env.file_dict
                )
                self.gdf = sqlite_test.run_model_checks()

            QgsMessageLog.logMessage(
                f"Taak gestart opslaan resultaten", level=Qgis.Info
            )
            self.csv_path = hrt.gdf_write_to_csv(
                self.gdf,
                path=self.test_env.output_vars["log_path"],
                filename=self.test_env.output_vars["general_checks_filename"],
                index=True,
            )
            return True
        except OSError as e:
            self.os_retry = None
            self.os_error.emit(self, self.wait_cond, e)
            self.mutex.lock()
            try:
                self.wait_cond.wait(self.mutex)
            finally:
                self.mutex.unlock()
            if self.os_retry is True:
                return self.run()
            else:
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
            iface.messageBar().pushMessage(
                f"Taak {self.description} en opslag resultaten succesvol uitgevoerd",
                level=Qgis.Info,
            )
            try:
                title, widget = create_general_checks_result_widget(
                    csv_path=self.csv_path
                )
                self.result_widget_created.emit(title, widget)
            except Exception as e:
                raise e from None

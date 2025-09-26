import copy

# hhnk-threedi-tests
from hhnk_threedi_tools import SqliteCheck
from PyQt5.QtCore import QMutex, QWaitCondition, pyqtSignal
from qgis.core import Qgis, QgsTask
from qgis.utils import QgsMessageLog, iface


class BaseSqliteTask(QgsTask):
    """Base class for sqlite tasks. Requires the run_custom function to be defined"""

    result_widget_created = pyqtSignal(str, object)
    os_error = pyqtSignal(object, object, Exception)

    def __init__(self, folder, mutex=QMutex(), wait_cond=QWaitCondition(), description=None):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.result_text = None
        self.os_retry = None
        self.folder = folder
        self.mutex = mutex
        self.wait_cond = wait_cond
        self.layer_source = None
        self.sqlite_checks = SqliteCheck(self.folder)

    def set_result(self, res):
        self.os_retry = res

    def run_custom(self):
        """This function is unique for every test and actually starts a calculation."""
        pass

    def run(self):
        QgsMessageLog.logMessage(f"Taak {self.description} gestart", level=Qgis.Info)
        try:
            self.run_custom()
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

    def finished_custom(self):
        """Custom additional actions when task is finished. For instance loading layers."""
        # title, widget = self.create_result_widget(self.result_text, self.layer_source) #EXAMPLE
        title = None
        widget = None
        return title, widget

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
            iface.messageBar().pushMessage(
                f"Taak {self.description} en opslag resultaten succesvol uitgevoerd",
                level=Qgis.Info,
            )
            QgsMessageLog.logMessage(
                f"Taak {self.description} en opslag resultaten succesvol uitgevoerd",
                level=Qgis.Info,
            )
            try:
                title, widget = self.finished_custom()
                if widget is not None:
                    self.result_widget_created.emit(title, widget)
            except Exception as e:
                raise e from None

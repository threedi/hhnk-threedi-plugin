import copy
from PyQt5.QtCore import pyqtSignal
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from hhnk_threedi_plugin.qgis_interaction.layers_management.adding_layers import add_layers


# new
from hhnk_threedi_tools import OneDTwoDTest

description = "uitlezen waterstanden op tijdstappen en locaties uit 3di resultaten"


class readNodesTask(QgsTask):
    os_error = pyqtSignal(object, object, Exception)

    def __init__(self, test_env, mutex, wait_cond):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.test_env = copy.copy(test_env)
        self.layers_list = [test_env.layers["grid_nodes_2d_layer_vars"]]
        self.gdf = None
        self.os_retry = None
        self.mutex = mutex
        self.wait_cond = wait_cond

    def set_threedi_result(self, result):
        self.test_env.threedi_vars = copy.copy(result)

    def set_result(self, res):
        self.os_retry = res

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            if self.os_retry is None:
                one_d_two_d_test = OneDTwoDTest.from_path(
                    self.test_env.polder_folder,
                    revision=self.test_env.revision_path,
                    output_path=self.test_env.output_path,
                    dem_path=self.test_env.dem_path,
                )
                self.gdf = one_d_two_d_test.run_node_stats()

            QgsMessageLog.logMessage("Taak gestart opslaan resultaten", level=Qgis.Info)
            one_d_two_d_test.write(
                self.test_env.output_vars["grid_nodes_2d_filename"],
                one_d_two_d_test.results["node_stats"],
                csv_path=self.test_env.output_vars["log_path"],
                gpkg_path=self.test_env.output_vars["layer_path"],
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
                QgsMessageLog.logMessage("Before adding layers")
                add_layers(self.layers_list, self.test_env.group_structure)
            except Exception as e:
                raise e from None

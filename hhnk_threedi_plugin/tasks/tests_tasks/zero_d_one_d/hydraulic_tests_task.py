import copy
from PyQt5.QtCore import pyqtSignal
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from ....qgis_interaction.layers_management.adding_layers import add_layers

# hhnk-threedi-tests
from hhnk_threedi_tools import ZeroDOneDTest
import hhnk_research_tools as hrt

description = "hydraulische tests uitvoeren"


class hydraulicTestsTask(QgsTask):
    os_error = pyqtSignal(object, object, Exception)

    def __init__(self, test_env, mutex, wait_cond):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.test_env = copy.copy(test_env)
        self.layers_list = [
            self.test_env.layers["hidden_channels_layer_vars"],
            self.test_env.layers["hidden_structs_layer_vars"],
            self.test_env.layers["debit_primary_channels_layer_vars"],
            self.test_env.layers["debit_secondary_channels_layer_vars"],
            self.test_env.layers["debit_primary_structs_layer_vars"],
            self.test_env.layers["debit_secondary_structs_layer_vars"],
            self.test_env.layers["slope_impoundment_channels_primary_layer_vars"],
            self.test_env.layers["slope_impoundment_channels_secondary_layer_vars"],
            self.test_env.layers["slope_impoundment_structs_primary_layer_vars"],
            self.test_env.layers["slope_impoundment_structs_secondary_layer_vars"],
        ]
        self.channels_gdf = None
        self.structs_gdf = None
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
                zero_d_one_d = ZeroDOneDTest.from_path(self.test_env.polder_folder)
                self.channels_gdf, self.structs_gdf = zero_d_one_d.run_hydraulic()

            QgsMessageLog.logMessage(
                f"Taak gestart opslaan resultaten", level=Qgis.Info
            )
            hrt.gdf_write_to_csv(
                self.channels_gdf,
                path=self.test_env.output_vars["log_path"],
                filename=self.test_env.output_vars["hyd_test_channels_filename"],
            )
            hrt.gdf_write_to_csv(
                self.structs_gdf,
                path=self.test_env.output_vars["log_path"],
                filename=self.test_env.output_vars["hyd_test_structs_filename"],
            )
            hrt.gdf_write_to_geopackage(
                self.channels_gdf,
                path=self.test_env.output_vars["layer_path"],
                filename=self.test_env.output_vars["hyd_test_channels_filename"],
            )
            hrt.gdf_write_to_geopackage(
                self.structs_gdf,
                path=self.test_env.output_vars["layer_path"],
                filename=self.test_env.output_vars["hyd_test_structs_filename"],
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
                add_layers(self.layers_list, self.test_env.group_structure)
            except Exception as e:
                raise e from None

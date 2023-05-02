import copy
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from deprecated.qgis_interaction.layers_management.adding_layers import add_layers

description = "bepalen ontwateringsdiepte op basis van DEM hoogtes"

# hhnk-threedi-tests
from hhnk_threedi_tools import SqliteTest


class dewateringTask(QgsTask):
    def __init__(self, test_env):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.test_env = copy.copy(test_env)
        self.layers_list = [test_env.layers["dewatering_layer_vars"]]

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            test_sqlite = SqliteTest.from_path(
                self.test_env.polder_folder, **self.test_env.file_dict
            )
            test_sqlite.run_dewatering_depth()
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

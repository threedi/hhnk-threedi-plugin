from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
import hhnk_research_tools as hrt

description = "aanpassingen aan model uitvoeren"


class executeModelChangesTask(QgsTask):
    """
    Loads 3di results and constructs rain scenario based on it
    """

    def __init__(self, model_path, query):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.model_path = model_path
        self.query = query

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            hrt.execute_sql_changes(query=self.query, database=self.model_path)
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
                f"Taak {self.description} succesvol uitgevoerd", level=Qgis.Info
            )

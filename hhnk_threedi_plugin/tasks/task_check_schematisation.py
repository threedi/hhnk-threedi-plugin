from qgis.core import QgsTask, Qgis
import processing
from qgis.utils import QgsMessageLog
import pandas as pd


description = "controleer een 3Di schematisatie op fouten: (threedi:check_schematisation)"


class checkSchematisationTask(QgsTask):
    def __init__(self, folder):
        super().__init__(description, QgsTask.CanCancel)
        self.input_sqlite = folder.model.schema_base.sqlite_paths[0]
        self.output_csv = folder.output.sqlite_tests.path / "threedi_check_schematisation.csv"
        self.error = True

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)

        # we get the processing-tool parameters from folder

        params = {
            "INPUT": self.input_sqlite.as_posix(),
            "OUTPUT": self.output_csv.as_posix(),
            "ADD_TO_PROJECT": False
            }

        # we run the tool
        result = processing.run("threedi:check_schematisation", params)

        if self.output_csv.exists():
            df = pd.read_csv(self.output_csv)
            self.error = (df.level == "INFO").any()


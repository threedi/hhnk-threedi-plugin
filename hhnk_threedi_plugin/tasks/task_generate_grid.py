from qgis.core import QgsTask, Qgis
import processing
from qgis.utils import QgsMessageLog


description = "genereer een grid.gpkg vanuit een 3Di schematisatie"


class generateGridTask(QgsTask):
    def __init__(self, folder):
        super().__init__(description, QgsTask.CanCancel)
        self.input_sqlite = folder.model.schema_base.sqlite_paths[0]
        self.output_gpkg = folder.output.path / "grid.gpkg"

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)

        # we get the processing-tool parameters from folder

        params = {"INPUT_SPATIALITE": self.input_sqlite.as_posix(), "OUTPUT": self.output_gpkg.as_posix()}

        # we run the tool
        processing.run("threedi:threedi_generate_computational_grid", params)

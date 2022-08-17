import copy
from PyQt5.QtCore import pyqtSignal
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from hhnk_threedi_plugin.gui.sql_preview.model_changes_preview import modelChangesPreview

# old

# from hhnk_threedi_tools.tests.model_state.get_proposed_updates.get_weir_width_updates import \
#     get_proposed_adjustments_weir_width
# from hhnk_threedi_tools.variables.database_variables import width_col
# from hhnk_threedi_tools.tests.model_state.variables.new_columns_mapping import weirs_new_width_col
# from hhnk_threedi_tools.variables.database_aliases import a_weir_id


# new
from hhnk_threedi_tools.core.folders import Folders
from hhnk_threedi_tools.variables.database_variables import width_col
from hhnk_threedi_tools.variables.model_state import weirs_new_width_col
from hhnk_threedi_tools.variables.database_aliases import a_weir_id

description = "aanpassingen breedte gestuurde stuwen bepalen"


class weirWidthTask(QgsTask):
    result_widget_created = pyqtSignal(object)

    def __init__(self, test_env):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.test_env = copy.copy(test_env)
        self.preview_df = None

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:

            folder = Folders(self.test_env.polder_folder)
            self.preview_df = folder.model.proposed_adjustments(
                "weirs", self.test_env.conversion_vars.to_state
            )

            # self.preview_df = get_proposed_adjustments_weir_width(test_env=self.test_env)
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
                widget = None
                if not self.preview_df.empty:
                    widget = modelChangesPreview(
                        window_title="Calculation type putten",
                        description="Waarden in het rood worden aangepast naar waarden "
                        "in het groen",
                        df=self.preview_df,
                        id_col=a_weir_id,
                        old_col=width_col,
                        new_col=weirs_new_width_col,
                    )
                self.result_widget_created.emit(widget)
            except Exception as e:
                raise e from None

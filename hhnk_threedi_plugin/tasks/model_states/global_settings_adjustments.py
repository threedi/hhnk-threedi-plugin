import copy
from PyQt5.QtCore import pyqtSignal
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from ...gui.sql_preview.model_changes_preview import modelChangesPreview

description = "aanpassingen aan global settings bepalen"

# old
# from hhnk_threedi_tools.variables.database_variables import id_col, control_group_col
# from hhnk_threedi_tools.tests.model_state.variables.new_columns_mapping import global_settings_new_col_name
# from hhnk_threedi_tools.tests.model_state.get_proposed_updates.get_global_settings_updates import get_proposed_adjustments_global_settings

# new

from hhnk_threedi_tools.variables.database_variables import id_col, control_group_col
from hhnk_threedi_tools.variables.model_state import global_settings_new_col_name
from hhnk_threedi_tools import Folders


class globalSettingTask(QgsTask):
    result_widget_created = pyqtSignal(object)

    def __init__(self, test_env):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.test_env = copy.copy(test_env)
        self.preview_df = None
        self.ids_to_delete = None
        self.ids_to_add = None

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:

            folder = Folders(self.test_env.polder_folder)
            (
                self.preview_df,
                self.ids_to_delete,
                self.ids_to_add,
            ) = folder.model.proposed_adjustments(
                "global_settings", self.test_env.conversion_vars.to_state
            )

            # self.preview_df, self.ids_to_delete, self.ids_to_add = \
            #     get_proposed_adjustments_global_settings(test_env=self.test_env)
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
                        window_title="global settings",
                        description="Rijen in het groen worden toegevoegd, "
                        "rijen in het rood worden verwijderd. "
                        f"Waarden in {control_group_col} worden "
                        f"vervangen door waarden in {global_settings_new_col_name}",
                        df=self.preview_df,
                        id_col=id_col,
                        old_col=control_group_col,
                        new_col=global_settings_new_col_name,
                        delete_rows_ids=self.ids_to_delete,
                        add_rows_ids=self.ids_to_add,
                    )
                self.result_widget_created.emit(widget)
            except Exception as e:
                raise e from None

import os
from PyQt5.QtCore import pyqtSignal, QMutex, QWaitCondition
from qgis.core import QgsTask, Qgis

from qgis.utils import QgsMessageLog, iface
from hhnk_threedi_plugin.gui.sql_preview.model_changes_preview import modelChangesPreview

# new
from hhnk_threedi_tools import BankLevelTest
from hhnk_threedi_tools.variables.database_aliases import a_cross_loc_id
from hhnk_threedi_tools.variables.database_variables import (
    bank_level_col,
    conn_node_id_col,
    storage_area_col,
)
from hhnk_threedi_tools.variables.bank_levels import (
    new_bank_level_col,
    new_storage_area_col,
)

from hhnk_threedi_plugin.tasks.utility_functions.handle_os_errors import check_os_error

from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR
import hhnk_threedi_plugin.qgis_interaction.project as project


def get_bank_levels_manholes_task(results_widget, folder, output=True):
    """
    creates task that calculates new manholes and bank level updates from 3di results,
    then adds the loading of 3di results as a dependency to that task

    Used in model states conversions and bank levels test
    """
    try:
        mutex = QMutex()
        wait_cond = QWaitCondition()
        calculate_task = calculateBankLevelsManholesTask(
            folder, create_output=output, mutex=mutex, wait_cond=wait_cond
        )
        calculate_task.os_error.connect(check_os_error)
        calculate_task.bank_level_widget_created.connect(
            results_widget.tabs.add_bank_levels_tab
        )
        calculate_task.new_manholes_widget_created.connect(
            results_widget.tabs.add_new_manholes_tab
        )
        return calculate_task
    except Exception as e:
        raise e from None


description = "berekenen nieuwe bank levels en manholes"

class calculateBankLevelsManholesTask(QgsTask):
    bank_level_widget_created = pyqtSignal(object)
    new_manholes_widget_created = pyqtSignal(object)
    os_error = pyqtSignal(object, object, Exception)

    def __init__(self, folder, mutex, wait_cond, create_output=False):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.folder = folder
        self.create_out = create_output
        self.new_manholes_df = None
        self.new_bank_levels_df = None
        self.all_1d2d_flowlines = None
        self.all_channels = None
        self.cross_loc_new_all = None
        self.all_manholes = None
        self.os_retry = None
        self.mutex = mutex
        self.wait_cond = wait_cond

    def set_result(self, res):
        self.os_retry = res

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            if self.os_retry is None:
                self.bl_test = BankLevelTest(self.folder)
                self.bl_test.import_data()
                self.bl_test.run()
            QgsMessageLog.logMessage("Taak gestart opslaan resultaten", level=Qgis.Info)
            if self.create_out:
                self.create_output()
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

    def create_output(self):
        try:
            self.output_layers_list = []
            path = self.folder.output.bank_levels.path
            self.bl_test.write(path, path)
        except Exception as e:
            raise e from None

    def create_widgets(self):
        bank_levels_widget = None
        new_manholes_widget = None
        if not self.bl_test.results["cross_loc_new"].empty:
            bank_levels_widget = modelChangesPreview(
                window_title="Voorgestelde aanpassingen bank levels",
                description="Waarden in rood worden vervangen voor waarden in het groen.",
                df=self.bl_test.results["cross_loc_new"],
                id_col=a_cross_loc_id,
                old_col=bank_level_col,
                new_col=new_bank_level_col,
                searchable=True,
                new_col_editable=True,
                rows_selectable=True,
            )
        if not self.bl_test.results["new_manholes_df"].empty:
            new_manholes_widget = modelChangesPreview(
                window_title="Voorgestelde toevoegingen manholes",
                description="Rijen in groen worden toegevoegd aan model. "
                "Deselecteer een rij om deze over te slaan. "
                f"Waar een waarde gegeven is in {new_storage_area_col} "
                f"wordt de waarde van {storage_area_col} aangepast.",
                df=self.bl_test.results["new_manholes_df"],
                id_col=conn_node_id_col,
                old_col=storage_area_col,
                new_col=new_storage_area_col,
                add_rows_ids=self.bl_test.results["new_manholes_df"][
                    conn_node_id_col
                ].tolist(),
                rows_selectable=True,
                searchable=True,
            )
        return bank_levels_widget, new_manholes_widget

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
            try:
                #if self.create_out:
                bank_levels_widget, new_manholes_widget = self.create_widgets()
                self.bank_level_widget_created.emit(bank_levels_widget)
                self.new_manholes_widget_created.emit(new_manholes_widget)

                #Load layers
                df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')

                proj = project.Project()
                proj.run(layer_structure_path=df_path,
                        subjects=['test_banklevels'],
                        folder=self.folder)
            
            except Exception as e:
                raise e from None

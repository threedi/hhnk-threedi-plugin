from qgis.core import QgsTask
from PyQt5.QtCore import QMutex, QWaitCondition
from ..load_3di_results_tasks import load3diResultsTask
from ..calculate_bank_levels_manholes import calculateBankLevelsManholesTask
from ...tasks.utility_functions.handle_os_errors import check_os_error


def get_bank_levels_manholes_task(results_widget, test_env, output=True):
    """
    creates task that calculates new manholes and bank level updates from 3di results,
    then adds the loading of 3di results as a dependency to that task

    Used in model states conversions and bank levels test
    """
    try:
        mutex = QMutex()
        wait_cond = QWaitCondition()
        calculate_task = calculateBankLevelsManholesTask(
            test_env, create_output=output, mutex=mutex, wait_cond=wait_cond
        )
        calculate_task.os_error.connect(check_os_error)
        # load_results_task = load3diResultsTask(test_env, confirm_scenario=False)
        # load_results_task.results_loaded.connect(calculate_task.set_threedi_results)
        # calculate_task.addSubTask(load_results_task, [], QgsTask.ParentDependsOnSubTask)
        calculate_task.bank_level_widget_created.connect(
            results_widget.tabs.add_bank_levels_tab
        )
        calculate_task.new_manholes_widget_created.connect(
            results_widget.tabs.add_new_manholes_tab
        )
        return calculate_task
    except Exception as e:
        raise e from None

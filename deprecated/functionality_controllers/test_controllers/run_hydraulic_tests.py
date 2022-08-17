from qgis.core import QgsApplication
from PyQt5.QtCore import QMutex, QWaitCondition
from hhnk_threedi_plugin.qgis_interaction.layers_management.removing_layers import remove_layers
from hhnk_threedi_plugin.tasks.load_3di_results_tasks import load3diResultsTask
from hhnk_threedi_plugin.tasks.tests_tasks.zero_d_one_d.zero_d_one_d_task import zeroDOneDTask
from hhnk_threedi_plugin.tasks.tests_tasks.zero_d_one_d.hydraulic_tests_task import hydraulicTestsTask
from hhnk_threedi_plugin.tasks.utility_functions.handle_os_errors import check_os_error


def add_next_tasks(zero_d_task, hydraulic_tests_task, task_manager):
    try:
        if (
            zero_d_task.test_env.threedi_vars is not None
            and hydraulic_tests_task.test_env.threedi_vars is not None
        ):
            task_manager.addTask(zero_d_task)
            task_manager.addTask(hydraulic_tests_task)
    except Exception as e:
        raise e from None


def run_hydraulic_tests(test_env):
    """
    Fuctions runs all tests that are part of 0d1d tests:
    - Loads 3di results
    - Gathers 0d1d information: water levels at several time steps throughout the
    3di rain scenario at calculation nodes
    - Hydraulic test: water levels in channels and at structs at several time steps
    throughout 3di rain scenario

    input: tests_env ---> contains information about:
        output variables
        input paths
        layers to be created

    Creates a task that runs on separate thread for each test
    """
    try:
        remove_layers([item for item in test_env.layers.values()])
        task_manager = QgsApplication.taskManager()
        zero_d_mutex = QMutex()
        zero_d_wait_cond = QWaitCondition()
        zero_d_task = zeroDOneDTask(
            test_env=test_env, mutex=zero_d_mutex, wait_cond=zero_d_wait_cond
        )
        zero_d_task.os_error.connect(check_os_error)
        test_env.tasks.append(zero_d_task)
        hydraulic_mutex = QMutex()
        hydraulic_wait_cond = QWaitCondition()
        hydraulic_tests_task = hydraulicTestsTask(
            test_env=test_env, mutex=hydraulic_mutex, wait_cond=hydraulic_wait_cond
        )
        hydraulic_tests_task.os_error.connect(check_os_error)
        test_env.tasks.append(hydraulic_tests_task)
        load_results_task = load3diResultsTask(test_env=test_env, confirm_scenario=True)
        test_env.tasks.append(load_results_task)
        load_results_task.results_loaded.connect(zero_d_task.set_threedi_result)
        load_results_task.results_loaded.connect(
            hydraulic_tests_task.set_threedi_result
        )
        load_results_task.results_loaded.connect(
            lambda: add_next_tasks(zero_d_task, hydraulic_tests_task, task_manager)
        )
        task_manager.addTask(load_results_task)
    except Exception as e:
        raise e from None

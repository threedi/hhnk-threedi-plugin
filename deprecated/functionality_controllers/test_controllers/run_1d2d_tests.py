#TODO deprecated

from qgis.core import QgsApplication
from PyQt5.QtCore import QMutex, QWaitCondition
from hhnk_threedi_plugin.qgis_interaction.layers_management.removing_layers import remove_layers
from hhnk_threedi_plugin.tasks.load_3di_results_tasks import load3diResultsTask
# from hhnk_threedi_plugin.tasks.tests_tasks.one_d_two_d.read_nodes_task import readNodesTask
# from hhnk_threedi_plugin.tasks.tests_tasks.one_d_two_d.flowlines_task import flowLinesTask
# from hhnk_threedi_plugin.tasks.tests_tasks.one_d_two_d.waterlevels_task import waterlevelsTask
from hhnk_threedi_plugin.tasks.utility_functions.handle_os_errors import check_os_error


def run_tests(task_manager, flowlines_task, read_nodes_task, waterlevel_task):
    try:
        if (
            flowlines_task.test_env.threedi_vars is not None
            and read_nodes_task.test_env.threedi_vars is not None
            and waterlevel_task.test_env.threedi_vars is not None
        ):
            task_manager.addTask(flowlines_task)
            task_manager.addTask(read_nodes_task)
            task_manager.addTask(waterlevel_task)
    except Exception as e:
        raise e from None

    # def one_d_two_d_tests_execution(self, test_env):
    #     try:
    #         test_env.polder_folder = self.polder_folder
    #         run_1d2d_tests(test_env=test_env)
    #     except Exception as e:
    #         self.iface.messageBar().pushMessage(str(e), Qgis.Critical)
    #         pass

    
def run_1d2d_tests(test_env):
    """
    Fuctions runs all tests that are part of 1d2d tests:
    - Loads 3di results
    - Reads flowlines from results
    - Reads nodes from results
    - Reads water levels at different timesteps
    input: tests_env ---> contains information about:
        output variables
        input paths
        layers to be created

    Creates a task that runs on separate thread for each test
    """
    try:
        remove_layers([item for item in test_env.layers.values()])
        task_manager = QgsApplication.taskManager()
        load_task = load3diResultsTask(test_env=test_env, confirm_scenario=True)
        test_env.tasks.append(load_task)
        flowlines_wait_cond = QWaitCondition()
        flowlines_mutex = QMutex()
        flowlines_task = flowLinesTask(
            test_env=test_env, mutex=flowlines_mutex, wait_cond=flowlines_wait_cond
        )
        flowlines_task.os_error.connect(check_os_error)
        test_env.tasks.append(flowlines_task)
        read_nodes_wait_cond = QWaitCondition()
        read_nodes_mutex = QMutex()
        read_nodes_task = readNodesTask(
            test_env=test_env, mutex=read_nodes_mutex, wait_cond=read_nodes_wait_cond
        )
        read_nodes_task.os_error.connect(check_os_error)
        test_env.tasks.append(read_nodes_task)
        waterlevel_task = waterlevelsTask(test_env=test_env)
        test_env.tasks.append(waterlevel_task)
        load_task.results_loaded.connect(flowlines_task.set_threedi_result)
        load_task.results_loaded.connect(read_nodes_task.set_threedi_result)
        load_task.results_loaded.connect(waterlevel_task.set_threedi_result)
        load_task.results_loaded.connect(
            lambda: run_tests(
                task_manager, flowlines_task, read_nodes_task, waterlevel_task
            )
        )
        task_manager.addTask(load_task)
    except Exception as e:
        raise e from None

from qgis.core import QgsApplication
from ...qgis_interaction.layers_management.removing_layers import remove_layers
from ...tasks.task_creation_functions.create_bank_levels_manholes_task import (
    get_bank_levels_manholes_task,
)
from hhnk_threedi_tools import create_backups
from hhnk_threedi_tools.variables.model_state import (
    one_d_two_d_state,
    one_d_two_d_from_calc,
)
from ...gui.proposed_changes_dialog import modelChangesDialog


def handle_model_changes_task(result_widget, task, model_path):
    task_manager = QgsApplication.taskManager()
    task.taskCompleted.connect(result_widget.handle_execution_result_success)
    task.taskCompleted.connect(
        lambda: create_backups(model_path=model_path, manholes_bank_levels_only=True)
    )
    task.taskTerminated.connect(
        lambda: result_widget.handle_execution_result_failed(task.exception)
    )
    task_manager.addTask(task)


def run_bank_levels_test(polder_folder, parent):
    """
    Fuctions runs all bank levels test:
    - Loads 3di results
    - Calculate what bank level heights should be from 3di results and model information
    - Proposes the adding of new manholes for nodes that don't have manholes associated with them
    except when those nodes are on fixed drainage area limits

    input: tests_env ---> contains information about:
        output variables
        input paths
        layers to be created
    parent: PyQt5 object that takes ownership of the result widget

    return value: widget containing proposed changes to user

    Creates a task that runs on separate thread for each test
    """
    try:
        model_path = polder_folder.model.schema_base.database.path
        
        results_widget = modelChangesDialog(
            model_path=model_path,
            parent=parent,
            to_state=one_d_two_d_state,
            one_d_two_d_source=one_d_two_d_from_calc,
        )
        results_widget.query_execution_task_created.connect(
            lambda task: handle_model_changes_task(results_widget, task, model_path)
        )
        task_manager = QgsApplication.taskManager()
        calculate_task = get_bank_levels_manholes_task(results_widget, polder_folder)
        calculate_task.taskCompleted.connect(results_widget.has_changes)
        calculate_task.taskCompleted.connect(results_widget.show)
        task_manager.addTask(calculate_task)
        return results_widget
    except Exception as e:
        raise e from None

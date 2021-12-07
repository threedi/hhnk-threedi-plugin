from qgis.core import QgsApplication, QgsTask
from hhnk_threedi_tools import create_backups
from hhnk_threedi_tools.variables.model_state import (
    one_d_two_d_from_calc,
    one_d_two_d_state,
    hydraulic_test_state,
    one_d_two_d_keep,
)
from ..tasks.model_states.global_settings_adjustments import globalSettingTask
from ..tasks.model_states.manholes_update_adjustments import updateManholesTask
from ..tasks.model_states.weir_widths_update_adjustments import weirWidthTask
from ..tasks.model_states.channels_settings_adjustments import channelsCalcTask
from ..tasks.task_creation_functions.create_bank_levels_manholes_task import (
    get_bank_levels_manholes_task,
)
from ..gui.proposed_changes_dialog import modelChangesDialog


def handle_model_changes_task(result_widget, task, on_success, model_path):
    """
    Starts changes to model execution. Depending on whether they are executed successfull, calls
    success and failure handlers. In case we have recalculated bank levels updates timestamp.
    """
    task_manager = QgsApplication.taskManager()
    task.taskCompleted.connect(lambda: on_success(model=model_path))
    task.taskCompleted.connect(result_widget.handle_execution_result_success)
    task.taskTerminated.connect(
        lambda: result_widget.handle_execution_result_failed(task.exception)
    )
    task_manager.addTask(task)


def run_model_states_conversion(parent, test_env, on_succes):
    """
    Converts model between states. Model has to be in identifiable state in order for
    this function to work correctly (see detect_model_state function). If the detected state is
    incorrect, results of using this function are undefined.

    If we are converting to 1d2d state from hydraulic test state, we need backups of the original
    values. These are automatically created when converting using this function, but may not exist
    if these changes were made manually. Needed backups are:
        - backup_global_settings (to reinsert rows needed for target state)
        - backup_manholes (for original calculation_type column)
        - backup_channels (for original calculation_type column)
        - backup_controlled_weir_widths (for original width column)
    """
    try:
        model_path = test_env.src_paths["model"]
        from_state = test_env.conversion_vars.from_state
        to_state = test_env.conversion_vars.to_state
        one_d_two_d_source = test_env.conversion_vars.one_d_two_d_source
        task_manager = QgsApplication.taskManager()
        # Creates widget to show proposed changes
        results_widget = modelChangesDialog(
            model_path=model_path,
            parent=parent,
            to_state=to_state,
            one_d_two_d_source=one_d_two_d_source,
        )
        results_widget.query_execution_task_created.connect(
            lambda task: handle_model_changes_task(
                results_widget, task, on_succes, model_path
            )
        )
        create_backups(model_path=model_path, state=from_state)
        # Bank levels
        if to_state == one_d_two_d_state:
            if one_d_two_d_source == one_d_two_d_from_calc:
                bank_levels_manholes_task = get_bank_levels_manholes_task(
                    results_widget=results_widget, test_env=test_env, output=False
                )
                test_env.tasks.append(bank_levels_manholes_task)
        # global settings
        global_settings_task = globalSettingTask(test_env=test_env)
        global_settings_task.result_widget_created.connect(
            results_widget.tabs.add_global_settings_tab
        )
        test_env.tasks.append(global_settings_task)
        if from_state == hydraulic_test_state or to_state == hydraulic_test_state:
            # Only hyd state is different
            # update manholes
            update_manholes_task = updateManholesTask(test_env=test_env)
            update_manholes_task.result_widget_created.connect(
                results_widget.tabs.add_update_manholes_tab
            )
            test_env.tasks.append(update_manholes_task)
            # weir width
            weir_width_task = weirWidthTask(test_env=test_env)
            weir_width_task.result_widget_created.connect(
                results_widget.tabs.add_weir_widths_tab
            )
            test_env.tasks.append(weir_width_task)
            # channels isolation
            channels_calc_task = channelsCalcTask(test_env=test_env)
            channels_calc_task.result_widget_created.connect(
                results_widget.tabs.add_channels_tab
            )
            test_env.tasks.append(channels_calc_task)
        if test_env.tasks:
            # Add tasks for execution
            main_task = test_env.tasks[0]
            rest = test_env.tasks[1:]
            for item in rest:
                main_task.addSubTask(item, [], QgsTask.ParentDependsOnSubTask)
            # GUI changes on completion
            main_task.taskCompleted.connect(results_widget.has_changes)
            main_task.taskCompleted.connect(results_widget.show)
            task_manager.addTask(main_task)
            return results_widget
    except Exception as e:
        raise e from None

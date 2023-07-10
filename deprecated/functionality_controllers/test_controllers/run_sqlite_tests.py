from qgis.core import QgsApplication
from PyQt5.QtCore import QMutex, QWaitCondition
from deprecated.qgis_interaction.layers_management.removing_layers import remove_layers
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.profiles_used_task import profilesUsedTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.isolated_channels_task import isolatedChannelsTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.controlled_structs_task import controlledStructsTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.impervious_surface_task import impSurfaceTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.weir_height_task import weirHeightTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.geometries_task import geometriesTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.structs_channel_task import structsChannelsTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.general_checks_task import generalChecksTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.dem_max_val_task import demMaxValTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.dewatering_task import dewateringTask
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.watersurface_area_task import watersurfaceAreaTask
from hhnk_threedi_plugin.tasks.utility_functions.handle_os_errors import check_os_error


def run_sqlite_tests(results_widget, test_env):
    """
    Fuctions runs all tests that are part of model (sqlite) tests:
    input: tests_env ---> contains information about:
        output variables
        input paths
        layers to be created
        tests that were selected:
            checks if name of gui checkbox object is in list of selected checkboxes

    Creates a task that runs on separate thread for each test

    Output: returns information about success of issues found in the user interface
    """
    try:
        if test_env.layers is not None:
            remove_layers([item for item in test_env.layers.values()])
        task_manager = QgsApplication.taskManager()
        if "impervious_surface_chk" in test_env.selected_tests:
            task = impSurfaceTask(test_env=test_env)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "profiles_used_chk" in test_env.selected_tests:
            profiles_mutex = QMutex()
            profiles_wait_cond = QWaitCondition()
            task = profilesUsedTask(
                test_env=test_env, mutex=profiles_mutex, wait_cond=profiles_wait_cond
            )
            task.os_error.connect(check_os_error)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "controlled_structs_chk" in test_env.selected_tests:
            contr_structs_mutex = QMutex()
            contr_structs_wait_cond = QWaitCondition()
            task = controlledStructsTask(
                test_env=test_env,
                mutex=contr_structs_mutex,
                wait_cond=contr_structs_wait_cond,
            )
            task.os_error.connect(check_os_error)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "weir_height_chk" in test_env.selected_tests:
            weir_mutex = QMutex()
            weir_wait_cond = QWaitCondition()
            task = weirHeightTask(
                test_env=test_env, mutex=weir_mutex, wait_cond=weir_wait_cond
            )
            task.os_error.connect(check_os_error)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "geometry_chk" in test_env.selected_tests:
            geometry_mutex = QMutex()
            geometry_wait_cond = QWaitCondition()
            task = geometriesTask(
                test_env=test_env, mutex=geometry_mutex, wait_cond=geometry_wait_cond
            )
            task.os_error.connect(check_os_error)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "structs_channel_chk" in test_env.selected_tests:
            structs_channel_mutex = QMutex()
            structs_channel_wait_cond = QWaitCondition()
            task = structsChannelsTask(
                test_env=test_env,
                mutex=structs_channel_mutex,
                wait_cond=structs_channel_wait_cond,
            )
            task.os_error.connect(check_os_error)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "general_tests_chk" in test_env.selected_tests:
            gen_tests_mutex = QMutex()
            gen_tests_wait_cond = QWaitCondition()
            task = generalChecksTask(
                test_env=test_env, mutex=gen_tests_mutex, wait_cond=gen_tests_wait_cond
            )
            task.os_error.connect(check_os_error)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "isolated_channels_chk" in test_env.selected_tests:
            isolated_mutex = QMutex()
            isolated_wait_cond = QWaitCondition()
            task = isolatedChannelsTask(
                test_env=test_env, mutex=isolated_mutex, wait_cond=isolated_wait_cond
            )
            task.os_error.connect(check_os_error)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "max_dem_chk" in test_env.selected_tests:
            task = demMaxValTask(test_env=test_env)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "dewatering_depth_chk" in test_env.selected_tests:
            task = dewateringTask(test_env=test_env)
            test_env.tasks.append(task)
            task_manager.addTask(task)
        if "watersurface_area_chk" in test_env.selected_tests:
            watersurface_mutex = QMutex()
            watersurface_wait_cond = QWaitCondition()
            task = watersurfaceAreaTask(
                test_env=test_env,
                mutex=watersurface_mutex,
                wait_cond=watersurface_wait_cond,
            )
            task.os_error.connect(check_os_error)
            task.result_widget_created.connect(results_widget.add_section)
            test_env.tasks.append(task)
            task_manager.addTask(task)
    except Exception as e:
        raise e from None

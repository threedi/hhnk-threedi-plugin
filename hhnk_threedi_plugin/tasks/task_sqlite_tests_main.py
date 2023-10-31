from qgis.core import QgsApplication

from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from PyQt5.QtCore import QMutex, QWaitCondition

from hhnk_threedi_plugin.tasks.utility_functions.handle_os_errors import check_os_error
import hhnk_threedi_plugin.qgis_interaction.project as project

from hhnk_threedi_plugin.tasks.sqlite_test_tasks.sqlite_test_tasks import (
    impSurfaceTask, 
    profilesUsedTask, 
    controlledStructsTask, 
    weirHeightTask, 
    geometriesTask, 
    structsChannelsTask,
    generalChecksTask,
    isolatedChannelsTask,
    gridTask,
    demMaxValTask,
    dewateringTask,
    watersurfaceAreaTask,
    crossSectionDuplicateTask,
    crossSectionNoVertexTask,
    )


from hhnk_threedi_plugin.dependencies import HHNK_THREEDI_PLUGIN_DIR
import os

def task_sqlite_tests_main(parent_widget, folder, selected_tests):        
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


    task_manager = QgsApplication.taskManager()

    #Map buttons to tasks
    test_task={
            "impervious_surface_chk":impSurfaceTask,
            "profiles_used_chk":profilesUsedTask,
            "controlled_structs_chk":controlledStructsTask,
            "weir_height_chk":weirHeightTask,
            "geometry_chk":geometriesTask,
            "structs_channel_chk":structsChannelsTask,
            "general_tests_chk":generalChecksTask,
            "isolated_channels_chk":isolatedChannelsTask,
            "grid_chk":gridTask,
            "max_dem_chk":demMaxValTask,
            "dewatering_depth_chk":dewateringTask,
            "watersurface_area_chk":watersurfaceAreaTask,
            "cross_section_duplicate_chk":crossSectionDuplicateTask,
            "cross_section_no_vertex_chk":crossSectionNoVertexTask,
            }
        


    folder.tasks=[]

    for selected_test in selected_tests:
        print(selected_test)
        if selected_test in test_task:
            task = test_task[selected_test](folder=folder)
            task.os_error.connect(check_os_error)
            task.result_widget_created.connect(parent_widget.add_section) #Voeg widget van taak toe aan de parent_widget.

            folder.tasks.append(task) #Voeg tasks aan folders toe zodat ze blijven bestaan. Anders werkt 'finished' binnen de taak niet.
            task_manager.addTask(task)



    def print_done():
        QgsMessageLog.logMessage(
                f"All sqlite tasks finished - loading results into project", level=Qgis.Info
            )

        df_path = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'layer_structure', 'testprotocol.csv')

        #Load layers
        proj = project.Project()
        proj.run(layer_structure_path=df_path,
                    subjects=['test_sqlite'],
                    folder=folder)
        
        QgsApplication.taskManager().allTasksFinished.disconnect()

    task_manager_connect = task_manager.allTasksFinished.connect(print_done)


    # QgsMessageLog.logMessage(
    #         f"Alle sqlite taken gestart main", level=Qgis.Info
    #     )





    # if "impervious_surface_chk" in selected_tests:
    #     task = impSurfaceTask(folder=folder, mutex=None, wait_cond=None)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     # test_env.tasks.append(task)
    #     task_manager.addTask(task)




    # if "profiles_used_chk" in selected_tests:
    #     profiles_mutex = QMutex()
    #     profiles_wait_cond = QWaitCondition()
    #     task = profilesUsedTask(test_env=test_env, mutex=profiles_mutex, wait_cond=profiles_wait_cond)
    #     task.os_error.connect(check_os_error)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     test_env.tasks.append(task)
    #     task_manager.addTask(task)
    # if "controlled_structs_chk" in selected_tests:
    #     contr_structs_mutex = QMutex()
    #     contr_structs_wait_cond = QWaitCondition()
    #     task = controlledStructsTask(
    #         test_env=test_env,
    #         mutex=contr_structs_mutex,
    #         wait_cond=contr_structs_wait_cond,
    #     )
    #     task.os_error.connect(check_os_error)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     test_env.tasks.append(task)
    #     task_manager.addTask(task)
    # if "weir_height_chk" in selected_tests:
    #     weir_mutex = QMutex()
    #     weir_wait_cond = QWaitCondition()
    #     task = weirHeightTask(
    #         test_env=test_env, mutex=weir_mutex, wait_cond=weir_wait_cond
    #     )
    #     task.os_error.connect(check_os_error)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     test_env.tasks.append(task)
    #     task_manager.addTask(task)
    # if "geometry_chk" in selected_tests:
    #     geometry_mutex = QMutex()
    #     geometry_wait_cond = QWaitCondition()
    #     task = geometriesTask(
    #         test_env=test_env, mutex=geometry_mutex, wait_cond=geometry_wait_cond
    #     )
    #     task.os_error.connect(check_os_error)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     test_env.tasks.append(task)
    #     task_manager.addTask(task)
    # if "structs_channel_chk" in selected_tests:
    #     structs_channel_mutex = QMutex()
    #     structs_channel_wait_cond = QWaitCondition()
    #     task = structsChannelsTask(
    #         test_env=test_env,
    #         mutex=structs_channel_mutex,
    #         wait_cond=structs_channel_wait_cond,
    #     )
    #     task.os_error.connect(check_os_error)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     test_env.tasks.append(task)
    #     task_manager.addTask(task)
    # if "general_tests_chk" in selected_tests:
    #     gen_tests_mutex = QMutex()
    #     gen_tests_wait_cond = QWaitCondition()
    #     task = generalChecksTask(
    #         test_env=test_env, mutex=gen_tests_mutex, wait_cond=gen_tests_wait_cond
    #     )
    #     task.os_error.connect(check_os_error)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     test_env.tasks.append(task)
    #     task_manager.addTask(task)
    # if "isolated_channels_chk" in selected_tests:
    #     isolated_mutex = QMutex()
    #     isolated_wait_cond = QWaitCondition()
    #     task = isolatedChannelsTask(
    #         test_env=test_env, mutex=isolated_mutex, wait_cond=isolated_wait_cond
    #     )
    #     task.os_error.connect(check_os_error)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     test_env.tasks.append(task)
    # #     task_manager.addTask(task)
    # if "max_dem_chk" in selected_tests:
    #     task = demMaxValTask(test_env=test_env)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     test_env.tasks.append(task)
    #     task_manager.addTask(task)
    # if "dewatering_depth_chk" in selected_tests:
    #     task = dewateringTask(test_env=test_env)
    #     test_env.tasks.append(task)
    #     task_manager.addTask(task)
    # if "watersurface_area_chk" in selected_tests:
    #     watersurface_mutex = QMutex()
    #     watersurface_wait_cond = QWaitCondition()
    #     task = watersurfaceAreaTask(
    #         test_env=test_env,
    #         mutex=watersurface_mutex,
    #         wait_cond=watersurface_wait_cond,
    #     )
    #     task.os_error.connect(check_os_error)
    #     task.result_widget_created.connect(parent_widget.add_section)
    #     test_env.tasks.append(task)
    #     task_manager.addTask(task)

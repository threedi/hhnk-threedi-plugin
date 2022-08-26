import os
from PyQt5.QtWidgets import (
    QPushButton,
    QFileDialog,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
    QWidget,
    QSpacerItem,
)
from PyQt5.QtCore import Qt, pyqtSignal
from qgis.core import QgsApplication
from pathlib import Path
from qgis.core import Qgis
from hhnk_threedi_plugin.gui.utility.file_widget import fileWidget

from hhnk_threedi_plugin.gui.path_verification_functions import is_valid_model_path
from hhnk_threedi_plugin.error_messages.input_error_messages import invalid_model_path

from hhnk_threedi_plugin.gui.tests.bank_levels_widgets.proposed_changes_dialog import modelChangesDialog
import hhnk_threedi_plugin.tasks.task_bank_levels as task_bank_levels
import hhnk_threedi_tools as htt

def setupUi(bank_levels_widget):
    # Create button to start tests
    bank_levels_widget.start_bank_levels_btn = QPushButton("Begin tests")

    bank_levels_widget.model_selector = fileWidget(
        select_text="Selecteer model:",
        file_dialog_title="Selecteer een model (.sqlite)",
        file_mode=QFileDialog.ExistingFile,
        name_filter="*.sqlite",
    )
    # Main layout
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(bank_levels_widget.model_selector)
    main_layout.addSpacerItem(QSpacerItem(25, 5, QSizePolicy.Expanding))
    main_layout.addWidget(bank_levels_widget.start_bank_levels_btn)
    bank_levels_widget.setLayout(main_layout)


class bankLevelsWidget(QWidget):
    """
    Initialization:
        bankLevelsWidget(caller (object keeping track of current paths throughout program
                                (has to have member 'current_source_paths')),
                        parent (PyQt5 object inherits control of the widget))

    Signals:

    start_bank_levels_tests(object (test_env))
    """

    # start_bank_levels_tests = pyqtSignal(object)

    def __init__(self, caller, parent=None):
        super().__init__(parent)
        setupUi(self)
        # ----------------------------------------------------------
        # Variables
        # ----------------------------------------------------------
        self.caller = caller
        self.parent = parent
        self.results_widget = None
        self.tasks=[]
        # ----------------------------------------------------------
        # Signals
        # ----------------------------------------------------------
        self.start_bank_levels_btn.clicked.connect(self.bank_level_test_execution)
       

    def bank_level_test_execution(self):

        model_path=self.parent.input_data_dialog.model_selector.filePath()
        if not is_valid_model_path(model_path):
            message=invalid_model_path.format(model_path)
            self.caller.iface.messageBar().pushMessage(message, Qgis.Critical)
        else:
            try:
                if (
                    self.results_widget is not None
                    and self.results_widget
                    and self.results_widget.isVisible()
                ):
                    self.results_widget.close()

                self.run_bank_levels_test(
                    folder=self.caller.folder, parent=self.parent, model_path=model_path
                )
            except Exception as e:
                self.iface.messageBar().pushMessage(str(e), Qgis.Critical)
                pass


    #Functionality controller
    def handle_model_changes_task(self, task, model_path):
        task_manager = QgsApplication.taskManager()
        task.taskCompleted.connect(self.result_widget.handle_execution_result_success)
        task.taskCompleted.connect(lambda: htt.create_backups(model_path=model_path, manholes_bank_levels_only=True))
        task.taskTerminated.connect(lambda: self.result_widget.handle_execution_result_failed(task.exception))
        self.tasks.append(task)
        task_manager.addTask(task)


    #Functionality controller
    def run_bank_levels_test(self, folder, parent, model_path):
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
            self.results_widget = modelChangesDialog(
                model_path=model_path,
                parent=parent,
                to_state="0d1d_test", #zero_d_one_d_name
                one_d_two_d_source="1d2d uit berekening", #one_d_two_d_from_calc
            )
            self.results_widget.query_execution_task_created.connect(
                lambda task: self.handle_model_changes_task(task, model_path)
            )
            task_manager = QgsApplication.taskManager()
            task = task_bank_levels.get_bank_levels_manholes_task(results_widget=self.results_widget, folder=folder)
            task.taskCompleted.connect(self.results_widget.has_changes)
            task.taskCompleted.connect(self.results_widget.show)
            self.tasks.append(task)
            task_manager.addTask(task)
        except Exception as e:
            raise e from None

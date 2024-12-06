from dataclasses import dataclass
from hhnk_threedi_plugin.hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget

@dataclass
class SchematisationBuilder:
    """
    All actions in the schematisation_builder tab of the HHNK 3Di Toolbox.

    UI includes (from top to down):
    SelectProjectLabel : QLabel
    SelectProjectComboBox : QComboBox
    CreateProjectLabel : QLabel
    CreateProjectPlainTextEdit : QPlainTextEdit
    CreateProjectPushButton : QPushButton
    SchematisationBuilderVerticalSpacer : Spacer
    ProjectTabWidget : QTabWidget
        tab_status_0 : QWidget
            SelectPolderLabel : QLabel
            SelectPolderFileWidget : QgsFileWidget
            ExportDAMOandHyDAMOPushButton : QPushButton
        tab_status_1 : QWidget
            ValidatePushButton : QPushButton    
    """
    dockwidget: HHNK_toolboxDockWidget

    def __post_init__(self):
        """Connect all callback-functions to widgets."""
        pass

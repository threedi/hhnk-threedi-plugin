from dataclasses import dataclass
from hhnk_threedi_plugin.hhnk_toolbox_dockwidget import HHNK_toolboxDockWidget

@dataclass
class SchematisationBuilder:
    """All actions in the schematisation_builder tab of the HHNK 3Di Toolbox."""
    dockwidget: HHNK_toolboxDockWidget

    def __post_init__(self):
        """Connect all callback-functions to widgets."""
        pass

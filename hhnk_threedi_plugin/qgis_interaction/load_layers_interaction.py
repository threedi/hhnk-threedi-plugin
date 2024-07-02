# %%
"""
Created on Fri Jan 28 13:45:01 2022

@author: wietse.vangerwen

This script combines input from a folder object folder.py with qgis layer
and essentially forms the configuration for klimaatsommen (qgis3_export_pdfs)
"""

from pathlib import Path

if __name__ == "__main__":
    # add hhnk_threedi_plugin to path.
    import os
    import sys

    sys.path.append(str(Path(os.path.abspath(__file__)).parents[2]))

# First-party imports
import os

# Third-party imports
# Local imports
import hhnk_research_tools as hrt
from qgis.core import Qgis
from qgis.utils import iface

import hhnk_threedi_plugin.qgis_interaction.project as project

# from hhnk_threedi_plugin.qgis_interaction.styling import path as PATH #TODO deze verwijderen uit init?
from hhnk_threedi_plugin.dependencies import HHNK_THREEDI_PLUGIN_DIR

# globals
STYLING_DIR = Path(__file__).parent / "styling"


def load_sqlite(filepath):
    """Use the 3Di NenS plugin to load the sqlite into the project.

    The __init__ of threedi_schema_editor is updated for this using dependencies.py

    Parameters
    ----------
    filepath (str): path to sqlite
    """
    # schema_plugin = qgis.utils.plugins["threedi_schematisation_editor"]
    try:
        from threedi_models_and_simulations.utils_qgis import get_schematisation_editor_instance

        schema_plugin = get_schematisation_editor_instance()

        if schema_plugin:
            model_gpkg = Path(str(filepath)).with_suffix(".gpkg")
            if str(model_gpkg) != str(schema_plugin.model_gpkg):
                schema_plugin.load_from_spatialite(filepath)
    except:
        iface.messageBar().pushMessage(
            f"Failed loading sqlite. Load manually using schematisation editor. Path: {filepath}",
            level=Qgis.Critical,
        )

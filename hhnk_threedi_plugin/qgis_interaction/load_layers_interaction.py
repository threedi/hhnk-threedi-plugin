# %%
"""
Created on Fri Jan 28 13:45:01 2022

@author: wietse.vangerwen

This script combines input from a folder object folder.py with qgis layer
and essentially forms the configuration for klimaatsommen (qgis3_export_pdfs)
"""

if __name__ == "__main__":
    # add hhnk_threedi_plugin to path.
    import os
    import pathlib
    import sys

    sys.path.append(str(pathlib.Path(os.path.abspath(__file__)).parents[2]))

# First-party imports
import os
import pathlib

# Third-party imports
from pathlib import Path

# Local imports
import hhnk_research_tools as hrt

import hhnk_threedi_plugin.qgis_interaction.project as project

# from hhnk_threedi_plugin.qgis_interaction.styling import path as PATH #TODO deze verwijderen uit init?
from hhnk_threedi_plugin.dependencies import HHNK_THREEDI_PLUGIN_DIR

# globals
STYLING_DIR = pathlib.Path(__file__).parent / "styling"


def load_sqlite(filepath):
    """Use the 3Di NenS plugin to load the sqlite into the project.

    The __init__ of threedi_schema_editor is updated for this using dependencies.py

    Parameters
    ----------
    filepath (str): path to sqlite
    """
    import qgis

    schema_plugin = qgis.utils.plugins["threedi_schematisation_editor"]

    model_gpkg = Path(str(filepath)).with_suffix(".gpkg")
    if str(model_gpkg) != str(schema_plugin.model_gpkg):
        schema_plugin.load_from_spatialite(filepath)

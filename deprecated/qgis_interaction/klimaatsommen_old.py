# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:04:17 2021

@author: chris.kerklaan

This script combines input from a folder object folder.py with qgis layer
and essentially forms the configuration for klimaatsommen (qgis3_export_pdfs)
"""

import os
from ..project import Layer, Project, send_message
from ..styling import path as PATH
import copy
from hhnk_threedi_tools.core.folders import Folders

QML_PATH = f"{PATH}/klimaatsommen"
STRUCTURE = {
    "Klimaatsommen": {
        # Group : [ layer1, layer2, layer3]
        "Resultaat klimaatsommen": ["ruimtekaart", "peilgebieden", "geen_schade"],
        "schadekaarten": [
            "schade_per_peilgebied",
            "schade_per_peilgebied_plas",
            "schade_per_peilgebied_overlast",
            "cw_schade_overlast",
            "cw_schade_plas",
        ],
        "schade_correctie": [
            "schade_per_peilgebied_correctie",
            "schade_per_peilgebied_plas_correctie",
            "schade_per_peilgebied_overlast_correctie",
            "cw_schade_plas_correctie",
            "cw_schade_overlast_correctie",
        ],
        "inundatievlakkenkaart": [
            "inundatiediepte_T0010",
            "inundatiediepte_T0100",
            "inundatiediepte_T1000",
        ],
        "inundatie_plas": [
            "inundatiediepte_T0010_plas",
            "inundatiediepte_T0100_plas",
            "inundatiediepte_T1000_plas",
        ],
        "inundatie_overlast": [
            "inundatiediepte_T0010_overlast",
            "inundatiediepte_T0100_overlast",
            "inundatiediepte_T1000_overlast",
        ],
        "inundatiedieptekaart": [
            "inundatiediepte_T0010",
            "inundatiediepte_T0100",
            "inundatiediepte_T1000",
        ],
    }
}

vectors = [
    "ruimtekaart",
    "peilgebieden",
    "geen_schade",
    "schade_per_peilgebied",
    "schade_per_peilgebied_plas",
    "schade_per_peilgebied_overlast",
    "schade_per_peilgebied_correctie",
    "schade_per_peilgebied_plas_correctie",
    "schade_per_peilgebied_overlast_correctie",
    "polder_polygon",
    "polder_polygon_wit",
]

SUBJECT = "klimaatsommen"
THEMES = {
    "inundatie_overlast": [
        "peilgebieden",
        "brtachtergrondkaartgrijs",
        "inundatiediepte_T0100_overlast",
        "polder_polygon",
        "inundatiediepte_T1000_overlast",
        "inundatiediepte_T0010_overlast",
    ],
    "inundatie_plas": [
        "peilgebieden",
        "brtachtergrondkaartgrijs",
        "polder_polygon",
        "inundatiediepte_T0100_plas",
        "inundatiediepte_T1000_plas",
        "inundatiediepte_T0010_plas",
    ],
    "inundatie_totaal": [
        "peilgebieden",
        "brtachtergrondkaartgrijs",
        "inundatiediepte_T1000",
        "inundatiediepte_T0010",
        "polder_polygon",
        "inundatiediepte_T0100",
    ],
    "landgebruik": ["polder_polygon", "polder_polygon_wit"],
    "ruimtekaart": ["brtachtergrondkaartgrijs", "polder_polygon", "ruimtekaart"],
    "schade_overlast": [
        "cw_schade_overlast",
        "Luchtfoto Actueel Ortho 25cm RGB",
        "polder_polygon",
        "schade_per_peilgebied_overlast",
    ],
    "schade_overlast_corr": [
        "cw_schade_overlast_correctie",
        "Luchtfoto Actueel Ortho 25cm RGB",
        "polder_polygon",
        "schade_per_peilgebied_overlast_correctie",
    ],
    "schade_plas": [
        "schade_per_peilgebied_plas",
        "Luchtfoto Actueel Ortho 25cm RGB",
        "cw_schade_plas",
        "polder_polygon",
    ],
    "schade_plas_corr": [
        "schade_per_peilgebied_plas_correctie",
        "cw_schade_plas_correctie",
        "Luchtfoto Actueel Ortho 25cm RGB",
        "polder_polygon",
    ],
    "schade_totaal": [
        "cw_schade_overlast",
        "Luchtfoto Actueel Ortho 25cm RGB",
        "schade_per_peilgebied",
        "cw_schade_plas",
        "polder_polygon",
    ],
    "schade_totaal_corr": [
        "cw_schade_overlast_correctie",
        "cw_schade_plas_correctie",
        "Luchtfoto Actueel Ortho 25cm RGB",
        "polder_polygon",
        "schade_per_peilgebied_correctie",
    ],
}


def load_klimaatsommen_layers(
    folder: Folders, revision, structure=STRUCTURE, themes=THEMES
):
    """loads klimaatsommen layers
    Groups are created at the same time when layers are added to them

    """

    # get path
    path = (
        str(folder.threedi_results.climate_results[revision].pl / "02_output_rasters")
        + "/"
    )

    if not folder.threedi_results.climate_results[revision].exists:
        send_message(f"{revision} cannot be found", SUBJECT)

    folder_files = folder.all_files

    # replace key
    structure_copied = copy.deepcopy(structure)
    structure_copied[f"Klimaatsommen: {revision}"] = structure_copied.pop("Klimaatsommen")

    project = Project(structure_copied, SUBJECT)
    project.generate_groups()
    for parent_group, values in structure.items():
        for group_name, layer_list in values.items():
            layers = []
            for layer_name in layer_list:
                if layer_name in vectors:
                    type = "vector"
                    ext = ".shp"
                else:
                    type = "raster"
                    ext = ".tif"

                full_path = path + layer_name + ext
                qml = QML_PATH + f"/{layer_name}.qml"

                # some files are present somewhere else
                if layer_name in folder_files and not os.path.exists(full_path):
                    full_path = folder_files[layer_name].path

                layer = Layer(full_path, layer_name, type, qml, SUBJECT)
                if layer.valid:
                    layers.append(layer)

            project.add_layers(layers, group_name, reverse=False)

    # now do all the themes
    for theme_name, theme_layers in themes.items():
        project.add_theme(theme_name, theme_layers)

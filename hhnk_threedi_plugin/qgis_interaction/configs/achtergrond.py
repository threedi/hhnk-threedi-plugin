# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:02:16 2021

@author: chris.kerklaan
"""
LIZARD_LANDGEBRUIk = "contextualWMSLegend=0&crs=EPSG:28992&dpiMode=7&featureCount=10&format=image/png&layers=intern:nl:cover:fun-1801c&styles&url=https://demo.lizard.net/wms/public/?"
PDOK_LUCHTFOTO = "tileMatrixSet=EPSG:28992&crs=EPSG:28992&layers=Actueel_ortho25&styles=default&format=image/jpeg&url=https://service.pdok.nl/hwh/luchtfotorgb/wmts/v1_0"
WATERLOPEN_LEGGER_2020 = "crs='EPSG:28992' filter='' url='https://kaarten.hhnk.nl/arcgis/rest/services/od_legger/od_legger_wateren_2020_oppervlaktewateren_vg/FeatureServer/1'"

from ..project import Layer, Project
from hhnk_threedi_tools import Folders

SUBJECT = "Achtergrond"
STRUCTURE = {
    SUBJECT: [
        "Landgebruik (v1801c)",
        "Luchtfoto actueel (PDOK)",
        "Legger Waterlopen 2020",
    ]
}


def load_achtergrond_layers(
    folder: Folders,
    landgebruik: bool,
    luchtfoto: bool,
    waterlopen_2020: bool,
):

    project = Project(STRUCTURE, SUBJECT)
    if landgebruik or luchtfoto or waterlopen_2020:
        project.add_group("Achtergrond", index=-1)

    if waterlopen_2020:
        layer = Layer(
            WATERLOPEN_LEGGER_2020,
            "Legger Waterlopen 2020",
            "arcgisfeatureserver",
            subject=SUBJECT,
        )
        project.add_layer(layer, "Achtergrond")

    if landgebruik:
        # landgebruik lizard
        layer = Layer(
            LIZARD_LANDGEBRUIk, "Landgebruik (v1801c)", "wms", subject=SUBJECT
        )
        project.add_layer(layer, "Achtergrond")

    if luchtfoto:
        # landgebruik pdok
        layer = Layer(
            PDOK_LUCHTFOTO, "Luchtfoto actueel (PDOK)", "wms", subject=SUBJECT
        )
        project.add_layer(layer, "Achtergrond")

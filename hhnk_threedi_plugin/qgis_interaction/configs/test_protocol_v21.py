# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:27:11 2021

@author: chris.kerklaan

This script is the configuration for "test protocol v21"
 Structuur is opgebouwd als volgt:
     
Structure = {
    Group name: { Subgroup name: [(filename_layer1, Qgis layer name)]},
    
    }

LINKS = {
    Group name: poth to filenames
    } 
    
#TODO:
    Toevoegen van testlagen aan views

"""
import os
from ..project import Layer, Project, send_message
from ..styling import path as PATH
from ..styling.wms import LIZARD_LUCHTFOTO, PDOK_LUCHTFOTO
from hhnk_threedi_tools import Folders

QML_PATH = f"{PATH}/test_protocol_v21"
STRUCTURE = {
    "Opmerkingen": [("opmerkingen.shp", "Opmerkingen")],
    # Group                 # Subgroup                    # Layer names
    "Datachecker output": {
        "Kunstwerken niet in model": [
            (
                "datachecker_output.gdb|layername=channel_loose",
                "Watergang: channel loose",
            ),
            (
                "datachecker_output.gdb|layername=channel_nowayout",
                "Watergang: channel nowayout",
            ),
            (
                "datachecker_output.gdb|layername=culvert|subset='isusable' = '0'",
                "Duikers niet in model",
            ),
            (
                "datachecker_output.gdb|layername=weirs|subset='isusable' = '0'",
                "Stuwen niet in model",
            ),
            (
                "datachecker_output.gdb|layername=bridge|subset='isusable' = '0'",
                "Bruggen niet in model",
            ),
            (
                "datachecker_output.gdb|layername=fixed_dam|subset='isusable' = '0'",
                "Vaste dammen niet in model",
            ),
            (
                "datachecker_output.gdb|layername=pumpstation|subset='isusable' = '0'",
                "Gemaal niet in model",
            ),
            ("datachecker_output.gdb|layername=kruising_zonder_kunstwerk", "KZK"),
            (
                "datachecker_output.gdb|layername=crosssection|subset='isusable' = '0'",
                "Gemeten niet in model",
            ),
        ],
        "Kunstwerken met aannames": [
            (
                "datachecker_output.gdb|layername=culvert|subset='aanname' LIKE ('%width,width%')",
                "Duiker aanname: doorstroomafmeting",
            ),
            (
                "datachecker_output.gdb|layername=culvert|subset='aanname' LIKE ('%bed_level_up%')",
                "Duiker aanname: bob",
            ),
            ("datachecker_output.gdb|layername=levee", "Levee: 30 cm boven max peil"),
            (
                "datachecker_output.gdb|layername=weirs|subset='aanname' LIKE ('%crest_width%')",
                "Stuw aanname: breedte",
            ),
            (
                "datachecker_output.gdb|layername=fixeddrainagelevelarea|subset='streefpeil_bwn2 = -10'",
                "Peilgebied aanname: streefpeil",
            ),
        ],
        "Kunstwerken": [
            ("datachecker_output.gdb|layername=channel", "datachecker_output channel"),
            (
                "datachecker_output.gdb|layername=weirs|subset='isusable' = '1'",
                "Stuwen wel in model",
            ),
            (
                "datachecker_output.gdb|layername=culvert|subset='isusable' = '1'",
                "Duikers wel in model",
            ),
            (
                "datachecker_output.gdb|layername=bridge|subset='isusable' = '1'",
                "Bruggen wel in model",
            ),
            (
                "datachecker_output.gdb|layername=fixed_dam|subset='isusable' = '1'",
                "Vaste dammen wel in model",
            ),
            (
                "datachecker_output.gdb|layername=pumpstation|subset='isusable' = '1'",
                "Gemaal wel in model",
            ),
        ],
    },
    "Modelbuilder feedback": [
        ("misfit_lines.shp", "misfit_lines"),
        ("misfit_points.shp", "misfit_points"),
        (
            "model_feedback.shp|layerid=0|subset='message' IN ('Channel segment too short (<5m)','Reference level lowered due to culvert','Reference level lowered due to orifice','culvert ending connection node receives 10m2 storage','weir ending connection node receives 10m2 storage','connection node was removed because it was not connected')",
            "Model feedback ter info",
        ),
        (
            "model_feedback.shp|layerid=0|subset='message' NOT IN ('Channel segment too short (<5m)','Reference level lowered due to culvert','Reference level lowered due to orifice','culvert ending connection node receives 10m2 storage','weir ending connection node receives 10m2 storage','connection node was removed because it was not connected')",
            "Model feedback naar kijken",
        ),
        (
            "model_feedback.shp|layerid=0|subset='level' NOT IN ('INFO', 'WARNING')",
            "Model feedback ernstig",
        ),
    ],
    "HDB export": [
        ("HDB.gdb|layername=duikers_op_peilgrens", "HDB duikers op peilgrens"),
        ("HDB.gdb|layername=stuwen_op_peilgrens", "HDB stuwen op peilgrens"),
        ("HDB.gdb|layername=gemalen_op_peilgrens", "HDB gemalen op peilgrens"),
        ("HDB.gdb|layername=Levee_overstromingsmodel", "HDB Levee_overstromingsmodel"),
    ],
    "DAMO export": [
        ("DAMO.gdb|layername=Stuw", "Stuw"),
        ("HDB.gdb|layername=Sturing_3Di", "Stuw, automatisch (HDB)"),
        ("DAMO.gdb|layername=Brug", "Brug"),
        ("DAMO.gdb|layername=Gemaal", "Gemaal"),
        ("DAMO.gdb|layername=AquaductLijn", "Aquaduct"),
        ("DAMO.gdb|layername=VasteDam", "VasteDam"),
        ("DAMO.gdb|layername=Vispassage", "Vispassage"),
        ("DAMO.gdb|layername=Sluis", "Sluis"),
        ("DAMO.gdb|layername=GW_PRO", "DAMO GW_PRO"),
        ("datachecker_output.gdb|layername=crosssection", "datachecker crosssection"),
        ("DAMO.gdb|layername=HydroObject", "Waterlopen"),
    ],
    "DAMO huidig (WMS - HHNK)": [
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/28' table='' sql=",
            "Stuw",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/12' table='' sql=",
            "Brug",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/1' table='' sql=",
            "Gemaal",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/2' table='' sql=",
            "Gemaal peilafwijking",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/9' table='' sql=",
            "Duiker syphon hevel",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/10' table='' sql=",
            "Duiker, syphon, hevel (lijn)",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/6' table='' sql=",
            "Aquaduct lijn",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/5' table='' sql=",
            "Aquaduct punt",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/11' table="
            " sql=",
            "Dam",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/15' table="
            " sql=",
            "Vispassage",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_kunstwerken_en_inrichtingselementen/MapServer/3' table="
            " sql=",
            "Sluis",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_oppervlaktewateren/MapServer/0' table="
            " sql=",
            "Boezem",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_oppervlaktewateren/MapServer/1' table="
            " sql=",
            "Waterlopen, primair",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_oppervlaktewateren/MapServer/2' table="
            " sql=",
            "Waterlopen, secundair, tertiair",
        ),
    ],
    "Peilgebieden": [
        ("HDB.gdb|layername=hydro_deelgebieden", "hydro_deelgebieden (hdb)"),
        ("DAMO.gdb|layername=PeilafwijkingGebied", "PeilafwijkingGebied (damo)"),
        ("DAMO.gdb|layername=PeilgebiedPraktijk", "PeilgebiedPraktijk (damo)"),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_gebieden/MapServer/20' table="
            " sql=",
            "PeilafwijkingGebied (damo huidig)",
        ),
        (
            "crs='EPSG:28992' filter='' url='https://maps.hhnk.nl/arcgis/rest/services/ws/geoweb_ws_gebieden/MapServer/0' table="
            " sql=",
            "PeilgebiedPraktijk (damo huidig)",
        ),
        (
            "datachecker_output.gdb|layername=fixeddrainagelevelarea|subset='code' NOT LIKE ('%1000%')",
            "Peilgebieden (datacheck)",
        ),
        ("polder_polygon.shp", "polder_polygon"),
    ],
}

THEMES = {
    "0d1d Kaart1: Debiet": [
        "PeilafwijkingGebied (damo)",
        "PeilgebiedPraktijk (damo)",
        "Peilgebieden (datacheck)",
        "polder_polygon",
    ],
    "0d1d Kaart2: Uitzakken initieel peil": [
        "Waterlopen",
        "PeilafwijkingGebied (damo)",
        "PeilgebiedPraktijk (damo)",
        "Peilgebieden (datacheck)",
        "polder_polygon",
    ],
    "0d1d Kaart3: Streefpeilhandhaving": [
        "Waterlopen",
        "PeilafwijkingGebied (damo)",
        "PeilgebiedPraktijk (damo)",
        "Peilgebieden (datacheck)",
        "polder_polygon",
    ],
    "0d1d Kaart4: Verhang en opstuwing": [
        "Waterlopen",
        "PeilafwijkingGebied (damo)",
        "PeilgebiedPraktijk (damo)",
        "Peilgebieden (datacheck)",
        "polder_polygon",
    ],
    "1d2d Bank level test": ["Peilgebieden (datacheck)", "polder_polygon"],
    "1d2d Kaart1: Debiet": ["levee: 30 cm boven max peil", "polder_polygon"],
    "1d2d Kaart2: Waterdiepte": [
        "levee: 30 cm boven max peil",
        "Waterlopen",
        "polder_polygon",
    ],
    "DAMO": [
        "Watergang: channel loose",
        "Watergang: channel nowayout",
        "Duikers niet in model",
        "Stuwen niet in model",
        "Bruggen niet in model",
        "Gemaal niet in model",
        "Peilgebied aanname: streefpeil",
        "Stuw",
        "Stuw, automatisch (HDB)",
        "Brug",
        "Gemaal",
        "DuikerSifonHevel_punt",
        "DuikerSifonHevel_lijn",
        "Aquaduct",
        "VasteDam",
        "Sluis",
        "DAMO GW_PRO",
        "datachecker crosssection",
        "Waterlopen",
        "hydro_deelgebieden (hdb)",
        "PeilafwijkingGebied (damo)",
        "PeilgebiedPraktijk (damo)",
        "Peilgebieden (datacheck)",
        "polder_polygon",
    ],
    "DAMO Live verbinding": [
        "Stuw",
        "Brug",
        "Gemaal",
        "Gemaal peilafwijking",
        "Duiker, syphon, hevel (lijn)",
        "Sluis",
        "Boezem",
        "Waterlopen, primair",
        "Waterlopen, secundair, tertiair",
        "PeilafwijkingGebied (damo huidig)",
        "PeilgebiedPraktijk (damo huidig)",
        "Peilgebieden (datacheck)",
        "polder_polygon",
    ],
    "DEM": ["Peilgebieden (datacheck)", "polder_polygon", "dem hillshade", "dem"],
    "Datachecker: Data niet in model": [
        "Watergang: channel loose",
        "Watergang: channel nowayout",
        "Duikers niet in model",
        "Stuwen niet in model",
        "Bruggen niet in model",
        "Gemaal niet in model",
        "KZK",
        "Gemeten niet in model",
        "Peilgebied aanname: streefpeil",
        "Model feedback ernstig",
        "Waterlopen",
        "hydro_deelgebieden (hdb)",
        "PeilafwijkingGebied (damo)",
        "PeilgebiedPraktijk (damo)",
        "Peilgebieden (datacheck)",
        "polder_polygon",
    ],
    "Lege Kaart": ["Waterlopen", "Peilgebieden (datacheck)", "polder_polygon"],
    "Modelbuilder check": [
        "misfit_lines",
        "misfit_points",
        "Model feedback naar kijken",
        "Model feedback ernstig",
        "Waterlopen",
        "PeilafwijkingGebied (damo)",
        "PeilgebiedPraktijk (damo)",
        "Peilgebieden (datacheck)",
        "polder_polygon",
    ],
    "SQLite test: Drooglegging": [
        "PeilafwijkingGebied (damo)",
        "PeilgebiedPraktijk (damo)",
        "Peilgebieden (datacheck)",
        "dem",
    ],
    "SQLite test: Verschil oppervlaktewater": [
        "DAMO Waterdeel",
        "channel_surface_from_profiles",
        "polder_polygon",
    ],
    "Testprotocol1d2d stroming over peilgrens": [
        "Peilgebieden (datacheck)",
        "polder_polygon",
    ],
}
SUBJECT = "test_protocol_v21"


def get_link(folder, filename):
    if filename.endswith("gdb") or "polder_polygon" in filename:
        path = folder.source_data.path
        type = "vector"
    elif "misfit" in filename or "feedback" in filename:
        path = folder.source_data.modelbuilder.path
        type = "vector"
    elif filename.startswith("crs"):
        path = filename  # wms
        type = "wms"
    elif "opmerkingen" in filename:
        path = folder.source_data.wsa_output_administratie.path
        type = "vector"
    else:
        print("Could not find path for:", filename)
    return path, type


def load_test_protocol_v21_layers(folder: Folders, structure=STRUCTURE, themes=THEMES):
    """loads klimaatsommen layers
    Groups are created at the same time when layers are added to them

    """

    # get path
    project = Project(structure, SUBJECT)
    project.generate_groups()

    # create groups
    for parent_group, values in structure.items():
        if type(values) is dict:
            for subgroup, layers in values.items():
                for layer in layers:
                    filename, qgis_name = layer
                    folder_path, _type = get_link(folder, filename.split("|")[0])
                    full_path = folder_path + "/" + filename
                    qml_path = QML_PATH + "/" + project.standardize(qgis_name) + ".qml"
                    print(full_path, qgis_name, qml_path)
                    layer = Layer(full_path, qgis_name, _type, qml_path, SUBJECT)
                    project.add_layer(layer, subgroup)
        else:
            for layer in values:
                filename, qgis_name = layer
                folder_path, _type = get_link(folder, filename.split("|")[0])
                full_path = folder_path + "/" + filename
                qml_path = QML_PATH + "/" + project.standardize(qgis_name) + ".qml"
                print(full_path, qgis_name, qml_path)
                layer = Layer(full_path, qgis_name, _type, qml_path, SUBJECT)
                project.add_layer(layer, parent_group)

    # now do all the themes
    for theme_name, theme_layers in themes.items():
        project.add_theme(theme_name, theme_layers)

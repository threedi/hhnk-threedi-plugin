# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:49:39 2022

@author: chris.kerklaan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:08:36 2021

@author: chris.kerklaan
"""
import os
import pandas as pd
from hhnk_threedi_plugin.qgis_interaction.project import Project
from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR

from qgis.core import QgsLayoutExporter, QgsRenderContext, QgsLayoutSize, QgsUnitTypes

LAYOUT_PATH = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'qgis_interaction', 'styling', 'print_layouts', 'wsa_kaarten.qpt')

def load_print_layout():
    project = Project() #subject="Layout klimaatsommen")
    project.add_print_layout_template(LAYOUT_PATH, "wsa_kaarten1")


def create_pdfs(folder, revisie):

    project = Project() #subject="Mapcomposer klimaatsommen")
    polder = folder.name
    output_path = folder.output.climate[revisie].path

    subtitle = "Maatregel model {} (rev{})".format(polder, revisie)

    # Select print composer
    dic = {}
    # Schadekaarten
    dic[0] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_cw_schade_totaal.pdf".format(polder, revisie),
        "theme": "klimaatsommen_schade_totaal",
        "title": "Schade",
        "legenda": "legenda_schade",
    }
    dic[1] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_cw_schade_plas.pdf".format(polder, revisie),
        "theme": "klimaatsommen_schade_plas",
        "title": "Schade plasvorming",
        "legenda": "legenda_schade",
    }
    dic[2] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_cw_schade_overlast.pdf".format(polder, revisie),
        "theme": "klimaatsommen_schade_overlast",
        "title": "Schade watersysteem",
        "legenda": "legenda_schade",
    }

    # #Gecorrigeerde schadekaarten
    dic[3] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_cw_schade_totaal_corr.pdf".format(polder, revisie),
        "theme": "klimaatsommen_schade_totaal_corr",
        "title": "Schade",
        "legenda": "legenda_schade",
    }
    dic[4] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_cw_schade_plas_corr.pdf".format(polder, revisie),
        "theme": "klimaatsommen_schade_plas_corr",
        "title": "Schade plasvorming",
        "legenda": "legenda_schade",
    }
    dic[5] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_cw_schade_overlast_corr.pdf".format(polder, revisie),
        "theme": "klimaatsommen_schade_overlast_corr",
        "title": "Schade watersysteem",
        "legenda": "legenda_schade",
    }

    # Inundatiekaarten
    dic[6] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_inundatie_totaal.pdf".format(polder, revisie),
        "theme": "klimaatsommen_inundatie_totaal",
        "title": "Inundatie",
        "legenda": "legenda_inundatie",
    }
    dic[7] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_inundatie_plas.pdf".format(polder, revisie),
        "theme": "klimaatsommen_inundatie_plas",
        "title": "Inundatie plasvorming",
        "legenda": "legenda_inundatie",
    }
    dic[8] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_inundatie_overlast.pdf".format(polder, revisie),
        "theme": "klimaatsommen_inundatie_overlast",
        "title": "Inundatie watersysteem",
        "legenda": "legenda_inundatie",
    }

    # Ruimtekaart
    dic[9] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_ruimtekaart.pdf".format(polder, revisie),
        "theme": "klimaatsommen_ruimtekaart",
        "title": "Ruimtekaart",
        "legenda": "legenda_ruimtekaart",
    }

    # Landgebruik
    dic[10] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_landgebruik.pdf".format(polder, revisie),
        "theme": "klimaatsommen_landgebruik",
        "title": "Landgebruik",
        "legenda": "legenda_landgebruik",
    }

    # Set dict in dataframe that will be looped.
    df = pd.DataFrame(
        columns=["composer_name", "pdf_name", "theme", "title", "legenda"]
    )
    df = df.append([dic[a] for a in dic], ignore_index=True)

    df["pdf_path"] = df["pdf_name"].apply(lambda x: os.path.join(output_path, x))

    # legenda_ids = df['legenda'].unique().tolist()
    legenda_ids = [
        "legenda_schade",
        "legenda_inundatie",
        "legenda_ruimtekaart",
        "legenda_landgebruik",
    ]

    # Connect to project and al print composers
    layoutmanager = project.instance.layoutManager()

    for index, row in df.iterrows():
        result = create_pdf_from_composer(
            layoutmanager,
            project,
            composer_name=row["composer_name"],
            title=row["title"],
            subtitle=subtitle,
            legenda_ids=legenda_ids,
            selected_legenda=row["legenda"],
            theme=row["theme"],
            output_file=row["pdf_path"],
        )

        if result == 0:
            project.send_message(f"pdf aangemaakt: {row['pdf_name']}", level=0)
        else:
            project.send_message(
                f"pdf niet gelukt: {row['pdf_name']}, {result}", level=1
            )


def create_pdf_from_composer(
    layoutmanager,
    project,
    composer_name,
    title,
    subtitle,
    legenda_ids,
    selected_legenda,
    theme,
    output_file,
):
    layout_item = layoutmanager.layoutByName(composer_name)  # test is the layout name

    # -------------------------------------------------------------------------------------
    # Change layout settings
    # -------------------------------------------------------------------------------------
    label_item = layout_item.itemById("titel")
    label_item.setText(title)

    label_item = layout_item.itemById("subtitel")
    label_item.setText(subtitle)

    # Hide all legend items, only show selected legend.
    for legenda_id in legenda_ids:
        legenda_item = layout_item.itemById(legenda_id)
        legenda_item.setVisibility(False)
        if legenda_id == selected_legenda:
            legenda_item.setVisibility(True)

    map = layout_item.referenceMap()
    map.setFollowVisibilityPresetName(theme)

    # Poging om extent goed te zetten, maar handmatig is beter.
    # map.setExtent(project.mapcanvas_extent)
    # -------------------------------------------------------------------------------------
    # Export
    # -------------------------------------------------------------------------------------
    pdf_settings = QgsLayoutExporter.PdfExportSettings()
    pdf_settings.textRenderFormat = (
        QgsRenderContext.TextFormatAlwaysText
    )  # If not changed the labels will be ugly in the pdf

    # image_settings = QgsLayoutExporter.ImageExportSettings()

    export = QgsLayoutExporter(layout_item)
    result = export.exportToPdf(output_file, pdf_settings)
    return result


from hhnk_threedi_tools import Folders
folder = Folders(r"C:\Users\chris.kerklaan\Documents\Github\hhnk-threedi-tools\test_polder")
revisie = "hoekje_volledig"
create_pdfs(folder, revisie)
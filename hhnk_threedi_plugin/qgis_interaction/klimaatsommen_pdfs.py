# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:08:36 2021

@author: chris.kerklaan
"""
import os
import pandas as pd
from hhnk_threedi_plugin.qgis_interaction.project import Project
import hhnk_research_tools as hrt
import hhnk_threedi_tools as htt


def load_print_layout():
    """Loads layout in project. """

    template_path = hrt.get_pkg_resource_path(package_resource=htt.resources.qgis_print_layouts,
                                            name="wsa_kaarten_landscape.qpt")


    project = Project() #subject="Layout klimaatsommen")
    project.layout.add_from_template(template_path=template_path, name="wsa_kaarten1")


def create_pdfs(folder, revisie):
    #TODO verplaatsen naar csv
    project = Project() #subject="Mapcomposer klimaatsommen")
    polder = folder.name
    output_path = folder.threedi_results.climate_results[revisie].path

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

    #Gecorrigeerde schadekaarten
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

    # # Ruimtekaart
    dic[9] = {
        "composer_name": "wsa_kaarten1",
        "pdf_name": "{}_rev{}_ruimtekaart.pdf".format(polder, revisie),
        "theme": "klimaatsommen_ruimtekaart",
        "title": "Ruimtekaart",
        "legenda": "legenda_ruimtekaart",
    }

    # Landgebruik
    # dic[10] = {
    #     "composer_name": "wsa_kaarten1",
    #     "pdf_name": "{}_rev{}_landgebruik.pdf".format(polder, revisie),
    #     "theme": "klimaatsommen_landgebruik",
    #     "title": "Landgebruik",
    #     "legenda": "legenda_landgebruik",
    # }

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

    for index, row in df.iterrows():
        print(f"creating pdf at {row['pdf_path']}")
        result = project.layout.create_pdf_from_composer(
            composer_name=row["composer_name"],
            title=row["title"],
            subtitle=subtitle,
            legenda_ids=legenda_ids,
            selected_legenda=row["legenda"],
            theme=row["theme"],
            output_file=row["pdf_path"],
        )

        if result == 0:
            print(f"pdf aangemaakt: {row['pdf_name']}")
        else:
            print(f"pdf niet gelukt: {row['pdf_name']}, {result}")

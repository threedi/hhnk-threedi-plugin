# Data locaties & bewegingen
**Doel:** Uitleg over waar data wordt geexporteerd, opgeslagen en hoe data vervolgens beweegt.  
**Lezerspubliek:** Ontwikkelaars & gegevensbeheerders

## 1. Export
In de de `db_exporter` worden gegevens van drie bronnen gebruikt. 
* DAMO 
* CS Objecten
* BGT (Basisregistratie Grootschalige topografie)

Alle drie de bronnen zijn oracle databases die binnen HHNK draaien (zijn niet van buiten de HHNK omgeving beschikbaar). In DAMO en CS Objecten zitten objectdata die het waterschap beheerd. CS Objecten speelt een centrale rol in het Centraal Data Platform binnen HHNK. Objecten die als 'asset' gezien worden zitten hier in, denk aan stuwen en gemalen. Er is overlap met DAMO, maar in CS Objecten zit meer informatie. O.a. Hydro-object is een laag die (nog) niet in CS Objecten zit, maar alleen in DAMO. Voor de modelbuilder gebruiken we de waterdelen en ondersteunende waterdelen uit de BGT. 

De `db_exporter` haalt de benodigde lagen voor een gegeven gebied op uit de database (via config files in de resources) en slaat deze op in een geopackage. Dit is de bron voor de `IntermediateConverter` en de `HyDAMO-validator`.


## 2. Datapaden
_Locaties van ruwe export, omgezet, gevalideerd, verbeterd, schematisatie._

Dit is nu eigenlijk nog meer een ontwerp. Hier moeten we naartoe werken. Is mogelijk niet volledig en moet nog gereviewed worden.

```text
{project_naam}
├── 00_config
│   ├── 00_Export
│       ├── databases.json
│   ├── 03_HyDAMO_Validator
│       ├── validationrules.json
│   ├── 04_HyDAMO_Fixer
│       ├── fixes.json
│   ├── 05_3Di_Converter
│       ├── brug.json
│       ├── duiker.json
│       ├── gemaal.json
│       ├── hydroobject.json
│       ├── profiel.json
│       ├── stuw.json
│   └── README.md
├── 01_source_data
│   ├── 00_Export
│       ├── raw_export.gpkg
│       ├── rasters
│           └── ...
│   ├── 01_Intermediate_Converter
│       ├── DAMO.gpkg
│   ├── 02_HyDAMO
│       ├── HyDAMO.gpkg
│   ├── 03_HyDAMO_Validator
│       ├── Set 1
│           ├── results.gpkg
│           ├── validation_result.json
│       ├── Set 2...
│   ├── 04_HyDAMO_Fixer
│       ├── Set 1
│           ├── HyDAMO.gpkg
│           ├── fixer_result.json
│       ├── Set 2...
│   ├── 05_3Di_Converter
│       ├── ??? komt hier wel iets terecht -> schematisatie eindigt bij 02_schematisation
│   └── polder.gpkg
│   └── README.md
├── 02_schematisation
│   └── 00_basis
│       └── {project_naam}.gpkg
│       └── rasters
│           └── ...
│   └── ...
│   └── README.md
├── 03_3di_results
│   └── ...
│   └── ...
│   └── README.md
└── 04_test_results
│   └── ...
│   └── ...
│   └── README.md
└── log.log
```

## 3. Datastroom (bestand- en opslag)
Hoe de uitvoer van elke stap de invoer voor de volgende vormt is weergegeven in onderstaande flowchart.

```mermaid
flowchart TD
    %% Subgraphs voor overzicht
    subgraph 00_config [00_config]
        direction TB
        DB["00_Export/databases.json"]:::style_0
        VR["03_HyDAMO_Validator/validationrules.json"]:::style_0
        FIXES["04_HyDAMO_Fixer/fixes.json"]:::style_0
        CONVERSION_CONFIGS["05_3Di_Converter/{}.json"]:::style_0
    end

    DB ~~~ VR
    VR ~~~ FIXES
    FIXES ~~~ CONVERSION_CONFIGS

    subgraph 01_source_data [01_source_data]
        direction TB
        POLDER["polder.gpkg"]:::style_0
        RAW_EXPORT["00_Export/raw_export.gpkg"]:::style_A
        INTERMEDIATE["01_Intermediate_Converter/DAMO.gpkg"]:::style_B
        HYDAMO["02_HyDAMO/HyDAMO.gpkg"]:::style_C
        VALIDATION_SET1["03_HyDAMO_Validator/set_1/results.gpkg"]:::style_D
        FIX_SET1["04_HyDAMO_Fixer/set_1/HyDAMO.gpkg"]:::style_E
        VALIDATION_SET2["03_HyDAMO_Validator/set_2/results.gpkg"]:::style_D
        FIX_SET2["04_HyDAMO_Fixer/set_2/HyDAMO.gpkg"]:::style_E
    end

    subgraph 02_schematisation [02_schematisation]
        direction TB
        SCHEMA["00_basis/{project_naam}.gpkg"]:::style_F
    end

    %% Datastromen
    DB -->|DatabaseExporter| RAW_EXPORT
    POLDER -->|DatabaseExporter| RAW_EXPORT
    RAW_EXPORT -->|IntermediateConverter| INTERMEDIATE
    INTERMEDIATE -->|DAMO2HyDAMOConverter| HYDAMO
    VR -->|HyDAMOValidator| VALIDATION_SET1
    HYDAMO -->|HyDAMOValidator| VALIDATION_SET1
    HYDAMO -->|HyDAMOFixer| FIX_SET1
    FIXES -->|HyDAMOFixer| FIX_SET1
    VALIDATION_SET1 -->|HyDAMOFixer| FIX_SET1
    FIX_SET1 -->|HyDAMOValidator| VALIDATION_SET2
    FIX_SET1 -->|HyDAMOFixer| FIX_SET2
    VALIDATION_SET2 -->|HyDAMOFixer| FIX_SET2
    CONVERSION_CONFIGS -->|3DiConverter| SCHEMA
    FIX_SET2 -->|3DiConverter| SCHEMA

    %% Gradient styling from A to F
    classDef style_0 fill:#cccccc,stroke:#333,stroke-width:2px;
    classDef style_A fill:#e0b3ff,stroke:#333,stroke-width:2px;
    classDef style_B fill:#b3c6ff,stroke:#333,stroke-width:2px;
    classDef style_C fill:#b3ffe0,stroke:#333,stroke-width:2px;
    classDef style_D fill:#ffffb3,stroke:#333,stroke-width:2px;
    classDef style_E fill:#ffd6b3,stroke:#333,stroke-width:2px;
    classDef style_F fill:#ff4d4d,stroke:#333,stroke-width:2px;

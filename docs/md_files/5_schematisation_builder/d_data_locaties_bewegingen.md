# Data locaties & bewegingen
**Doel:** Uitleg over waar data wordt geexporteerd, opgeslagen en hoe data vervolgens beweegt.  
**Lezerspubliek:** Ontwikkelaars & gegevensbeheerders

## 1. Export
_Wat waar vandaan._



## 2. Datapaden
_Locaties van ruwe export, omgezet, gevalideerd, verbeterd, schematisatie._

Dit is nu eigenlijk nog meer een ontwerp. Hier moeten we naartoe werken. Is mogelijk niet volledig en moet nog gereviewed worden.

```text
{project_naam}
├── 00_config
│   ├── 00_Export
│       ├── databases.json
│   ├── 04_HyDAMO_Validator
│       ├── validationrules.json
│   ├── 05_HyDAMO_Fixer
│       ├── fixes.json
│   ├── 06_3Di_Converter
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
_Hoe de uitvoer van elke stap de invoer voor de volgende vormt._

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
    VR -->|HyDAMOValidator| VALIDATION_SET2
    FIX_SET1 -->|HyDAMOValidator| VALIDATION_SET2
    FIX_SET1 -->|HyDAMOFixer| FIX_SET2
    FIXES -->|HyDAMOFixer| FIX_SET2
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

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
│       ├── intermediate_conversion.gpkg
│   ├── 02_DAMO
│       ├── DAMO.gpkg
│   ├── 03_HyDAMO
│       ├── HyDAMO.gpkg
│   ├── 04_HyDAMO_Validator
│       ├── Set 1
│           ├── results.gpkg
│           ├── validation_result.json
│       ├── Set 2...
│   ├── 05_HyDAMO_Fixer
│       ├── Set 1
│           ├── HyDAMO.gpkg
│           ├── fixer_result.json
│       ├── Set 2...
│   ├── 06_3Di_Converter
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
    subgraph Config [00_config]
        Export["00_Export"]:::config
        Validator["04_HyDAMO_Validator"]:::config
        Fixer["05_HyDAMO_Fixer"]:::config
        Converter["06_3Di_Converter"]:::config
    end

    subgraph SourceData [01_source_data]
        SD_Export["00_Export/raw_export.gpkg"]:::data
        SD_Intermediate["01_Intermediate_Converter/intermediate_conversion.gpkg"]:::data
        SD_DAMO["02_DAMO/DAMO.gpkg"]:::data
        SD_HyDAMO["03_HyDAMO/HyDAMO.gpkg"]:::data
        SD_Validator["04_HyDAMO_Validator/Set_X/results.gpkg"]:::data
        SD_Fixer["05_HyDAMO_Fixer/Set_X/HyDAMO.gpkg"]:::data
    end

    subgraph Schematisation [02_schematisation]
        Schema["00_basis/{project_naam}.gpkg"]:::schema
    end

    subgraph ThreeDiResults [03_3di_results]
        ThreeDi["3Di resultaten"]:::results
    end

    %% Datastromen
    Export -->|stap 1| SD_Export
    SD_Export -->|stap 2| SD_Intermediate
    SD_Intermediate -->|stap 3| SD_DAMO
    SD_DAMO -->|stap 4| SD_HyDAMO
    SD_HyDAMO -->|validator| Validator
    Validator -->|validated| SD_Validator
    SD_Validator -->|fixer| Fixer
    Fixer -->|fixed| SD_Fixer
    SD_Fixer -->|converter| Converter
    Converter -->|schematisatie| Schema
    Schema -->|3Di input| ThreeDi

    %% Styling
    classDef config fill:#f9f,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    classDef data fill:#bbf,stroke:#333,stroke-width:2px
    classDef schema fill:#bfb,stroke:#333,stroke-width:2px
    classDef results fill:#ffb,stroke:#333,stroke-width:2px,stroke-dasharray: 2 2



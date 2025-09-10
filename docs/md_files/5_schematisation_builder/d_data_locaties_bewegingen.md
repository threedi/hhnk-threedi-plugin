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
```

## 3. Datastroom (bestand- en opslag)
_Hoe de uitvoer van elke stap de invoer voor de volgende vormt._

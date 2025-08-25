# Architectuur, code & tests
**Doel:** Uitleggen hoe het systeem op hoofdlijnen werkt en hoe de onderdelen samenhangen. Beschrijven van de rol van elke codecomponent en de interne structuur. Uitleg over tests en testdatasets.   
**Lezerspubliek:** Ontwikkelaars & architecten

## 1. Systeemstroomschema
_Flowio-diagram met uitleg._

## 2. Overzicht componenten
_Lijst van modules en hun verantwoordelijkheden._

| Type | Volgorde nr. | Module | Rol | Bestand |
|------|----------------|--------|-----|---------|
| Kernlogica | 1 | Database exporter | Genereert een ruwe export op basis van een polder polygoon. | hhnk-threedi-tools/hhnk_threedi_tools/core/schematisation_buider/DB_exporter.py |
| Kernlogica | 2 | Intermediate converter | Zet ruwe export om in DAMO formaat. | hhnk-threedi-tools/hhnk_threedi_tools/core/schematisation_buider/intermediate_converter.py |
| Kernlogica | 3 | DAMO naar HyDAMO converter | Zet DAMO om in HyDAMO formaat. | hhnk-threedi-tools/hhnk_threedi_tools/core/schematisation_buider/DAMO_HyDAMO_converter.py |
| Kernlogica | 4 | HyDAMO validator | Trapt validatieregels af op HyDAMO bestand. | hhnk-threedi-tools/hhnk_threedi_tools/core/schematisation_buider/HyDAMO_validator.py |
| Kernlogica | 5 | HyDAMO fixer | Interpreteert validatieresultaten en biedt mogelijkheden tot automatische fixes. | hhnk-threedi-tools/hhnk_threedi_tools/core/schematisation_buider/... |
| Kernlogica | 6 | 3Di converter | Zet het (verbeterde) HyDAMO bestand om in een 3Di schematisatie | hhnk-threedi-tools/hhnk_threedi_tools/core/schematisation_buider/HyDAMO_conversion_to_3di.py |
| Interfaces |   | ... | ... | hhnk-threedi-tools/hhnk_threedi_tools/core/schematisation_buider/schematisation_builder.py |
| Interfaces |   | ... | ... | hhnk-threedi-plugin/hhnk_threedi_plugin/gui/schematisation_builder.py |

### Database exporter
_..._

### Intermediate converter
_Waarom zijn ze nodig, hoe is de code opgebouwd (parent, child classes), functionaliteiten per converter._

### DAMO naar HyDAMO converter
_..._

### HyDAMO validator
_Fork van, hoe gebruiken we de bestaande functionaliteiten in de validator, waarom hebben we custom func toegevoegd, link naar overzicht validatieregels_

### HyDAMO fixer
_..._

### 3Di converter
HyDAMO_conversion_to_3di mogelijk straks niet meer relevant door volledige QGIS integratie. Anders is het netjes om HyDAMO_conversion_to_3di.py te vernoemen naar HyDAMO_3Di_converter.py voor uniformiteit.

## 3. Testoverzicht
- **Unittests** – Controleren individuele functies/klassen in isolatie.  
- **Integratietests** – Controleren dat componenten (exporter, (hy)damo converter, validator, fixer, schematisation converter) goed samenwerken.  
- **End-to-end tests** – Controleren van de volledige datastroom: export → omzetten naar (hy)damo → valideren → verbeteren → her-valideren → omzetten naar schematisatie (op objectniveau, danwel voor de gehele set).  

| Testbestand | Type test | Status | Scope | Input dataset | Output dataset | Beschrijving | Testvariabelen |
|----------|-----------|--------|-------|------------------------|-------------------------|-------------|----------------|
| _test_....py_ | _..._ | 🟢 Getest | _..._ | _.../....gpkg_ | _.../....gpkg_ | _..._ | _..._ |
| test_flow_profiles.py | End-to-end | 🟠 Gedeeltelijk getest | Volledige flow | _.../....gpkg_ | _.../....gpkg_ | Controleert volledige dataverwerking: conversie naar (hy)damo → validatie → verbetering → conversie naar model | _..._ |
| _test_....py_ | _..._ | 🔴 Niet getest | _..._ | _.../....gpkg_ | _.../....gpkg_ | _..._ | _..._ |

### Testomgeving opzetten en tests uitvoeren
_Hier linken naar doc threedi-tools_  

### Testdata en integratie
...

- Alle tests draaien automatisch bij pull requests.  
- Mergen vereist dat alle tests slagen.  
# Architectuur, code & tests
**Doel:** Uitleggen hoe het systeem op hoofdlijnen werkt en hoe de onderdelen samenhangen. Beschrijven van de rol van elke codecomponent en de interne structuur. Uitleg over tests en testdatasets.   
**Lezerspubliek:** Ontwikkelaars & architecten

## 1. Systeemstroomschema
_Flowio-diagram met uitleg._



## 2. Overzicht componenten
_Lijst van modules en hun verantwoordelijkheden._

| Type | Volgorde nr. | Module | Rol | Bestand |
|------|----------------|--------|-----|---------|
| Kernlogica | 1 | Database exporter | Genereert een ruwe export op basis van een polder polygoon. | /hhnk_threedi_tools/core/schematisation_buider/ DB_exporter.py |
| Kernlogica | 2 | Intermediate converter | Zet ruwe export om in DAMO formaat. | /hhnk_threedi_tools/core/schematisation_buider/ intermediate_converter.py |
| Kernlogica | 3 | DAMO naar HyDAMO converter | Zet DAMO om in HyDAMO formaat. | /hhnk_threedi_tools/core/schematisation_buider/ DAMO_HyDAMO_converter.py |
| Kernlogica | 4 | HyDAMO validator | Trapt validatieregels af op HyDAMO bestand. | /hhnk_threedi_tools/core/schematisation_buider/ HyDAMO_validator.py |
| Kernlogica | 5 | HyDAMO fixer | Interpreteert validatieresultaten en biedt mogelijkheden tot automatische fixes. | /hhnk_threedi_tools/core/schematisation_buider/ ... |
| Kernlogica | 6 | 3Di converter | Zet het (verbeterde) HyDAMO bestand om in een 3Di schematisatie | /hhnk_threedi_tools/core/schematisation_buider/ HyDAMO_conversion_to_3di.py |
| Interfaces |   | ... | ... | /hhnk_threedi_tools/core/schematisation_buider/ schematisation_builder.py |
| Interfaces |   | ... | ... | /hhnk_threedi_plugin/gui/ schematisation_builder.py |

### Database exporter
_functionaliteit / waarom nodig_

_code opbouw_


### Intermediate converter
Intermediate converter vormt een schakel tussen de ruwe exportbestanden (DAMO, CSO & HDB) en de uiteindelijke HyDAMO/3Di-invoer, door de ruwe exportbestanden om te zetten in DAMO-formaat volgens standaard. De intermediate converter zorgt voor:
* Inlezen en valideren van lagen.
* Bewerken en verrijken van data (IDs, geometrie, koppelingen).
* Schrijven van consistente outputs.

De code is opgebouwd rond een parent klasse en meerdere child klassen.

### **IntermediateConverter** (parent class)
| Type | Inputlagen | Output |
|------|------------|---------|
| Parent klasse | generiek (verschilt per child) | Consistente dataflow en output naar GeoPackage |

| Functie | Beschrijving | Helper functies |
|---------|--------------|-----------------|
| `load_layers()` | Laadt benodigde lagen in het interne `_Data` object | – |
| `process_data()` | Abstract: wordt overschreven in child class om data te bewerken | – |
| `write_outputs()` | Schrijft gewijzigde lagen naar GeoPackage | – |

---

### **GemaalIntermediateConverter**
| Type | Inputlagen | Output |
|------|------------|---------|
| Child class | `gemaal`, `pomp`, `hydroobject` | Gemaal- en pomptabellen met koppelingen en correcties |

| Functie | Beschrijving | Helper functies |
|---------|--------------|-----------------|
| `load_layers()` | Laadt gemaal-, pomp- en hydroobjectlagen | – |
| `update_gemaal_layer()` | Verwerkt pomplagen en koppelt deze aan gemaal | `_add_column_gemaalid`, `_add_column_globalid`, `_adjust_pomp_maximalecapaciteit`, `_make_pomp_layer` |
| `write_outputs()` | Schrijft lagen naar GeoPackage | – |

---

### **PeilgebiedIntermediateConverter**
| Type | Inputlagen | Output |
|------|------------|---------|
| Child class | `peilgebiedpraktijk` | Opschoning en voorbereiding voor validatie (nog beperkt) |

| Functie | Beschrijving | Helper functies |
|---------|--------------|-----------------|
| `load_layers()` | Laadt peilgebiedpraktijk | – |
| `update_peilgebied_layer()` | Placeholder, nog niet geïmplementeerd | – |
| `write_outputs()` | Schrijft peilgebiedlagen naar GeoPackage | – |

---

### **ProfileIntermediateConverter**
| Type | Inputlagen | Output |
|------|------------|---------|
| Child class | `hydroobject`, `gw_pro`, `gw_prw`, `gw_pbp`, `iws_geo_beschr_profielpunten`, `peilgebiedpraktijk` | Profiel-tabellen en gekoppelde hydroobjecten |

| Functie | Beschrijving | Helper functies |
|---------|--------------|-----------------|
| `load_layers()` | Laadt hydroobject- en profielgerelateerde tabellen | – |
| `process_linemerge()` | Voegt hydroobjecten samen per peilgebied (linemerge) | – |
| `create_profile_tables()` | Bouwt tabellen: `profielgroep`, `profiellijn`, `profielpunt` | `_assign_hydroobject_ids` |
| `connect_profiles_to_hydroobject_without_profiles()` | Koppelt profielen aan hydroobjecten zonder profiel | `_add_z_to_point_geometry_based_on_column`, `_drop_z_from_linestringz_geometry` |
| `write_outputs()` | Schrijft profiel- en hydroobjectlagen naar GeoPackage | – |

---

### **_Data**
| Type | Inputlagen | Output |
|------|------------|---------|
| Helper class | Afhankelijk van aangeroepen converter | Consistente dataset en toegang tot tabellen |

| Functie | Beschrijving | Helper functies |
|---------|--------------|-----------------|
| Opslag & beheer | Houdt lagen als GeoDataFrames bij, gedeeld tussen converters | – |
| Properties | Toegang tot tabellen via `self.data` | – |




### DAMO naar HyDAMO converter
_functionaliteit / waarom nodig_

_code opbouw_


### HyDAMO validator
_functionaliteit / waarom nodig_

_code opbouw_
_Fork van, hoe gebruiken we de bestaande functionaliteiten in de validator, waarom hebben we custom func toegevoegd, link naar overzicht validatieregels_

### HyDAMO fixer
_functionaliteit / waarom nodig_

_code opbouw_


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
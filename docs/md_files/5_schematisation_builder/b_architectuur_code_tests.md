# Architectuur & ontwerp
**Doel:** Uitleggen hoe het systeem op hoofdlijnen werkt en hoe de onderdelen samenhangen.  
**Lezerspubliek:** Ontwikkelaars & architecten

## 1. Systeemstroomschema
_Flowio-diagram met uitleg._

## 2. Overzicht componenten
_Lijst van modules en hun verantwoordelijkheden._

## 3. Gegevensstroomschema (conceptueel)
_Laat zien hoe gegevens tussen componenten bewegen, inclusief opslag._

<hr style="border: 2px solid #000; margin: 2em 0;">


# Componenten & code
**Doel:** Beschrijven van de rol van elke codecomponent en de interne structuur.  
**Lezerspubliek:** Ontwikkelaars

## 1. Module-overzicht
_Lijst van modules/klassen met korte samenvatting._

## 2. Functie-overzicht
_Lijst van functies binnen modules/klassen met korte samenvatting._

<hr style="border: 2px solid #000; margin: 2em 0;">


# Tests
**Doel:** Uitleg over tests en testdatasets.  
**Lezerspubliek:** Ontwikkelaars

## 1. Testoverzicht
- **Unittests** – Controleren individuele functies/klassen in isolatie.  
- **Integratietests** – Controleren dat componenten (exporter, (hy)damo converter, validator, fixer, schematisation converter) goed samenwerken.  
- **End-to-end tests** – Controleren van de volledige datastroom: export → omzetten naar (hy)damo → valideren → verbeteren → her-valideren → omzetten naar schematisatie (op objectniveau, danwel voor de gehele set).  

| Testnaam | Type test | Status | Scope | Input dataset | Output dataset | Beschrijving | Testvariabelen |
|----------|-----------|--------|-------|------------------------|-------------------------|-------------|----------------|
| _test_....py_ | _..._ | 🟢 Getest | _..._ | _.../....gpkg_ | _.../....gpkg_ | _..._ | _..._ |
| test_flow_profiles.py | End-to-end | 🟠 Gedeeltelijk getest | Volledige flow | _.../....gpkg_ | _.../....gpkg_ | Controleert volledige dataverwerking: conversie naar (hy)damo → validatie → verbetering → conversie naar model | _..._ |
| _test_....py_ | _..._ | 🔴 Niet getest | _..._ | _.../....gpkg_ | _.../....gpkg_ | _..._ | _..._ |

## 2. Testomgeving opzetten en tests uitvoeren
_Hier linken naar doc threedi-tools_  

## 3. Testdata
...

## 4. Integratie
- Alle tests draaien automatisch bij pull requests.  
- Mergen vereist dat alle tests slagen.  

<hr style="border: 2px solid #000; margin: 2em 0;">

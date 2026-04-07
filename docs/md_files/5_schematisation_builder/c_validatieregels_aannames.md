# Validatieregels & aannames
**Doel:** Vastleggen van validatie- en verbeteringsregels met onderbouwing.  
**Lezerspubliek:** Ontwikkelaars & hydrologen

## 1. Validatieregels
De validatieregels zijn gedefineerd in een JSON-bestand in de resources map van de hhnk-threedi-tools, [hier](https://github.com/threedi/hhnk-threedi-tools/blob/main/hhnk_threedi_tools/resources/schematisation_builder/validationrules.json). Dit bestand is invoer voor de HyDAMOValidatieModule.

Een tabel-overzicht (CSV-bestand) van de validatieregels staat [hier](https://github.com/threedi/hhnk-threedi-tools/blob/main/hhnk_threedi_tools/resources/schematisation_builder/validation_rules.csv). Daarnaast is er een `general_rules.csv` voor algemene regels. Beide zijn, ter documentatie, gegenereerde overzichten (vanuit het JSON-bestand) met [dit script](https://github.com/threedi/hhnk-threedi-tools/blob/main/hhnk_threedi_tools/core/schematisation_builder/utils/export_validation_rules_overview.py). De CSV's worden automatisch bijgewerkt via een GitHub Actions workflow wanneer het JSON-bestand wijzigt.

## 2. Verbeteringslogica
_Automatische en handmatige stappen inclusief aannames._
_Link naar excel overzicht in threedi-tools._


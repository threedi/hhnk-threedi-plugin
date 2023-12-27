# **Werkafspraken**

## **Logboek**
Gedurende het gehele modelleerproces is het van belang een logboek bij te houden van gemaakte stappen en wijzigingen in het model. Neem in het logboek op door wie, wanneer en in welke modelrevisie de wijzigingen zijn gemaakt. Daarnaast heeft het de voorkeur om wijzigingen in in het model via SQL aan te brengen en in het logboek te noteren, zodat deze eenvoudig opnieuw uitgevoerd kunnen worden. Het logboek ziet er bijvoorbeeld zo uit:

``` sql
-------Revisie 4------------
-- Wouter van Esse, 25 oktober 2021
-- Duiker vervangen door stuw op aangeven gebiedsbeheerder
DELETE FROM v2_orifice WHERE code LIKE 'KDU-JL-3420'
;
INSERT INTO v2_cross_section_definition (code, id,width,shape)
VALUES ("KST-Q-23237", 9999001,1,1)
;
INSERT INTO v2_weir (zoom_category, code, display_name,
    discharge_coefficient_negative, sewerage, 
    discharge_coefficient_positive, external, crest_type, 
    friction_type, friction_value,
	connection_node_start_id, connection_node_end_id, 
    crest_level, cross_section_definition_id) 
VALUES (4, "KST-Q-23237", "KST-Q-23237", 0.8, 0, 0.8, 0, 4, 2, 
        0.03,2597, 1051, -0.6, 9999001)
;
```
Geef ook aan wanneer het model is gebruikt voor het maken van de hydraulische toets of klimaatsommen en of dit om de referentie situatie of een maatregel scenario gaat.



<!---
TODO aanvullen? Nieuwe methode model governance?
-->
## **Logboek**
Gedurende het gehele modelleerproces is het van belang een logboek bij te houden van gemaakte stappen en wijzigingen in het model. Neem in het logboek op door wie, wanneer en in welke modelrevisie de wijzigingen zijn gemaakt. Daarnaast heeft het de voorkeur om wijzigingenin in het model via SQL aan te brengen en in het logboek te noteren, zodat deze eenvoudig opnieuw uitgevoerd kunnen worden. Het logboek ziet er bijvoorbeeld zo uit:

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

## **Referentie- en maatregelmodel**
In het BWN2-project is sprake van referentiemodellen en maatregelmodellen. Zoals de naam doet vermoeden gaat het in de referentiemodellen om de referentie situatie; het watersysteem zoals dit er op dat moment in de praktijk bij ligt. Daarnaast zijn voor sommige polders modellen aangepast om maatregelen te testen of ruimtelijke ontwikkelingen te toetsen. Het is belangrijk om onderscheid te blijven maken tussen deze typen modellen. De referentiemodellen zijn de onderligger voor de toetsing en vertrekpunt voor nieuwe projecten of vragen. Deze modellen zijn met revisienummer en modelleur opgeslagen in het modellenregister.

## **Hydraulische toets en klimaatsommen**
Binnen de referentie of maatregelmodellen kan nog onderscheid gemaakt worden tussen het model voor de hydraulische toets (HT) en de modellen voor de klilmaatsommen.

### Hydraulische toets
In de HT wordt getoetst of het watersyteem voldoende kan afvoeren onder normale omstandigheden. Dat wil zeggen dat het watersysteem maximaal af moet kunnen voeren zonder dat er knelpunten of wateroverlast ontstaat. De maximale afvoer is voor polders vastgelegd in de afvoernorm (meestal 14,4 mm/dag of 10 m3/min/100ha, in grote polderder soms 9 of 8 m3/min/100ha). In deze afvoersituatie mag de opstuwing in peilgebieden (~30cm) of verhang in watergangen (~2-4 cm/km) niet boven bepaalde grenswaarden uitkomen. De genoemde waarden zijn afhankelijk van gebiedseigenschappen. Ook duikers mogen niet te veel opstuwing geven (~1cm). 

Het model dat hoort bij de HT heeft in 3Di een 0D inloop-component. Alle neerslag (14,4 mm/dag) gaat hiermee geforceerd het watersysteem in moet zo worden afgevoerd. Zo wordt dus alleen het watersysteem getoetst.

### Klimaarsommen

## **Circulair modelleren**


<!---
TODO
-->
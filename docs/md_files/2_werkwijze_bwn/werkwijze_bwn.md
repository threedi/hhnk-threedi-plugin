# **Werkwijze BWN2**
Voor het programma BWN2 zijn modellen en een werkwijze opgesteld. Het doel hiervan is om alle polders binnen HHNK op eenduidige manier te toetsen op mogelijke wateroverlast. Deze toetsing is uitgevoerd tussen 2015 en 2020, maar kan periodiek worden herhaald wanneer (ruimtelijke) ontwikkelingen plaatsvinden. Door deze werkwijze te volgen zijn eveneens eenduidige vergelijkingen te maken tussen referentie en maatregel of ontwikkel scenarios. 

## **Hydraulische toets en klimaatsommen**
BWN2 toetst het watersysteem op twee manieren, ten eerste middels de hydraulische toets (HT) en via klimaatsommen.

### Hydraulische toets
In de HT wordt getoetst of het watersysteem voldoende kan afvoeren onder normale omstandigheden. Dat wil zeggen dat het watersysteem maximaal af moet kunnen voeren zonder dat er knelpunten of wateroverlast ontstaat. De maximale afvoer is voor polders vastgelegd in de afvoernorm (meestal 14,4 mm/dag of 10 m3/min/100ha, in grote polders soms 9 of 8 m3/min/100ha). In deze afvoersituatie mag de opstuwing in peilgebieden (~30cm) of verhang in watergangen (~2-4 cm/km) niet boven bepaalde grenswaarden uitkomen. Ook duikers mogen niet te veel opstuwing geven (~1cm). De genoemde waarden zijn afhankelijk van gebiedseigenschappen. 

Het model dat hoort bij de HT heeft in 3Di een 0D inloop-component. Alle neerslag (~14,4 mm/dag) gaat hiermee geforceerd het watersysteem in moet zo worden afgevoerd. Zo wordt dus alleen het watersysteem getoetst. De resultaten van de [0d1d_test](..\4_gebruik_plugin\g_0d1d_test.md) worden gebruikt voor de hydraulische toets (mits de modelleur tevreden is met het functioneren van het model). 

De resultaten van opstuwing en verhang worden via kaarten gedeeld met de watersysteem-adviseurs. Ze worden gebruikt voor het identificeren van maatregelen en zijn  input voor de leggertool. Met de leggertool worden minimale profielen van watergangen voor afvoer vastgesteld.

### Klimaatsommen
Met klimaatsommen wordt een set van [18 stochasten](..\3_achtergronden_en_uitgangspunten\g_achtergrond_klimaatsommen\1_achtergrond_klimaatsommen.md) bedoeld waarmee het watersysteem op extreme neerslag wordt getoetst. De modellen zijn zo ingesteld dat neerslag via het maaiveld zijn weg moet zoeken naar het watersysteem. Infiltratie is ingesteld en er zijn drie [modelstaten](..\4_gebruik_plugin\d_modelstaat_aanpassen.md) met verschillende bodemberging (GLG/GGG/GHG). Uiteraard kan water vanuit het watersysteem op het maaiveld stromen. De resultaten van de klimaatsommen worden [opgewerkt](..\4_gebruik_plugin\j_werkwijze_klimaatsommen.md) tot drie inundatiekaarten bij T10/100/1000 en een kaart met de netto contante waarde van de schade.

## **Modellen**

### Modelvarianten

### Circulair modelleren
HHNK past sinds 2015 circulair modelleren toe. Bij circulair modelleren worden verbeteringen in gegevens bij de bron aangepast. Voor HHNK is dit de DAMO-database. Modellen worden direct uit de brongegevens opgebouwd. Hierdoor komen de verbeterde gegevens voor toekomstige modellen en andere toepassingen beschikbaar, in plaats van dat ze verloren gaan in een modelversie. Voor het controleren van de brongegevens en het automatisch opbouwen van modellen heeft HHNK samen met Nelen & Schuurmans een [datachecker](..\2_werkwijze_bwn\e_model_controleren_verbeteren\1_datachecker.md) en [modelbuilder](..\2_werkwijze_bwn\e_model_controleren_verbeteren\2_modelbuilder.md) ontwikkeld.

### Datacontrole

### Modellen maken

### Referentie- en maatregelmodellen
In het BWN2-project is sprake van referentiemodellen en maatregelmodellen. Zoals de naam doet vermoeden gaat het in de referentiemodellen om de referentie situatie; het watersysteem zoals dit er op dat moment in de praktijk bij ligt. Daarnaast zijn voor sommige polders modellen aangepast om maatregelen te testen of ruimtelijke ontwikkelingen te toetsen. Het is belangrijk om onderscheid te blijven maken tussen deze typen modellen. De referentiemodellen zijn de onderligger voor de toetsing en vertrekpunt voor nieuwe projecten of vragen. Deze modellen zijn met revisienummer en modelleur opgeslagen in het modellenregister.

### HHNK 3Di plugin


De hoofdstukken hieronder beschrijven de werkwijze stap voor stap.

* [Werkafspraken](a_werkafspraken/werkafspraken.md)<br>
* [Nieuw model](c_nieuw_model/1_nieuw_model.md)
* [Bestaand model aanpassen en uploaden](d_bestaand_model_aanpassen_uploaden/1_bestaand_model_aanpassen_uploaden.md)
* Model controleren en verbeteren:<br>
    1. [Datachecker](e_model_controleren_verbeteren/1_datachecker.md)
    2. [Modelbuilder feedback](e_model_controleren_verbeteren/2_modelbuilder_feedback.md)
    3. [Sqlite checks](e_model_controleren_verbeteren/3_sqlite_checks.md)
    4. [0d1d test](e_model_controleren_verbeteren/4_0d1d_test.md)
    5. [Banklevel test](e_model_controleren_verbeteren/5_banklevel_test.md)
    6. [1d2d test](e_model_controleren_verbeteren/6_1d2d_test.md)
* [Hydraulische toets](..\2_werkwijze_bwn\f_hydraulische_toets\1_hydraulische_toets.md)
* [Klimaatsommen](..\2_werkwijze_bwn\g_werkwijze_klimaatsommen\1_werkwijze_klimaatsommen.md)
* [Maatregel of scenariomodel](..\2_werkwijze_bwn\h_maatregel_of_scenariomodel\1_maatregel_of_scenariomodel.md)


[Introductie QGIS plugin](b_introductie_qgis_plugin/1_introductie_qgis_plugin.md)
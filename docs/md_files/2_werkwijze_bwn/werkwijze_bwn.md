# **Werkwijze BWN2**
Voor het programma BWN2 zijn modellen en een werkwijze opgesteld. Het doel hiervan is om alle polders binnen HHNK op eenduidige manier te toetsen op mogelijke wateroverlast. Deze toetsing is uitgevoerd tussen 2015 en 2020, maar kan periodiek worden herhaald of wanneer (ruimtelijke) ontwikkelingen plaatsvinden. Door deze werkwijze te volgen zijn eveneens eenduidige vergelijkingen te maken tussen referentie en maatregel of ontwikkel scenarios. 

## **Hydraulische toets en klimaatsommen**
BWN2 toetst het watersysteem op twee manieren, ten eerste middels de hydraulische toets (HT) en via klimaatsommen.

### Hydraulische toets
In de HT wordt getoetst of het watersysteem voldoende kan afvoeren onder normale omstandigheden. Dat wil zeggen dat het watersysteem maximaal af moet kunnen voeren zonder dat er knelpunten of wateroverlast ontstaat. De maximale afvoer is voor polders vastgelegd in de afvoernorm (meestal 14,4 mm/dag of 10 m3/min/100ha, in grote polders soms 9 of 8 m3/min/100ha). In deze afvoersituatie mag de opstuwing in peilgebieden (~30cm) of verhang in watergangen (~2-4 cm/km) niet boven bepaalde grenswaarden uitkomen. Ook duikers mogen niet te veel opstuwing geven (~1cm). De genoemde waarden zijn afhankelijk van gebiedseigenschappen. 

De resultaten van opstuwing en verhang worden via kaarten gedeeld met de watersysteem-adviseurs. Ze worden gebruikt voor het identificeren van maatregelen en zijn  input voor de leggertool. Met de leggertool worden minimale profielen van watergangen voor afvoer vastgesteld.

### Klimaatsommen
Met klimaatsommen wordt een set van [18 stochasten](..\3_achtergronden_en_uitgangspunten\g_achtergrond_klimaatsommen\1_achtergrond_klimaatsommen.md) bedoeld waarmee het watersysteem op extreme neerslag wordt getoetst. De modellen zijn zo ingesteld dat neerslag via het maaiveld zijn weg moet zoeken naar het watersysteem. Infiltratie is mogelijk en er zijn drie [modelstaten](..\4_gebruik_plugin\d_modelstaat_aanpassen.md) met verschillende bodemberging (GLG/GGG/GHG). Uiteraard kan water vanuit het watersysteem op het maaiveld stromen. De resultaten van de klimaatsommen worden [opgewerkt](..\4_gebruik_plugin\j_werkwijze_klimaatsommen.md) tot drie inundatiekaarten bij T10/100/1000 en een kaart met de netto contante waarde van de schade.

### Wateroverlast versus plasvorming
In de resultaten wordt onderscheid gemaakt tussen wateroverlast en plasvorming. Wateroverlast treedt daar op waar inundatie vanuit de watergang plaatsvind of wanneer afvoer vanaf het maaiveld niet mogelijk is door verhoogde waterstanden in de watergangen. Plasvorming zijn die plaatsen waar plassen op het maaiveld ontstaan als gevolg van neerslag die niet af kan stromen.

Dit onderscheid helpt modelleurs en beleidsmakers bij het bepalen van de oorzaak van wateroverlast en daarmee bij het vinden van effectieve maatregelen.

## **BWN2-Modellen**
Voor de toetsing gebruikt HHNK 3Di modellen. [3Di](https://3diwatermanagement.com/) is hydrodynamische modelsoftware waarmee zowel 1D (watergangen, riolering) als 2D (maaiveld) of 1D-2D gerekend kan worden. HHNK heeft de modellen of schematisatie specifiek ontworpen voor de hierboven beschreven doelen. De modellen bestaan uit:
* alle watergangen en kunstwerken in een 1D watersysteem,
* een maaiveldmodel gebaseerd op o.a. het AHN in het 2D rekendomein,
* ruimtelijk variabele bodemwrijving in het 2D rekendomein, 
* een vereenvoudigde bodem middels ruimtelijk variabele infiltratiesnelheid en maximale bodemberging, en
* koppeling tussen het 1D watersysteem en het 2D maaiveld.

De modellen zijn opgedeeld in ca. 55 clusters die samen alle ca. 225 polders van HHNK bevatten. De ruimtelijke resolutie van de rasters en daarmee de resulterende inundatiekaarten is 50x50cm.  

Riolering in stedelijk gebied is sterk vereenvoudigd meegenomen in de infiltratie en bodembergingsrasters.

### Modelvarianten
Voor het testen van de schematisatie, de hydraulische toets en de klimaatsommen gebruikt HHNK vijf verschillende varianten van de modellen:
1. Het 0d1d test model. <br>
    Dit model wordt ook gebruikt voor de HT en heeft een 0D inloop-component. Alle neerslag (~14,4 mm/dag) gaat hiermee geforceerd het watersysteem in moet zo worden afgevoerd. Zo wordt dus alleen het watersysteem getoetst. De resultaten van de [0d1d_test](../4_gebruik_plugin/g_0d1d_test.md) worden gebruikt voor de hydraulische toets (mits de modelleur tevreden is met het functioneren van het model). 
2. Het 1d2d test model.<br>
    Dit model bevat het 1D watersysteem en het 2D maaiveld, maar geen infiltratie. Het dient  voor de [1d2d test](../4_gebruik_plugin/i_1d2d_test.md).
3. Drie 1d2d GXG modellen.<br>
    Deze modellen bevatten alle hierboven genoemde componenten, met voor de bodembergings drie verschillende initieel beschikbare [bodemberging](../3_achtergronden_en_uitgangspunten/e_onderliggende_rasterdata/1_onderliggende_rasterdata#rasterkaart-bodemberging) rasters, voor GLG, GGG en GHG. Ze worden gebruikt voor de [klimaatsommen](#klimaatsommen).

### Referentie- en maatregelmodellen
In het BWN2-project is sprake van referentiemodellen en maatregelmodellen. Zoals de naam doet vermoeden gaat het in de referentiemodellen om de referentie situatie; het watersysteem zoals dit er op dat moment in de praktijk bij ligt. Daarnaast zijn voor sommige polders modellen aangepast om maatregelen te testen of ruimtelijke ontwikkelingen te toetsen. Het is belangrijk om onderscheid te blijven maken tussen deze typen modellen. De referentiemodellen zijn de onderligger voor de toetsing en vertrekpunt voor nieuwe projecten of vragen. Deze modellen zijn met revisienummer en modelleur opgeslagen in het HHNK-3Di-modellenregister.

## Circulair modelleren
HHNK past sinds 2015 circulair modelleren toe. Bij circulair modelleren worden verbeteringen in gegevens bij de bron aangepast. Hierdoor komen de verbeterde gegevens voor toekomstige modellen en andere toepassingen beschikbaar, in plaats van dat ze verloren gaan in een modelversie. Modellen worden direct uit de brongegevens opgebouwd. Voor HHNK is dit de DAMO-database. 

Voor het controleren van de brongegevens en het automatisch opbouwen van modellen heeft HHNK samen met Nelen & Schuurmans een datachecker en modelbuilder ontwikkeld. Deze systemen gebruiken een export vanuit DAMO om op een groot aantal punten de gegevens te controleren. De controles richten zich erop dat vanuit de gegevens een valide 3Di model opgebouwd kan worden. Dit model noemen we het basismodel. De uitgangspunten hiervan zijn [hier](../3_achtergronden_en_uitgangspunten/achtergronden_en_uitgangspunten.md) te vinden.

## HHNK 3Di plugin
Na de automatische modelbouw wordt het model verder gecontroleerd door meerdere testberekeningen en checks uit te voeren. Deze zijn nader beschreven in de beschrijving van de [HHNK 3Di plugin](../4_gebruik_plugin/_introductie_plugin.md).

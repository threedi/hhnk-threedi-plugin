# **Bescherming Wateroverlast Noorderkwartier**
De afgelopen jaren heeft het hoogheemraadschap geïnvesteerd in de inrichting van het watersysteem om wateroverlast te beperken en het systeem aan de normen (NBW) te laten voldoen. Dit betekent echter niet dat er geen wateroverlast meer kan optreden. Het hoogheemraadschap wil daarom  samen met de omgeving in zetten op een verdere ontwikkeling naar een klimaatadaptieve leefomgeving, waarbij de bestrijding van wateroverlast zoals omschreven in het Deltaprogramma gezamenlijk wordt ingevuld. Om inzicht te verkrijgen in de gevolgen van de extreme neerslag is een modelonderzoek uitgevoerd. Binnen HHNK staat dit bekend als het BWN2-project (Bescherming Wateroverlast Noorderkartier).

Met 3Di-modellen zijn op een hoog detailniveau de waterstromen en inundaties berekend in de situatie nu en waar bekend is de effectiviteit van maatregelen getoetst. Deze handleiding beschrijft de werkwijze voor het maken en controleren van deze 3Di modellen, die binnen HHNK bekend staan als BWN2-modellen. Bij de werkwijze horen ook klimaatsommen en het verwerken van de modeluitkomsten tot inundatie en verwachte schade bij verschillende herhalingstijden. Deze stappen zijn grotendeels geautomatiseerd middels een door HHNK ontwikkelde plugin (voor QGIS/3Di Modeler Interface): HHNK 3Di plugin.

## **Referentie- en maatregelmodellen**
In het BWN2-project is sprake van referentiemodellen en maatregelmodellen. Zoals de naam doet vermoeden gaat het in de referentiemodellen om de referentie situatie; het watersysteem zoals dit er op dat moment in de praktijk bij ligt. Daarnaast zijn voor sommige polders modellen aangepast om maatregelen te testen of ruimtelijke ontwikkelingen te toetsen. Het is belangrijk om onderscheid te blijven maken tussen deze typen modellen. De referentiemodellen zijn de onderligger voor de toetsing en vertrekpunt voor nieuwe projecten of vragen. Deze modellen zijn met revisienummer en modelleur opgeslagen in het modellenregister.

## **Hydraulische toets en klimaatsommen**
Binnen de referentie of maatregelmodellen kan nog onderscheid gemaakt worden tussen het model voor de hydraulische toets (HT) en de modellen voor de klimaatsommen.

### Hydraulische toets
In de HT wordt getoetst of het watersysteem voldoende kan afvoeren onder normale omstandigheden. Dat wil zeggen dat het watersysteem maximaal af moet kunnen voeren zonder dat er knelpunten of wateroverlast ontstaat. De maximale afvoer is voor polders vastgelegd in de afvoernorm (meestal 14,4 mm/dag of 10 m3/min/100ha, in grote polders soms 9 of 8 m3/min/100ha). In deze afvoersituatie mag de opstuwing in peilgebieden (~30cm) of verhang in watergangen (~2-4 cm/km) niet boven bepaalde grenswaarden uitkomen. De genoemde waarden zijn afhankelijk van gebiedseigenschappen. Ook duikers mogen niet te veel opstuwing geven (~1cm). 

Het model dat hoort bij de HT heeft in 3Di een 0D inloop-component. Alle neerslag (14,4 mm/dag) gaat hiermee geforceerd het watersysteem in moet zo worden afgevoerd. Zo wordt dus alleen het watersysteem getoetst.

### Klimaatsommen


## **Circulair modelleren**

Dit document licht toe hoe de plugin te gebruiken, welke data benodigd is en achtergrondinformatie over de opbouw van de plugin. 

De handleiding is opgebouwd uit de volgende onderdelen:

- [Werkwijze BWN](../2_werkwijze_bwn/werkwijze_bwn.md)
- [Achtergronden en uitgangspunten](../3_achtergronden_en_uitgangspunten/achtergronden_en_uitgangspunten.md)
- [Gebruik plugin](../4_gebruik_plugin/gebruik_plugin.md)

## **Installatie HHNK 3Di plugin**
Klik [hier](../installatie/installatie_handleiding.md) om het stappenplan van de installatie van de plugin te doorlopen.

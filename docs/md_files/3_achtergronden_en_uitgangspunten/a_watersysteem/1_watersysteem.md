## Functioneren watersysteem
Eén van de belangrijkste controles voordat een model wordt gemaakt is of het watersysteem valide is. Dat wil zeggen of alle watergangen kunnen afvoeren naar een afvoergemaal of ander kunstwerk. Dit gaat in een aantal stappen, beginnend bij de modelgrenzen.

### Modelgrens
De modelleur kiest in de modelbuilder voor een regio waarvoor hij een model wil maken. Deze regio's zijn opgeslagen onder Polders_V4 in de [HDB](../f_inhoud_HDB/1_inhoud_HDB.md). In de datachecker zijn alle peilgebieden binnen deze gebieden samengevoegd tot poldercluster. Eigenlijk kies je daarom in de modelbuilder voor een poldercluster. De geometrie van de peilgebieden wordt gebruikt omdat deze wordt bijgehouden, die van polder niet. Zo liggen kunstwerken altijd op de grens van het model. 

### Afvoerkunstwerken
Alle kunstwerken op de grens van het model zijn vervolgens kandidaten om een afvoer kunstwerk te worden. Dit zijn gemalen of stuwen met de functie ```afvoer``` of ```aan- of afvoer``` en duikers die in de HDB zijn aangemerkt als ```op overstort```.

### Peilgrens zonder kunstwerk
Binnen de polders wordt gecontroleerd of op elke watergang die een peilgrens kruist een kunstwerk ligt die het peil kan regelen. Locaties waar dit niet zo is worden aangemerkt als fout en ```Kruising zonder kunstwerk``` genoemd.

Het kan zo zijn dat het kunstwerk op de kruising wordt afgekeurd, omdat het niet in staat is af te voeren. Als dit het geval is kan er alsnog een kruising zonder kunstwerk worden aangemaakt:

1. Duiker op peilgrens is afsluitbare inlaat  (type 1 of 2) en dus naar verwachting niet gebruikt voor afvoer
2. Stuw of gemaal zonder functie ```afvoer``` of ```aan- of afvoer```
3. Vispassages worden niet meegenomen als afvoerkunstwerk.

### Losliggende watergangen
Alle watergangen die helemaal los liggen (soms greppels, maar soms ook tekenfouten) worden verzameld in de laag ```channel_loose``` in de datachecker. 

### Verbondenheid watersysteem
De laatste controle is of alle watergangen binnen de modelgrenzen verbonden zijn met een afvoerkunstwerk (op de modelgrens). Watergangen binnen peilgebieden of peilafwijkingsgebieden die niet logischerwijs kunnen afvoeren worden aangemerkt als fout. Dat is het geval in de volgende gevallen:

1. Onderbemaling zonder gemaal,
2. Opmaling zonder stuw of duiker,
3. Laagste peilgebied van omliggende zonder gemaal, of
4. Hoogste peilgebied van omliggende zonder stuw of duiker.

Vervolgens worden watergangen met een kruising zonder kunstwerk ook weggelaten. Alle overgebleven watergangen worden samengevoegd mits ze verbonden zijn. De delen die nu niet kruisen met een afvoerkunstwerk, worden verzameld in de laag ```channel_nowayout```. 

De watergangen in beide lagen worden aangemerkt als fout en niet meegenomen in de modelbouw. Het spreekt voor zich dat deze lagen belangrijk zijn voor de controle van de inputgegevens.


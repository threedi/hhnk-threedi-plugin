## **Onderliggende rasterdata**
In de 3Di poldermodellen zitten de volgende 4 rasterkaarten:
1. DEM;
2. Weerstand;
3. Infiltratie;
4. Bodemberging.

Hoe deze kaarten zijn opgebouwd wordt hieronder beschreven..
Alle rasters bevatten waardes op subgridniveau (0,5 m bij 0,5 m) die door 3Di op een verantwoorde
manier worden opgeschaald tot de veel grotere rekencellen.

### **Maaiveldhoogte DEM**


DTM AHN3 

Fill nodata 

Panden BAG (versie 1-10-2017) opgedrukt, dmv: maaiveldhoogte 75%-percentiel rondom +5cm (update jan 2020, dit was 15cm) 

Watervlakken op 10 m NAP (uit 'actuele' BGT, sturen we mee) 

EPSG:28992 (RD New), afgeronde origin, rastergrootte, FLOAT32, nodata -9999 

### **Bodemwrijving/Weerstand**
De weerstandkaart heeft betrekking op de stroming over maaiveld en wordt uitgedrukt in Manning waarde die veel wordt toegepast voor het modelleren van ondiep water stroming. Hoe lager de Manningwaarde (s/m1/3) hoe lager de weerstand. In 3Di wordt de inverse Manningswaarde gebruikt en deze wordt ook wel de Stricklerwaarde genoemd (s/m1/3). Deze waarde wordt bepaald op basis van onderstaande voorwaardes.

Waterlopen
* 45-30: Zeer schoon;
* 35-20: Schoon;
* 25-15: Licht begroeid;
* 20-10: Matig begroeid;
* 16-5: Vrij sterk begroeid;
* <10: Zeer sterk begroeid;

Betonnen duikers
* 75-100: Duiker recht en schoon;
* 70-90: Duiker met bochten, verbindingen en enige verontreiniging;
* 55-75: Rioolbuis met mangaten, inlaten e.d. recht;
* 70-85: Niet afgewerkt bij stalen bekisting;
* 60-85: Niet afgewerkt bij gladde houten bekisting;
* 50-65: Niet afgewerkt bij ruwe houten bekisting;

Er wordt voorgesteld om de weestandskaart op te bouwen uit de BGT kaart en daarbij de volgende uitganspunten aan te houden:
* Wegdeel_v
* 
* 
* 
* 
* 

De weerstand die wordt gebruikt in de 3Di poldermodellen is in onderstaande figuur weergegeven.
De Stricklerwaarde voor de onderstaande kaart varieert tussen de 100 m1/3/s en de 17 m1/3/s. De
minste weerstand (100 m1/3/s) is toegekend aan watervlakken, agrarische percelen hebben een
weerstand van 33 m1/3/s, wegen 25,6 m1/3/s en de hoogste weerstand (17 m1/3/s) is toegekend aan
stedelijk gebied (wegen, huizen en erven) en fruitteelt (en natuur).


Conversie vanuit landgebruiksraster op basis van ' Conversietabel_landgebruik_2018.csv'. Raster wordt per model aangemaakt (voor zover Wouter weet staat deze niet in lizard). Eenheid in Manningsweerstand. 

### **Maximale infiltratiecapaciteit/Infiltratie**
Opgebouwd door Jeroen en geleverd aan N&S voor gebruik in modelbuilder. Voor methode zie: bijlagen in corsa stuk: 18.0035563 

### **Maximale bodemberging/Bodemberging**
Opgebouwd vanuit:  

PAWN bodemtypering,  

landgebruik 2018 voor verhard gebied, dit overschrijft PAWN typering met zand.

Bepalen ontwateringsdiepte met behulp van GLG, GHG, GGG (gemiddelde tussen GLG en GHG) en de AHN3. GXG zijn afkomstig landelijk model Alterra. In stedelijk gebied is de GLG en GHG niet (overal) beschikbaar, hier is daarom streefpeil gebruikt. Streefpeil moet een gebiedsbrede export uit 2017 zijn geweest. 

CAPSIM tabellen (uit SOBEK) voor vertalen bodemtyperingen en ontwateringsdiepte naar bodemberging. In deze tabellen zit de werking van de onverzadigde zone verwerkt. 

De drie bergingsrasters zijn opgeslagen als losse Geotifs die de modelbuilder per model uit knipt. 
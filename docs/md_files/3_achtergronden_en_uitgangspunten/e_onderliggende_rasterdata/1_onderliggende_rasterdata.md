## **Onderliggende rasterdata**
### **Maaiveldhoogte DEM**
DTM AHN3 

Fill nodata 

Panden BAG (versie 1-10-2017) opgedrukt, dmv: maaiveldhoogte 75%-percentiel rondom +5cm (update jan 2020, dit was 15cm) 

Watervlakken op 10 m NAP (uit 'actuele' BGT, sturen we mee) 

EPSG:28992 (RD New), afgeronde origin, rastergrootte, FLOAT32, nodata -9999 

### **Bodemwrijving**
Conversie vanuit landgebruiksraster op basis van ' Conversietabel_landgebruik_2018.csv'. Raster wordt per model aangemaakt (voor zover Wouter weet staat deze niet in lizard). Eenheid in Manningsweerstand. 

### **Maximale infiltratiecapaciteit**
Opgebouwd door Jeroen en geleverd aan N&S voor gebruik in modelbuilder. Voor methode zie: bijlagen in corsa stuk: 18.0035563 

### **Maximale bodemberging**
Opgebouwd vanuit:  

PAWN bodemtypering,  

landgebruik 2018 voor verhard gebied, dit overschrijft PAWN typering met zand. 

Bepalen ontwateringsdiepte met behulp van GLG, GHG, GGG (gemiddelde tussen GLG en GHG) en de AHN3. GXG zijn afkomstig landelijk model Alterra. In stedelijk gebied is de GLG en GHG niet (overal) beschikbaar, hier is daarom streefpeil gebruikt. Streefpeil moet een gebiedsbrede export uit 2017 zijn geweest. 

CAPSIM tabellen (uit SOBEK) voor vertalen bodemtyperingen en ontwateringsdiepte naar bodemberging. In deze tabellen zit de werking van de onverzadigde zone verwerkt. 

De drie bergingsrasters zijn opgeslagen als losse Geotifs die de modelbuilder per model uit knipt. 
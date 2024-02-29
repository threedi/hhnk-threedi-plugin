## **Duikers**
### **Algemeen**
Duikers moeten gekoppeld kunnen worden aan een watergang. De onderliggende watergang wordt alleen verwijderd als het een kruising zonder kunstwerk oplevert. 

In sommige gevallen worden duikers gemodelleerd als orifice. Tijdens het project hebben we meermaals last gehad van instabiliteit rondom korte duikers. Voor lange duikers is het echter van belang de weerstand als gevolg van de wand mee te nemen, dit gebeurt niet bij de orifice in 3Di.

Alle duikers zijn gemodelleerd volgens de volgende stappen:
1.	Duikers korter dan 10 m als korte overlaten (orifice) met discharge coëfficiënt op 1.0

2. Lange overlaat (orifice) met discharge coëfficiënten op 1.0, mits:

	a.	Duiker breedte of diameter is factor 3 kleiner dan breedte watergang op streefpeil, en

	b.	Duiker is korter dan 25m, en

	c.	Het verschil tussen de bob beneden- en bovenstrooms is kleiner dan 10 cm.

3.	Alle andere duikers (lang, breed of schuin) als culvert maar toevoegen 1m2 storage op begin en eind node daar waar dat nog niet het geval is.

Duikers aan een stuw of gemaal worden niet in het model opgenomen. De stuw of het gemaal vormen dan de verbinding die de duiker representeert.

### **Afmetingen**
De afmetingen van een duiker worden overgenomen uit DAMO (VORMKOKER, HOOGTEOPENING en BREEDTEOPENING). 
Indien er geen data beschikbaar is wordt er een waarde aangenomen van rond de 0.5 meter, bob op streefpeil minus duikerhoogte.


### **Duikers op een peilgrens**
In de afbeelding hieronder wordt met behulp van een blokkenschema uitgelegd hoe duikers die op een peilgrens liggen in het model worden meegenomen.
![Alt text](../../../images/3_achtergronden_en_uitgangspunten/Duikers_op_peil(afwijking)grens.png)

### **Sifons**
Sifons worden opart behandeld (ze doorlopen niet bovenstaande schema) omdat ze (vrijwel) altijd op een peilgrens liggen. Ze worden uit de schematisatie gehaald samen met het hydroobject waar ze op liggen. Bij duikers wordt het deel van een hydroobject dat onder de duiker ligt weg geknipt om ruimte te maken voor de duikers. Bij sifons kan dit niet, omdat die altijd nog een hydroobject kruist. Sifons moeten daarom exact (gesnapt en even lang) op het onderliggende hydroobject liggen voor een correcte weergave in het model.

### **Coëfficienten**
De discharge coefficient van een duiker is 1.0 in het geval dat de duiker open staat. Indien het om een inlaat op een peilgrens gaat, wordt aangenomen dat de duiker is afgesloten en is de discharge coefficient gelijk aan 0. Dit wordt ook weergegeven in de afbeelding onderaan deze pagina.

Voor sommige duikers is tijdens het modelleren gekozen om de stroming in een richting open te zetten en de andere dicht te houden. Hiermee kunnen waterbergingen gevuld worden zonder complexere sturing, of uitgelaten op de boezem (met vaste waterstand) als de waterstand in de polder hoger is dan de boezem.
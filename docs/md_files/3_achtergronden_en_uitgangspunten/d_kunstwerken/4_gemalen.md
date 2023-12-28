## **Gemalen**
### **Capaciteit**
De capaciteit wordt bepaald door gebruik te maken van onderstaande volgorde. Dit vormt tevens de rangorde voor prioritering bij het opnemen van de capaciteit in het model. Een capaciteit van 0 betekent dat de capaciteit 0 is. Een capaciteit van null betekent dat de capaciteit niet is ingevuld en dat er een aanname volgt (stap 3). 

1. Als de functie '904/98 doorspoelpomp', '1 aanvoergemaal' of '3 opmaling' is: 0 m3/s. 
2. Als de functie '2 afvoergemaal', '4 onderbemaling', 'aan- en afvoergemaal' of 'op- en onderbemaling' is:  

    a. Zoals in DAMO onder MAXIMALECAPACITEIT 

    b. (waarbij 0=0≠null) 
3. Niet ingevuld (null): Aanname

    a. Primair: 25 m3/min 
    
    b. Secundair: 1 m3/min 

Let hierbij op dat de capaciteiten in DAMO weergegeven worden in m3/min en in de model-sqlite in l/s.

### **Richting**
De richting waarin gemalen het water pompen is van laag peil naar hoog peil op basis van het initiële water level van de connection nodes.

### **Aan- en afslagpeilen**
Het aan- en afslagpeil is gebaseerd op het streefpeil lage zijde (afvoeraanname). Dit gaat niet goed bij aanvoer-gemalen, maar omdat die een capaciteit van 0 meekrijgen heeft dit geen effect in de modellen. Het aanslagpeil is gelijk aan het streefpeil+0.02m en het afslagpeil is gelijk aan het streefpeil-0.03m.
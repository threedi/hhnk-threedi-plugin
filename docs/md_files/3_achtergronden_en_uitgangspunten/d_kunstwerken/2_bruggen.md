## **Bruggen**
### **Breedte**
De breedte wordt in de FME-export bepaalt aan de hand van de kolom BREEDTEOPENING in de laag DOORSTROOMOPENING uit DAMO. Er kunnen meerdere doorstroomopeningen per brug aanwezig zijn. In FME worden deze opgeteld en weergegeven in de laag BRUG in kolom `Som_doorstroomopeningen`. In de modellen worden meerdere openingen dus samengevoegd.

Als er een doorstroombreedte bekend is en die breedte valt tussen een range van 0.5 meter tot 50 meter, dan is de breedte van de brug gelijk aan de doorstroombreedte. Anders wordt voor primair  20.02 meter aangenomen en voor secundair 10.01 meter.

### **Diepte**
De diepte van bruggen staat niet in de basisgegevens. Deze wordt aangenomen op basis van de waterdiepte. In de datachecker wordt nu, waar beschikbaar, de getabelleerde bodemhoogte meegenomen. Na het toepassen van de ingemeten profielen op de watergang wordt bij iedere brug (v2_orifice met code: KBR*) op beide connection nodes gekeken wat de laagste bodemhoogte van de aangesloten kanalen is. Deze bodemhoogte+1cm wordt meegegeven aan de bruggen. Aan het einde van de routine wordt de bodemhoogte van kanalen naar BOB/crest_level-1cm gezet indien deze gelijk of hoger was dan de BOB/crest_level. 

Het verlagen van de watergangen aan de hand van kunstwerken vindt plaats aan het einde van de modelbuilder routine om er voor te zorgen dat het model goed rekent. Als een brug is verlaagd n.a.v. de laagste watergang, wordt dit doorgetrokken naar de hogere watergang. Dit vindt dus plaats nadat de bruggen zijn verlaagd naar waterganghoogte. 

### **Doorstroomhoogte**
Als de diepte van de waterloop ter plaatse van een brug is aangepast naar bodemhoogte van de watergang berekent de modelbuilder de doorstroomhoogte opnieuw met de HOOGTEONDERZIJDE van de brug uit DAMO. Hiervoor geldt een minimale doorstroomhoogte van 1 meter. Bij geen ingevulde waarde in DAMO komt de bovenkant van het profiel op NAP +10,01 meter.

### **Coëfficiënten**
De discharge coefficient voor een brug is 1. Dit betekent dat met brug de discharge even groot is als zonder brug en de waterstroom dus niet gehinderd wordt door de brug. 

In 3Di worden wel energie verliezen meegenomen voor het smaller of breder worden van het stroomprofiel.
## **Bruggen**
### **Breedte**
Als er geen doorstroombreedte bekend is bij een brug of de breedte valt buiten de range van 0.5 tot 50 meter nemen we de volgende waarden aan: 

Primaire bruggen: 20.02 m 

Secundaire bruggen: 10.01 m 

### **Diepte**
De diepte van bruggen leveren we niet mee. Deze wordt aangenomen op de waterdiepte. In de datachecker wordt nu waar beschikbaar de getabelleerde bodemhoogte meegenomen. Na het toepassen van de ingemeten profielen op de watergang wordt bij iedere brug (v2_orifice met code: KBR*) op beide connection nodes gekeken wat de laagste bodemhoogte van de aangesloten kanalen is. Deze bodemhoogte+1cm wordt meegegeven aan de bruggen. Aan het einde van de routine wordt net als voorheen de bodemhoogte van kanalen naar BOB/crest_level-1cm gezet indien deze gelijk of hoger was dan de BOB/crest_level. 

Het verlagen van de watergangen aan de hand van kunstwerken vindt plaats aan het einde van de modelbuilder routine om er voor te zorgen dat het model goed rekent. Dit vindt dus plaats nadat de bruggen zijn verlaagd naar waterganghoogte. Het klopt dus wat je zegt in punt 1, dat als de brug is verlaagd n.a.v. de laagste watergang dit door wordt getrokken naar de hogere watergang. 

### **Doorstroomhoogte**
Als de diepte van de waterloop ter plaatse van een brug is aangepast naar bodemhoogte van de watergang berekent de modelbuilder de doorstroomhoogte opnieuw met de HOOGTEONDERZIJDE van de brug uit DAMO. Hiervoor geldt een minimale doorstroomhoogte van 1 meter. Bij geen ingevulde waarde in DAMO komt de bovenkant van het profiel op NAP +10,01 meter.

### **Coefficienten**
De discharge coefficient pog/neg = 1
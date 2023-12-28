## **Watergangen**
De HydroObjecten uit DAMO vormen de basis voor de watergangen in het model. De Hydroobjecten worden allen samengevoegd en vervolgens opgeknipt op alle kruispunten. Alle watergangen liggende binnen het modelgebied en zonder [fouten](../a_watersysteem/1_watersysteem.md) verbonden met het afvoergemaal of stuw komen in het model. 

Duikers worden vervolgens op basis van hun ligging uit de watergangen geknipt. 
Andere kunstwerken worden met een lengte van 5m uit de watergangen geknipt, omdat in dit in 3Di verbindingen tussen twee punten moeten zijn. Als hierdoor hele korte segmenten ontstaan worden kunstwerken iets opgeschoven.
Alle watergangen die overblijven komen als v2_channel in het model en krijgen aan het begin een eindpunt een connection node en ten minste één [dwarsprofiel](4_profiel.md).
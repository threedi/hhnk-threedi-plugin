## **Watergangen en kunstwerken**
De HydroObjecten uit DAMO vormen de basis voor de watergangen in het model. De hydroobjecten worden allen samengevoegd en vervolgens opgeknipt op alle kruispunten. Hierdoor zijn de watergangen uit het model niet zonder bewerking terug te herleiden naar een DAMO hydroobject.
Alle watergangen liggende binnen het modelgebied en zonder [fouten](../a_watersysteem/1_watersysteem.md) verbonden met het afvoergemaal of stuw komen in het model.

Watergangen lopen in DAMO door onder kunstwerken en hebben een (deels) overlappende geometrie met duikers. Duikers worden daarom vervolgens uit de watergangen geknipt. 
Bij andere kunstwerken wordt de puntgeometrie omgezet in lijnen en met een lengte van 5m uit de watergangen geknipt, omdat in dit in 3Di verbindingen tussen twee punten moeten zijn. Als hierdoor hele korte segmenten ontstaan worden kunstwerken iets opgeschoven.
Alle watergangen die overblijven komen als v2_channel in het model en krijgen aan het begin een eindpunt een connection node en ten minste één [dwarsprofiel](4_profiel.md).
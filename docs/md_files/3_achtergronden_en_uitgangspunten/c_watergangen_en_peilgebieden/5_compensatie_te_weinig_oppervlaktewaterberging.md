## **Compensatie te weinig oppervlaktewaterberging**
De berging in 1D (connection nodes + profielen watergangen) wordt per peilgebied vergeleken met het oppervlak van de BGT-waterdelen (vlakken). Een tekort aan berging wordt gelijk verdeeld toegekend als bergingsoppervlak aan secundaire connection nodes.

De berging kan berekend worden met de volgende formule.

Berging in profielen = 	profielbreedte 1 x lengte 1 + gemiddelde profielbreedte 1&2 x lengte 2	+ profielbreedte 2 x lengte 3  

![Alt text](../../../images/3_achtergronden_en_uitgangspunten/berging_in_profielen.png)

Bij het berekenen van de 1D-berging in het profiel wordt minder dan 2 m2 per connection node niet toegekend (en vervalt dus), om instabiliteit te voorkomen. Het is niet bekend hoe groot dit risico op instabiliteit is. 
Daarnaast wordt een bergingsoverschot niet gecorrigeerd. Er kan geen negatieve berging worden toegekend. In dit geval moeten profielen worden gecorrigeerd. 

In de plugin geeft een van de [sqlight tests](../../4_gebruik_plugin/c_sqlite_checks.md#eenmalige-testen) de overschatting van wateroppervlakte op streefpeil weer per peilgebied. Na het uitvoeren van de checks en [inladen van de lagen](../../4_gebruik_plugin/b_project_starten.md#4-gegevens-bekijken) kan deze kaart via [map theme](../../4_gebruik_plugin/b_project_starten.md#5-map-themes) ``SQLight test: Verschil oppervlaktewater`` bekeken worden.
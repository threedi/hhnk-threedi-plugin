## **Compensatie te weinig oppervlaktewaterberging**
De BWN-modellen bevatten zowel 2D maaiveld als 1D watergangen. Om te voorkomen dat op watergangen die in 1D gemodelleerd zijn ook op het 2D berging en stroming kan plaatsvinden, wordt in het 2D maaiveld op NAP +10 m gezet. Het kan echter toch nog voorkomen dat de berging in 2D verschilt van het 1D, bijvoorbeeld door aannames in profielen. Op basis van onderstaande controle kan dit worden gecorrigeerd. De controle wordt uitgevoerd op basis van het basismodel (uit de modelbuilder), de modelleur dient bij wijzigingen in het model zelf rekening te houden met de verschillen tussen 1D en 2D.

De berging in 1D (connection nodes + profielen watergangen) wordt per peilgebied vergeleken met het oppervlak van de BGT-waterdelen (vlakken). Een tekort aan berging wordt gelijk verdeeld toegekend als bergingsoppervlak aan secundaire connection nodes.

De berging kan berekend worden met de volgende formule.

Berging in profielen = 	profielbreedte_1 x lengte_1 + gemiddelde profielbreedte 1&2 x lengte_2	+ profielbreedte_2 x lengte_3  

![Alt text](../../../images/3_achtergronden_en_uitgangspunten/berging_in_profielen.png)

Bij het berekenen van de 1D-berging in het profiel wordt minder dan 2 m2 per connection node niet toegekend (en vervalt dus), om instabiliteit te voorkomen. Het is niet bekend hoe groot dit risico op instabiliteit is. 
Daarnaast wordt een bergingsoverschot niet gecorrigeerd. Er kan geen negatieve berging worden toegekend. In dit geval moeten profielen worden gecorrigeerd. 

In de plugin geeft een van de [sqlite tests](../../4_gebruik_plugin/c_sqlite_checks.md#eenmalige-testen) de overschatting van wateroppervlakte op streefpeil weer per peilgebied. Na het uitvoeren van de checks en [inladen van de lagen](../../4_gebruik_plugin/b_project_starten.md#4-gegevens-bekijken) kan deze kaart via [map theme](../../4_gebruik_plugin/b_project_starten.md#5-map-themes) `sqlite test: Verschil oppervlaktewater` bekeken worden.
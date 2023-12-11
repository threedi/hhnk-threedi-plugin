## **Profiel**
Het profiel wordt bepaald door gebruik te maken van onderstaande volgorde. Dit vormt tevens de rangorde voor prioritering bij het opnemen van het profiel in het model. Voor het bepalen van het profiel worden alleen dieptemetingen aan de bovenkant van de baggerlaag (Z2) gebruikt in plaats van dieptemetingen bij de harde bodem (Z1). Ook worden er alleen 'natte' dieptemetingen gebruikt om dubbele berging en stroming op het droge talud te voorkomen.  

1. Gemeten profielen uit DAMO *
    * a. GW_PBP 
    * b. GW_PRO 
    * c. GW_PRW 
    * d. IWS_GEO_BESCHR_PROFIELPUNTEN 
2. Zelf afgeleide profielen o.a. uit BGT. 
    * a. In kolommen HydroObject (zelf toegevoegd) 
        * i. breedte_getabuleerd (text) (nog te doen: dit opnemen in kolom DAMO HydroObject BREEDTE) 
        * ii. hoogte_getabuleerd (text) volgens tabel hieronder (Waterdiepte bij verschillende grondsoort) 
            1. alleen positieve getallen en punt als scheidingsteken 
            2. gelijk aantal breedtes en hoogtes 
        * iii. bodemhoogte_NAP (double) 
        * iv. keuze_profiel (text) (de bron van bovenstaande) 
3. Leggerprofielen uit DAMO **
    * a. In kolommen HydroObject: 
        * i. WS_BODEMBREEDTE 
        * ii. WS_BODEMHOOGTE 
        * iii. WS_TALUD_LINKS 
        * iv. WS_TALUD_RECHTS 
        
         ![Alt text](../../../images/3_achtergronden_en_uitgangspunten/Tabel_profiel.png)
4. Aanname volgens uitgangspuntennotitie N&S (primair: streefpeil – 1.0m, secundair: streefpeil – 0.5m)
5. Aanname bodemhoogte: NAP -10m 

*Voordat de gemeten DAMO-profielen aangeleverd zijn, zijn ze gefiltreerd op:
* Datachecker crossprofile hoogte mag niet 0,0 zijn 
* Datachecker crossprofile diepte mag niet <0,3m 
* Datachecker crossprofile breedte mag niet <2m 
* Datachecker crossprofile aantal punten mag niet <5
* Continuïteit x-richting profielpunten
* Profiel moet wel koppelbaar zijn met watergang (moet hydroobject_id hebben) 
* Profiel moet in gebied liggen met streefpeil in DAMO 

<span style="color:yellow"> *LN: @Wouter en @Jelle, To do: Leeftijd 2009 en jonger. Is dit inmiddels al doorgevoerd?*</span>

**De leggerprofielen worden omgerekend volgens:
Bodembreedte = breedte_op_streefpeil-((streefpeil tov NAP - bodemhoogte tov NAP)*(talud_links+talud_rechts)).

De bed_level in een watergang wordt bepaald door onderstaande volgorde:
1. De legger ws_bodemhoogte van hydroobject.
2. Aanname primaire watergangen: streefpeil - 1m indien geen bodemhoogte bekend OF streefpeil-bodemhoogte heeft onrealistische waarde (< 0.2 meter of > 20 meter) (tenzij hellend gebied, dan geld deze laatste check niet).
3. Zelfde als 2 maar voor niet primaire watergangen: streefpeil - 0.5 meter. In hellend gebied wordt hij 10.5 meter onder streefpeil gezet bij ontbrekende waarde, ik weet niet zeker of dit met reden is of dat hier spraken is van een typefout. 
4. -10 meter indien nog steeds niets is ingevuld.

De bed_level van een dwarsprofiel wordt bepaald door de profielen en worden apart gecontroleerd.

<span style="color:yellow"> *LN: @Wouter en @Jelle, de hieronderstaande informatie is een gedeelte van hoe het geïmplementeerd is in het model. Het is dus niet compleet. Zijn er belangrijke punten die nog missen?*</span>

Hoe dit uiteindelijk allemaal wordt toegevoegd aan het model is een zeer verweven proces. Enkele onderdelen hiervan zijn hieronder beschreven. 
1. De gemeten profielen worden toegewezen aan watergangen op basis van de channel-linemerge laag uit de datachecker. Zo worden de gemeten profielen over een aantal kruispunten en kunstwerken heen getild. Er wordt vanuit gegaan dat het profiel van (bijvoorbeeld) de primaire watergang niet wijzigt over het kruispunt met een secundaire watergang. Het kan voorkomen dat een profiel door deze methodiek over een peilgrens heen wordt getrokken. Profielen worden tot maximaal 250 meter buiten de waterloop geëxtrapoleerd. 
<span style="color:yellow"> *LN: @Wouter en @Jelle, Dit komt uit april 2019, is dit nog steeds zo?*</span>
2. De referentiehoogte wordt bepaald aan de hand van het gemeten/BGT/legger profiel of aanname. De bodemhoogte wordt berekend als een diepte onder streefpeil. Als een profiel over een peilgrens heen wordt getrokken zorgt dit ervoor dat de juiste diepte gebruikt wordt. De bodemhoogte wordt indien aanwezig verlaagd naar de minimale stuwhoogte en/of actiewaarde. 
3. De referentiehoogtes zijn veelal verlaagd ivm de kruinhoogte van de orifices. Deze aanpassing kan je terugvinden in de feedback folder van de modelbuilder in de laag model_feedback.shp. 
4. Er wordt gecontroleerd of de bodemhoogte lager ligt dan het afslagpeil van een gemaal.
## **Resultaten downloaden**
Naast het starten van simulaties, is het downloaden van de resultaten van de (test)berekeningen mogelijk middels het notebook. Hieronder is toegelicht hoe dat in zijn werk gaat:

1. Om een simulatie te downloaden, kun je het beste gebruik maken van de meest recente versie van ``xx_download_gui_vx``. Door te dubbelklikken op de nieuwste versie, word je doorgestuurd naar het volgende scherm:

   ![](../images/usage/notebook_download_simulation_1.png)

2. Doorloop nu de eerste stap door ergens te klikken in het veld met ``#imports`` en vervolgens crtl + enter. Dit levert het onderstaande invoerscherm op:

   ![](../images/usage/notebook_download_simulation_2.png)

3. Loop vervolgens stap voor stap de volgende punten af:

   1. ``Login with API keys``: voer hier de Lizard API key in
   2. ``Search for simulation on lizard``: typ de naam van de te downloaden simulatie in en klik vervolgens op ``search``
   3. ``Select simulation results``: hier komt een overzicht te staan met de simulaties die overeenkomen met de zoekterm ingevoerd in stap 2. Selecteer de de simulatie of simulaties die je wil downloaden
   4. ``Select filetype``: selecteer hier welke ``File results`` en ``Raster results`` gedownload moeten worden. <br>
      ``File results``: <br>
      * raw 3Di output (.nc): bevat de resultaten van de simulatie (noodzakelijk) <br>
      * aggregated 3Di output (.nc): bevat verschillende tijdstappen van de resultaten van de simulatie (noodzakelijk) <br>
      * grid administration (.h5): ? <br>
      * calculation core logging (.txt): bevat verschillende bestanden met informatie over simulatie 

      ``Raster results``: <br>
      * Max water level: dit raster bevat de maximale waterstand (m NAP) over de gehele simulatieduur <br>
      * Max water depth: dit raster bevat de maximale waterdieptes (m) over de gehele simulatieduur <br>
      * Total damage: dit raster bevat de berekende schade als gevolg van inundatie <br>
      * Water level at selected time: dit raster bevat de waterstand op een gekozen tijdstip <br>
      * Water depth at selected time: dit raster bevat de waterdiepte op een gekozen tijdstip <br>
      * Depth (damage calc): ? 
   5. ``Select output folder/name``: kies hier de ``Sub folder`` waar de resultaten weggeschreven moeten worden 
   6. ``Download selected``: hier kun je kiezen uit een aantal opties:<br>
      a. DEM extent: laat deze aangevinkt als je het DEM als extent wil gebruiken en vink deze uit als je dat niet wil<br>
      b. Timestep raster: hier kan gekozen worden om voor een bepaald tijdstip een raster te downloaden. Als hier niets wordt gekozen, zal de laatste tijdstap worden gedownload <br>
      ##### klopt de tekst bij b? Met name de laatste zin
      c. Resolution (m): voer hier de gewenste resolutie van het te downloaden raster in <br>
   Klik vervolgens op ``Download`` om de resultaten te downloaden
   7. ``Download klimaatsommen``: deze wordt alleen gebruikt voor het downloaden van klimaatsommen. Bij deze stap zijn twee invoervelden: <br>
      a. Locatie DEM: voer hier de locatie in van de DEM die bij te downloaden resultaten hoort. Deze verschijnt als het goed is automatisch bij het klikken op het veld <br>
      b. Naam van de batch folder (maak aan als niet bestaat!): kies hier de folder waar de resultaten weggeschreven moeten worden. Bijvoorbeeld: als je de resultaten van de ``ggg`` situatie wil downloaden, kies je hier ook voor de batch folder ``ggg`` <br>
      Klik vervolgens op ``Download batch`` om een batch te downloaden
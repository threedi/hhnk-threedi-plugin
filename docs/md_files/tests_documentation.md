# Uitleg tests en functionaliteit

Op deze pagina vind je de inhoudelijke uitleg van de HHNK Toolbox checks en de functionaliteit.

- [Uitleg tests en functionaliteit](#uitleg-tests-en-functionaliteit)
      - [01\_source\_data](#01_source_data)
        - [DIT LIJKT OOK VERANDERD TE ZIJN. WAT IS MINIMAAL NODIG? \> actie voor Wietse om dit te verduidelijken](#dit-lijkt-ook-veranderd-te-zijn-wat-is-minimaal-nodig--actie-voor-wietse-om-dit-te-verduidelijken)
        - [Wat is minimaal nodig voor tests? \> Actie voor Wietse](#wat-is-minimaal-nodig-voor-tests--actie-voor-wietse)
      - [Modelbuilder output](#modelbuilder-output)
    - [ Duikers als orifice](#-duikers-als-orifice)
      - [02\_schematisation:](#02_schematisation)
      - [03\_3di\_results](#03_3di_results)
      - [04\_test\_results](#04_test_results)
    - [```QGIS``` project](#qgis-project)
  - [Modelstaat aanpassen](#modelstaat-aanpassen)
        - [IK ZIE DEZE TABEL NERGENS?](#ik-zie-deze-tabel-nergens)
        - [IK ZOU ONDERSTAANDE GRAAG EEN KEER UITGELEGD KRIJGEN](#ik-zou-onderstaande-graag-een-keer-uitgelegd-krijgen)
  - [Sqlite checks  WE: *Nu begint de test documentatie pas? Indeling niet handig.*](#sqlite-checks--we-nu-begint-de-test-documentatie-pas-indeling-niet-handig)
    - [Data verificatie](#data-verificatie)
      - [1. Ondoorlatend oppervlak](#1-ondoorlatend-oppervlak)
      - [2. Gebruikte profielen](#2-gebruikte-profielen)
      - [3. Gestuurde kunstwerken](#3-gestuurde-kunstwerken)
      - [4. Bodemhoogte stuw](#4-bodemhoogte-stuw)
      - [5. Geometrie](#5-geometrie)
      - [6. Bodemhoogte kunstwerken](#6-bodemhoogte-kunstwerken)
      - [7. Algemene tests](#7-algemene-tests)
      - [8. Geïsoleerde watergangen](#8-geïsoleerde-watergangen)
      - [9. Genereer grid](#9-genereer-grid)
        - [Nog aanvullen](#nog-aanvullen)
    - [Eenmalige tests](#eenmalige-tests)
      - [1. Maximale waarde DEM](#1-maximale-waarde-dem)
      - [2. Ontwateringsdiepte](#2-ontwateringsdiepte)
      - [3. Oppervlaktewater](#3-oppervlaktewater)
  - [0d1d tests/hydraulische toets](#0d1d-testshydraulische-toets)
  - [Bank levels  WE: *@Jelle verouderd, hebben we al aanpassing?*](#bank-levels--we-jelle-verouderd-hebben-we-al-aanpassing)
  - [1d2d tests](#1d2d-tests)
  - [Klimaatsommen](#klimaatsommen)


<span style="color:yellow"> WE: *Kun je nummering met meerdere niveaus toepassen en de nummers ook terug laten komen in de hoofdstukken hieronder?*</span>

<h2>Algemene concepten<h2>

<h3>Standaard project indeling<h3>

De HHNK Toolbox werkt het makkelijkst wanneer een project op een bepaalde manier is ingedeeld. Als een project op die manier is ingedeeld worden de meeste paden automatisch ingevuld wanneer je een polder selecteert. De indeling is als 
volgt:

![](../images/documentation/default_folder_top_level.png)

#### 01_source_data
<span style="color:yellow"> WE: *Hier meer achtergrond geven. Wat zit er in deze bestanden en mappen, waar komen ze vandaar en waar worden ze voor gebruikt? Meestal in opmaak voor controle.*</span>

![](../images/documentation/default_folder_source_data.png) 
##### DIT LIJKT OOK VERANDERD TE ZIJN. WAT IS MINIMAAL NODIG? > actie voor Wietse om dit te verduidelijken


<span style="color:yellow"> WE: *In het plaatje mist de map peilgebieden met daarin een shape van de peilgebieden. Of was het zonder mapje? Deze moet beginnen met peilgebieden_ en is nodig voor de naverwerking. @Jelle, waarom deze niet uit de nieuwe geopackage halen?*</span>

<span style="color:yellow"> WE: *De DAMO gdb en HDB worden inmiddels door de plugin omgezet naar geopackage. Let wel op als je een nieuwe export hebt gemaakt je de geopackage weg gooit. We hebben als doel over te stappen naar geopackage, maar dat werkt nog niet in de modelbuilder.*</span>

Nodig voor tests:

    DAMO.gdb
    datachecker_output.gdb
    HDB.gdb
    polder_polygon (alle extensies)

##### Wat is minimaal nodig voor tests? > Actie voor Wietse

#### Modelbuilder output
De modelbuilder geeft naast het gemaakte model feedback over een aantal onderdelen van de modelbouw. Het is belangrijk deze te controleren. Dit zijn:

-  **channel_surface_from_profiles**: het oppervlakte open water in de 1D profielen om te vergelijken met de BGT waterdelen.
-  **culvert_to_orifice**: duikers die in het model als orifice zijn geschematiseert. <span style="color:yellow"> WE: *Uitleggen welke dat zijn in beschrijving modelbuilder, stukje hieronder op de juiste plek zetten*</span>
-  **impervious_surface(_simple)**: weergave van de oppervlakken gebruikt voor de impervious surface (0d1d berekening)
-  **misfits_lines / _points**: kunstwerken die bij het inpassen in de watergangen niet dezelfde lengte hebben gekregen of helemaal niet zijn gelukt. Deze moeten meestal handmatig met de hand aan het model toegevoegd worden.
-  **model_feeback**: overige opmerkingen en aannames. 



### <span style="color:yellow"> Duikers als orifice</span>
Vanwege rekensnelheid, maar vooral vanwege aanhoudende instabiliteit in 3Di rondom korte duikers schemateseren we een deel van de duikers als doorlaat. De uitgangspunten hierbij zijn:
1.	Lange overlaat (orifice) met discharge coëfficiënten op 1.0, mits:

	   a.	Duiker breedte of diameter is factor 3 kleiner dan breedte watergang op streefpeil en,

      b.	Duiker is korter dan 25m (zo veel mogelijk culverts voor eerste test, als er toch nog instabiele lange duikers ontstaan dan misschien langere afstand kiezen) en,

      c.	Het verschil in bob is kleiner dan 10 cm.
      
2.	Duikers korter dan 10 m (die reeds als orifice werden gemodelleerd) als lange overlaten met discharge coëfficiënt op 1.0
3.	Alle andere duikers (lang, breed of schuin) blijven culvert maar toevoegen 1m2 storage op begin en eind node daar waar dat nog niet tenminste het geval is
4.	Alle bruggen krijgen discharge coëfficiënt op 1.0 (voorheen vaak 0.8)

Indeling 01_source_data/modelbuilder_output:

![](../images/documentation/default_folder_source_data_modelbuilder_output.png)

Nodig voor tests: <span style="color:yellow"> WE: *Welke test? Waarom? Of verwijzing naar onderdeel hieronder.*</span>

    channel_surface_from_profiles (shapefile uit modelbuilder)

#### 02_schematisation:

In deze map moet minimaal de map ``00_basis`` zitten. De map basis bevat het basis model van waaruit meerdere modelstaten kunnen worden gemaakt. In de map basis plaats je een nieuw aangemaakt model. Een 3Di model bestaat uit een sqlite database en een map met één of meerdere rasters. Plaats maar één sqlite in de map basis.
 De andere modelstaten worden gegenereerd bij het ['splitten'](usage.md#5-modelstaten-maken) van de modellen of wanneer nieuwe revisies worden gemaakt. De Excel bestanden bevatten de instellingen voor het genereren van de verschillende modelstaten.

![](../images/documentation/default_folder_schematisation.png) 

Nodig voor tests: <span style="color:yellow"> WE: *Welke test? Waarom? Of verwijzing naar onderdeel hieronder.*</span>

    model.sqlite

Indeling 02_schematisation/00_basis/rasters: 
<span style="color:yellow"> WE: *Leg uit wat deze rasters zijn. Of verwijs naar waar de dat doet.*</span>

![](../images/documentation/default_folder_model_rasters.png)

Nodig voor tests: <span style="color:yellow"> WE: *Welke test? Waarom? Of verwijzing naar onderdeel hieronder.*</span>
    
    dem_[polder] (waar [polder] de naam van de polder is)

#### 03_3di_results
In de deze map worden resultaten van berekeningen opgeslagen. De indeling is als volgt:

![](../images/documentation/default_folder_3di_results.png)

In de mappen zijn de resultaten te vinden van de simulaties die gemaakt zijn. De conventie van de naam van de mappen is als volgt:

```{naam schematisatie} #{revisie nummer} {model type}```

Bijvoorbeeld:

![](../images/documentation/revision_example.png)

#### 04_test_results

De ```04_test_results``` map is de map die (standaard) wordt gebruikt door de plugin om resultaten van tests op te slaan. De indeling van deze map wordt bepaald door de plugin en is als volgt:

![](../images/documentation/default_folder_test_results.png)

De ```0d1d_tests``` en de ```1d2d_tests``` mappen worden verder ingedeeld per gebruikte 3Di revisie:

Bijvoorbeeld:

![](../images/documentation/revision_output_example.png)

### ```QGIS``` project

De meeste tests die deel uitmaken van de toolbox voegen, als onderdeel van hun output, een kaartlaag (of meerdere 
kaartlagen) toe aan het op dat moment geopende ```QGIS```-project. Elke test beheert zijn eigen ```QGIS layer group``` 
en diens subgroepen. De hoofdgroepen zijn als volgt:

![](../images/documentation/qgis_groups.png)

Wanneer je een test opnieuw aanzet worden deze lagen automatisch verwijderd en opnieuw aangemaakt. Als je de lagen wilt behouden (bijvoorbeeld ter vergelijking), dan kun je bijvoorbeeld de hoofdgroepen hernoemen. Let op: je zult in dit geval ook een andere output map moeten specificeren.

## Modelstaat aanpassen
<span style="color:yellow"> WE: *Dit is geen test. Ik heb moeite met de indeling. De splitsing van usage en test documentation vind ik onhandig. Ik zie liever een soort tutorial, een opbouw die de workflow volgt. Goed om een hoofdstuk te hebben met de mappenstructuur aan het begin, maar dat kan meer op hoofdlijnen wat mij betreft.*</span>

Het aanpassen van de modelstaat is een hulpmiddel om te zorgen dat het rekenen met een model zo foutloos mogelijk gebeurt. Binnen de werkwijze van HHNK worden twee belangrijke model toetsingen gedaan:

1. 0d1d toetsing van het model t.b.v. de hydraulische randvoorwaarde (alleen watersysteem)
2. 1d2d toetsing van het model t.b.v. klimaatsommen (watersysteem, maaiveld en bodem)

Door de modelstaat aan te passen worden specifieke instellingen in het model aangepast. In de map van de [schematisatie](#indeling-02_schematisation) staat in ``model_settings.xlsx`` per modelstaat wat de instellingen zijn. Deze manier heeft voordelen ten opzichte van het werken met aparte modellen, omdat andere wijzigingen in het model (zoals het aanpassen van een duiker) dan niet in twee modellen hoeft te worden doorgevoerd. De aanpassingen in het model die worden gedaan bij het aanpassen van de modelstaat hebben betrekking op de uitwisseling tussen het watersysteem (1D) en het maaiveld (2D). 

Met deze aanpassingen in gedachten worden drie modelstaten onderscheiden:

1. Niet gedefinieerd/uit modelbuilder

    Van een model in deze staat wordt voor conversie aangenomen dat het een model betreft dat in de staat is zoals het uit de modelbuilder komt.


2. Hydraulische toets staat (0d1d staat)
<span style="color:yellow"> WE: *Uitleggen wat dit is?*</span>

    Van een model in deze staat wordt aangenomen dat:

    * In tabel ```v2_global_settings``` '0d1d_test' staat bij ``name`` en dat de sturing is uitgeschakeld (```control_group_id``` is ```NULL```/leeg).
  
    * De volgende tabellen in het model staan: <span style="color:yellow"> WE: *kan denk ik weg, merk je als gebruiker niet. Wat welk nuttig zou zijn te beschrijven welke wijzigingen of verschillen er zijn tussen de modelstaten. Dus sturing uit/aan, stuwen 10breder en alles isolated voor 0d1dstaat. Vervolgens zijn er nog meer standaard staten, namelijk voor de batch berekening.*</span>
    ##### WAAR ZOUDEN DEZE MOETEN STAAN, WANT IK ZIE ZE NIET TUSSEN DE LAGEN STAAN

            backup_channels
            backup_manholes
            backup_controlled_weir_widths
            backup_global_settings
    
3. 1d2d toets staat <span style="color:yellow"> WE: *Wat hebben we aan deze beschrijving? Leg uit waarom het bestaat en wat iemand er mee moet.*</span>
    
    Van een model in deze staat wordt aangenomen dat:
    * In tabel ```v2_global_settings``` '1d2d_test' staat bij ``name` en sturing aan staat (```control_group_id``` is niet ```NULL```/leeg).
      
    * De tabel ```backup_global_settings``` bestaat. 
##### IK ZIE DEZE TABEL NERGENS?

Het is belangrijk dat de gedetecteerde staat overeenkomt met de daadwerkelijke staat van het model, aangezien de gedetecteerde staat van het model bepaalt welke aanpassingen er worden gedaan. > IK SNAP DIT STUK NIET <span style="color:yellow"> WE: *ik ook niet.*</span>

Aanpassingen per staat 
##### IK ZOU ONDERSTAANDE GRAAG EEN KEER UITGELEGD KRIJGEN

Van modelbuilder staat naar hydraulische toets/0d1d staat:

| Tabel in model                 |  Aanpassingen                          |
|------------------------------- | -------------------------------------- |
| v2_global_settings             | Verwijderen rijen waar ```name``` niet '0d1d_test' is.<br>Aanpassen ```control_group_id``` naar ```NULL```. |
| v2_manhole                     | Aanpassen ```calculation_type``` naar '1' |
| v2_channel                     | Aanpassen ```calculation_type``` naar '101' |
| v2_weir                        | Aanpassen ```width``` naar ```width``` maal 10 voor gestuurde stuwen |

Van modelbuilder staat naar 1d2d staat:

| Tabel in model                 | Aanpassingen 'Berekenen uit 3Di resultaat'              | Aanpassingen 'Uit backup van eerdere 1d2d staat'  |
|------------------------------- | ------------------------------------------------------- | ------------------------------------------------- |
| v2_global_settings             | Verwijderen rijen waar ```name``` '0d1d_test' is.       | Verwijderen rijen waar ```name``` '0d1d_test' is. |
| v2_cross_section_location      | Oude waarden in ```bank_level``` vervangen voor berekende bank levels. <span style="color:yellow"> WE: *Wat wordt hier berekend? Updaten met inzihct dat levees voor 1d2d verbindingen werken? @Wietse*</span> | Oude waarden in ```bank_level``` vervangen door waarden in ```backup_bank_levels``` |
| v2_manhole                     | Toevoegen nieuw berekende manholes. | - |

Van hydraulische toets/0d1d staat naar 1d2d staat:

| Tabel in model                 |  Aanpassingen 'Berekenen uit 3Di resultaat'               | Aanpassingen 'Uit backup van eerdere 1d2d staat'  |
|------------------------------- | --------------------------------------------------------- | ------------------------------------------------- |
| v2_global_settings             | Verwijderen rijen waar ```name``` '0d1d_test' is.<br>Rijen toevoegen uit ```backup_global_settings``` waar ```name``` niet '0d1d_test' is. | Geen verschil |
| v2_channel                     | Aanpassen ```calculation_type``` naar originele waarde uit ```backup_channels``` | Geen verschil |
| v2_weir                        | Aanpassen ```width``` naar originele waarde uit ```backup_controlled_weir_widths``` | Geen verschil |
| v2_manhole (update)            | Aanpassen ```calculation_type``` naar originele waarde uit ```backup_manholes``` | Geen verschil |
| v2_manhole (nieuw)             | Toevoegen nieuw berekende manholes. | - |
| v2_cross_section_location      | Oude waarden in ```bank_level``` vervangen voor berekende bank levels. | Oude waarden in ```bank_level``` vervangen door waarden in ```backup_bank_levels``` |

## Sqlite checks <span style="color:yellow"> WE: *Nu begint de test documentatie pas? Indeling niet handig.*</span>

De sqlite checks zijn bedoeld om te checken of het model geschikt is om mee te rekenen. Hieronder worden de tests inhoudelijk toegelicht.

### Data verificatie
<span style="color:yellow"> WE: *overal tenminste vertellen wat het is, waarom uitvoeren, waar resultaat zichtbaar, wat controleren en wat eraan doen*</span>

#### 1. Ondoorlatend oppervlak

   Berekent het oppervlak van de polder op basis van de ```polder_shapefile``` en het ondoorlatend oppervlak (impervious surface, 0d) in het model. Het verschil tussen de twee zou niet te groot moeten zijn. <span style="color:yellow"> WE: *Waar zien we dit resultaat? Hoe fout op te lossen?*</span>

#### 2. Gebruikte profielen
   
   Koppelt de v2_cross_section_definition laag van het model (discrete weergave van de natuurlijke geometrie van de watergangen) aan de v2_channel laag (informatie over watergangen in het model). Het resultaat van deze toets is een weergave van de breedtes en dieptes van watergangen in het model ter controle. <span style="color:yellow"> WE: *@Wietse gebruiken we die shape uit de modelbuilder hier niet meer voor?*</span>
 
#### 3. Gestuurde kunstwerken
   
   Deze test selecteert alle gestuurde kunstwerken (uit de v2_culvert, v2_orifice en v2_weir tabellen van het model) op basis van de v2_control_table. Per kunstwerk worden actiewaarden opgevraagd. Per gevonden gestuurd kunstwerk
   wordt ook relevante informatie uit de HDB database toegevoegd, zoals het streefpeil en minimale en maximale kruinhoogtes. <span style="color:yellow"> WE: *Waar zien we dit resultaat? Wat controleren? Wat aanpassen? (hieronder herhaal ik het niet, algemene opmerking hierboven toegevoegd)*</span>

#### 4. Bodemhoogte stuw
    
   Deze test vergelijkt de minimale kruinhoogte uit de sturingstabel met de aanliggende watergangen. Als de bodemhoogte van de watergang hoger ligt dan de minimale kruinhoogte moet hier nog iets in worden aangepast door in de
   v2_cross_section tabel het reference_level aan te passen. Deze aanpassingen worden automatisch gegenereerd en ter goedkeuring aan de gebruiker voorgelegd.

#### 5. Geometrie

   Deze test checkt of de geometrie van een object in het model correspondeert met de start- of end node in de v2_connection_nodes tabel. Als de verkeerde id's worden gebruikt geeft dit fouten in het model.
   
#### 6. Bodemhoogte kunstwerken

   Test checkt of de kruinhoogte of bodemhoogte van een kunstwerk lager ligt dan de bodemhoogte van aanliggende watergangen. Als dit zo is moet dat worden aangepast om met het model te kunnen rekenen.
   
#### 7. Algemene tests
   
   De algemene tests is een collectie van checks op fouten die ervoor zorgen dat het model niet kan worden opgebouwd of waardoor er niet meer gerekend kan worden. In het resultaat wordt onderscheid gemaakt tussen fouten en waarschuwingen. Fouten moeten worden opgelost, waarschuwingen zijn aandachtspunten. In de resultaten wordt omschreven wat het probleem is.
   
#### 8. Geïsoleerde watergangen

   Test bepaalt welk aandeel van watergangen geen verbinding heeft met het maaiveld (isolated). Het aandeel mag niet te groot zijn omdat neerslag de watergangen dan onvoldoende kunnen bereiken.

#### 9. Genereer grid
##### Nog aanvullen
   
### Eenmalige tests

De eenmalige tests zijn er om een aantal randvoorwaarden te controleren. Als geverifieerd is dat hieraan is voldaan, dan hoeven ze niet opnieuw te worden gedraaid.

#### 1. Maximale waarde DEM

   Als de maximale waarde in de DEM te hoog is, duidt dat meestal op een fout in het bestand (de nodata waarde is waarschijnlijk verkeerd ingevoerd). Deze test berekent deze maximale waarde. <span style="color:yellow"> WE: *foute nodata is toch meestal een heel groot negatief getal? Dan vind je die niet met de max denk ik. Ook toevoegen dat 10 meestal de max is omdat watergangen daarop worden dicht gesmeerd.*</span>
 
#### 2. Ontwateringsdiepte
   
   Deze test controleert of het initiële water niveau per polder onder de maaiveldhoogte (DEM) ligt. Het initiële water niveau moet onder het oppervlak liggen.
  
#### 3. Oppervlaktewater

   Deze test controleert per peilgebied in het model hoe groot het gebied is dat het oppervlaktewater beslaat in het model. Dit totaal is opgebouwd uit de ```storage_area``` uit de ```v2_connection_nodes``` tabel opgeteld bij het 
   oppervlak van de watergangen (uitgelezen uit de ```channel_surface_from_profiles```) shapefile. Vervolgens worden de 
   totalen per peilgebied vergeleken met diezelfde totalen uit de DAMO database. De resultaten geven een indicatie van over- of onderschatting van het oppervlaktewater in het model.
   
## 0d1d tests/hydraulische toets

Als de sqlite tests zijn uitgevoerd, eventuele aanpassingen zijn gemaakt en het model is opgebouwd voor rekenen met 3Di wordt de hydraulische toets gedraaid. Deze toets is een test bui ontworpen om het 1d watersysteem in het model te controleren. De test bui begint met een droge dag, vijf dagen neerslag gelijk aan de maalcapaciteit (in de meeste polders is dit 14,4 mm/dag) en dan twee dagen droog. Deze bui is zo ontworpen dat we een aantal eigenschappen van het watersysteem kunnen toetsen:

- **streefpeil handhaving**: blijven waterpeilen constant tijdens de droge dag?
- **stationaire afvoer**: stabiliseert het peil en de afvoer na de 5 dagen neerslag?
- **herstel streefpeil**: herstelt het streefpeil na de natte periode?

![](../images/documentation/hydraulische_toets_bui.png)

Voer deze test uit met het model in 0d1d-staat (zie [Model staat aanpassen](#modelstaat-aanpassen)).

Het resultaat van het simuleren van deze bui kan vervolgens worden geanalyseerd met de HHNK Toolbox. De kaarten die het resultaat zijn van die analyse kunnen worden gebruikt om eventuele onrealistische resultaten te vinden die worden veroorzaakt door fouten in het model. <span style="color:yellow"> WE: *maak concreet!*</span>

De tests die worden gedaan door de Toolbox zijn onderverdeeld in: <span style="color:yellow"> WE: *waar of hoe moet deze test gedraaid worden?*</span>
* 0d1d test

  In deze test worden de 1d nodes uit het 3Di resultaat gefilterd en op vaste tijdstappen de waterstand voor deze nodes
  uitgelezen. Deze tijdstappen zijn:
   * Aan het begin van de som
   * Aan het begin van de regen
   * Een dag voor het einde van de regen
   * Aan het einde van de regen
   * Aan het einde van de som

  Op basis van deze informatie worden de volgende waarden bepaald (in centimeters):
   * Het verschil in waterstand tussen het begin van de som en het begin van de regen (uitzakking initieel peil)
   * Het verschil in waterstand tussen het begin van de regen en het einde van de regen (streefpeilhandhaving)
   * Het verschil in waterstand tussen het einde van de regen en een dag daarvoor (stabiele waterstandsverhoging einde regen)
   * Het verschil in waterstand tussen het einde van de regen en het einde van de som (herstel streefpeil)

<span style="color:yellow"> WE: *leg uit waarom hier naar kijken, wat zijn redelijke waarden, wat aanpassen, veelvoorkomende fouten?*</span>   
  
* Hydraulische test

  In deze test worden eveneens de 1d nodes uit het 3Di resultaat gefilterd. Voor kunstwerken en watergangen corresponderend met deze nodes worden de waterstanden aan het begin en einde van het scenario uitgelezen. Voor deze watergangen en kunstwerken wordt het volgende bepaald:
  
    * Het debiet in m3/s (q)
    * Het verhang (cm/km)
    * De stroomsnelheid in m/s (u)
    * De stroomrichting

Als er voldoende vertrouwen in de uitkomsten van het model is, kan het verhang over watergangen en kunstwerken worden vergeleken met geldende normen (bijvoorbeeld 4 cm/km).
  <span style="color:yellow"> WE: *is de HT een aparte knop of gaat dat gelijk mee met de 0d1d toets?*</span> 

  <span style="color:yellow"> WE: *Wie keurt dit model goed? Beschrijf ook de werkwijze voor de watersysteemanalyse, in dit geval overleg met watersysteemadviseurs en gebiedsbeheerders*</span> 

## Bank levels <span style="color:yellow"> WE: *@Jelle verouderd, hebben we al aanpassing?*</span>

Als het 0d1d model is goedgekeurd kan deze test worden gedraaid. De bank levels test is grotendeels bedoeld om het model klaar te maken voor 3Di simulaties waarbij uitwisseling plaatsvindt tussen het watersysteem en het maaiveld.
Door de resultaten van de simulatie te analyseren wordt bepaald welke watergangen een 1d2d verbinding hebben over een levee heen. Voor deze watergangen wordt een bank level voorgesteld gelijk aan de hoogte van de levee om vroegtijdige 
uitwisseling te voorkomen. Voor overige watergangen is het voorgestelde bank level streefpeil + 10, waar het streefpeil bepaald wordt aan de hand van de ```connection_node_start_id``` die correspondeert met de watergang. 

Als een 1d2d verbinding op een connection node ligt wordt voorgesteld hier een manhole aan toe te voegen met drain level 
gelijk aan de levee hoogte.

Het draaien van de bank levels test kan worden gedaan met elk 3Di resultaat zolang het rekengrid niet is veranderd. De inhoud van het scenario is hierbij niet relevant.

## 1d2d tests

Wanneer de bank levels zijn bijgewerkt en waar nodig manholes zijn toegevoegd kan de 1d2d test worden gedraaid. Dit houdt in dat er opnieuw een test bui wordt gesimuleerd met 3Di.

Deze test werkt alleen wanneer het model in de 1d2d-toets-staat is ingesteld (zie [Model staat aanpassen](#modelstaat-aanpassen)).

De test bui begint in dit geval met een uur droog, dan twee uur regen (17,75 mm/uur), dan 12 uur droog. <span style="color:yellow"> WE: *Waarom?*</span>

![](../images/documentation/1d2d_toets_bui.png)

Het resultaat van het simuleren van deze bui met het model kan vervolgens worden geanalyseerd met de HHNK Toolbox. De kaarten die het resultaat zijn van die analyse kunnen worden gebruikt om eventuele onrealistische resultaten te vinden 
die worden veroorzaakt door fouten in het model.

Als de 1d2d test resultaten goedgekeurd zijn is het model klaar voor gebruik.

De test die worden gedaan door de Toolbox zijn als volgt onder te verdelen:

* Resultaat nodes inlezen

  Deze functie leest alle 2d nodes uit het 3Di resultaat en berekent de volgende waarden:
    * de minimale DEM waarde binnen het gebied van de betreffende node (geometrie is omgezet naar een vierkant)
    * het totale oppervlak dat de node beslaat
  
  Vervolgens wordt op drie tijdstappen (het begin van de regen het einde van de regen en het einde van de som) de volgende informatie berekend:
    * de waterstand op de genoemde tijdstappen
    * de hoeveelheid water (volume in m3) per tijdstap
    * het natte oppervlak per tijdstap (in m2)
    * opslag van regen in het gebied van de node (hoeveelheid water / totale oppervlak gebied)
 

* Stroomlijnen inlezen

  Deze functie leest alle stroomlijnen in uit het 3Di resultaat. Vervolgens wordt gekeken naar het type van de lijn (1D2D of 2D). Vervolgens wordt op drie tijdstappen (het begin van de regen het einde van de regen en het einde van de 
  som) het volgende bepaald:
    * De waterstand per tijdstap
    * Het debiet (q) in m3/s per tijdstap
    * De stroomsnelheid in m/s per tijdstap
    * De stroomrichting per tijdstap
    
* Waterstanden uitlezen

  Deze functie bepaalt de waterstanden op de gegeven tijdstappen op basis van het 3Di resultaat. Vervolgens wordt op basis van de DEM en de waterstand per tijdstap de waterdiepte bepaald.

## Klimaatsommen  
De gevolgen van klimaatverandering worden steeds beter merkbaar. Onder andere in de vorm van hevigere (piek) en/of langdurige (blok) neerslagsituaties. Om de gevolgen van deze neerslagevenementen in beeld te brengen, worden een aantal scenario's met verschillende herhalingstijden doorgerekend. De drie herhalingstijden die gesimuleerd kunnen worden zijn:

1. T10 (neerslagsituatie die zich statistisch gezien 1x in de 10 jaar voordoet)
2. T100 (neerslagsituatie die zich statistisch gezien 1x in de 100 jaar voordoet)
3. T1000 (neerslagsituatie die zich statistisch gezien 1x in de 10 jaar voordoet)

Voor deze herhalingstijden zijn twee verschillende neerslagduren mogelijk:

1. Piek: hevige neerslagsituatie die in 2 uur valt
2. Blok: langdurige neerslagsituatie met een lage neerslagintensiteit die 48 uur duurt 

Daarnaast is de grondwater conditie voorafgaand aan de neerslagsituatie van invloed op het verloop van het scenario. De volgende drie grondwater condities kunnen worden toegepast: 
1. Gemiddeld laagste grondwaterstand (GLG): de gemiddeld laagste grondwaterstand wordt vastgesteld op basis van metingen van grondwaterstanden op de 14e en 28e van de maand. Per jaar worden de drie laagste grondwaterstanden geselecteerd en gemiddeld over minimaal 8 jaar.
2. Gemiddelde grondwaterstand (GGG): de gemiddelde grondwaterstand wordt vastgesteld op basis van metingen van grondwaterstanden op de 14e en 28e van de maand. Deze metingen worden over het jaar gemiddeld en vervolgens gemiddeld over minimaal 8 jaar.
3. Gemiddeld hoogste grondwaterstand (GHG): de gemiddeld hoogste grondwaterstand wordt vastgesteld op basis van metingen van grondwaterstanden op de 14e en 28e van de maand. Per jaar worden de drie hoogste grondwaterstanden geselecteerd en gemiddeld over minimaal 8 jaar.

In totaal zijn er 18 mogelijke scenario's: <span style="color:yellow"> WE: *deze tabel voegt voor mij niets toe.*</span> <br>

| Herhalingstijd  | Neerslagduur | Grondwater conditie   |
|-----------------|--------------|-----------------      |
| T10    | Piek   | GLG
| T100   | Piek   | GLG
| T1000  | Piek   | GLG
| T10    | Piek   | GGG
| T100   | Piek   | GGG
| T1000  | Piek   | GGG
| T10    | Piek   | GHG
| T100   | Piek   | GHG
| T1000  | Piek   | GHG
| T10    | Blok   | GLG
| T100   | Blok   | GLG
| T1000  | Blok   | GLG
| T10    | Blok   | GGG
| T100   | Blok   | GGG
| T1000  | Blok   | GGG
| T10    | Blok   | GHG
| T100   | Blok   | GHG
| T1000  | Blok   | GHG

Hieronder is voor zes scenario's van herhalingstijd en neerslagduur de opbouw weergegeven:

![](../images/documentation/neerslagevents_piek_blok.png)

Bron: Brede Methodiek Wateroverlast
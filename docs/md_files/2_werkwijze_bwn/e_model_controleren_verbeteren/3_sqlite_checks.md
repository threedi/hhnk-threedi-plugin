## Sqlite checks
Nadat de modelbuilder feedback test is uitgevoerd, kunnen de sqlite testen worden uitgevoerd. De sqlite testen zijn bedoeld om het model te controleren op (potentiële) fouten in de data en deze te corrigeren waar nodig. Na de sqlite testen is het model klaar om op te bouwen en om de 0d1d test te draaien (zie [0d1d test](4_0d1d_test.md)).

De sqlite testen bestaan uit negen data verificatie testen en drie eenmalige testen. 

### **Werkwijze HHNK 3Di plugin**
Wanneer in de 'main' van de HHNK toolbox de juiste modellen folder en polder zijn geselecteerd, kunnen de sqlite testen uitgevoerd worden. Volg onderstaande stappen:

1. Ga naar 'Checks' in de HHNK Toolbox.
2. Kies voor 'Sqlite tests'.
![Alt text](../../../images/2_werkwijze_bwn/e_model_controleren_verbeteren/3_sqlite_checks/sqlite_checks_venster_HHNK_Toolbox.png)
3. Selecteer in het Model sqlite check venster alle testen van ondoorlatend oppervlak tot en met oppervlaktewater. Zorg er ook voor dat data verificatie en eenmalige tests zelf zijn geselecteerd. Het 'Model sqlite checks' venster zou er dan zo uit moeten zien als op onderstaande afbeelding.
![Alt text](../../../images/2_werkwijze_bwn/e_model_controleren_verbeteren/3_sqlite_checks/model_sqlite_venster.png)

4. Klik op 'Start tests'.
5. QGIS laadt vervolgens de resultaten in onder de sqlite checks in de HHNK toolbox en in 'Lagen'.


### **Uitkomsten van de test**
De uitkomsten van de testen worden geladen in 'lagen', maar zijn ook zichtbaar aan de rechterzijde van het scherm bij 'sqlite checks' onder 'checks' in de HHNK toolbox. De uitkomsten van de testen kunnen er zo uit zien als op onderstaande afbeelding.
![Alt text](../../../images/2_werkwijze_bwn/e_model_controleren_verbeteren/3_sqlite_checks/Resultaten_sqlite_checks.png)

<span style="color:yellow"> Notitie voor mezelf: *Hier meer uitleg over welke kaarten geladen worden*</span>

### **Beoordeling resultaten**
Voor iedere test moet nagegaan worden of de waarden in het model voldoen. Hieronder wordt uitgelegd waar je bij iedere test op moet letten.
#### Data verificatie testen
<span style="color:yellow"> Notitie voor mezelf: *overal tenminste vertellen wat het is, waarom uitvoeren, waar resultaat zichtbaar, wat controleren en wat eraan doen*</span>

* Test 1: Ondoorlatend oppervlak

  Deze test berekent het oppervlak van de polder op basis van de ```polder_shapefile``` en het ondoorlatend oppervlak (impervious surface, 0d) in het model. Het verschil tussen de twee zou niet te groot moeten zijn. 

  <span style="color:yellow"> Notitie voor mezelf: *Waar kun je dit resultaat vinden? Hoe pas je het resultaat aan? Hoe fout op te lossen?*</span>

* Test 2: Gebruikte profielen

  Deze test koppelt de v2_cross_section_definition laag van het model (discrete weergave van de natuurlijke geometrie van de watergangen) aan de v2_channel laag (informatie over watergangen in het model). Het resultaat van deze toets is een weergave van de breedtes en dieptes van watergangen in het model ter controle. Deze breedtes en dieptes kunnen gevonden worden onder sqlite checks in de HHNK toolbox. Hier kun je klikken op 'Bekijk resultaat' onder het kopje 'Gebruikte profielen watergangen'. Er wordt dan een tabel geopend met de naam 'watergangen_breedte'. In de 12e en 13e kolom kunnen de breedtes en dieptes van ieder gedeelte van een watergang gecontroleerd worden. <span style="color:yellow">  Hier uitleg over realistisch resultaten</span>. Indien deze waardes niet voldoen, kunnen de breedtes van de watergangen aangepast worden in v2_cross_section_definition tabel. De dieptes van de watergangen kunnen aangepast worden in de v2_cross_section_location tabel door het reference level aan te passen.
  Onder 'Lagen' zijn de resultaten van deze test ook zichtbaar.
  
  <span style="color:yellow"> LN: @Wouter @Jelle *Wat zijn realistische waardes voor deze test?*</span>

  <span style="color:yellow"> WE: *@Wietse gebruiken we die shape uit de modelbuilder hier niet meer voor?*</span> 
  
* Test 3: Gestuurde kunstwerken 

  Deze test selecteert alle gestuurde kunstwerken (uit de v2_culvert, v2_orifice en v2_weir tabellen van het model) op basis van de v2_control_table. Per kunstwerk worden actiewaarden opgevraagd. Per gevonden gestuurd kunstwerk wordt ook relevante informatie uit de HDB database toegevoegd, zoals het streefpeil en minimale en maximale kruinhoogtes. De resultaten van deze test kunnen gevonden worden onder sqlite checks in de HHNK toolbox. Hier kun je klikken op 'Bekijk resultaat' onder het kopje 'Gestuurde kunstwerken'. Er wordt dan een tabel geopend met de naam 'gestuurde_kunstwerken'. 
  Onder 'Lagen' zijn de resultaten van deze test ook zichtbaar.
  
   <span style="color:yellow"> Notitie voor mezelf: *Wat moet er gecontroleerd worden? Wat zijn realistische waardes voor deze test? Hoe pas je het resultaat aan?*</span>


* Test 4: Bodemhoogte stuw

  Deze test vergelijkt de minimale kruinhoogte uit de sturingstabel met de aanliggende watergangen. De resultaten van deze test kunnen gevonden worden onder sqlite checks in de HHNK toolbox. Hier kun je klikken op 'Bekijk resultaat' onder het kopje 'Bodemhoogte stuw'. Als de bodemhoogte van de watergang hoger ligt dan de minimale kruinhoogte moet hier nog iets in worden aangepast door in de v2_cross_section_location tabel het reference_level aan te passen. Deze aanpassingen worden automatisch gegenereerd en ter goedkeuring aan de gebruiker voorgelegd. Deze voorgelegde aanpassingen kun je vinden onder sqlite checks in de HHNK toolbox als je klikt op 'Bekijk voorgestelde aanpassingen' bij het kopje 'Bodemhoogte stuw'. Deze aanpassingen kunnen goedgekeurd worden door te klikken op 'Aanvaard aanpassingen'.

* Test 5: Geometrie

  Deze test controleert of de geometrie van een object in het model correspondeert met de start- of end node in de v2_connection_nodes tabel. Als de verkeerde id's worden gebruikt geeft dit fouten in het model. De resultaten van deze test kunnen gevonden worden onder sqlite checks in de HHNK toolbox. Hier kun je klikken op 'Bekijk resultaat' onder het kopje 'Geometrie'. 

  <span style="color:yellow"> Notitie voor mezelf: *Wat moet er gecontroleerd worden? Wat zijn realistische waardes voor deze test? Hoe pas je het resultaat aan, of worden aanpassingen automatisch gegenereerd en voorgelegd?*</span>
  
* Test 6: Bodemhoogte kunstwerken 

  Deze test controleert of de kruinhoogte of bodemhoogte van een kunstwerk hoger ligt dan de bodemhoogte van aanliggende watergangen. Als dit niet zo is moet dat worden aangepast om met het model te kunnen rekenen. De resultaten van deze test kunnen gevonden worden onder sqlite checks in de HHNK toolbox. Hier kun je klikken op 'Bekijk resultaat' onder het kopje 'Bodemhoogte kunstwerken'. Er wordt dan een tabel geopend met de naam 'bodemhoogte_kunstwerken' waarin alle gevallen worden laten zien waar de kruinhoogte of bodemhoogte van een kunstwerk lager ligt dan de bodemhoogte van aanliggende watergangen. De kruinhoogte of bodemhoogte wordt weergegeven door de kolom 'struct_reference_level'. De bodemhoogte van de watergangen wordt weergegeven door de kolom 'cross_reference_level'. Deze waardes kunnen worden aangepast in ......
  
  <span style="color:yellow"> Notitie voor mezelf: *Waar kunnen de hoogtes worden aangepast in v2_culvert en v2_orrifice de kruin- of bodemhoogte van een kunstwerk?*</span>   

* Test 7: Algemene tests

  De algemene tests is een collectie van checks op fouten die ervoor zorgen dat het model niet kan worden opgebouwd of waardoor er niet meer gerekend kan worden. De resultaten van deze test kunnen gevonden worden onder sqlite checks in de HHNK toolbox. Hier kun je klikken op 'Bekijk fouten in model' onder het kopje 'Algemene tests'. In het resultaat wordt onderscheid gemaakt tussen fouten en waarschuwingen. Fouten moeten worden opgelost, waarschuwingen zijn aandachtspunten. In de resultaten wordt omschreven wat het probleem is. De waardes kunnen worden aangepast door naar de bijbehorende tabel te gaan die wordt aangegeven in de eerste kolom.

* Test 8: Geïsoleerde watergangen

  Deze test bepaalt welk aandeel van watergangen geen verbinding heeft met het maaiveld (isolated). Het aandeel mag niet te groot zijn omdat neerslag de watergangen dan onvoldoende kunnen bereiken. De resultaten van deze test kunnen direct bij het kopje 'Geïsoleerde watergangen' onder de sqlite checks in the HHNK toolbox gevonden worden.

  <span style="color:yellow"> Notitie voor mezelf: *Wat is een realistisch Percentage geïsoleerde watergangen? Hoe kan dit worden aangepast*</span>
  
* Test 9: Genereer grid
  
  Deze test genereert het rekenraster onder andere op basis van grid refinements en rekencel grootte (bepaald in global settings). Voor deze test hoeft er niks gecontroleerd te worden. Het rekenraster kan terug gevonden worden onder...

  <span style="color:yellow"> Notitie voor mezelf: *Waar kan het rekenraster terug gevonden worden?*</span>

#### Eenmalige testen
De eenmalige tests zijn er om een aantal randvoorwaarden te controleren. Als geverifieerd is dat hieraan is voldaan, dan hoeven ze niet opnieuw te worden gedraaid.
* Test 1: Maximale waarde DEM

  Als de maximale waarde in de DEM te hoog is, duidt dat meestal op een fout in het bestand (de nodata waarde is waarschijnlijk verkeerd ingevoerd). Deze test berekent deze maximale waarde. Deze maximale waarde kan direct bij het kopje 'Geïsoleerde watergangen' onder de sqlite checks in the HHNK toolbox gevonden worden. Als er bij staat 'voldoen aan de norm' dan hoeft er niks aangepast te worden. Als dat niet zo is...
  
  <span style="color:yellow"> WE: *foute nodata is toch meestal een heel groot negatief getal? Dan vind je die niet met de max denk ik. Ook toevoegen dat 10 meestal de max is omdat watergangen daarop worden dicht gesmeerd.*</span>

  <span style="color:yellow"> Notitie voor mezelf: *Wat staat er als er geen 'voldoet aan de norm staat', en hoe kan het dan aangepast worden?*</span>

* Test 2: Ontwateringsdiepte

  Deze test controleert of het initiële water niveau per polder onder de maaiveldhoogte (DEM) ligt. Het initiële water niveau moet onder het oppervlak liggen.
  
* Test 3: Oppervlaktewater 

  Deze test controleert per peilgebied in het model hoe groot het gebied is dat het oppervlaktewater beslaat in het model. Dit totaal is opgebouwd uit de ```storage_area``` uit de ```v2_connection_nodes``` tabel opgeteld bij het 
   oppervlak van de watergangen (uitgelezen uit de ```channel_surface_from_profiles```) shapefile. Vervolgens worden de 
   totalen per peilgebied vergeleken met diezelfde totalen uit de DAMO database. De resultaten geven een indicatie van over- of onderschatting van het oppervlaktewater in het model.
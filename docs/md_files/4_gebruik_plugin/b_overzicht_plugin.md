 De HHNK Toolbox is opgedeeld in drie delen:

![](../images/usage/header_main.png)
1. Main: hier wordt het model ingeladen, kunnen resultaten worden ingeladen en is het mogelijk om simulaties te starten
2. Checks: dit onderdeel geeft de gebruiker de mogelijkheid om controles uit te voeren voor het model
3. Modelbouw: werkt alleen op de server van HHNK (wordt later toegevoegd aan handleiding)

Er zijn twee mogelijkheden om met de toolbox aan de slag te gaan:
1. HHNK levert de benodigde data (model) aan (klik [hier](#1-data-aangeleverd-door-hhnk))
2. Gebruiker van de plugin bouwt een model vanaf de 'grond' op (klik [hier](#2-zelf-een-model-maken))

Nadere informatie over de inhoud van de testen, benodigde data en het interpreteren van resultaten zijn te vinden via onderstaande links:
* Voor inhoudelijke uitleg van de tests, zie [Documentatie](tests_documentation.md).
* Voor uitleg over de benodigde data, zie [Bron data](needed_data.md).
* Voor uitleg over de interpretatie van resultaten, zie !!!

## Main
Klik op het tabblad 'Main' om naar dit onderdeel te gaan.

![](../images/usage/header_main.png)

## 1. Data aangeleverd door HHNK
Volg onderstaande werkwijze als HHNK de benodigde data (model) aanlevert (optie 1). Als je zelf een model vanaf de 'grond' gaat bouwen, klik dan [hier](#2-zelf-een-model-maken) (optie 2)

1. [Map aanmaken](#1-map-aanmaken)
2. [Data kopiëren](#2-data-kopiëren)
3. [Model inladen](#3-model-inladen)
4. [Inladen resultaten tests (indien van toepassing)](#4-inladen-resultaten-tests-indien-van-toepassing)
5. [Modelstaten maken](#5)
6. [Berekeningen uitvoeren](#6-berekeningen-uitvoeren)

### 1. Map aanmaken <span style="color:yellow"> WE: *verouderd, kan inmiddels met toolbox*</span>
Maak een nieuwe map aan in de verkenner (locatie staat vrij, maar raadzaam om lokaal te werken) met de naam van het aangeleverde gebied (bijvoorbeeld polder_X). Dat kan er als volgt uit zien: `C:\Users\{gebruiker}\Documents\3Di\polder_X`. 

`{gebruiker}` is de naam van de Windows-gebruiker.

### 2. Data kopiëren 
Kopieer de aangeleverde data naar de map die in stap 1 is gemaakt. Hieronder is een voorbeeld te zien waaruit de aangeleverde data (deze kan qua inhoud verschillen) is opgebouwd. <span style="color:yellow"> WE: *peilgebieden ontbreken*</span>

![](../images/usage/copy_data.PNG)

### 3. Model inladen
Het model kan vervolgens ingeladen worden door bij `modellen folder` (1) door de volgende handeling: als je in stap 1 de map hebt aangemaakt in het pad: `C:\Users\{gebruiker}\Documents\3Di\polder_X`, kies je bij `modellen folder` het volgende pad om het model in te kunnen laden: `C:\Users\{gebruiker}\Documents\3Di`. Vervolgens kan bij `polder` (2) gekozen worden voor `polder_X`. 

`{gebruiker}` is de naam van de Windows-gebruiker.

![](../images/usage/load_polder_legend.png)

### 4. Inladen lagen
Via de knop ``laad lagen`` (3) kun je diverse lagen inladen om inzicht te geven in het model.

![](../images/usage/load_polder_legend.png)

Vervolgens verschijnt het onderstaande scherm met een aantal keuzes: 

![](../images/usage/load_test_results.png)

Afhankelijk van de tests die zijn uitgevoerd, kan er gekozen worden tussen het inladen van de van 0d1d, 1d2d of de klimaatsom resultaten. Indien er nog geen testberekeningen of klimaatsommen zijn gemaakt, klik dan hier: [Testberekeningen uitvoeren](#5-testberekeningen-uitvoeren)

Daarnaast kunnen nog een aantal andere opties aangevinkt worden:
* [Sqlite (3Di plugin)](#sqlite-3di-plugin)
* [Grid genereren](#grid-genereren)
* [Sqlite testen](#sqlite-testen)
* [Banklevel test](#banklevel-test)
* [Basis layout](#basis-layout)
* [Achtergrondkaarten](#achtergrondkaarten)

#### Sqlite (3Di plugin)
Deze optie geeft de mogelijkheid om de schematisatie (.sqlite) van het model in te laden.

#### Grid genereren
##### NIEUWE FOUTMELDING > ZIE LOGBOEK. GEEN IDEE HOE OP TE LOSSEN.

Bij het genereren van het grid kan het voorkomen dat er een foutmelding wordt weergegeven dat de .sqlite te oud is. ![](../images/usage/old_sqlite_error.PNG) Ga naar [bekende problemen](#bekende-problemen) om de oplossing te bekijken.  

#### Sqlite testen
De sqlite tests zijn bedoeld om het model te controleren op (potentiële) fouten in de data en deze te corrigeren waar nodig. Na de sqlite tests is het model klaar om op te bouwen en om de 0d1d toets te draaien (zie 
[0d1d toets/Hydraulische toets](tests_documentation.md#1d2d-tests)). Voor de inhoudelijke uitleg van de tests, zie:
[Sqlite tests](tests_documentation.md#sqlite-tests)

#### Banklevel test
Door de ``banklevel test`` in te laden, kun je de resultaten inzien die volgen uit de test die is uitgevoerd. Verdere toelichting over de ``banklevel test`` is te vinden in [banklevel test](tests_documentation.md#bank-levels).

#### Basis layout
Met het inladen van de ``basis layout`` krijg je inzicht in de resultaten die volgen uit controles die zijn uitgevoerd om te kijken of het model goed is opgebouwd vanuit de brondata of dat er nog data mist.

#### Achtergrondkaarten
Met de optie ``achtergrondkaarten`` kun je verschillende soorten kaarten als achtergrond onder de schematisatie leggen. Dit is bijvoorbeeld handig om te controleren of een breedte van een watergang in het model overeenkomt met de breedte op de luchtfoto. 

Onderstaande stappen zijn uit te voeren als er nog geen testberekeningen en testen voor het model zijn uitgevoerd.
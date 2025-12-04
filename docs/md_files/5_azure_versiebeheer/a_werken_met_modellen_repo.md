# Versiebeheer modellen
Het versiebeheer is een hulpmiddel om 3di wateroverlast modellen te beheren en zo aanpassingen te kunnen detecteren en archiveren. Het versiebeheer vindt plaats in Azure en verloopt via github (git_model_repo) en automatiseert het instellen van git hooks, git Large File Storage (LFS), en de benodigde .gitattributes en .gitignore bestanden. Met het toepassen van deze functionaliteiten is versiebeheer + extra inzicht bij de 3Di modellen mogenlijk gemaakt. Hiermee beogen we zowel intern als extern het overzicht te bewaken over de aanpassingen van 3di modellen, bijvoorbeeld bij het uitvoeren van scenariostudies. 


### Hoofdfunctionaliteiten voor versiebeheer
1. Azure DevOps & GitHub integratie
    - Modellen/Repositories worden gehost op Azure DevOps
    - Uitchecken en diffen tussen modelvarianten in GitHub Desktop
    - Initialisatie en beheer zijn hierop afgestemd 

2. Script: bin/initialize_repo.bat
    - Voegt Git hooks toe aan model repository
        - Git hooks
            - Automatische installatie van hooks voor o.a. pre-commit, commit-msg, post-commit, etc.
            - Hooks zorgen voor standaardisatie en extra checks bij commits en pushes binnen de model repo
    - Initialiseert Git LFS (Large File Storage)
        - Git LFS
            - Zorgt dat grote bestanden (zoals rasters en modellen) via LFS worden beheerd
            - Voorkomt dat grote bestanden direct in git worden opgeslagen
    - Maakt of vult .gitattributes en .gitignore aan 
        - .gitattributes en .gitignore
            - .gitattributes regelt welke bestanden via LFS gaan
            - .gitignore voorkomt dat ongewenste, tijdelijke of backup bestanden in git worden opgeslagen

### Locatie model repository & lokaal

- De modellen staan in Azure devops. Inloggen bij Azure Devops kan via de interne Azure omgeving van HHNK. Link is intern beschikbaar.
- Modellen kunnen uitgecheckt worden met Github Desktop. Modellen worden per user uitgecheckt in de map `E:\github\modellen_db\<username>\<model_name>` (De schijf E kan worden ingesteld in de interne hydrologen omgeving).


# Opzet/Werkafspraken modellen repo

### Main branch

- De main branch is de branch waar het laatste basismodel in is opgeslagen. 
- De main branch is klaargezet door een RepoAdmin, dit basismodel dient als bron voor alle scenario branches.
- Pushen vanaf een branch naar de main branch is niet mogelijk zonder een pull request.


### Branches / scenarios

- Als aan het (basis)model wordt gewerkt, dan gebeurd dit dus in een branch. Branches van het basismodel kunnen als deze af zijn via een `pull request` worden samengevoegd met de main branch.
- Elke gebruiker kan zijn scenarios ook eenzelfde bescherming geven als de main branch, om bijvoorbeeld onverhoopte aanpassingen van 3di modellen te voorkomen.
- Afspraken over naamgeving van branches en scenarios:
    - Een persoonlijke werk branch begint met `work_<naam_hydroloog>`
    - De scenario branches beginnen met `scenario_<project_naam>` 

#### Voorbeeld van branch structuur die op den duur kan ontstaan
    main - Basismodel 't Hoekje  
    │
    ├── work_jan  
    │
    ├── scenario_basisvariant
    │
    └── scenario_klimaatadaptatie

### Pull request

Een pull request (PR) is een verzoek om wijzigingen van een branch samen te voegen met een andere branch (meestal main).
Volg de volgende stappen:

1. Maak een branch aan en commit je wijzigingen.
2. Push je branch naar de remote repository.
3. Open een pull request in Azure DevOps.
4. Laat de wijzigingen reviewen door collega(’s).
5. Na goedkeuring wordt de branch samengevoegd (gemerged) met de doelbranch.

Een PR zorgt voor controle, review en goedkeuring voordat wijzigingen definitief worden.

### Pushen en pullen en commit messages
- Committen: Lokale wijzigingen opslaan in je branch.

- Pushen: Je lokale commits uploaden naar de remote repository.

- Pullen: Nieuwe wijzigingen van de remote repository ophalen naar je lokale repository.

### Mergen van branches
Mergen betekent het samenvoegen van de inhoud van twee branches.

- Dit gebeurt meestal via een pull request.
- Conflicten moeten eerst opgelost worden voordat het mergen kan plaatsvinden.
- Na het mergen zijn de wijzigingen van beide branches beschikbaar in de doelbranch (bijvoorbeeld main).


# Lokaal werken met Azure/Github repo

## Een nieuwe repo opzetten
### Aanmaken nieuwe repo
1. Op de interne Azure omgeving van HHNK, ga in de linker werkbalk naar `repos`. Klik bovenin achter HHNK / Intern / Repos / Files / op `Intern` en kies `nieuwe repository`.

2. Geef de Repository naam op. De BWN modellen noteren we op de volgende wijze: `bwn_<cluster id>_<modelnaam>`. Gebruik alleen kleine letters. Het polder id kun je vinden onder [Polder clusters](../polder_clusters.md). Bijvoorbeeld `bwn_20_wijdewormer`.


### Initializeren 
Na het aanmaken van een model repository is het nodig om deze te initialiseren. Dit voegt de benodigde git hooks
(in de folder .git/hooks), initialiseert git LFS (Large File Storage) en maakt of voegt toe aan de .gitattributes en
.gitignore files.

Volg de volgende stappen:
1. Clone het net aangemaakte repository op in de [locatie](#locatie-model-repository--lokaal) met (bijvoorbeeld) github desktop, zie `Clone een bestaande Azure devops repo` hieronder.
2. Open Vs Code en ga naar de speciaal ingerichte locatie met threedi tools `D:\github\00_modellen_db\hhnk-threedi-tools\` op de hydrologenserver.
3. Start een terminal met command prompt (cmd) en voor het volgende commando uit:

    ```shell
    # ensure the correct python environment in active
    pixi shell
    # eventueel de repo vertrouwen als dit nodig is
    git config --global --add safe.directory D:/github/00_modellen_db/hhnk-threedi-tools
    # install git hooks etc.
    hhnk_threedi_tools\git_model_repo\bin\initialize_repo.bat E:\github\modellen_db\<username>\<model_name>
    ```


### Toevoegen van benodigde data
De Main branch is standaard beschermd voor aanpassingen. Dit zorgt er voor dat de main niet per ongeluk aangepast kan worden. Om de main dus van data te voorzien is de volgende stap het aanmaken van een branch (`work_<username>`). In github kun je een branch aanmaken, welke je vervolgens kunt vullen met de beoogde data.

De gehele folderstructuur vanuit de model opbouw kan hier worden toegevoegd aan de branch. Om vervuiling van de repository tegen te gaan is de `.gitignore` file gevuld met de bestanden die toegestaan zijn binnen de repo. De gehele map vanuit de model opbouw kan dus worden toegevoegd, waarna de `.gitignore` filterd wat gewenst is en wat niet. 

Het kan voorkomen dat er extra data moet worden opgeslagen binnen de repository, dit kan dan worden aangepast in de `.gitigore` file.
 
### Pull request opzetten voor de main branch
Wanneer de `work_<username>` branch klaar is om als basismodel te dienen, kunnen we dit doorzetten naar de main. Aangezien de main beschermd is moet dit via het hierboven beschreven [Pull Request](#pull-request). Als je die stappen hebt doorlopen dan staat het hoofdmodel op de main branch en kunnen andere gebruikers hiervandaan een Clone maken en verder werken.


## Clone een bestaande Azure devops repo

1. Op de interne Azure omgeving van HHNK, ga in de linker werkbalk naar `repos`. Kies vervolgens boven in in de werkbalk met de pulldown het model/repo dat je wilt hebben.

2. Vervolgens verschijnt een overzicht van de bestanden in het rechter deel van het scherm . Kies in dit deel van het scherm rechtsboven op `Clone`. Kies hier HTTPS en kopieer de link (deze begint met `https://HHNK@`).

3. Start Github Desktop en kies `File`,`Clone repository`. Kies de optie/tabblad `URL` en vul onder `repository URL` de gekopieerde URL in. Kies vervolgens de map waar de repo moet komen [locatie](#locatie-model-repository--lokaal) en klik op `Clone`.

4. Klik vervolgens in Azure op 'Generate Git credentials' en kopieer de gebruikersnaam en wachtwoord. Deze kunnen in Github Desktop geplakt worden onder `Username` en `Password` in de popup die verschijnt bij het clonen.

## Git Hooks in git_model_repo

### Wat zijn git hooks?
Git hooks zijn scripts die automatisch worden uitgevoerd bij bepaalde git-acties, zoals committen, pushen of mergen. Ze helpen om consistentie, kwaliteit en automatisering te waarborgen.

### Overzicht van geïnstalleerde hooks

- **pre-commit**  
  Voert checks/taken uit vóór een commit. 
    - Zijn er veranderde bestanden
    - Taken, zoals omschrijven naar geojson en detecteren van verschillen
  
- **commit-msg**  
  Controleert of commit messages voldoen aan afspraken (zoals een ticketnummer of beschrijving). Dit zorgt voor een ingevuld commit veld, wat dient als extra logboek voor de aanpassingen binnen een branch.   
  

- **post-commit**  
  Kan gebruikt worden om na een commit extra acties uit te voeren, zoals notificaties of automatische documentatie.  
  

- **post-checkout, post-merge, post-rewrite, prepare-commit-msg**  
  Automatiseren taken na het wisselen van branches, mergen, herschrijven van geschiedenis of voorbereiden van commit messages.

### Hoe werken de hooks?
De hooks worden automatisch geplaatst in `.git/hooks` bij initialisatie van de repo met het script:
```
<pad naar hhnk-threedi-tools>\hhnk_threedi_tools\git_model_repo\bin\initialize_repo.bat <pad naar model repo>
```
Ze zijn direct actief en vereisen geen handmatige installatie.

### Hooks uitbreiden
Wil je extra checks of acties toevoegen?  
- Voeg je script toe aan de betreffende hook in `.git/hooks`  
- Zorg dat het script uitvoerbaar is (`chmod +x <hook>` op Linux/Mac)



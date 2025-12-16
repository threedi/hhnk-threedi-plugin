# Werk afspraken
Hier staan een aantal werkafspraken die we volgen om het overzicht te bewaren binnen het werken met het versiebeheer.
## Lokaal werken
### Locatie lokale model repository

- De modellen worden gehost op Azure devops. Inloggen bij Azure Devops kan via de interne Azure omgeving van HHNK. Link is intern beschikbaar.
- Modellen kunnen uitgecheckt worden met Github Desktop. Modellen worden per user uitgecheckt in de map `E:\github\modellen_db\<username>\<model_name>` (De schijf E kan worden ingesteld in de interne hydrologen omgeving).

### Naam van model repository
- De BWN modellen noteren we op de volgende wijze: `bwn_<cluster id>_<modelnaam>`


## Werken met Github & Azure
Hieronder een aantal afspraken en info voor het werken met Azure en Github.

### Main branch
- De main branch is de branch waar het meest recente basismodel in is opgeslagen. 
- De main branch is klaargezet door een RepoAdmin, dit basismodel dient als bron voor alle toekomstige scenario branches.
- Pushen vanaf een branch naar de main branch is niet mogelijk zonder review van een collega.


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

### Pushen en pullen en commit messages
- Committen: Lokale wijzigingen opslaan in je branch.
    - Om te kunnen commiten voorzie je de commit van een titel en opmerkingen van de aanpassingen die je hebt gemaakt.

- Pushen: Je lokale commits uploaden naar de remote repository.

- Pullen: Nieuwe wijzigingen van de remote repository ophalen naar je lokale repository.


### Pull request

Een pull request (PR) is een verzoek om wijzigingen van een branch samen te voegen met een andere branch (meestal main).
Volg de volgende stappen:

1. Maak een branch aan en commit je wijzigingen.
2. Push je branch naar de remote repository.
3. Open een pull request in Azure DevOps.
4. Laat de wijzigingen reviewen door je collega(’s).
5. Na goedkeuring wordt de branch samengevoegd (gemerged) met de doelbranch.

Een PR zorgt voor controle, review en goedkeuring voordat wijzigingen definitief worden.


### Mergen van branches
Mergen betekent het samenvoegen van de inhoud van twee branches.

- Dit gebeurt meestal via een pull request.
- Conflicten moeten eerst opgelost worden voordat het mergen kan plaatsvinden.
- Na het mergen zijn de wijzigingen van beide branches beschikbaar in de doelbranch (bijvoorbeeld main).


## Werken met Git Hooks
### Wat zijn git hooks?
Git hooks zijn scripts die automatisch worden uitgevoerd bij bepaalde Github-acties, zoals committen, pushen of mergen. Ze helpen om consistentie, kwaliteit en automatisering te waarborgen.

### Overzicht van geïnstalleerde hooks

- **pre-commit**  
  Voert checks/taken uit vóór een commit. 
    - Controleren of er bestanden zijn gewijzigd.
    - Als deze zijn gewijzigd dit dan het omschrijven van de modelschematisatie van .gpkg naar .geojson om verschillen te kunnen diffen.
  
- **commit-msg**  
  Controleert of commit messages voldoen aan afspraken (zoals een ticketnummer of beschrijving). Dit zorgt voor een ingevuld commit veld, wat dient als extra logboek voor de aanpassingen binnen een branch.   
  

- **post-commit**  
  Heeft nu geen functie, maar kan gebruikt worden om na een commit extra acties uit te voeren, zoals notificaties of automatische documentatie.  
  

- **post-checkout, post-merge, post-rewrite, prepare-commit-msg**  
  Automatiseren andere taken na het wisselen van branches, mergen, herschrijven van geschiedenis of voorbereiden van commit messages.

### Hoe werken de hooks?
De hooks worden automatisch geplaatst in `.git/hooks` bij initialisatie van de repo met het script:
```
<pad naar hhnk-threedi-tools>\hhnk_threedi_tools\git_model_repo\bin\initialize_repo.bat <pad naar model repo>
```
Ze zijn direct actief en vereisen geen handmatige installatie.

### Hooks uitbreiden
Wil je extra checks of acties toevoegen?  
- Voeg je script toe aan de betreffende hook in `.git/hooks`  
- Zorg dat het script uitvoerbaar is



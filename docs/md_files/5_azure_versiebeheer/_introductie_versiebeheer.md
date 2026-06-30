# Introductie versiebeheer modellen
Het versiebeheer is een hulpmiddel om 3di wateroverlast modellen te beheren en zo aanpassingen te kunnen detecteren en archiveren. Het versiebeheer vindt plaats in Azure en verloopt via github (git_model_repo) en automatiseert het instellen van git hooks, git Large File Storage (LFS) en de benodigde .gitattributes en .gitignore bestanden. Met het toepassen van deze functionaliteiten is versiebeheer + extra inzicht bij de 3Di modellen mogelijk gemaakt. Hiermee beogen we zowel intern als extern het overzicht te bewaken over de aanpassingen van 3di wateroverlast modellen, bijvoorbeeld bij het uitvoeren van scenariostudies. 


Deze handleiding voor het versiebeheer is opgebouwd uit de volgende onderdelen:

- [1. Opzetten van een model repository, wanneer er nog geen repository beschikbaar is voor het beoogde model.](../5_azure_versiebeheer/a_opzetten_repository.md) 
- [2. Clonen van een model repository, wanneer er al een repository opgezet is.](../5_azure_versiebeheer/b_clonen_repository.md)
- [3. Extra werk afspraken voor uniformiteit binnen het versiebeheer.](../5_azure_versiebeheer/c_werkafspraken.md)
- [4. Instellingen voor het storage probleem van LFS.](../5_azure_versiebeheer/d_bug_lfs.md)



## Hoofdfunctionaliteiten voor versiebeheer
1. Integratie met Azure DevOps & GitHub 
    - Modellen/Repositories worden gehost op Azure DevOps
    - Lokaal uitchecken en diffen tussen modelvarianten in GitHub Desktop
    - Initialisatie en beheer zijn hierop afgestemd 

2. Functionaliteiten: bin/initialize_repo.bat
    - Toevoegen van Git hooks toe aan model repository
        - Git hooks
            - Automatische installatie van hooks voor o.a. pre-commit, commit-msg, post-commit, etc.
            - Hooks zorgen voor standaardisatie en extra checks bij commits en pushes binnen de model repo
    - Initialiseren Git LFS (Large File Storage)
        - Git LFS
            - Zorgt dat grote bestanden (zoals rasters en modellen) via LFS worden beheerd
            - Voorkomt dat grote bestanden direct in git worden opgeslagen
    - Vullen van .gitattributes en .gitignore aan 
        - .gitattributes en .gitignore
            - .gitattributes regelt welke bestanden via LFS gaan
            - .gitignore voorkomt dat ongewenste, tijdelijke of backup bestanden in git worden opgeslagen



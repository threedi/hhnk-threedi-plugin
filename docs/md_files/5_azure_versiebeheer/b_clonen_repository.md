## Clonen van een bestaande Azure devops repo

1. Op de interne Azure omgeving van HHNK, ga in de linker werkbalk naar `repos`. Kies vervolgens boven in in de werkbalk met de pulldown naast de naam van de repo dat je wilt clonen.

2. Vervolgens verschijnt een overzicht van de bestanden in het rechter deel van het scherm. Kies in dit deel van het scherm rechtsboven op `Clone`. Kies hier HTTPS en kopieer de link (deze begint met `https://HHNK@`).

3. Start Github Desktop en kies `File`->`Clone repository`. Kies de optie/tabblad `URL` en vul onder `repository URL` de gekopieerde URL in. Kies vervolgens de map waar de repo moet komen ([zie locatie](c_werkafspraken.md###-Locatie-model-repository-lokaal)) en klik op `Clone`.

4. Klik vervolgens in Azure op 'Generate Git credentials' en kopieer de gebruikersnaam en wachtwoord. Deze kunnen in Github Desktop geplakt worden onder `Username` en `Password` in de popup die verschijnt bij het clonen.

5. De repository is gecloned, je kunt nu een branch selecteren of aanmaken in Github Desktop. 

6. Start met het initializeren van de benodigde bestanden.


## Initializeren 
Na het aanmaken van een model repository is het nodig om deze te initialiseren. Dit voegt de benodigde git hooks toe
(uit de folder .git/hooks), initialiseert git LFS (Large File Storage) en past de .gitattributes en
.gitignore files aan.

Volg de volgende stappen:
1. Open Vs Code en ga naar de speciaal ingerichte locatie met threedi tools `D:\github\00_modellen_db\hhnk-threedi-tools\` op de hydrologenserver (514).
2. Start een terminal met command prompt (cmd) en voor het volgende commando uit:

    ```shell
    # ensure the correct python environment in active
    pixi shell
    # eventueel de repo vertrouwen als dit nodig is
    git config --global --add safe.directory D:/github/00_modellen_db/hhnk-threedi-tools
    # install git hooks etc.
    hhnk_threedi_tools\git_model_repo\bin\initialize_repo.bat Y:\02.modelrepos\<username>\<model_name>
    ```
3. controleer of de bovenstaande actie goed is uitgevoerd (hooks/LFS/etc).

4. Optioneel bij het ontbreken van model schematisatie in de main: Voeg de benodigde data toe!


## Toevoegen van benodigde data
De Main branch is standaard beschermd voor aanpassingen. Dit zorgt er voor dat de main niet per ongeluk aangepast kan worden. Om de main dus van data te voorzien is de volgende stap het aanmaken van een branch (`work_<username>`). In github kun je een branch aanmaken, welke je vervolgens kunt vullen met de beoogde data.

De gehele folderstructuur vanuit de model opbouw kan hier worden toegevoegd aan de branch. Om vervuiling van de repository tegen te gaan is de `.gitignore` file gevuld met de bestanden die toegestaan zijn binnen de repo. De gehele map vanuit de model opbouw kan dus worden toegevoegd, waarna de `.gitignore` filterd wat gewenst is en wat niet. 

Het kan voorkomen dat er extra data moet worden opgeslagen binnen de repository, dit kan dan worden aangepast in de `.gitigore` file.

Hernoem de readme.md naar logboek.md en houdt hier je aanpassingen en werkstappen in bij.
 
### Pull request opzetten voor de main branch
Wanneer de `work_<username>` branch klaar is om als basismodel te dienen, kunnen we dit doorzetten naar de main. Aangezien de main beschermd is moet dit via hier beschreven [Pull Request](c_werkafspraken.md#pull-request). Vraag een hydroloog van HHNK om je aanpassingen te reviewen. Dit doe je in de regel als er een nieuw basismodel gereed is. Als je die stappen hebt doorlopen dan staat het hoofdmodel op de main branch en kunnen andere gebruikers hiervandaan een Clone maken en verder werken.
## Een nieuwe model repository opzetten
Wanneer het beoogde poldermodel nog geen eigen repository heeft, dan moet dit nog worden aangemaakt. Hieronder wordt beschreven hoe je dit kunt doen.

### Aanmaken nieuwe repo
1. Op de interne Azure omgeving van HHNK, ga in de linker werkbalk naar `repos`. Klik bovenin achter HHNK / Intern / Repos / Files / op `Intern` en kies `nieuwe repository`.

2. Geef de Repository naam op. De BWN modellen noteren we op de volgende wijze: `bwn_<cluster id>_<modelnaam>`. Gebruik alleen kleine letters. Het polder id kun je vinden onder [Polder clusters](../polder_clusters.md). Bijvoorbeeld `bwn_20_wijdewormer`.

3. De main branch is nu aangemaakt, hier moet nog een basismodel in worden gezet. Aangezien de main branch beschermd is moet dit via een work_branch in combinatie met een pull request worden aangeleverd. 

4. Ga dus verder met het clonen en initializeren van deze main branch [Clonen van een model repository](..\5_azure_versiebeheer\b_clonen_repository.md)

## **Modelstaat aanpassen/maken**

Als er nog geen modelstaten en testberekeningen uitgevoerd zijn, kunnen de volgende stappen doorlopen worden:

1. Klik op ``Model splitten en uploaden`` (4). 

   ![](../images/usage/load_polder_legend.png)

2. Hierna wordt het volgende scherm weergegeven:
![](../images/usage/load_modelsplitter_legend.png)
Als er een Excel met modelinstellingen aanwezig is in het pad ``C:\Users\{gebruiker}\Documents\3Di\polder_Bart\02_schematisation``, dan zullen een aantal opties tevoorschijn komen (zoals in vak 1 is te zien). Als er nog geen Excel aanwezig is in het voorgenoemde pad, klik dan [hier](needed_data.md#model-instellingen) om de opbouw van de Excel te bekijken. In de Excel is het tevens mogelijk om de modelinstellingen aan te passen, zoals de simulatie tijdstappen of de startdatum. De modelsplitter geeft de mogelijkheid om een aantal modelstaten te genereren, zoals in het vak met de ``1`` is te zien. De modelstaten voor de te genereren modellen staan automatisch in het rechtervak met daarboven ``Enabled``. In het rechtervak laat je de modelstaten staan waarvan je een model wil laten maken. Als je een bepaalde modelstaat niet nodig hebt, kun je deze naar het linkervak slepen met daarboven ``Disabled``.  
3. Druk op ``Run: Model Splitter`` (2) om de modelsta(a)t(en) die onder ``Enabled`` staan te genereren
4. Geef een ``Commit message`` mee (3)
5. Upload de modelsta(a)t(en) door op ``Upload modelversion(s)`` te klikken (4)

`{gebruiker}` is de naam van de Windows-gebruiker.

### 3. Modelstaat aanpassen

Wanneer je op deze knop klikt open zich een nieuw venster:

![](../images/usage/model_states_conversion_legend.png)

1. Selecteer een model
   
2. Zodra een model is geselecteerd wordt de huidige staat gedetecteerd (zie 
   [Modelstaat aanpassen](tests_documentation.md#modelstaat-aanpassen)). Het is belangrijk dat de gedetecteerde staat    klopt.
3. Kies de staat om het model naar om te zetten
4. Deze sectie wordt beschikbaar als we bij 3 '1d2d toets' als nieuwe staat hebben geselecteerd. Er zijn twee opties 
   wanneer we het model omzetten naar de 1d2d toets staat: <br>
   4a. We can calculate the correct configuration from a 3Di result 
   * 4a.1 <br>
     Bereken de 1d2d staat op basis van een 3Di resultaat:
     Selecteer een 3Di resultaat map (bevat een ```.nc``` en een ```.h5``` file). Dit resultaat wordt alleen gebruikt om 
     het rekengrid te bepalen. Het maakt dus niet uit of het resultaat een 0d1d of 1d2d som betreft.
       
    * 4a.2 <br>
    Selecteer de datachecker geodatabase die bij het model hoort. <br>
     
    4b. Je kunt er ook voor kiezen om een eerdere 1d2d staat te gebruiken voor het omzetten van het model, mits er een 
    backup beschikbaar is. Deze backup is ook beschikbaar als de ```bank levels``` al eerder zijn berekend.
   
Wanneer je op 'OK' klikt worden alle benodigde aanpassingen berekend en voorgelegd aan de gebruiker:

![](../images/usage/model_states_changes_dialog.png)

In sommige gevallen kunnen de nieuwe waarden handmatig worden aangepast. In sommige gevallen kunnen bepaalde rijen 
worden uitgesloten zodat ze niet worden meegenomen in het aanpassen van het model.

Controleer de voorgestelde aanpassingen en klik op 'Aanpassingen uitvoeren' om ze door te voeren. Als er handmatige 
aanpassingen zijn gedaan of er rijen zijn uitgesloten dan worden deze wijzigingen weergegeven zodat ze kunnen worden 
opgeslagen:

![](../images/usage/model_states_manual_changes.png)
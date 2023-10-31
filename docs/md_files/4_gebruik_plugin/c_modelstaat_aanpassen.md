# Modelstaten

De modelstaten zijn afgeleide modellen van het basismodel, waarin vastgestelde initiële settings worden meegegeven bij het aanmaken van het model. Hieronder volgens de stappen om een benodigde modelstaat te initiëren.
1. De initiële settings worden uitgelezen uit een 'model_settings.xlsx' in de ...\02_schematisations folder. In de Excel is het mogelijk om de modelinstellingen aan te passen (o.a. rasters, tijdstappen of de startdatum). Indien deze Excel niet aanwezig is kan er geen modelstaat worden geinitiëerd. Als er nog geen Excel aanwezig is in het voorgenoemde pad, klik dan [hier](needed_data.md#model-instellingen) om de opbouw van de Excel te bekijken.

2. Klik op ``Model splitten en uploaden`` (4). 
   ![](../images/usage/load_polder_legend.png)

3. Hierna wordt het volgende scherm weergegeven:
![](../images/usage/load_modelsplitter_legend.png) 
Afhankelijk van de 'model_settings.xlsx' volgen de verschillende modelstaten (zie vak 1).  De modelsplitter kan vervolgens de modelstaten genereren, zoals in het vak met de ``1`` is te zien. De beschikbare modelstaten staan bij default onder ``Enabled``. De niet gewenste modelstaten sleep je naar ``Disabled``.  
4. Druk op ``Run: Model Splitter`` (2) om de modelsta(a)t(en) die onder ``Enabled`` staan te initiëren.
5. Geef een ``Commit message`` mee (3).
6. Upload de modelsta(a)t(en) door op ``Upload modelversion(s)`` te klikken (4)

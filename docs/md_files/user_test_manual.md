# Handleiding voor gebruikerstesten


## Voorbereiding
Om (een branch van) de plugin en modules te testen, voer je de volgende de volgende handelingen uit:

0. zorg voor lokale clones van `hhnk-research-tools`, `hhnk-threedi-tools` en `hhnk-threedi-plugin` en zorg dat je de [deze in edit-mode hebt geinstalleerd](#installatie-van-modules-in-edit-mode).
1. zorg dat je een kopie hebt van `c:\Users\{user}\AppData\Roaming\3Di\QGIS3\profiles\default\python\plugins\hhnk_threedi_plugin\api_keys.txt`
2. verwijder de folder `c:\Users\{user}\AppData\Roaming\3Di\QGIS3\profiles\default\python\plugins\hhnk_threedi_plugin`
3. kopieer de folder `hhnk_threedi_plugin` naar `c:\Users\{user}\AppData\Roaming\3Di\QGIS3\profiles\default\python\plugins`
4. kopieer je `apy_keys.txt` naar `c:\Users\{user}\AppData\Roaming\3Di\QGIS3\profiles\default\python\plugins\hhnk_threedi_plugin\api_keys.txt`
5. Herstart de Modeller Interface

Je kunt nu door naar [gebruikerstests](#gebruikerstests)

## Installatie van modules in edit-mode
Verifieer of de modules nu naar de repositories verwijzen in de Python-console van de Modellers Interface. Voer in de Python console:

```
import hhnk_threedi_tools
hhnk_threedi_tools.__file__
```

Je nu het pad naar de `__init__.py` in de lokale clone van `hhnk_threedi_tools` terug krijgen:

![](../images/develop/verify_modules_editable.PNG)

Als je naar de correcte directory, voor zowel `hhnk_threedi_tools` als `hhnk_research_tools` dan kun je verder me het [testen van de plugin](#testen-van-de-plugin)


Verwijst ht pad niet naar de resporitory maar naar de plugin-dir, dan komt dat omdat daar de plugin nog staat. Verwijder `hhnk-research-tools` en `hhnk-threedi-tools` uit `c:\Users\{user}\AppData\Roaming\3Di\QGIS3\profiles\default\python\plugins\hhnk_threedi_plugin\external-dependencies`

Bestaan de modules niet, of heb je deze net verwijderd uit de external-dependencies folder


Je voegt `hhnk-research-tools` en `hhnk-threedi-tools` op de volgende wijze toe aan de QGIS omgeving vna de Modellers Interface
1. Zorg voor een lokale clone van de repositories
2. Open de OSGeo4W shell en controlleer of je in de shell van 3Di Model Interface zit:

```
python
import sys
sys.executable
```
In je pad zou er vergelijkbaar uit moeten zien `C:\\PROGRA~1\\3DIMOD~1.28\\bin\\python.exe`. `3DIMOD` geeft aan dat je in de QGIS install zit van de M.I. en niet in een andere. 

3.  en navigeer naar de het pad in hhnk-research-tools waar setup.py staat. Voer in:
```
pip install -e .
```
4. Herhaal hetzelfde voor hhnk-threedi-tools

![](../images/develop/install_modules_editable.PNG)


## gebruikerstests

### 
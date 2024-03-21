# **Nieuw basismodel maken binnen HHNK omgeving**

In de omgeving van HHNK kan actuele data geëxporteerd worden en kunnen de datachecker en modelbuilder gedraaid worden om een nieuw basis model te maken. Volg hiervoor de volgende stappen:

*LET OP: er kan maar één model tegelijkertijd opgebouwd worden omdat de datachecker en modelbuilder dezelfde locaties en database gebruiken. Zorg ook voor administratie van in- en output omdat deze wordt overschreven.*

## Maak een export van de huidige DAMO en HDB met FME

1. Ga hiervoor naar `srv300d1.corp.hhnk.nl` via remote desktop en open FME (v2021), <br>
2. Open nu het meest recente fme script voor de export: `\\corp.hhnk.nl\data\Hydrologen_data\Data\01.basisgegevens\00.Export\01_DAMOHDBexport_<datum>.fmw`, <br>
3. Druk linksboven op de play-knop en vul in het scherm in welke [gebieden](#overzicht-gebieden) je wilt exporteren en eventueel een unieke naam voor de export. <br>
4. Plaats de data (DAMO.gdb en HDB.gdb) in de map input `\\corp.hhnk.nl\data\Hydrologen_data\Data\modelbuilder\data\input`. <br>

## Draai de datachecker

5. Ga naar `srvota155` via Remote Desktop on open Visual Studio Code via het start menu (dus niet via de batch-file die de Modeller Interface python omgeving activeert).
6. Open in VS Code de map van de modelbuilder `\\corp.hhnk.nl\data\Hydrologen_data\Data\modelbuilder\`
7. Open het bestand `datachecker_visual_studio.py` in de map `datachecker`.
8. Selecteer rechtsonder in Visual Studio de python interpreter `threedipy` en draai het script (SHIFT+ENTER), selecteer eventueel ook bij het scherm dat zich opent rechtsboven de juiste interpreteer en probeer opnieuw.
9. Zodra de Datachecker klaar is wordt de `datachecker_output` weggeschereven naar de uitvoermap `data/output`.
10. Controleer eerst het resultaat voordat het model wordt gemaakt.

## Draai de modelbuilder

11. Zorg dat je zeker bent dat er in de tussentijd geen ander model via de datachecker is gedraaid.
12. Herhaal stap 5 en 6.
13. Open het bestand `modelbuilder_visual_studio.py` in de map `modelbuilder`.
14. Pas in het python bestand de laatste regel aan naar het id en de naam van het [gebied](#overzicht-gebieden) waarvoor je een model wilt maken. Deze polders worden uit de datachecker data geknipt en gebruikt om het model op te bouwen. De gegevens voor het model moeten dus in de datachecker zitten! De poldernaam wordt gebruikt voor oa naamgeving van bestanden.
14. Zodra de Modelbuilder klaar is wordt het model en feedback weggeschreven naar de uitvoermap `data/output`.
15. Kopieer voor [gebruik in de plugin](../4_gebruik_plugin/b_project_starten.md) de bestanden naar de projectmap. De output van de modelbuilder staat al in de juiste mappenstructuur. Alleen de datachecker_output moet nog naar 01_source_data gekopieerd worden.

## Debugging
Mocht onverhoopt iets niet werken staan in de mappenstructuur van de modelbuilder verschillende logbestanden. Eventueel kan in de genoemde python scripts de optie `DEBUG=True` worden ingesteld om nog meer logging te ontvangen.

De tussenstappen in de datachecker en modelbuilder zijn opgeslagen in een postgis database op de server. Om de tussenstappen te bekijken kun je verbinding maken met deze database via qgis (het olifant symbool van postgrs-database), met de volgende instellingen:

* Name: DCMB (vrije keuze)
* Service: (leeg)
* Host: localhost
* Port: 5433
* Database: datachecker
* SSL mode: allow

Onder authentication kies je `basic`. De username en pasword zijn `postgres`.


## Overzicht gebieden

    ID	Naam						Code Polders V4
    1	Heerhugowaard				"03150","03350"
    2	Drieban						"6090"
    3	Purmer						"5801","5802","5803"
    4	Grootlimmerpolder			"04230","04290","04300"
    5	Koegras						"2060","2040","2010","20601"
    6	Marken						"5160"
    7	HUB				    		"04310","04320","04541","04542"
    8	Beemster					"5400","5401"
    9	VNK				    		"6750"
    10	t Hoekje					"2020","2040"
    11	Assendelft					"04751","04752","04380"
    12	Grootslag					"6700","6770","6780","6080"
    13	Heiloo						"04170","04650","04160","04200"
    14	Purmerend					"5741","5742","5721","5722","5841","5842","5320"
    15	Starnmeer					"04460"
    16	Eijerland					8040,"8071"
    17	Mijzen						"04520"
    18	Oudorp						"03765"
    20	Wijdewormer					"5310"
    21	Noorderkaag					"03703"
    23	Edam Volendam Katwoude		"5360","5781","5761","5762","5782"
    24	VRNK-Oost					"2100","2110","03190","03200","03210","6753"
    25	Wieringermeer				"7701","7702","7703","7704"
    26	Binnenduinrand Egmond		"04100","04150","04902","04220","04902-00"
    27	Geestmerambacht				"03764","03751","03240","03801","03802","03763","03300","03752"
    28	Waterland						"5170","5470","5821","5480","5230","5240","5560","5220","5180","5410","5250","5440","5500","5150","5510","5260","5520","5822","5200","5490","5210","5530","5540","5550","5570","5460","5600","5610","5620","5580","5390","5171"
    29	Schermer					"04851","04852","04853"
    30	Zijpe-West					"2751","2752","2775","2754","2780","2779","2050","2756"
    31	Oosterpolder Hoorn			"6110","6100"
    32	Westzaan					"04400","04390"
    33	Bergermeer					"04070","04080","04090","04952","04953","04640"
    34	Wieringerwaard				"2080"
    35	Schagerkogge				"03010","03020","03030","03040","03050","03060","03701","03702"
    36	Zeevang						"5701","5702","5703","5704","5705"
    37	Westerkogge					"6130"
    38	Alkmaardermeerpolders		"04250","04280","04260","04420","04270", "04240"
    39	Wieringen					"2851","2852","2854","2855","2856"
    40	Zijpe-Zuid					"2757","2758","2759","2781","2763","2764","2765","2766"
    41	Egmondermeer				"04130","04110","04951"
    42	Oostzaan					"5330","5340"
    43	HOUW (Wohoobur)				"6180","6190","6200","6210"
    44	Zijpe-Noord					"2767","2768","2772","2769","2773","2774","2120"
    45	Callantsoog					"2030","2040"
    46	Bergen-Noord				"04010","04020","04030","04040","04050","04060"
    47	Berkmeer e.o.				"6230","6240","03130","03140"
    48	Valkkoog en Schagerwaard	"03080","03090"
    49	Waar Woud Spek eet			"03100","03110","03120","03340"
    50	Wormer						"5270","5280","5290","5300"
    51	Eilandspolder				"04801","04802","04803","04804","04470"
    53	VRNK-West					"03160","03170","03180","03070"
    54	Anna Paulowna				"2803","2804","2805"
    55	NZK-polders					"04340","04580","04590","04610","04410"
    56	Beetskoog					"5010","5020","5030","5040","5050","5080"
    57	Texel-Zuid					"8010","8020","8030","8071"


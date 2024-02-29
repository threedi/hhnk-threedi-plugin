## **Initieel peil**
Het initieel peil in de modellen wordt uitgelezen uit de attributen tabel van de peilgebieden in de DAMO export, kolom peil_wsa. Het initieel peil wordt bepaald door gebruik te maken van onderstaande volgorde. 

1. Peil in HDB Hydrodeelgebied <br>
    a. Winterpeil <br>
    b. Zomerpeil
2. Vast peil uit DAMO.W_Streefpeil, namelijk: <br>
    a. 901  Vast peilbeheer; streefpeil jaarrond <br>
    b. 904  Dynamisch peilbeheer; streefpeil jaarrond <br>
    c. 915  Vrij afwaterend op buitenwater; ondergrenspeil jaarrond <br>
    d. 916  Vrij afwaterend op boezemwater; ondergrenspeil jaarrond <br>
    e. 918  Onderbemaling; ondergrenspeil <br>
    f. 919  Opmaling; bovengrenspeil <br>
    g. 920  Opstuwing; bovengrenspeil <br>
    h. 921  Op- en onderbemaling; ondergrenspeil <br>
    i. 922  Op- en onderbemaling; bovengrenspeil 
3. Winterpeil, namelijk: <br>
    a. 902  Seizoensgebonden peilbeheer; streefpeil winter <br>
    b. 907  Dynamisch seizoensgebonden peilbeheer; streefpeil winter 
4. Zomerpeil (maar vaak is dan ook een winterpeil aanwezig en zal dus winterpeil worden gekozen), namelijk: <br>
    a. 903  Seizoensgebonden peilbeheer; streefpeil zomer <br>
    b. 908  Dynamisch seizoensgebonden peilbeheer; streefpeil zomer <br>
    c. 917  Wateraanvoer Wieringermeer; streefpeil zomer
5. Flexibel peil <br>
    a. 914  Flexibel peilbeheer; bovengrenspeil jaarrond
6. Dataminingpeil obv 20-percentiel per peilgebied. De waterhoogtes hiervoor worden opnieuw afgeleid van de AHN3 en actueel ingetekende hydro-objecten uit de DAMO-database.

Als de peil_wsa kolom niet is ingevuld, wordt het streefpeil volgens bovenstaande lijst bepaald of wordt er gebruik gemaakt van de aanname NAP -10m. 
## **Initieel peil**
Het initieel peil wordt uitgelezen uit de attribute table van de peilgebieden, kolom peil_wsa. Deze kolom vullen we aan de hand van onderstaande volgorde:

1. Peil in HDB Hydrodeelgebied 
    * a. Winterpeil
    * b. Zomerpeil
2. Vast peil uit DAMO.W_Streefpeil, namelijk: 
    * a. 901  Vast peilbeheer; streefpeil jaarrond
    * b. 904  Dynamisch peilbeheer; streefpeil jaarrond
    * c. 915  Vrij afwaterend op buitenwater; ondergrenspeil jaarrond
    * d. 916  Vrij afwaterend op boezemwater; ondergrenspeil jaarrond
    * e. 918  Onderbemaling; ondergrenspeil
    * f. 919  Opmaling; bovengrenspeil
    * g. 920  Opstuwing; bovengrenspeil
    * h. 921  Op- en onderbemaling; ondergrenspeil
    * i. 922  Op- en onderbemaling; bovengrenspeil 
3. Winterpeil, namelijk: 
    * a. 902  Seizoensgebonden peilbeheer; streefpeil winter 
    * b. 907  Dynamisch seizoensgebonden peilbeheer; streefpeil winter 
4. Zomerpeil (maar vaak is dan ook een winterpeil aanwezig en zal dus winterpeil worden gekozen), namelijk:
    * a. 903  Seizoensgebonden peilbeheer; streefpeil zomer 
    * b. 908  Dynamisch seizoensgebonden peilbeheer; streefpeil zomer
    * c. 917  Wateraanvoer Wieringermeer; streefpeil zomer
5. Flexibel peil
    * a. 914  Flexibel peilbeheer; bovengrenspeil jaarrond
6. Dataminingpeil obv 20-percentiel per peilgebied. De waterhoogtes hiervoor worden opnieuw afgeleid van de AHN3 en actueel ingetekende hydro-objecten uit de DAMO-database.

Als deze kolom niet is ingevuld, wordt het peil streefpeil uit DAMO volgens bovenstaande lijst of wordt er gebruik gemaakt van de aanname NAP -10m 
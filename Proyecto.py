print ("""                        
    1.Región de Arica y Parinacota (15)
    2.Región de Tarapacá (01)
    3.Region de Antofagasta (02)
    4.Region de Atacama (03)
    5.Región de Coquimbo (04)
    6.Región de Valparaiso (05)
    7.Región Metropolitana (13)
    8.Región de  O'higgins (06)
    9.Región del Maule (07)
    10.Región del Ñuble (16)
    11.Región del Biobio (08)
    12.Región de la Araucania (09)
    13.Región de los Rios (14)
    14.Región de los Lagos (10)
    15.Región de Aysén  (11)
    16.Región de Magallanes (12)
    """) #Este print hace que muestre en formato lista, todas las regiones de chile

x = int(input("Ingrese el numero correspondiente segun la region: ")) # un input con un INT para ingresar valores numericos enteros para escoger una de las regiones que el usuario quiera
 

if x == 1: #se da una condicion if, ya que, en este if, si se ingresa un 1, damos paso a la informacion de arica y parinacota (segun mi menú) 
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")# aqui un input para ingresar una de las 2 opciones de este submenu
     

    if z == "a": #Si es usuario elige la opcion "a" del submenú, ingresa a esta condicion

        import matplotlib.pyplot as plt #Se hace un llamado a la libreria para que muestre el grafico
        ejex=['21/06/2021','22/06/2021','23/06/2021','24/06/2021','25/06/2021','26/06/2021','27/06/2021','28/06/2021','29/06/2021','30/06/2021','01/07/2021','02/07/2021','03/07/2021','04/07/2021']#En el eje X, mostrare los datos que estan dentro de esa lista
        ejey=[858,1497,2254,3102,4446,5656,6745,8414,9238,9898,10587,11891,12866,13908]# En el eje Y, mostrare los datos que estan dentro de esta lista
        plt.plot(ejex,ejey)# este plt.plot hace que se ingresen los datos de las variables, al grafico  
        plt.title("Examenes PCR acumulados en la Region de Arica y Parinacota")#Es un titulo para darle al grafico
        plt.show()#plt.show(), lo que hace es desplegar el grafico por pantalla

    if z == "b": #Si el usuario elige la opcion "b" en el submenu que está mas arriba, ingresa a esta condicion, que es basicamente el mismo codigo que el de la opcion "a", pero con distinta informacion
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021','22/06/2021','23/06/2021','24/06/2021','25/06/2021','26/06/2021','27/06/2021','28/06/2021','29/06/2021','30/06/2021','01/07/2021','02/07/2021','03/07/2021','04/07/2021']#En el eje X del grafico, se posicionará todo lo que está dentro de esta lista 
        primas = [858,639,757,848,1344,1210,1089,1669,824,660,689,1304,975,1042]# En el eje Y del grafico, se mostrara todo lo que está dentro de la lista "primas"

        plt.bar(range(14), primas, edgecolor='black')#Este plt.bar lo que hace es colocar que habran 14 barras, con el valor de la variable primas, y el borde de las barras será de color negro 

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Arica y parinacota ")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()
#Lo que resta de codigo ya viene siendo lo mismo que he explicado por el momento...

if x == 2:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021','22/06/2021','23/06/2021','24/06/2021','25/06/2021','26/06/2021','27/06/2021','28/06/2021','29/06/2021','30/06/2021','01/07/2021','02/07/2021','03/07/2021','04/07/2021']
        ejey=[2163,3404,4633,5724,7092,9248,9716,12022,13520,14437,15519,16804,18040,19388]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados Region de Tarapacá")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [	2163,1241,1229,1121,1368,1156,1468,2306,1498,917,1082,1285,1236,1348]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Tarapaca")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()

if x == 3:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[5502,9746,10659,13155,15660,17950,20390,25383,30535,31442,33721,36363,38613,41325]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de Antofagasta")
        plt.show()
        

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [5502,	4244,	913,	2496,	2505,	2290,	2440,	4993,	5152,	907,	2279,	2642,	2250,	2712]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Antofagasta")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()

if x == 4:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[1485,2515,3137,3889,5783,7280,8658,9703,10804,12339,13068,13849,16380,18016]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de Atacama")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [1485,	1030,	622,	752,	1894,	1497,	1378,	1405,	1101,	1535,	729,	781,	2531,	1636]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Atacama")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()


if x == 5:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[3513,5234,6389,7377,10078,12683,15292,18255,19476,20896,22046,23741,26516,30211]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de Coquimbo")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [3513,	1721,	1155,	988,	2701,	2605,	2609,	2963,	1221,	1420,	1150,	1695,	2775,	3695]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Coquimbo")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()

if x == 6:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[7064,10099,12103,15375,22253,28730,35616,40891,43745,45869,49255,55568,62258,69077]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de Valparaiso")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [7064,	3035,	2004,	3272,	6878,	6477,	6886,	5275,	2854,	2124,	3386,	6313,	6690,	6819]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Valparaiso")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()

if x == 7:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[26272,40018,49324,61231,83298,106748,129135,149813,158973,167211,178321,200032,221117,243542]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region Metropolitana")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [	26272,13746,9306,11907,22067,23450,2238,20678,9160,8238,11110,21711,21085,22425]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Metropolitana")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()


if x == 8:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[2712,4020,5120,6004,9114,12030,15307,17774,18949,19694,20578,23526,26406,29423]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de Ohiggins")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [2712,1308,1100,884,3110,2916,3277,2467,1175,745,884,2948,2880,3107]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region O'higgins")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()


if x == 9:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[4103,5834,6890,8401,12217,16746,21730,26420,28242,29135,30542,34620,38942,43036]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region del Maule")
        plt.show()

    if z == "b":
        
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [4103,1731,105	,1511,3816,4529,4984,4690,1822,893,1407,4078,4322,4094]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Maule")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()


if x == 10:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[2194,3601,4097,4881,6649,8319,10173,11566,12367,12860,13603,15520,17216,19049]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region del Ñuble")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [2194,1407,496,784,1768,1670,1854,1393,801,493,743,1917,1696,1833]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Ñuble")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()


if x == 11:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[6287,9495,12145,17866,26246,33500,40551,48510,51699,53999,59722,65445,73720,81179,88062]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region del Biobio")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [6287,	3208,2650,5721,8380,7254,7051,7959,3189,2300,5723,8275,7459,6883]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region biobio")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()


if x == 12:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[3259,5125,5894,7484,10715,14059,17304,20394,21768,22801,24161,27074,30326,33715]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de la Araucania")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [3259,1866,769,1590,3231,3344,3245,3090,1374,1033,1360,2913,3252,3389]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region de la Araucania")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()


if x == 13:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[1545,2418,2972,3854,6472,8972,11291,12814,13784,14268,15196,17761,19956,22153]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de Los Rios")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [1545,	873,554,882,2618,2500,2319,1523,970,484,928,2565,2195,2197]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region de los Rios")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()


if x == 14:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[3777,5844,6911,8908,14157,19568,24372,28858,31018,32128,34092,39331,44613,49105]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de Los Lagos")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [3777,2067,1067,1997,5249,5411,4804,4486,2160,1110,1964,5239,5282,4492]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region de los Lagos")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()

if x == 15:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[669,921,1008,1389,2139,2671,3393,3936,4169,4346,4696,5195,5676,6201]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de Aysen")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [669,252,87,381,750,532,722,543,233,177,350,499,481,525]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region de Aysén del General Carlos Ibáñez del Campo")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()

if x == 16:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        ejey=[1076,1321,1623,1916,2922,3700,4593,5183,5618,5919,6179,7126,8164,8836]
        plt.plot(ejex,ejey)
        plt.title("Examenes PCR acumulados en la Region de Magallanes")
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021', '22/06/2021', '23/06/2021', '24/06/2021', '25/06/2021', '26/06/2021', '27/06/2021', '28/06/2021', '29/06/2021' ,'30/06/2021' ,'01/07/2021','02/07/2021' ,'03/07/2021','04/07/2021']
        primas = [1076,245,302,293,1006,778,893,590,435,301,260,947,1038,672]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region de Magallanes")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()

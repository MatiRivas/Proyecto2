
print("""Como desea realizar su busqueda?:
a.- Nombre
v = input(b.- Codigo
""")

print ("""
    1.Región de Arica y Parinacota (15)
    2.Región de Tarapacá (01)
    3.Region de Antofagasta (02)
    4.Region de Atacama (03)
    5.Región de Coquimbo (04)
    6.Región de Valparaiso (05)
    7.Región Metropolitana (13)
    8.Región del Libertador General Bernardo O'higgins (06)
    9.Región del Maule (07)
    10.Región del Ñuble (16)
    11.Región del Biobio (08)
    12.Región de la Araucania (09)
    13.Región de los Rios (14)
    14.Región de los Lagos (10)
    15.Región de Aysén del General Carlos Ibáñez del Campo (11)
    16.Región de Magallanes (12)
    """)
x = int(input("Ingrese el numero correspondiente segun la region: "))

if x == 1:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":
        import matplotlib.pyplot as plt
        ejex=[999,1000,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
        plt.show()

    if z == "b":
    
        import matplotlib.pyplot as plt
        fechas = ['21/06/2021','22/06/2021','23/06/2021','24/06/2021','25/06/2021','26/06/2021','27/06/2021','28/06/2021','29/06/2021','30/06/2021','01/07/2021','02/07/2021','03/07/2021','04/07/2021']
        primas = [858,639,757,848,1344,1210,1089,1669,824,660,689,1304,975,1042]

        plt.bar(range(14), primas, edgecolor='black')

        plt.xticks(range(14), fechas, rotation=60)
        plt.title("examenes PCR no acumulados Region Arica y parinacota ")
        plt.ylim(min(primas)-1, max(primas)+1)
        plt.show()


if x == 2:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

    if z == "a":

        import matplotlib.pyplot as plt
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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
        ejex=[4,8,13,17,20]
        ejey=[54,67,98,78,45]
        plt.plot(ejex,ejey)
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

import matplotlib.pyplot as plt
import pandas as pd
regiones = ['Arica y Parinacota', 'Tarapaca', 'Antofagasta', 'Atacama', 'Coquimbo', 'Valparaiso', 'Metropolitana', 'Ohiggins', 'Maule', 'Ñuble', 'Biobio', 'Araucania', 'Los Rios', 'Los Lagos', 'Aysen ', 'Magallanes']
codigos = ['15', '01', '02', '03', '04', '05', '13', '06', '07', '16', '08', '09', '14', '10', '11', '12']

archivo = open("c:/Matia/Desktop/Proyecto Progra/PCR_T.csv", "r")
contenido = archivo.readlines()
print(contenido)

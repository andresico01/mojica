
import datetime
import csv
import pandas as pd
import numpy as np


def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_maximo(datos_pandas, file_name)
    funcion_Minimo(datos_pandas, file_name)
    funcion_Promedio(datos_pandas, file_name)
    funcion_Varianza(datos_pandas, file_name)
    funcion_Mediana(datos_pandas, file_name)
    funcion_Desviacion(datos_pandas, file_name)
    datos_graficar = leer_datos(file_name)


    return datos_graficar


def funcion_Varianza(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]

    total = 0
    n = len(valores_temperatura)
    media = float(sum(valores_temperatura))/n
    for i in valores_temperatura:
        valor = i - media
        cuadrado = valor**2
        total += cuadrado

    varianza = total / (n-1)
    dato_guardar = [1, date_string, "Varianza", varianza]
    guardar(dato_guardar, file_name)


def funcion_Desviacion(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    Desviacion = np.std(valores_temperatura)
    dato_guardar = [1, date_string, "Desviacion", Desviacion]
    guardar(dato_guardar, file_name)


def funcion_maximo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    dmax= max(valores_temperatura)
    dato_guardar = [1, date_string, "Maximo", dmax]
    guardar(dato_guardar, file_name)
    
    



def  funcion_Minimo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    dmin=min(valores_temperatura)
    dato_guardar = [1, date_string, "Minimo", dmin]
    guardar(dato_guardar, file_name)
    


def funcion_Promedio(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    from statistics import mean
    prom=mean(valores_temperatura)
    dato_guardar = [1, date_string, "Promedio", prom]
    guardar(dato_guardar, file_name)



def funcion_Mediana(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    Mediana = np.median(valores_temperatura)
    dato_guardar = [1, date_string, "Mediana", Mediana]
    guardar(dato_guardar, file_name)



def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas


def guardar(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)

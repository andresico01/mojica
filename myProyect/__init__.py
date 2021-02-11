
import datetime
import csv
import pandas as pd
import numpy as np

def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas


def guardar(leer_datos, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(leer_datos(file_name))

def funcion_Varianza(leer_datos, file_name,guardar):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    data = leer_datos(file_name)
    valores_temperatura = data[data["sensor"] == "Temperatura"]["value"]
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


def funcion_Desviacion(leer_datos, file_name,guardar):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    data = leer_datos(file_name)
    valores_temperatura = data[data["sensor"] == "Temperatura"]["value"]
    Desviacion = np.std(valores_temperatura)
    dato_guardar = [1, date_string, "Desviacion", Desviacion]
    guardar(dato_guardar, file_name)


def funcion_maximo(leer_datos,file_name,guardar):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    data = leer_datos(file_name)
    valores_temperatura = data[data["sensor"] == "Temperatura"]["value"]
    dmax= max(valores_temperatura)
    dato_guardar = [1, date_string, "Maximo", dmax]
    guardar(dato_guardar, file_name)
    
    



def  funcion_Minimo(leer_datos, file_name,guardar):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    data = leer_datos(file_name)
    valores_temperatura = data[data["sensor"] == "Temperatura"]["value"]
    dmin=min(valores_temperatura)
    dato_guardar = [1, date_string, "Minimo", dmin]
    guardar(dato_guardar, file_name)
    


def funcion_Promedio(leer_datos, file_name,guardar):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    data = leer_datos(file_name)
    valores_temperatura = data[data["sensor"] == "Temperatura"]["value"]
    from statistics import mean
    prom=mean(valores_temperatura)
    dato_guardar = [1, date_string, "Promedio", prom]
    guardar(dato_guardar, file_name)



def funcion_Mediana(leer_datos, file_name,guardar):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    data = leer_datos(file_name)
    valores_temperatura = data[data["sensor"] == "Temperatura"]["value"]
    Mediana = np.median(valores_temperatura)
    dato_guardar = [1, date_string, "Mediana", Mediana]
    guardar(dato_guardar, file_name)




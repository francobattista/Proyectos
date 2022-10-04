#####PERCEPTRON######
from tokenize import String
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#POR LAS COSAS QUE PROBE, FUNCIONA EXCELENTE. TENGO Q VER EL TEMA DEL GRAFICO (POR EL MOMENTO ESTA HARDCODEADO)

def readData(arch):
    return pd.read_csv(arch) 

def initVars():
    for i in range(cant_entradas + 1): #sumando la columna del umbral
        weights.append(0)
    
    return weights

def calc_activacion(weights,data):
    return np.dot(weights,data)


def calc_y(v):
    if(v >= 0):
        return 1
    return -1

def calc_w(weights,norm,error,dato_actual):
    return weights + (norm)*(error)*dato_actual

def calc_error(v):
    return 

def grafica(w):
    plt.scatter(df.iloc[:,0],df.iloc[:,1])

    plt.plot([1,2,3,4],[1,0.5,0,-0.5]) #[1,2,3,4,5,6,7],[0.3496,0.9171,1.4847,2.0523,2.6198,3.1874,3.7550]

    plt.show()

def main():
    weights = initVars()

    targets = df.iloc[:,2] #Los targets

    datos = df.copy(deep=True) 

    datos.iloc[:,2] = 1 #Tien el umbral. El negativo se lo agrego despues en la resta
    #EL ALGORITMO FUNCIONA, EL UNICO TEMITA ES EL DEL UMBRAL. SI LO PONGO -1, ME AFECTA LOS X.

    end = False 
    hayError = True
    while(hayError):

        hayError = False
        for i in range(cant_datos): #Despues lo voy a reemplazar para no hacer tantos for, pero por ahora me es mas facil
            print('---------------DATO' + str(i) + '-------------------------')
            dato_actual = datos.iloc[i]
            v = calc_activacion(weights,dato_actual)
            print("VALOR DE V ",v)
            y = calc_y(v)
            print("VALOR DE Y ",y)
            error = targets.iloc[i]-y
            if(error != 0):
                hayError = True
            print("VALOR DE error ",error)
            weights = calc_w(weights,norm,error,dato_actual)
            print(weights)

    grafica(weights) #Me pasa pasarle la funcion resultado. Para el ejemplo de la catedra anda pipi cucu


df = []
df = readData('and.csv')
weights = []
cant_entradas = 2
norm = 0.5
cant_datos = df.shape[0]
main()

#EJERCICIO 2 -> DATA.CSV

#EJERCICIO 3 -> TEXTCK.

#EJERCICIO 4 -> EN LOS TARGETS USO -1 PQ ASI PROGRAME EL ALGORITMO. DEBERIA CAMBIARLO SEGUN EL CASO
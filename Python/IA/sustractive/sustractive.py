import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math as Math


def readData(name):
    return pd.read_csv(name + '.csv')

def calculaPotencialesIniciales():
    potenciales=[]
    for i in range(n):
        potenciales.append(formula(i))
    return potenciales

def formula(i):
    value = 0
    for j in range(n):
        value += (Math.e**(-((np.linalg.norm(data.iloc[i]-data.iloc[j]))/((Ra/2)**2))))
    return value

def calculaCentros(potencialesIniciales):
    cdk = pd.DataFrame([],columns=['X1','X2'])
    index = potencialesIniciales.index(max(potencialesIniciales))
    cdk.append(data.iloc[index])
    potencialesIniciales[index] = 0.0 #no se si se pasan por referencia o por valor, creo q los arreglos siempre son por ref.
    return cdk, potencialesIniciales #si, los pasa por referencia asi q al pedo hacer esto pero ya q estamos lo dejo asi


def recalculoPotenciales():
    pass

def main():
    potencialesIniciales = calculaPotencialesIniciales()
    it=0
    while(it<1):

        cdk, potencialesIniciales = calculaCentros(potencialesIniciales)

        potencialesIniciales = recalculoPotenciales()

        it+=1

data = readData("data")
#Hiperparametros
Ra = 0.6
Rb = 0.9
n = data.shape[0]
cdk = pd.DataFrame([],columns=['X1','X2'])


main()









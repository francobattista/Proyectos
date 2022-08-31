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

def calculaCentros(potencialesIniciales,centrosOriginal, potencialCdk):
    
    rta=False
    index = potencialesIniciales.index(max(potencialesIniciales))
    
    if(acceptedRatio(potencialCdk, potencialesIniciales[index])):
        centrosOriginal.append(data.iloc[index])
        rta=True
    #potencialesIniciales[index] = 0.0 #no se si se pasan por referencia o por valor, creo q los arreglos siempre son por ref.

    return centrosOriginal, rta  #si, los pasa por referencia asi q al pedo hacer esto pero ya q estamos lo dejo asi


def recalculoPotenciales(potenciales,cdk,data):
    p = []
    cdkActual = cdk[len(cdk)-1] #me da el length de cdk, por ende la ultima posicion, y por ened el que tengo q usar
    cdkIndex = busca(cdkActual,data)
    #index = (potenciales.[x]) #me da la posicion que esta el elemento q encontre arriba
    for i in range(n):
        p.append(potenciales[i]-(potenciales[cdkIndex]*Math.e**(-((np.linalg.norm(data.iloc[i] - data.iloc[cdkIndex]))/((Rb/2)**2)))))
    return p, potenciales[cdkIndex]

def busca(cdkActual,data):
    index = -1
    for i in range(n):
        if((data.iloc[i] == cdkActual).all()):
            index=i

    return index


def acceptedRatio(potCdk, potMax):
    print(potCdk)

    print(potMax)

    print(((AR/100) * potCdk))
    return potMax > ((AR/100) * potCdk)

def main():
    cdk = [] #no usar dataFrane por ahora
    checkAR = True
    potencialCdk = -1
    potencialesIniciales = calculaPotencialesIniciales()
    it=0
    while(checkAR): # == True
        #acceptedRatio(maxPotencial,AR,potencialCdk)):

        cdk, checkAR = calculaCentros(potencialesIniciales,cdk,potencialCdk)


        potencialesIniciales, potencialCdk = recalculoPotenciales(potencialesIniciales,cdk,data)


        print(cdk)


data = readData("data")
#Hiperparametros
Ra = 0.6
Rb = 0.9
AR = 60
n = data.shape[0]



main()


#AR 0.6






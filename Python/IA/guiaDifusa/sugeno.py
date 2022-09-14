from calendar import c
import pandas as pd
import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt



def cuadratica(x,a,b,c):
    return a*(x**2) + b*x + c

def lineal():
    pass


#Espacio o dominio
eX = np.linspace(-20,20,10) #el espacio para representarlas. Desde -20 a 20 (Ese es el rango que van los puntos). el 3er parametro es la cantidad de datos devuelve. 


#Funciones linguisticas entradas
fPequeño = fuzz.gbellmf(eX,6,4,-10) #gbell es de por la campana

fMediano = fuzz.gbellmf(eX,4,4,0)

fGrande = fuzz.gbellmf(eX,6,4,10)


#Entrada de prueba
entradaPrueba = -10

plt.plot(eX,fPequeño)

plt.plot(eX,fMediano)

plt.plot(eX,fGrande)

plt.plot([entradaPrueba,entradaPrueba],[0.0,1.0],linestyle = "--")

plt.show()

#ENTRADA -> ENTRE MENOS DIEZ Y DIEZ

entrada = np.arange(-10,10)


#Camapanas especializadas en entrada, calculando w
salidaZ = []
for i in range(len(entrada)):
    w1 = fuzz.gbellmf(entrada[i],6,4,-10) #gbell es de por la campana

    w2 = fuzz.gbellmf(entrada[i],4,4,0) #gbell es de por la campana

    w3 = fuzz.gbellmf(entrada[i],6,4,10) #gbell es de por la campana

    print(w1)
    print(w2)
    print(w3)

    #Valores w especializados en salida

    z1= cuadratica(w1,1,0.1,6.4) #Pequeña

    z2= cuadratica(w2,1,-0.5,4) #Mediana

    z3= cuadratica(w3,1.8,1,-2) #Grande

    print(z1)
    print(z2)
    print(z3)



    #Salida con la formulita
    form = ((w1*z1) + (w2*z2) + (w3*z3)) / (w1 + w2 + w3)
    print(form)
    print(entrada[i])
    plt.scatter(entrada[i],form)
    salidaZ.append(form)




plt.show()
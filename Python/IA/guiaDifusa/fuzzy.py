
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#errorx = np.linspace(-20,20,10)

#xBaja = fuzz.trapmf(errorx,[-20, -15, -6, -3])
#xMedia = fuzz.trapmf(errorx,[-6, -3,3,6])
#xAlta = fuzz.trapmf(errorx,[3,6,15,20])

#errory = np.linspace(-3,15,10)

#yBaja = fuzz.trapmf(errory,[-2.46, -1.46,1.46,2.46])
#yMedia = fuzz.trapmf(errory,[1.46,2.46,5,7])
#yAlta = fuzz.trapmf(errory,[5,7,13,15])


#plt.plot(errorx,xBaja,label='XBAJA')

#plt.plot(errorx,xMedia,label='XMEDIA')

#plt.plot(errorx,xAlta,label='XALTA')

#plt.show()


#plt.plot(errory,yBaja,label='yBAJA')

#plt.plot(errory,yMedia,label='yMEDIA')

#plt.plot(errory,yAlta,label='yALTA')


#entradaX = np.array([-8]) #,-5,5,8

#xBaja = fuzz.trapmf(entradaX,[-20, -15, -6, -3])
#xMedia = fuzz.trapmf(entradaX,[-6, -3,3,6])
#xAlta = fuzz.trapmf(entradaX,[3,6,15,20])

#plt.plot(xBaja,label='XBAJA')

#print(xBaja)

#plt.plot(xMedia,label='XMEDIA')

#plt.plot(xAlta,label='XALTA')

#plt.plot([entradaX,entradaX],[0.0,1.0],linestyle = "--")


#plt.show()


#VAMOSW DE NUEVO!


def union(data):
    aux = np.zeros(data[0].size)
    for j in range(len(data)):
        for i in range(aux.size):
            aux[i] = max(aux[i], data[j][i])
    return aux


def cut(value, mf):
    value = float(value)
    aux = np.zeros(mf.size)
    if (type(value) is int) or (type(value) is float):
        for i in range(mf.size):
            aux[i] = min(value, mf[i])
        return aux
    else:
        return -1

#---------------memberships antecendentes---------
eX = np.linspace(-30,20,10) #el espacio para representarlas. Desde -20 a 20 (Ese es el rango que van los puntos). el 3er parametro es la cantidad de datos devuelve. 

funcXBaja = fuzz.trapmf(eX,[-20, -15, -6, -3])

funcXMedia = fuzz.trapmf(eX,[-6, -3,3,6])

funcXAlta = fuzz.trapmf(eX,[3,6,15,20])

#-----------memberships consecuentes-------------
eY = np.linspace(-10,15,10)


funcYBaja = fuzz.trapmf(eY,[-2.46, -1.46,1.46,2.46])

funcYMedia = fuzz.trapmf(eY,[1.46,2.46,5,7])

funcYAlta = fuzz.trapmf(eY,[5,7,13,15])

#-------------------------------
entradaX = np.array([-8]) #,-5,5,8 ENTRADA!
#-----------------------------

#Valores de verdad de las funciones de membresia de entrada, para alta, baja y media, EN LOS PUNTOS DE "entradaX"
#Estos son los valores de cuanto pertenece el valor ingresado a cada funcion
valorXBaja = fuzz.trapmf(entradaX,[-20, -15, -6, -3])
valorXMedia = fuzz.trapmf(entradaX,[-6, -3,3,6])
valorXAlta = fuzz.trapmf(entradaX,[3,6,15,20])


plt.plot(eX,funcXBaja, label = "XBAJA") #Para el plot le tengo que pasar el primer parametro que me arma el dominio. Es para decirlde de donde empieza
plt.plot(eX,funcXMedia, label = "XMEDIA")
plt.plot(eX,funcXAlta, label = "XALTA")


plt.plot([entradaX,entradaX],[0.0,1.0],linestyle = "--")

plt.show()


plt.plot(eY,funcYBaja, label = "YBAJA") #Para el plot le tengo que pasar el primer parametro que me arma el dominio. Es para decirlde de donde empieza
plt.plot(eY,funcYMedia, label = "YMEDIA")
plt.plot(eY,funcYAlta, label = "YALTA")

#plt.plot([entradaX,entradaX],[0.0,1.0],linestyle = "--")

plt.show()




#Con estos 3 valores, tengo que actuar sobre las salidas. Tengo que cortar las funciones con estos valores que obtuve (truncarlos) LAS QUE SE CORTAN SON LAS CONSECUENTES

#METODO DE INFERENCIA 

funcYBajaPrima = cut(valorXBaja,funcYBaja)
funcYMediaPrima = cut(valorXMedia,funcYMedia)
funcYAltaPrima = cut(valorXAlta,funcYAlta)


#NO PUDE UNIR LAS FUNCIONES NO SE POR QUE.


result = union([funcYBajaPrima,funcYMediaPrima,funcYAltaPrima])


plt.plot(eY,result,label="RESULTADO")

plt.show()



#DEFUZIFICACION

centroid = fuzz.defuzz(eY,result,'centroid')

print(centroid)



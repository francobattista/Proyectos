import skfuzzy as fuzz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

def circulo(num_datos = 100,R = 1, minimo = 0,maximo= 1, center_x = 0 , center_y = 0):
    pi = math.pi
    r = R * np.sqrt(np.random.uniform(minimo, maximo, size = num_datos)) 
    theta = np.random.uniform(minimo, maximo, size= num_datos) * 2 * pi

    x = center_x + np.cos(theta) * r
    y = center_y + np.sin(theta) * r

    x = np.round(x,3)
    y = np.round(y,3)

    df = np.column_stack([x,y])
    df = pd.DataFrame(df)
    df.columns = ['x','y']

    
    return(df)
    
def suma_ipertenencias(i,centros,datos,k):
    value=0
    for x in range(k):
        if((datos.iloc[i] == centros[x]).all()):
            print("Div por cero, que hago?")
        else:
            value += ((1/(np.linalg.norm(datos.iloc[i]-centros[x])))**(1/(q-1)))
    return value
         


def calculoMki(datos,centros,n,c):

    list = [[0.0,0.0] for i in range(n)] #RECORDAR QUE SI NECESITO QUE SEA DE FLOATS LE TENGO QUE INDICAR CON .0 ESTO LO TENGO Q GENERALIZAR PQ AHORA ESTA PARA 2 
    per = pd.DataFrame(list,columns=c)

    for i in range(n):
        for j in range(k):
            if((datos.iloc[i] == centros[j]).all()):
                per.iloc[i]['K' + str(j) ] = 1 ##CAMBIAR!!!!!!
            else:
                per.iloc[i]['K' + str(j) ] = ((1/(np.linalg.norm(datos.iloc[i]-centros[j])))**(1/(q-1)))/suma_ipertenencias(i,centros,datos,k) #recordar que "linalg.norm" es el metodo para la norma matematica. Con pasarle dos puntos x e y me saca la distancia

    return per


def calc_pertenencias(mat_datos,centros_k,n,k):
    columnas = []
    for i in range(k):
        columnas.append('K'+ str(i) ) #me va creando el siguiente array : [X1,X2,.....]
    pertenencias = pd.DataFrame(columns=columnas)
    print("DATOS")
    print(mat_datos)

    print("PERTENENCIAS")
    print(pertenencias)

    print("CDK")
    print(centros_k)

    pertenencias = calculoMki(mat_datos,centros_k,n,columnas)    
    return pertenencias


def dist_euclidea_arr_v2(arr, x2): #ni lo use alfinal
    dista = []
    for i in range(arr.shape[0]):
        dista.append(np.linalg.norm(arr[i]-x2))
    
    return np.array(dista)

def def_labels(pertenencias,n):
    labels=[]
    for i in range(n):
        labels.append(max(pertenencias.iloc[i]))
    return labels

def readData():
    return pd.read_csv('data.csv')

def max(v):
    max = -10000000000000000000
    maxIn = -1
    for i in range(len(v)):
        if(v['K' + str(i)] > max):
            max=v[i]
            maxIn = i
    return maxIn

def actualiza_k(p,n,k,d):
    clusters = []
    for j in range(k):
        valor1=0
        valor2=0
        for i in range(n):
            valor1 += (((p.iloc[i]['K' + str(j)])**(q))*d.iloc[i]) #mat
            valor2 += ((p.iloc[i]['K' + str(j)])**(q)) #escalar
        clusters.append(valor1/valor2)

    return clusters

def sumatoriaPrueba(p,n,k):
    valor=0
    for i in range(n):
        valor += ((p.iloc[i]['K' + str(k)])**(q))
    
    return valor


def init_centros(mat_datos):
    
    arr = []
    arr.append(mat_datos.iloc[10])
    arr.append(mat_datos.iloc[20])
    #arr.append(mat_datos.iloc[30])
    return arr

def main():
    it=0
    centros_k = init_centros(mat_datos)

    while(it<30):
        mat_pertenencias = calc_pertenencias(mat_datos,centros_k,n,k)

        mat_labels= def_labels(mat_pertenencias,n)

        centros_k = actualiza_k(mat_pertenencias,n,k,mat_datos)

        it+=1

    colors = {0:'red', 1:'blue', 2:'green'}
    
    print(centros_k)

    print(mat_labels)
    #plt.scatter(d1['x'], d1['y'], c = 'b')
    #plt.scatter(d2['x'], d2['y'], c = 'r')
    #plt.scatter(d3['x'], d3['y'], c = 'g')
    plt.scatter(mat_datos['X'],mat_datos['Y'])
    
    plt.scatter(centros_k[0]['X'], centros_k[0]['Y'], c = 'black') #ATENCION! PARECE QUE LOS CENTROS ESTUVIERAN MAL PERO EN ESTE GRAFICO HAY OTRA ESCALA ENTONCES ME LOS PRINTEA LEJOS
    plt.scatter(centros_k[1]['X'], centros_k[1]['Y'], c = 'yellow')
    #plt.scatter(centros_k[2]['x'], centros_k[2]['y'], c = 'orange')
    plt.show()

    return centros_k


########LECUTRA Y PLOTEO DATOS#############

mat_datos = pd.read_csv('data.csv')

for i in range(len(mat_datos)):
    plt.scatter(mat_datos.iloc[i][0],mat_datos.iloc[i][1])
plt.show()


######FUZZY CMEANS#################

#mat_datos = readData()
#datos_1 = circulo(num_datos = 20,R = 10, center_x = 5, center_y = 30)
#datos_2 = circulo(num_datos = 20,R = 10, center_x = 20, center_y = 10)
#datos_3 = circulo(num_datos = 20,R = 10, center_x = 50, center_y = 50)
#mat_datos = datos_1.append(datos_2,ignore_index=True).append(datos_3,ignore_index=True)
k=2
#print(mat_datos)
n=mat_datos.shape[0]
q=1.5
cdk = main()


#######SUGENO#######

#Cada cdk es un cluster. Sugiere no mas de 2 cdk

#Espacio o dominio
eX = np.linspace(-1,1,10) #el espacio para representarlas. Desde -20 a 20 (Ese es el rango que van los puntos). el 3er parametro es la cantidad de datos devuelve. 


print("cenmtritos")
print(cdk[0]['X'])
print(cdk[1]['X'])


#Funciones linguisticas entradas
f1= fuzz.gbellmf(eX,0.58-0.46,cdk[0]['X'],0.1) #gbell es de por la campana.
f2 = fuzz.gbellmf(eX,0.665-0.587,cdk[1]['X'],0.1) #gbell es de por la campana.


plt.plot(f1)
plt.plot(f2)
plt.show()

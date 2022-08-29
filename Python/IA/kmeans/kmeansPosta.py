import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



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


def readData():
    return pd.read_csv('data1.csv',',')

def dist_euclidea_arr_v2(arr, x2):
    dista = []
    for i in range(arr.shape[0]):
        dista.append(np.linalg.norm(arr.loc[i]-x2))

    
    return dista#np.array(dista)

def recalcula_centros(labels,arr_puntos,n,k):
    proms = [0 for i in range(3)]
    conts = [0 for i in range(3)]

    
    print("DATOS")

    print(arr_puntos)
    


    
    for i in range(n):
        proms[labels[i]] += arr_puntos.iloc[i]#labels[i]][i]
        conts[labels[i]] += 1 #contador

    print("PROMEDIOS")
    print(proms)
    resultado = []
    for i in range(k):
        #if(conts[i]==0):
         #   resultado.append(proms[i]/1)
        #else:
        resultado.append(proms[i]/conts[i])
    print("RESULTADO")
    print(resultado)
        
    return resultado

def min(x1,x2,x3):
    arr = []
    arr.append(x1)
    arr.append(x2)
    arr.append(x3)

    return arr.index(np.array(arr).min())

def calcula_minimos(n,distances_matrix):
    min_matrix=[]

    for i in range(n):
        min_matrix.append(min(distances_matrix[0][i],distances_matrix[1][i],distances_matrix[2][i])) #me da la posicion del minimo, es decir, el cluster

    return min_matrix



def init_clusters(data,k):
    arr = []

    arr.append(data.loc[0])
    
    arr.append(data.loc[10])

    arr.append(data.loc[20])
    #for i in range(k):
    #   arr.append(data.loc[i]) #Que inicie con los k primeros datos (aleatorio y arbitrario)
    return arr
        

def init_distances(data,k,cluster_center):
    distances = []
    for i in range(k):
        distances.append(dist_euclidea_arr_v2(data,cluster_center[i]))
    return distances

def main(k):
    datos_1 = circulo(num_datos = 20,R = 10, center_x = 5, center_y = 30)
    datos_2 = circulo(num_datos = 20,R = 10, center_x = 20, center_y = 10)
    datos_3 = circulo(num_datos = 20,R = 10, center_x = 50, center_y = 50)
    data = datos_1.append(datos_2,ignore_index=True).append(datos_3,ignore_index=True)



    #data=readData()
    n=data.shape[0]
    cluster_center = init_clusters(data,k)
    distances_matrix = init_distances(data,k,cluster_center) #Entre los puntos y los K CentrosDK
    it=0
    while(it < 20):
        labels_matrix = calcula_minimos(n,distances_matrix)

        cluster_center = recalcula_centros(labels_matrix,data,n,k)

        distances_matrix = init_distances(data,k,cluster_center)

        it += 1

    colors = {0:'red', 1:'blue', 2:'green'}
    
    plt.scatter(datos_1['x'], datos_1['y'], c = 'b')
    plt.scatter(datos_2['x'], datos_2['y'], c = 'r')
    plt.scatter(datos_3['x'], datos_3['y'], c = 'g')

    plt.scatter(cluster_center[0]['x'], cluster_center[0]['y'], c = 'black') #ATENCION! PARECE QUE LOS CENTROS ESTUVIERAN MAL PERO EN ESTE GRAFICO HAY OTRA ESCALA ENTONCES ME LOS PRINTEA LEJOS
    plt.scatter(cluster_center[1]['x'], cluster_center[1]['y'], c = 'yellow')
    plt.scatter(cluster_center[2]['x'], cluster_center[2]['y'], c = 'orange')
    plt.show()



main(3)

#Aclaracion: el algoritmo funciona para 3 clusters. Esta hecho para mas clusters pero por ej en linea 79 me dio paja darle vuelta. Las inicializaciones tamb son par 3 k
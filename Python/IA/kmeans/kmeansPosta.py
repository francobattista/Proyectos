import math
import pandas as pd
import numpy as np



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

def recalcula_centros(labels,arr,n):
    proms = [0 for i in range(60)]
    conts = [0 for i in range(60)]
    print(labels)
    
    print(arr)
    for i in range(n):
        proms[labels[i]] += arr[labels[i]][i]
        conts[labels[i]] += 1 #contador

    resultado = []
    for i in range(n):
        if(conts[i]==0):
            resultado.append(proms[i]/1)
        else:
            resultado.append(proms[i]/conts[i])
        
    return resultado

def min(x1,x2,x3):
    arr = []
    arr.append(x1)
    arr.append(x2)
    arr.append(x3)
    print(arr)

    print(np.array(arr).min())
    return arr.index(np.array(arr).min())

def calcula_minimos(n,distances_matrix):
    min_matrix=[]

    print("MAT DISTANCIAS")
    print(distances_matrix[0][1])
    for i in range(n):
        min_matrix.append(min(distances_matrix[0][i],distances_matrix[1][i],distances_matrix[2][i])) #me da la posicion del minimo, es decir, el cluster
    print("minimos")
    print(min_matrix)
    return min_matrix



def init_clusters(data,k):
    arr = []
    for i in range(k):
        arr.append(data.loc[i]) #Que inicie con los k primeros datos (aleatorio y arbitrario)
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
    print(data)

    #data=readData()
    n=data.shape[0]
    cluster_center = init_clusters(data,k)
    distances_matrix = init_distances(data,k,cluster_center) #Entre los puntos y los K CentrosDK
    it=0
    while(it < 20):
        labels_matrix = calcula_minimos(n,distances_matrix)
        cluster_center = recalcula_centros(labels_matrix,distances_matrix,n)
        distances_matrix = init_distances(data,k,cluster_center)
        it += 1



main(3)
from mimetypes import init
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



def readData():
    data = pd.read_csv('data.csv') #ya es un dataFrame
    return data


################################################################


def init_centroids(data, k):
    n_dims = data.shape[1] #numero de columnas o dimensiones
    centroid_min = data.min().min() 
    centroid_max = data.max().max()
    centroids = [] #lista de centroides
    for centroid in range(k): #Recorro los k clusters
        centroid = np.random.uniform(centroid_min, centroid_max, n_dims) #Agarra un centroide aleatorio
        centroids.append(centroid) #Lo mete en la lista inicial de centroides

    print(centroids)
    centroids = pd.DataFrame(centroids, columns = data.columns) #creo un DF con los centroides

    return centroids




################################################################


def euclide_distance(a, b):
    return np.square(np.sum((a-b)**2))

################################################################

def kmeans(data, k):
    pass


################################################################


def show():
    datos_1 = pd.read_csv('data1.csv')
    datos_2 = pd.read_csv('data2.csv')
    datos_3 = pd.read_csv('data3.csv')
    plt.scatter(datos_1['x'], datos_1['y'], c = 'b')
    plt.scatter(datos_2['x'], datos_2['y'], c = 'r')
    plt.scatter(datos_3['x'], datos_3['y'], c = 'g')
    plt.show()



################################################################
def main():
    data=readData()
    centroids=init_centroids(data, 3)
    distancias = np.array([])
    for centroid in range(centroids.shape[0]):
        d = euclide_distance(centroids.iloc[centroid, :2], data.iloc[0,:2])
        distancias = np.append(distancias, d)

    print(centroids)
    print(distancias)


main()

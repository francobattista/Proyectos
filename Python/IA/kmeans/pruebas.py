import math
import numpy as np
import pandas as pd
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

################################################################

def show(datos_1,datos_2,datos_3):
    plt.scatter(datos_1['x'], datos_1['y'], c = 'b')
    plt.scatter(datos_2['x'], datos_2['y'], c = 'r')
    plt.scatter(datos_3['x'], datos_3['y'], c = 'g')
    plt.show()


def show2(data,centroids):
    plt.scatter(data.iloc[1:,0], data.iloc[1:,1],  marker = 'o', alpha = 0.2)
    plt.scatter(centroids.iloc[:,0], centroids.iloc[:,1],  marker = 'o', c = 'r')
    plt.scatter(data.iloc[0,0], data.iloc[0,1],  marker = 'o', c = 'g')
    for i in range(centroids.shape[0]):
        plt.text(centroids.iloc[i,0]+1, centroids.iloc[i,1]+1, s = centroids.index[i], c = 'r')

    plt.show()

################################################################

def assign_centroid(data, centroids):
    '''
    Receives a dataframe of data and centroids and returns a list assigning each observation a centroid.
    data: a dataframe with all data that will be used.
    centroids: a dataframe with the centroids. For assignment the index will be used.
    '''

    n_observations = data.shape[0]
    centroid_assign = []
    centroid_errors = []
    k = centroids.shape[0]



        # Calculate the errror
        errors = np.array([])
        for centroid in range(k):
            error = calculate_error(centroids.iloc[centroid, :2], data.iloc[observation,:2])
            errors = np.append(errors, error)

        # Calculate closest centroid & error 
        closest_centroid =  np.where(errors == np.amin(errors))[0].tolist()[0]
        centroid_error = np.amin(errors)

        # Assign values to lists
        centroid_assign.append(closest_centroid)
        centroid_errors.append(centroid_error)

    return (centroid_assign,centroid_errors)


################################################################



def initialize_centroids(k, data):

    n_dims = data.shape[1]
    centroid_min = data.min().min()
    centroid_max = data.max().max()
    centroids = []

    for centroid in range(k):
        centroid = np.random.uniform(centroid_min, centroid_max, n_dims)
        centroids.append(centroid)

    centroids = pd.DataFrame(centroids, columns = data.columns)

    return centroids

################################################################
def calculate_error(a,b):
    '''
    Given two Numpy Arrays, calculates the root of the sum of squared errores.
    '''
    error = np.square(np.sum((a-b)**2))

    return error    

################################################################

# Create data
datos_1 = circulo(num_datos = 20,R = 10, center_x = 5, center_y = 30)
datos_2 = circulo(num_datos = 20,R = 10, center_x = 20, center_y = 10)
datos_3 = circulo(num_datos = 20,R = 10, center_x = 50, center_y = 50)

#show(datos_1,datos_2,datos_3)

data = datos_1.append(datos_2).append(datos_3)

#print(data)

centroids = initialize_centroids(3, data)

print(centroids)


errors = np.array([])
print("data")
print(data)
for centroid in range(centroids.shape[0]):
    print(centroids.iloc[centroid, :2])
    print(data.iloc[0,:2])
    error = calculate_error(centroids.iloc[centroid, :2], data.iloc[0,:2]) ##Calcula distancia eu (o errores) para el punto N de la data y los K centroides. Es decir, me falta iterar la data.
    errors = np.append(errors, error)


print("errores")

print(errors)
#show2(data,centroids)

data['centroid'], data['error'] = assign_centroid(data.iloc[:,:2] ,centroids)
data[['centroid', 'error']].head()
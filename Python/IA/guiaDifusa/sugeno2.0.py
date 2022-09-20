import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial import distance_matrix
import pandas as pd
from matplotlib.pylab import mpl



########################################################## MINIMOS CUADRADOS #########################################################
 
 

def liner_fitting(data_x,data_y):
      size = len(data_x)
      i=0
      sum_xy=0
      sum_y=0
      sum_x=0
      sum_sqare_x=0
      average_x=0
      average_y=0
      while i<size:
          sum_xy+=data_x[i]*data_y[i]
          sum_y+=data_y[i]
          sum_x+=data_x[i]
          sum_sqare_x+=data_x[i]*data_x[i]
          i+=1
      average_x=sum_x/size
      average_y=sum_y/size
      return_k=(size*sum_xy-sum_x*sum_y)/(size*sum_sqare_x-sum_x*sum_x)
      return_b=average_y-average_x*return_k
      return [return_k,return_b]
 
 
def calculate(data_x,k,b):
    datay=[]
    for x in data_x:
        datay.append(k*x+b)
    return datay
 
 
def draw(data_x,data_y_new,data_y_old):
    plt.plot (data_x, data_y_new, label = "curva de ajuste", color = "negro")
    plt.scatter (data_x, data_y_old, label = "datos discretos")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title ("Datos de ajuste lineal de una variable")
    plt.legend(loc="upper left")
    plt.show()
 
 #aca arranca
parameter = liner_fitting(x,y)
draw_data = calculate(x,parameter[0],parameter[1])
draw(x,draw_data,y)




##########################################################CLUSTERING#########################################################
def subclust2(data, Ra, Rb=0, AcceptRatio=0.3, RejectRatio=0.1): #subclustering
    if Rb==0:
        Rb = Ra*1.15
        
    scaler = MinMaxScaler()
    scaler.fit(data) 
    ndata = scaler.transform(data) # estandariza los valores, los pone entre 0 y 1
    
    # 14/05/2020 cambio list comprehensions por distance matrix
    #P = np.array([np.sum([np.exp(-(np.linalg.norm(u-v)**2)/(Ra/2)**2) for v in ndata]) for u in ndata])
    #print(P)
    P = distance_matrix(ndata,ndata) # la distancia de cada punto de una matriz con cada punto de la otra, en resumen devuelve una matriz
    alpha=(Ra/2)**2
    P = np.sum(np.exp(-P**2/alpha),axis=0) #esto es el array de potenciales
   
    centers = []
    i=np.argmax(P) # le paso el potencial maximo (indice en realidad)
    C = ndata[i] #ahora si le paso el maximo
    p=P[i] # para luego la resta en el recalculo de potenciales
    centers = [C] #le asigno al centro
    
    #LO QUE VIENE ACÁ ES EL RECALCULO, NO LE VOY A DAR MUCHA PELOTA
    continuar=True
    restarP = True
    while continuar:
        pAnt = p
        if restarP:
            P=P-p*np.array([np.exp(-np.linalg.norm(v-C)**2/(Rb/2)**2) for v in ndata])            
        restarP = True  
        i=np.argmax(P)
        C = ndata[i]
        p=P[i]
        if p>AcceptRatio*pAnt:
            centers = np.vstack((centers,C))
        elif p<RejectRatio*pAnt:
            continuar=False
        else: 
            dr = np.min([np.linalg.norm(v-C) for v in centers])
            if dr/Ra+p/pAnt>=1:
                centers = np.vstack((centers,C))
            else:
                P[i]=0
                restarP = False
        if not any(v>0 for v in P):
            continuar = False
    distancias = [[np.linalg.norm(p-c) for p in ndata] for c in centers]
    labels = np.argmin(distancias, axis=0)
    centers = scaler.inverse_transform(centers)
    return labels, centers #RETORNA LOS CENTROS DE CLUSTER, Y LABELS (A QUE CLUSTER PERTENECE)



def genfis(cdk):
    eX = np.arange(-5,5,1) 
    print(cdk[0])

    rule = fuzz.gaussmf(eX,cdk[0],0.7) #Armo las gaussianas en base a las N reglas del clustering

    plt.plot(rule)

    rules.append(rule)


def train():
    pass



df = pd.read_csv("data.csv")
rules = []
labels, cdk = subclust2(df,0.6)

y = []
for i in range(df.shap e[0]):
    y.append(df[i][1])

x = []
for i in range(df.shape[0]):
    x.append(df[i][0])

for c in range(len(cdk)):
    genfis(cdk[c])

train(x,y)



plt.show()


#Ahora necesito sacar los consecuentes.

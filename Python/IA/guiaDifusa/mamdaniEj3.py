import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control
from skfuzzy import membership
import matplotlib.pyplot as plt


cantAutos = 1 #Entrada de autos (cant autos x minuto)
cantPeatones = 10 #Entrada de peatones (peaton x m2)


######CONJUNTOS DIFUSOS#############

#Autos: [Pocos, muchos] 
#Peatones : [Pocos, muchos]
#Tiempo semaforo con luz verde : [Poco tiempo, Mucho timepo]


#####Regla de inferencia##########

#Si hay muchos autos o pocos peatones, entonces el semaforo estara en verde mucho tiempo



#METODO


dominioAutos = np.arange(0,50,1) #La variable va a ser un arreglo de 50 valores del 0 al 50 de 1 en 1
dominioPeatones= np.arange(0,8,1)
dominioSemaforoTiempo= np.arange(0,65,1)



antecedenteAutos = control.Antecedent(dominioAutos, 'cantidadDeAutos') #Creo los antecedentes y consecuentes
antecedentePeatones = control.Antecedent(dominioPeatones, 'cantidadDePeatones')

consecuenteSemaforo = control.Consequent(dominioSemaforoTiempo,'tiempoSemaforo')


#Los valores para la mf son inventados: 

#Aca se crean las mf en base a la regla que hice. Es decir, use muchos auto y pocos peatones para regla 1, entonces con esas me alcanza y despues la regla del "codigo" la armo con Rule
#Si agregara otra regla que usa pocos autos, tengo que hacer su mf y luego ponerla en Rule
antecedenteAutos['muchos'] = membership.sigmf(antecedenteAutos.universe,30,0.2) #Creo las memberships. Una para mucho, y otra para poco, que son los dos valores que puede tomar linguisticamente
#antecedenteAutos['pocos'] = membership.sigmf(antecedenteAutos.universe,)


#antecedentePeatones['muchos'] = membership.sigmf(antecedentePeatones.universe)
antecedentePeatones['pocos'] = membership.sigmf(antecedentePeatones.universe,3,-1.5)

consecuenteSemaforo['mucho'] = membership.sigmf(consecuenteSemaforo.universe,40,0.19)
#consecuenteSemaforo['poco'] = membership.sigmf(consecuenteSemaforo.universe)


antecedenteAutos.view()
antecedentePeatones.view()

#Esta recibe, un antecedente con su expresion logica -> & : and; | : OR
#Aca crea las N reglas. Como en el ejemplo hago solo una regla, con esto basta
reglaInferencia = control.Rule(antecedenteAutos['muchos'] & antecedentePeatones['pocos'],consecuenteSemaforo['mucho'])

#Creo el sistema con estas dos lineas
controlSemaforo = control.ControlSystem(reglaInferencia)
simulacion = control.ControlSystemSimulation(controlSemaforo)

#Le meto los inputs
simulacion.input['cantidadDeAutos'] = cantAutos
simulacion.input['cantidadDePeatones'] = cantPeatones

#Ejecuto
simulacion.compute()
print(simulacion.output['tiempoSemaforo'])

consecuenteSemaforo.view(sim=simulacion)

plt.plot()
plt.show() #Hago esto pq sino en VSCODE los view se cierren al toque (comentar estas dos lineas y van a entender)
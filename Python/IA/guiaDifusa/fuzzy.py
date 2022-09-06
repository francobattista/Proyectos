from cProfile import label
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

errorx = np.linspace(-20,20,10)

xBaja = fuzz.trapmf(errorx,[-20, -15, -6, -3])
xMedia = fuzz.trapmf(errorx,[-6, -3,3,6])
xAlta = fuzz.trapmf(errorx,[3,6,15,20])

errory = np.linspace(-3,15,10)

yBaja = fuzz.trapmf(errory,[-2.46, -1.46,1.46,2.46])
yMedia = fuzz.trapmf(errory,[1.46,2.46,5,7])
yAlta = fuzz.trapmf(errory,[5,7,13,15])


plt.plot(errorx,xBaja,label='XBAJA')

plt.plot(errorx,xMedia,label='XMEDIA')

plt.plot(errorx,xAlta,label='XALTA')

#plt.show()


#plt.plot(errory,yBaja,label='yBAJA')

#plt.plot(errory,yMedia,label='yMEDIA')

#plt.plot(errory,yAlta,label='yALTA')


entradaX = np.array([-8]) #,-5,5,8

xBaja = fuzz.trapmf(entradaX,[-20, -15, -6, -3])
xMedia = fuzz.trapmf(entradaX,[-6, -3,3,6])
xAlta = fuzz.trapmf(entradaX,[3,6,15,20])

plt.plot([entradaX,entradaX],[0.0,1.0],linestyle = "--")

print(xBaja)

print(xMedia)

print(xAlta)



plt.show()

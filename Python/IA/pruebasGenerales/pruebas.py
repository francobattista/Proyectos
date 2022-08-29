import numpy as np
import pandas as pd
import matplotlib as plt

list = []


list.append([1,2,3])

list.append([2,2,4])

print(list)


npArray = np.array(list)

print(npArray)

#El npArray me ponia a los elementos en formato matriz

df = pd.DataFrame(list,columns=['X1','X2','X3'])
print(df)

#Ahora accedo al df con ['XN']

#El array de numpy te los tira en formato matriz y el data frame les tira un mejor formato

p1 = [1,2]
p2 = [4,5]
p3 = [6,7]

arr = []

arr.append(p1)
arr.append(p2)
arr.append(p3)
df2 = pd.DataFrame(arr,columns=['X1','X2'])
print(df2.iloc[0]['X1'])






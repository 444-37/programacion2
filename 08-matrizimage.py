import matplotlib
import matplotlib.pyplot as plt
#import random
import numpy as np 
plt.rcParams['image.cmap'] = 'gray'

filas=50
columnas=50
matriz=[[0]*filas]*columnas
matriz=np.array(matriz)

for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=i+j
#plt.imshow(m3) 
#plt.show()

plt.imshow(matriz)
#plt.imshow(matriz,vmin=0,vmax=50)
plt.show()

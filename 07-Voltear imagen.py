from PIL import Image
import matplotlib.pyplot as plt
#import random
import numpy as np 

i=´Imagen_gris.jpg´
imagena=Imagen.open(i)
matriz=np.array(imagen)
i=
filas=len(matriz)
columnas=len(matriz[0])
aux=0

plt.subplot(1,2,1)
plt.imshow(matriz, cmap="gray ")
matriz_dadavuelta=np.array(matriz)
for i in range(filas):
    for j in range(columnas):
        aux=matriz_dadavuelta[i][j]=matriz_dadavuelta[i][columnas-1-j]
    
plt.show()

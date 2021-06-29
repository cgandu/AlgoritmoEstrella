import heapq

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.pyplot import figure

 
#consideramos una grilla de 20x20 en la que los ceros son transitables y los 1 son barreras
grilla = np.array([

[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,0],
[0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,0],
[0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
[0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1],
[0,1,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,0],
[0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0],
[0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,1],
[0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
[0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
[0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1],
[0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
[0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1],
[0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]])

 

#indicamos inicio y final de recorrido

inicio = (19,0)

final = (0,19)

 

#ploteo mapa y caminos
#tamaño 10pulx10pulg
fig, ax = plt.subplots(figsize=(10,10))

ax.imshow(grid, cmap=plt.cm.Dark2)
#marcador inicio es el de color amarillo
ax.scatter(inicio[1],inicio[0], marker = "*", color = "yellow", s = 200)
#marcador final es del color rojo
ax.scatter(final[1],final[0], marker = "*", color = "red", s = 200)

plt.show()
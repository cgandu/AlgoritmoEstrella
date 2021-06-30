import heapq



#defino funcion heuristica que estime distancia en inea recta a destino ignorando obstaculos, como distancia Manhattan

def F_heuristica(a, b):
    #calculo distancia como un pitagoras
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def F_Estrella(mapa, ini, fin):

    #defino posiciones adyacentes para cada potencial posicion desde el punto en que me encuentro.
    #Para cada posicion se evaluaran 8 posiciones adyacentes (son 8 y no 4 porque se permiten movs en diagona)

    adyacentes = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    #Set con posiciones evaluadas y descartadas que ya no es necesario evaluar
    posiciones_descartadas = set()

    #guardo las posiciones 'padre' desde las que me movi. Permite rastrear hacia atras
    posicion_desde = {}

    #Costo de funcion G para cada iteracion 
    costoG = {ini:0}

    #Costo de funcion F para cada iteracion
    costoF = {ini:F_heuristica(ini, fin)}

    #lista con las posiciones consideradas para determinar en que direccion es el camino mas corto
    listaAbierta = []
    
    #Agrego costoF y posicion inicial a listaAbierta y
    # uso el modulo heapq que mantiene siempre ordenado con el primer elemento el mas chico
    #onda priority Queue
    heapq.heappush(listaAbierta, (costoF[ini], ini))

    #mientras listaAbierta tenga todavia posiciones a considerar
    while listaAbierta:
        #de la lista abierta tomo el primer elemento -que va a ser el destino inmediato de menor costoF- y retorna posicion '[1]
        actual = heapq.heappop(listaAbierta)[1]

        #si llegue al fin del recorrido, voy rastreando hacia atras posicion x posicion mientras haya una pos anterior existente
        if actual == fin:

            data = []

            while actual in posicion_desde:

                data.append(actual)

                actual = posicion_desde[actual]

            return data

        posiciones_descartadas.add(actual)

        for i, j in adyacentes:

            pos_de_adyacente = actual[0] + i, actual[1] + j            

            costo_estimado = costoG[actual] + F_heuristica(actual, pos_de_adyacente)

                #chequeo que el pos_de_adyacente no escape a las dimensiones del arreglo/mapa.
                #Si est fuera del mapa o es inicial lo ignoro y sigo con siguiente pos_de_adyacente
            if 0 <= pos_de_adyacente[0] < mapa.shape[0]:

                if 0 <= pos_de_adyacente[1] < mapa.shape[1]:                

                    if mapa[pos_de_adyacente[0]][pos_de_adyacente[1]] == 1:
                        #ini
                        continue

                else:
                    # llegue limite mapa en y
                    continue

            else:
                 # llegue limite mapa en x
                continue
            
             #si pos_de_adyacente esta en lista de descartados y el costo_estimado es mayor
             # que el costoG para esa pos, lo ignoro tb 
            if pos_de_adyacente in posiciones_descartadas and costo_estimado >= costoG.get(pos_de_adyacente, 0):

                continue
 

            if  costo_estimado < costoG.get(pos_de_adyacente, 0) or pos_de_adyacente not in [i[1]for i in listaAbierta]:

                posicion_desde[pos_de_adyacente] = actual

                costoG[pos_de_adyacente] = costo_estimado

                costoF[pos_de_adyacente] = costo_estimado + F_heuristica(pos_de_adyacente, fin)

                heapq.heappush(listaAbierta, (costoF[pos_de_adyacente], pos_de_adyacente)) 


import numpy as np

import matplotlib.pyplot as plt

from matplotlib.pyplot import figure 

#consideramos una grilla de 20x20 en la que los ceros son transitables y los 1 son barreras
def funcionRandom1():
    return np.random.choice(np.arange(0, 2), p=[0.67, 0.33])

def funcionRandom2():
    return np.random.choice(np.arange(0, 2), p=[0.33, 0.67])

grilla = np.empty((20,20), dtype=int)

def llenoGrilla():
    for i in range(20):
        for j in range(20):
            grilla[i, j] = funcionRandom1()
        
    for i in range (5, 15):
        for j in range(5, 15):
            grilla [i, j] = funcionRandom2()    
    
#indicamos inicio y final de recorrido

inicio = (19,0)
final = (0,19)

while True:
    try:
        
        llenoGrilla()        
        ruta_mas_corta = F_Estrella(grilla, inicio, final)
        
        #agrego posicion de inicio a la ruta ya que no la incluye
        ruta_mas_corta = ruta_mas_corta + [inicio]
        
        #F_Estrella me devuelve la ruta en reversa, pues rastrea los 'desde' para cada posicion, asi que lo invierto
        ruta_mas_corta = ruta_mas_corta[::-1]
        
    except:
        print("Hay error")
        continue
    else:
        
        break



print(ruta_mas_corta)

coor_X = []
coor_Y = []

for paso in (range(0, len(ruta_mas_corta))):
    
    x = ruta_mas_corta[paso][0]

    y = ruta_mas_corta[paso][1]

    coor_X.append(x)

    coor_Y.append(y)


#ploteo mapa y caminos
#tamaño 10pulx10pulg
fig, ax = plt.subplots(figsize=(10,10))

ax.imshow(grilla, cmap=plt.cm.Paired)
#marcador inicio es el de color amarillo
ax.scatter(inicio[1],inicio[0], marker = "*", color = "yellow", s = 200)
#marcador final es del color rojo
ax.scatter(final[1],final[0], marker = "*", color = "red", s = 200)
ax.plot(coor_Y, coor_X, color="yellow")

plt.show()

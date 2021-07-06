import heapq



#defino funcion que devuelva distancia en linea recta a destino

def F_Distancia_Recta(a, b):
    #calculo distancia como un pitagoras (distancia directa en diagonal)
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def F_Estrella(mapa, ini, fin):

    #defino posiciones adyacentes para cada potencial posicion desde el punto en que me encuentro.
    #Para cada posicion se evaluaran 4 posiciones u 8 si se aceptan movimientos en diagonal

    adyacentes = [(0,1),(0,-1),(1,0),(-1,0)]
    #Set con posiciones evaluadas y descartadas que ya no es necesario evaluar
    posiciones_descartadas = set()

    #guardo las posiciones 'padre' desde las que me movi. Permite rastrear hacia atras
    posicion_desde = {}

    #Costo de funcion G para cada iteracion 
    costoG = {ini:0}

    #Costo de funcion F para cada iteracion
    costoF = {ini:F_Distancia_Recta(ini, fin)}

    #lista con las posiciones consideradas para determinar en que direccion es el camino mas corto
    listaAbierta = []
    
    #Agrego costoF y posicion inicial a listaAbierta y
    # uso el modulo heapq que mantiene siempre ordenado la lista y y en el q el primero elemento es siempre el mas chico
    # https://docs.python.org/3/library/heapq.html
    heapq.heappush(listaAbierta, (costoF[ini], ini))

    #mientras listaAbierta tenga todavia posiciones a considerar
    while listaAbierta:
        #de la lista abierta tomo el primer elemento -que va a ser la pos con menor costoF de la lista- y obtengo posicion
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
            
            mult_terreno = 1       
              
                # chequeo que el pos_de_adyacente no escape a las dimensiones del mapa.
                # Si est fuera del mapa o es '1' lo ignoro y sigo con siguiente pos_de_adyacente
                # si es '2' aumento ultiplicador de terreno para calculo de distancia
            if 0 <= pos_de_adyacente[0] < mapa.shape[0]:

                if 0 <= pos_de_adyacente[1] < mapa.shape[1]:                
                    
                    #camino normal
                    if (mapa[pos_de_adyacente[0]][pos_de_adyacente[1]] == 0):
                        mult_terreno = 1
                        
                    
                    #pared
                    elif (mapa[pos_de_adyacente[0]][pos_de_adyacente[1]] == 1):
                        # obstaculo -paso al siguiente elemento del loop ==> continue
                        continue
                    #arena
                    elif mapa[pos_de_adyacente[0]][pos_de_adyacente[1]] == 2:
                        #terreno con mayor costo; cambio multiplicador de costo
                        mult_terreno = 3
                        
                    #agua
                    elif mapa[pos_de_adyacente[0]][pos_de_adyacente[1]] == 3:
                        #terreno con mayor costo; cambio multiplicador de costo
                        mult_terreno = 4
                        
                    #tierra
                    elif mapa[pos_de_adyacente[0]][pos_de_adyacente[1]] == 4:
                        #terreno con mayor costo; cambio multiplicador de costo
                        mult_terreno = 1.5
                        
                    #ripip
                    elif mapa[pos_de_adyacente[0]][pos_de_adyacente[1]] == 5:
                        #terreno con mayor costo; cambio multiplicador de costo
                        mult_terreno = 5
                        

                else:
                    # llegue limite mapa en y -paso al siguiente/continuo
                    continue

            else:
                 # llegue limite mapa en x -paso al siguiente/continuo
                continue
            costo_estimado_en_adyacente = costoG[actual] + F_Distancia_Recta(actual, pos_de_adyacente)*mult_terreno
            
             #si pos_de_adyacente esta en lista de descartados y el costo_estimado_en_adyacente es mayor
             # que el costoG para esa pos, no vale la pena volver a considerarla y contnuo/paso al siguiente
            if pos_de_adyacente in posiciones_descartadas and costo_estimado_en_adyacente >= costoG.get(pos_de_adyacente, 0):
                
                continue 
 
            # Si costo_estimado_en_adyacente es menor que el costoG previamente calculado p/esa posicion
            # o si nunca se habia analizado esa posicion
            if  costo_estimado_en_adyacente < costoG.get(pos_de_adyacente, 0) or pos_de_adyacente not in [i[1]for i in listaAbierta]:

                posicion_desde[pos_de_adyacente] = actual

                costoG[pos_de_adyacente] = costo_estimado_en_adyacente

                costoF[pos_de_adyacente] = costo_estimado_en_adyacente + F_Distancia_Recta(pos_de_adyacente, fin)

                heapq.heappush(listaAbierta, (costoF[pos_de_adyacente], pos_de_adyacente)) 
    return False

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.pyplot import figure 

#consideramos una grilla de 20x20: los ceros son transitables, 
#los 1 son barreras y los 2, 3, 4 y 5 un camino con mayor costo (por ej: un rio, camino de tierra, etc)

#arranco con un mapa vacio -lleno de 0- al que luego ire modificando
grilla = np.empty((20,20), dtype=int)

def funcionRandom(p0, p1, p2, p3, p4, p5):
    return np.random.choice(np.arange(0, 6), p=[p0, p1, p2, p3, p4, p5])



def llenoGrilla():
        global grilla
        grilla = np.ones((20,20), dtype=int)
        for i in range (20):
            grilla [i, 4] = funcionRandom(0.65, 0, 0.1, 0.2, 0.05, 0)
        for i in range(20):
            grilla[i, 9] = funcionRandom(0.65, 0, 0.25, 0.1, 0, 0)
        for i in range (20):
            grilla [i, 14] = funcionRandom(0.65, 0, 0.15, 0.15, 0.05, 0)

            

        for j in range (20):
            grilla [5, j] = funcionRandom(0.65, 0, 0.1, 0.2, 0.05, 0)
        for j in range (20):
            grilla [10, j] = funcionRandom(0.65, 0, 0.1, 0.2, 0.05, 0)
        for j in range (20):
            grilla [15, j] = funcionRandom(0.65, 0, 0.1, 0.2, 0.05, 0)



        for i in range (20):
            grilla [i, 0] = funcionRandom(0, 0, 0, 0, 0, 1)
        for i in range (20):
            grilla [i, 19] = funcionRandom(0, 0, 0, 0, 0, 1)
        for j in range (20):
            grilla [0, j] = funcionRandom(0, 0, 0, 0, 0, 1)
        for j in range (20):
            grilla [19, j] = funcionRandom(0, 0, 0, 0, 0, 1)
            

    
#indicamos inicio y final de recorrido

inicio = (19,0)
final = (0,19)

        



continua = True
while continua:
    op = input("Automapa [1], Mapa fijo [2], Salir [3]: " )
    if op == "1":
        llenoGrilla()
    elif op == "2":
        grilla = np.array([
                    [5,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
                    [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,0],
                    [0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,0],
                    [0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
                    [0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1],
                    [0,1,0,1,0,0,1,0,0,1,1,0,1,0,3,0,0,0,1,0],
                    [0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,0,3,0,1,0],
                    [0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,0],
                    [0,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,4,1,0],
                    [0,0,0,0,0,0,0,0,0,1,1,2,2,1,0,0,1,4,1,0],
                    [0,1,0,0,0,0,0,0,0,3,3,2,2,2,2,2,1,0,0,0],
                    [0,1,1,1,1,1,4,1,0,3,3,2,2,1,0,0,1,1,0,1],
                    [0,1,0,4,4,4,4,1,0,3,3,0,0,1,0,0,0,1,0,1],
                    [0,1,0,0,4,4,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
                    [0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1],
                    [0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
                    [0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1],
                    [0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
                    [0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]])
    elif op == "3":
        continua = False
        break
    else:
        print("Ingreso invalido")
        break


    ruta_mas_corta = F_Estrella(grilla, inicio, final)

    #agrego posicion de inicio a la ruta ya que no la incluye
    ruta_mas_corta = ruta_mas_corta + [inicio]

    #F_Estrella me devuelve la ruta en reversa, pues rastrea los 'desde' para cada posicion, asi que lo invierto
    ruta_mas_corta = ruta_mas_corta[::-1]





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

    ax.imshow(grilla, cmap=plt.cm.Accent)
    #marcador inicio es el de color amarillo
    ax.scatter(inicio[1],inicio[0], marker = "*", color = "yellow", s = 200)
    #marcador final es del color rojo
    ax.scatter(final[1],final[0], marker = "*", color = "red", s = 200)
    ax.plot(coor_Y, coor_X, color="yellow")

    plt.show()


    



    
    
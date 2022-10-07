state =[1,2,3,4,5,6,7,8,0]


def conflictos(state):
    
    # Se convirte el estado del nodo en arreglos bidimensionales
    filas = [state[:3],state[3:6],state[6:9]] # Filas separadas en arreglo 2d
    columnas = [[state[0], state[3], state[6]],[state[1], state[4], state[7]],[state[2], state[5], state[8]]] # Columnas separadas en arreglo 2d
    
    #Variables locales
    conflictos = 0 
    aux_filas = [[1,2,3],[4,5,6],[7,8,9]] # Orden en el que debería estar el node.state en su estado ideal a nivel de filas
    aux_columnas = [[1,4,7],[2,5,8],[3,6,9]] # # Orden en el que debería estar el node.state en su estado ideal a nivel de columnas

    for i in range(len(filas)):
        # Revisa si los números se encuentran el las filas correspondientes y si existe algun conflicto
        if aux_filas[i][0] in filas[i]:
             
            if aux_filas[i][1] in filas[i] and (filas[i].index(aux_filas[i][0]) > filas[i].index(aux_filas[i][1])):
                conflictos += 1

            if aux_filas[i][2] in filas[i] and (filas[i].index(aux_filas[i][0]) > filas[i].index(aux_filas[i][2])):
                conflictos += 1

        if (aux_filas[i][1] in filas[i] and aux_filas[i][2] in filas[i]) and (filas[i].index(aux_filas[i][1]) > filas[i].index(aux_filas[i][2])):
            conflictos += 1
    
    for i in range(len(columnas)):
        # Revisa si los números se encuentran el las columnas correspondientes y si existe algun conflicto
        if aux_columnas[i][0] in columnas[i]:
             
            if aux_columnas[i][1] in columnas[i] and (columnas[i].index(aux_columnas[i][0]) > columnas[i].index(aux_columnas[i][1])):
                conflictos += 1

            if aux_columnas[i][2] in columnas[i] and (columnas[i].index(aux_columnas[i][0]) > columnas[i].index(aux_columnas[i][2])):
                conflictos += 1

        if (aux_columnas[i][1] in columnas[i] and aux_columnas[i][2] in columnas[i]) and (columnas[i].index(aux_columnas[i][1]) > columnas[i].index(aux_columnas[i][2])):
            conflictos += 1
    
    return conflictos * 2


print(conflictos(state))





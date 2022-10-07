xyGrid = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
solucion = [(2,2),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]

#|3|2|1|
#|4|5|6|
#|7|8|0|
state =[3,2,1,4,5,6,7,8,0] #estado Inicial
filas = [state[0:3],state[3:6],state[6:9]]

columnas = [[state[0], state[3], state[6]],[state[1], state[4], state[7]],[state[2], state[5], state[8]]]

bandera = []
conflictos = []

for fila in range(len(filas)):
    for i in filas[fila]:
        if solucion[i][0] == fila:
            bandera.append(i)
    conflictos.append(bandera)
print(conflictos)        
for columna in range(len(columnas)):
    for i in columnas[columna]:
        if solucion[i][1] == columna:
            bandera.append(i)
    conflictos.append(bandera)
print(conflictos)
    
    
# #Metodo distancia de Manhattan
# def manhattan(xyGrid, xySolucion):
#     return abs(xySolucion[0]-xyGrid[0]) + abs(xySolucion[1] - xyGrid[1])



# sum=0

# for i in range(len(state)):
#     sum+= manhattan(xyGrid[state.index(i)], solucion[i])
#     if xyGrid[stateindex()]

# print('total: {}'.format(sum))
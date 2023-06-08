# TRADICIONAL
import numpy as np
matriz = np.array([[0, 1, 2], [3, 4, 5]])
for f in range(2):
    for c in range(3):
        print(matriz[f][c])
print("")
print(matriz[1,1])


# USANDO LISTAS
lista = [[1,2,3], [4,5,6]]
matris = np.array(lista)
print(matris)
print(matris[0][1])
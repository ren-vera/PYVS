import random
import numpy as np
Lista= []
for _ in range(10):
    numero_aleatorio= random.randint(0,500)
    Lista.append(numero_aleatorio)
    if numero_aleatorio % 2 == 0:
        print(numero_aleatorio)
Lista.append(501)
Lista.insert(0,501)
arreglo=np.array(Lista)
print("este es el nro max:",arreglo.max())
print(Lista.index(arreglo.max()))
print(arreglo)
valor_max=arreglo.max()

for i in range(len(arreglo)):
    if arreglo[i] == valor_max:
        print("la posicion del valor max es : ", i)
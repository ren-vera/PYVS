import numpy as np
arreglo = np.array([4,8,15,16,23,42]) #np.array significa (arreglo) en resumen xd
contar_hasta = len(arreglo) # (len) sirve para medir la longitud de una secuencia
for i in range (contar_hasta):
    arreglo [i] = arreglo [i] * 2
    print(arreglo)

arreglo0 = np.array(["a", "b", "c", "d"])
print(len(arreglo0)) #INDICA LA CANTIDAD DE ELEMENTOS DENTRO DEL ARREGLO []
print(arreglo0.shape) #INDICA LAS DIMENSIONES DEL ARREGLO []
print(arreglo0[1:3]) #MUESTRA LOS ELEMENTOS ENTRE LAS CORDENADAS QUE INDIQUÉ
print(arreglo0[1:2:3]) #indica que se desea obtener una porción del arreglo comenzando desde el índice 1, avanzando hasta el índice 2 (exclusivo) y tomando elementos en incrementos de 3
print(arreglo0.ndim) # MUESTRA LAS DIMENSIONES DEL ARREGLO EN ESTE CASO 1 (UNIDIMENSIONAL)
print(arreglo0[::2]) # INDICA QUE SE DESEA TOMAR TODOS LOS ELEMENTOS PARES DEL ARREGLO A=0 Y C=2
print(arreglo0[-1])

c = [i for i in range (0,5)]
print (c)

for i in range (len(arreglo)):
    print(arreglo[i])


ala = np.arange(4) #SE CREA UN ARREGLO CON 4 ELEMENTOS ENTEROS
print(ala)

epe = np.arange(4.0) #SE CREA UN ARREGLO CON 4 ELEMENTOS CON UN DECIMAL
print(epe)

efe = np.arange(4,7) #SE CREA UN ARREGLO CON ELEMENTOS ENTRE 4 Y 7 EXCLUTENDO EL ULTIMO
print(efe)

aka = np.arange(3,7,2) #SE CREA UN ARREGLO CON ELEMENTOS ENTRE 3 Y 7 CON UN INTERVALO DE 2, EXCLUYENDO EL ULTIMO
print(aka)


#Crear un array a partir de una lista:
lista = [1, 2, 3, 4, 5]
arr = np.array(lista)
print(arr)  # Output: [1 2 3 4 5]

#Crear un array a partir de una tupla:
tupla = (1, 2, 3, 4, 5) #UNA TUPLA ES SIMILAR A UNA LISTA PERO SU FORMATO ES CON () Y NO ES MODIFICABLE Y SE USAN PARA ALMACENAR UN TIPO DE ELEMENTO
arrr = np.array(tupla)
print(arrr)  # Output: [1 2 3 4 5]


#Crear un array a partir de una lista de listas(matriz):
lista_de_listas =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arrrr = np.array(lista_de_listas)
print(arrrr)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

array_entero = np.random.randint(0, 100, size=(1, 10))  
print(array_entero)

print(array_entero.max()) #numero mas grande
print(array_entero.min()) #numero mas chico
print(array_entero.sum()) #suma de todo
print(array_entero.mean()) #promedio de todos los elementos


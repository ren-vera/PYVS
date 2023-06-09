#CADA ELEMENTO DE UNA LISTA TIENE UNA POSICION ENUMERADA LLAMADA INDICE [0, 1, 2, 3]

lista = [1,"hola", 3.67,[1, 2, 3]]
print(lista)
print(lista[-2])
print(lista[-1])
lista.append(6500)#Nos permite agregar solo un elemento al final de la lista. SOLO UN ELEMENTO A LA VEZ
print(lista)

listaa = [17, 20, 23, 28, 30]
listaa[3] = 27 #ACTUALICE LA POSICION [3] DE LA LISTA CON EL NÚMERO 27
print(listaa)
print(listaa[1]) #PARA QUE IMPRIMA SOLO EL ELEMENTO DEL INDICE [1] DE MI LISTA 20

listab = [1, 2]
listab.extend([3,4])#Nos permite agregar distintos elementos al final de una lista
print(listab)

listac = [1, 3]
listac.insert(1, 2) #inserta un elemento en una posición especifica sin reemplazar el otro elemento. EL NÚMERO 2 ENTRA EN LA POSICION [1]. SOLO UN ELEMENTO A LA VEZ
print(listac)

listad = [1, 2, 3, 4, 5]
listad.remove(5)#borra el elemento en especifico que coloques en los parentecis 
print(listad)


listae = ["a", "b", "c", "d", "f"]
listae.pop(3)#borra un elemento segun la cordenada
print(listae)
listae = listab.pop() #recogerá el ultimo valor de la lista (listab)
print(listae)

listaf = [1, 2, 3]
listaf.reverse()#da vuelta la lista
print(listaf)

listag = [1, 9, 5, 3, 11]
listag.sort()#ordena la lista
print(listag)

listah = [1, 2, 3, 4, 5]
tamanio = len(lista)#cuantos elementos hay en la lista
print(tamanio)

lista_original = [1, 2, 3, 4, 5]
copia = lista_original.copy() #copia la lista
print(copia)

listai = ([1, 2, 3, 4, 5], "aa")
lista.clear() #borra la lista
print(lista)

lista = [1, 2, 3, 4, 2, 2, 5]
contador = lista.count(2) #se utiliza para contar el número de apariciones de un elemento en una lista.
print(contador)


texto1 = "\"hola mundo\""
texto_en_mayusculas = texto1.upper()#Transforma en mayusculas el texto
print(texto_en_mayusculas)

texto2 = "\"HOLA MUNDO\""
texto_en_minusculas = texto2.lower()#Transforma en minusculas el texto
print(texto_en_minusculas)

texto3 = "Hola Mundo"
posicion = texto3.find("d")#Nos da la posicion de un elemento dentro de una lista
print(posicion)

texto4 = "Hola Mundo"
texto_modificado = texto4.replace("Mundo", "Amigo")#Reemplaza una parte de la lista con otro elemento
print(texto_modificado)

ero = "lalala"
ndo = "lelele"
tcero = "lololo"
cto = "lululu"
win = [ero, ndo, tcero, cto]
print(win[2]) #OUTPOUT  LOLOLO

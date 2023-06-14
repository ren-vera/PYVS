def saludo():
    print("HOLA A TODOS HIJOS DE LA GRANDISIMA")
saludo()
#///////////////////////////////////////////////////////////////////////////
def sumar():
    num1 = 3
    num2 = 5
    return(num1 + num2)
print("La suma es: ", sumar())
#///////////////////////////////////////////////////////////////////////////
def sumar(a, b):
    suma = a + b
    print(f"La suma de los argumentos es: {suma}")

num11 = int(input("Ingrese el primer número: "))
num12 = int(input("Ingrese el segundo número: "))
sumar(num11, num12)

#////////////////////////////////////////////////////////////////////////////
def sumar(a, b):
    suma = a + b
    return(suma)

num21 = int(input("Ingrese el primer número: "))
num22 = int(input("Ingrese el segundo número: "))
print(f"La suma de los argumentos es: ", sumar(num21, num22))

#////////////////////////////////////////////////////////////////////////////////
def mostrar_valores():
    return("Buen día", 15,[10,20,30])
print(mostrar_valores())

#////////////////////////////////////////////////////////////////////////////////////
def resta(a,b):
    return a - b
print(resta(30,10))

#//////////////////////////////////////////////////////////////////////////
def resta(c, d):
    return c - d
print(resta(c=30,d=10))

#//////////////////////////////////////////////////////////////////////////
def funcion():
    return "Bienvenidos a python"
frase=funcion()
print(frase)

#//////////////////////////////////////////////////////////////////////////////
def resta (a = None, b = None):
    if a == None or b == None:
        print("Error, Faltan parámetros a la función")
        return
    return a - b
print(resta())

#//////////////////////////////////////////////////////////////////////////////
def calculo(precio, descuento):
    return precio - (precio * descuento / 100)
datos = [10000, 10]
print("El monto final a pagar es: ",calculo(* datos))

#///////////////////////////////////////////////////////////////////////////////
def saludo(nombre, mensaje = 'Python'):
    print(mensaje, nombre)
saludo(mensaje="Buen Día", nombre="Renato")


def resta(a, b):
    return a - b
resta(30, 10)


def resta(a, b):
    return a - b
resta(b = 30, a = 10)


def funcion():
    return "bienvenidos a python ☺"
frase = funcion()
print(frase)


def resta (a=None, b=None):
    if a  == None or b == None:
        print("Error, faltan parámetros a la funcione")
        return
    return a - b
resta()


def calculo(precio, descuento):
    return precio - (precio * descuento / 100)

datos = [10000, 10]
print("El monto final a pagar es: ",calculo(*datos))


def saludo(nombre, mensaje='Python'):
    print(mensaje, nombre)

saludo(mensaje="Buen día", nombre = "Pedro")











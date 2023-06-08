def saludo():
    print("HOLA A TODOS HIJOS DE LA GRANDISIMA")
saludo()

def sumar():
    num1 = 3
    num2 = 5
    return(num1 + num2)
print("La suma es: ", sumar())

def sumar(a, b):
    suma = a + b
    print(f"La suma de los argumentos es: {suma}")

num11 = int(input("Ingrese el primer número: "))
num12 = int(input("Ingrese el segundo número: "))
sumar(num11, num12)


def sumar(a, b):
    suma = a + b
    return(suma)

num21 = int(input("Ingrese el primer número: "))
num22 = int(input("Ingrese el segundo número: "))
print(f"La suma de los argumentos es: ", sumar(num21, num22))
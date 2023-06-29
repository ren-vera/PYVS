reservas = []

def ingresar_paseo(numero):
    reservas.append(numero)
    print(f"Reserva {numero} ingresada correctamente.")

def buscar_reservas_por_numero(numero):
    encontradas = [reserva for reserva in reservas if reserva == numero]
    if encontradas:
        print(f"Reservas encontradas para el número {numero}:")
        for reserva in encontradas:
            print(reserva)
    else:
        print(f"No se encontraron reservas para el número {numero}.")

def mostrar_reservas():
    if reservas:
        print("Reservas ingresadas:")
        for reserva in reservas:
            print(reserva)
    else:
        print("No se han ingresado reservas.")


def menu():
    while True:
        print("\n---- MENÚ ----")
        print("1. Ingresar reserva de paseo")
        print("2. Buscar reservas por número")
        print("3. Mostrar todas las reservas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = input("Ingrese el número de la reserva de paseo: ")
            ingresar_paseo(numero)
        elif opcion == "2":
            numero = input("Ingrese el número de reserva a buscar: ")
            buscar_reservas_por_numero(numero)
        elif opcion == "3":
            mostrar_reservas()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            menu()

import random

paseos = {
    997: {
        "Fecha": "20-06-2031",
        "Hora": "11:40",
        "Inicio": "Hospital",
        "Fin": "Plaza de armas",
        "Cantidad de Mascotas": 1,
        "Nombre de la Persona": "Renato Vera",
        "Precio": 5000
    },
    998: {
        "Fecha": "12-06-2023",
        "Hora": "16:15",
        "Inicio": "Mc donnald",
        "Fin": "DuocUC",
        "Cantidad de Mascotas": 4,
        "Nombre de la Persona": "Matias Mena",
        "Precio": 4000
    },
    999: {
        "Fecha": "15/06/2023",
        "Hora": "13:00",
        "Inicio": "Mall",
        "Fin": "Terminal de Buses",
        "Cantidad de Mascotas": 2,
        "Nombre de la Persona": "Hugo Mayorga",
        "Precio": 3500
    }
}

def grabar_reserva():
    global paseos
    numero_reserva = max(paseos.keys()) + 1
    fecha = input("Fecha del paseo : ")
    hora = input("Hora del paseo: ")
    inicio = input("Lugar de inicio del paseo: ")
    fin = input("Lugar de fin del paseo: ")
    cantidad_mascotas = int(input("Cantidad de mascotas a pasear: "))
    nombre_persona = input("Nombre de la persona que reserva: ")
    precio = random.randint(3500, 12900)
    
    if cantidad_mascotas < 1 or cantidad_mascotas > 5:
        print("Error: El número de mascotas solo puede estar entre 1 y 5.")
        return
    
    paseos[numero_reserva] = {
        "Fecha": fecha,
        "Hora": hora,
        "Inicio": inicio,
        "Fin": fin,
        "Cantidad de Mascotas": cantidad_mascotas,
        "Nombre de la Persona": nombre_persona,
        "Precio": precio
    }
    
    print(f"Reserva {numero_reserva} guardada exitosamente.")

def buscar_reserva():
    global paseos
    numero_reserva = int(input("Ingrese el número de reserva: "))
    
    if numero_reserva in paseos:
        reserva = paseos[numero_reserva]
        print("Información de la reserva:")
        print(f"Número de reserva: {numero_reserva}")
        for key, value in reserva.items():
            print(f"{key}: {value}")
    else:
        print("La reserva no existe.")

def imprimir_boleta():
    global paseos
    numero_reserva = int(input("Ingrese el número de reserva: "))
    
    if numero_reserva in paseos:
        reserva = paseos[numero_reserva]
        print("Boleta de Paseo")
        print(f"Fecha del paseo: {reserva['Fecha']}")
        print(f"Cantidad de mascotas paseadas: {reserva['Cantidad de Mascotas']}")
        print(f"Precio del paseo: ${reserva['Precio']}")
    else:
        print("La reserva no existe.")

def salir_programa():
    print("Autor: Matias Mena Y Renato Vera")
    print("Versión del programa: 7.0")
    exit()


while True:
    print("\n--- Bienvenidos a Te Paseo ---")
    print("1.- Grabar ")
    print("2.- Buscar ")
    print("3.- Imprimir boleta")
    print("4.- Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        grabar_reserva()
    elif opcion == 2:
        buscar_reserva()
    elif opcion == 3:
        imprimir_boleta()
    elif opcion == 4:
        salir_programa()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

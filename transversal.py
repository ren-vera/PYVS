import random

vehiculos = []

def grabar_vehiculo():
    print("Ingrese los datos del vehículo:")
    tipo = input("Tipo: ")
    patente = input("Patente: ")
    marca = input("Marca: ")
    precio = float(input("Precio: "))
    multas = []
    fecha_registro = input("Fecha de registro: ")
    nombre_dueño = input("Nombre del dueño: ")
    
    while len(patente) != 6 or not patente.isalnum():
        print("La patente debe tener 6 caracteres alfanuméricos.")
        patente = input("Patente: ")
    
    while len(marca) < 2 or len(marca) > 15:
        print("La marca debe tener entre 2 y 15 caracteres.")
        marca = input("Marca: ")
    
    while precio <= 5000000:
        print("El precio debe ser mayor a $5.000.000.")
        precio = float(input("Precio: "))
    
    vehiculo = {
        "Tipo": tipo,
        "Patente": patente,
        "Marca": marca,
        "Precio": precio,
        "Multas": multas,
        "Fecha de Registro": fecha_registro,
        "Nombre del Dueño": nombre_dueño
    }
    
    vehiculos.append(vehiculo)
    print("El vehículo se ha registrado exitosamente.")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo a buscar: ")
    encontrado = False
    
    for vehiculo in vehiculos:
        if vehiculo["Patente"] == patente:
            print("Información del vehículo:")
            for key, value in vehiculo.items():
                print(key + ": " + str(value))
            encontrado = True
            break
    
    if not encontrado:
        print("No se encontró ningún vehículo con esa patente.")

def imprimir_certificados():
    certificados = ["Emisión de contaminantes", "Anotaciones vigentes", "Multas"]
    
    for vehiculo in vehiculos:
        print("Datos del dueño:")
        print("Nombre: " + vehiculo["Nombre del Dueño"])
        print("Patente del auto: " + vehiculo["Patente"])
        
        for certificado in certificados:
            monto = random.randint(1500, 3500)
            print("Certificado: " + certificado)
            print("Monto: $" + str(monto))
            print()

def mostrar_menu():
    print("Bienvenido a la automotora Auto Seguro")
    print("Menú:")
    print("1. Grabar vehículo")
    print("2. Buscar vehículo")
    print("3. Imprimir certificados")
    print("4. Salir")
    print()

def programa_automotora():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada (1-4): ")
        
        if opcion == "1":
            grabar_vehiculo()
        elif opcion == "2":
            buscar_vehiculo()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
        print()
programa_automotora()


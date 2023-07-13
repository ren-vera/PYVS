menu = True
producto = []
base_de_datos = { 
    1111: {
        "Número de producto": "1111",
        "Nombre del producto": "tarjeta",
        "Precio": "52000"
    },
    1112:{
        "Número de producto": "1112",
        "Nombre del producto": "Placa Madre",
        "Precio": "1200000"
    },
    1113:{
        "Número de producto": "1113",
        "Nombre del producto": "Tarjeta SSD 240GB",
        "Precio": "30000"
    },
    1114:{
        "Número de producto": "1114",
        "Nombre del producto": "Tarjeta RAM 5G",
        "Precio": "55000"
    },
    1115:{
        "Número de producto": "1115",
        "Nombre del producto": "MOUSE LOGITECH",
        "Precio": "50000"
    },
    1116:{
        "Número de producto": "1116",
        "Nombre del producto": "Teclado Corsair",
        "Precio": "60000"
    },
    1117:{
        "Número de producto": "1117",
        "Nombre del producto": "Pendrive 5 GB",
        "Precio": "12000"
    },
    1118:{
        "Número de producto": "1118",
        "Nombre del producto": "Tarjeta NVME 1TB",
        "Precio": "100000"
    },
    1119:{
        "Número de producto": "1119",
        "Nombre del producto": "Ventilador GPU",
        "Precio": "19000"
    },
    1120:{
        "Número de producto": "1120",
        "Nombre del producto": "Ventilador CPU",
        "Precio": "20000"
    }
}



def grabar_producto():
    global producto
    print("---> Ingrese especificaciones <---")
    num_prod = int(input("Número de producto: "))
    nombre_prod = input("Nombre del producto: ")
    precio_prod = int(input("Precio: "))

    producto_s = {
        "Número de producto": num_prod,
        "Nombre del producto": nombre_prod,
        "Precio": precio_prod
    }
    
    if len(nombre_prod) >= 6:
        if precio_prod >= 500:
            producto.append(producto_s)
            print("\nEl producto ha sido ingresado")
        else:
            print("No hay stock")
    else:
        print("☻ El nombre debe ser más específico ☻")

def buscar_prod():
    global producto, base_de_datos
    num_prod = int(input("\nIngrese el número de producto: "))
    encontrado = False
    
    if num_prod in base_de_datos:
        producto_s = base_de_datos[num_prod]
        for key, value in producto_s.items():
            print(key + ": " + str(value))
        encontrado = True

    for producto_s in producto:
        if producto_s["Número de producto"] == num_prod:
            for key, value in producto_s.items():
                print(key + ": " + str(value))
            encontrado = True
            break

    if not encontrado:
        print("\nNo se encontró ningún producto con este número")

def imprimir_productos():
    global producto
    print("\n--- Lista de productos ---")
    for producto_s in producto:
        for key, value in producto_s.items():
            print(key + ": " + str(value))
        print()

def mostrar_menu():
    print("--- Benvenuto nel menu ---")    
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir")
    print("4.- Salir")
    print()

def programa_productos():
    global menu
    while menu:    
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            print("\nHa seleccionado la opción: Grabar") 
            grabar_producto()
            
        elif opcion == 2:
            print("\nHa seleccionado la opción: Buscar") 
            buscar_prod()

        elif opcion == 3:
            print("\nHa seleccionado la opción: Imprimir")
            imprimir_productos()
            
        elif opcion == 4:
            print("\nHa seleccionado la opción: Salir") 
            print("\nV_1.0 Renato Vera")
            break
            
        else:
            print("\nSelección Inválida")

programa_productos()
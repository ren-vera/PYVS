menu = True
producto = []

def grabar_producto():
    print("---> Ingrese especificaciones <---")
    num_prod = int(input("Número de producto: "))
    nombre_prod = input("Nombre del producto: ")
    precio_prod = int(input("Precio: "))

    producto_s = {
        "Número de producto": num_prod,
        "Nombre del producto": nombre_prod,
        "Precio": precio_prod
    }

    producto.append(producto_s)
    print("\nEl producto ha sido ingresado")

def buscar_prod():
    num_prod = int(input("\nIngrese el número de producto: "))
    encontrado = False
    for producto_s in producto:
        if producto_s["Número de producto"] == num_prod:
            for key, value in producto_s.items():
                print(key + ": " + str(value))
            encontrado = True
            break
    if not encontrado:
        print("\nNo se encontró ningún producto con este número")

def mostrar_menu():
    print("--- Benvenuto nel menu ---")    
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir")
    print("4.- Salir")
    print()

    
def programa_productos():
    while True:    
        mostrar_menu()
        opcion = int(input("Seleziona un'opzione: "))
        
        if opcion == 1:
            print("\nHa seleccionado la opción: Grabar") 
            grabar_producto()
            
        elif opcion == 2:
            print("\nHa seleccionado la opción: Buscar") 
            buscar_prod()

        elif opcion == 3:
            print("\nHa seleccionado la opción: Imprimir") 
            
        elif opcion == 4:
            print("\nHa seleccionado la opción: Salir") 
            break
            
        else:
            print("\nSelección Inválida") 
            
programa_productos()

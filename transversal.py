menu_principal = True

print("------ Bienvenido a AutoSeguro ------")
while  menu_principal :
    try:
        print("")
        print("1.- Grabar")
        print("2.- Buscar")
        print("3.- Imprimir certificados")
        print("4.- Salir")
        opcion = int(input("\nPor favor seleccione una opción: "))

        if opcion == 1 :
            print("\n Ha seleccionado la opción: Grabar")
            print("\nPor favor rellene el siguiente formulario: ")
            tipo_car = input("\nTIPO DE VEHICULO: ")
            patente_car = input("\nPATENTE DEL VEHICULO: ")
            marca_car = input("\nMARCA DEL VEHICULO: ")
            valor_car = int(input("\nPRECIO DEL VEHICULO: $"))
            consulta = input("\n¿El vehiculo tiene multas?: ")
        
            if consulta == "SI" or consulta =="si":
                multa_car = int(input("\nIngrese el monto de la multa: $"))
                fecha_multa_car = input("\nFecha de la multa (si/no): ")
        
            elif consulta == "NO" or consulta =="no":
                print("")
        
            fecha_registro_car = input("\nFecha del registro del vehiculo: ")
            dueño_car = input("\nDueño del vehiculo: ")  
            menu_principal = False     
        
        elif opcion == 2 :
            print("\n Ha seleccionado la opción: Buscar")
            break           

        elif opcion == 3 :
            print("\n Ha seleccionado la opción: Imprimir certificados")
            break

        elif opcion == 4 :
            print("\n Ha seleccionado la opción: Salir \n¡Vuelva Pronto!")
            break

        else:
            print("\nSelección invalida, Intente denuevo.")
            menu_principal = False

    except ValueError:
        print("\nPor favor ingrese números enteros")




























































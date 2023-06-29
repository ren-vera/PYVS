menu_principal = True
datos = []
print("-----Bienvenidos a Autoseguro-----")
while menu_principal:
    print("\n-----Menú Principal-----")
    print("\n1.- Grabar")
    print("\n2.- Buscar")
    print("\n3.- Imprimir certificados")
    print("\n4.- Salir")
    
    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        print("\nHa seleccionado la opción: Grabar")
        print("\nRellene el siguiente formulario: ")
        tipo_car = input("\nTipo de Vehiculo: ")
        patente_car = input("\nPatente del Vehiculo: ")
        marca_car = input("\nMarca del Vehiculo: ")
        precio_car = int(input("\nPrecio del Vehiculo: "))
        fecha_registro_car = input("\nFecha del registro del Vehiculo: ")
        dueño_car = input("\nDueño del Vehiculo: ")
        if precio_car >= 5000000 :
            print("")
        else:
            print("\nEl valor del Vehiculo no es mayor a 5.000.000")
        consulta = input("\nTiene multas?: ")
        if consulta == "SI" or consulta == "si" :
            falta_gravisima = int(input("Cantidad de Faltas Gravisimas (1,5 a 3 UTM): "))
            falta_grave = int(input("Cantidad de Faltas Graves (1 a 1,5 UTM): "))
            falta_menos_grave = int(input("Cantidad de faltas Menos Graves( 0,5 a 1 UTM): "))
            falta_leve = int(input("Cantidad de faltas leves (0,2 a 0,5 UTM): "))
            f_gravisima_monto = 126526 * falta_gravisima
            f_grave_monto = 75915 * falta_grave
            f_menos_grave_monto = 50610 * falta_menos_grave
            f_leve_monto = 25305 * falta_leve
            fecha_ultima_multa = input("Ingrese la fecha de la multa más reciente: ")
            print("Monto aproximado por Faltas Gravisimas: $", f_gravisima_monto, "\nMonto aproximado por Faltas Graves: $", f_grave_monto, "\nMonto aproximado por Faltas Menos Graves: $", f_menos_grave_monto, "\nMonto aproximado por Faltas Leves: $", f_leve_monto)
        else:
            f_gravisima_monto = 0
            f_grave_monto = 0
            f_menos_grave_monto = 0
            f_leve_monto = 0
            fecha_ultima_multa = "" 
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        vehiculo = {
            "tipo": tipo_car,
            "Patente": patente_car,
            "Marca": marca_car,
            "precio": precio_car,
            "FechaRegistro": fecha_registro_car,
            "Dueño": dueño_car
        }

        if consulta == "SI" or consulta == "si":
            vehiculo["Monto Faltas Gravisimas"] = f_gravisima_monto
            vehiculo["Monto Faltas Graves"] = f_grave_monto
            vehiculo["Monto Falta MenosGraves"] = f_menos_grave_monto
            vehiculo["Monto Faltas Leves"] = f_leve_monto
            vehiculo["Fecha Ultima Multa"] = fecha_ultima_multa

        datos.append(vehiculo)
        print("\nEl vehiculo ha sido registrado exitosamente")
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif opcion == 2:
        print("\nHa seleccionado la opcion: Buscar")
        buscar_patente = input("Ingrese la patente del vehiculo que desea buscar: ")
        
        if buscar_patente == 








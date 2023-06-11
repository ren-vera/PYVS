menu_principal = True
tipo_car = 0
patente_car = 0
marca_car = 0
valor_car = 0
multa_car = 0
fecha_multa_car = 0
fecha_registro_car = 0
dueño_car = 0
import random

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
            precio_Car = int(input("\nPRECIO DEL VEHICULO: $"))
            if precio_Car >= 5000000:
                valor_car = precio_Car
            else: 
                print("El precio no es mayor a 5.000.000")
            
            consulta = input("Tiene multas?: ")
            if consulta == "SI" or consulta == "si":
                falta_gravisima = int(input("Cantidad de Faltas Gravisimas (1,5 a 3 UTM): "))
                falta_grave = int(input("Cantidad de Faltas Graves (1 a 1,5 UTM): "))
                falta_menos_grave = int(input("Cantidad de faltas Menos Graves( 0,5 a 1 UTM): "))
                falta_leve = int(input("Cantidad de faltas leves (0,2 a 0,5 UTM): "))
                f_gravisima_monto = 126526 * falta_gravisima
                f_grave_monto = 75915 * falta_grave
                f_menos_grave_monto = 50610 * falta_menos_grave 
                f_leve_monto = 25305 * falta_leve 
                fecha_ultima_multa = input("Ingrese la fecha de la multa más reciente: ")
                print("Monto aproximado por Faltas Gravisimas: $",f_gravisima_monto,"\nMonto aproximado por Faltas Graves: $",f_grave_monto,"\nMonto aproximado por Faltas Menos Graves: $",f_menos_grave_monto,"\n" "Monto aproximado por Faltas Leves: $",f_leve_monto)
            else:
                print("")

            fecha_registro_car = input("\nFecha del registro del vehiculo: ")
            dueño_car = input("\nDueño del vehiculo: ")  
            print("")
            print("\nLos datos ingresados son los siguientes: ","\nTipo de auto: ",tipo_car,"\nPatente del vehiculo: ",patente_car,"\nMarca del vehiculo: ",marca_car,"\nValor del vehiculo: ",precio_Car,"\nMonto aproximado por Faltas Gravisimas: $",f_gravisima_monto,"\nMonto aproximado por Faltas Graves: $",f_grave_monto,"\nMonto aproximado por Faltas Menos Graves: $",f_menos_grave_monto,"\n" "Monto aproximado por Faltas Leves: $",f_leve_monto,"\nFecha de la multa más reciente: ",fecha_ultima_multa,"\nFecha del registro: ",fecha_registro_car,"\nDueño del vehiculo:",dueño_car)
        #//////////////////////////////////////////////////////////////////////////
        elif opcion == 2 :
            print("\n Ha seleccionado la opción: Buscar")
            buscar_patente = input("INGRESE PATENTE: ")   
            print("")
            if buscar_patente == patente_car:
                print("\nLos datos registrados son los siguientes: ","\nTipo de auto: ",tipo_car,"\nPatente del vehiculo: ",patente_car,"\nMarca del vehiculo: ",marca_car,"\nValor del vehiculo: ","\nMonto aproximado por Faltas Gravisimas: $",f_gravisima_monto,"\nMonto aproximado por Faltas Graves: $",f_grave_monto,"\nMonto aproximado por Faltas Menos Graves: $",f_menos_grave_monto,"\n" "Monto aproximado por Faltas Leves: $",f_leve_monto,"\nFecha de la multa más reciente: ",fecha_ultima_multa,"\nFecha del registro: ",fecha_registro_car,"\nDueño del vehiculo:",dueño_car)
            else:
                print("Esa patente no esta registrada.")
        #////////////////////////////////////////////////////////////////////////////
        elif opcion == 3 :
            print("\n Ha seleccionado la opción: Imprimir certificados")
            for i in range(1):
                valor_random_1 = random.randint(1500,3500)
                valor_random_2 = random.randint(1500,3500)
                valor_random_3 = random.randint(1500,3500)
                print("El valor de los certificados de emision de contaminantes tiene un costo de: $", valor_random_1)
                print("El valor de los ceritificados de anotaciones vigentes, tiene un costo de: $", valor_random_2)
                print("El valor de los certificados de multas, tiene un costo de : $",valor_random_3)
            menu_principal = False
        #//////////////////////////////////////////////////////////////////////////
        elif opcion == 4 :
            print("\n Ha seleccionado la opción: Salir \n¡Vuelva Pronto!\nRENATO VERA TECH 1.7")
            break
        #////////////////////////////////////////////////////////////////////////////
        else:
            print("\nSelección invalida, Intente denuevo.")
            
    except ValueError:
        print("\nPor favor ingrese números enteros")
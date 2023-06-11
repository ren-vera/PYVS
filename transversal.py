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

            consulta = input("\n¿El vehiculo tiene multas?: ")
        
            if consulta == "SI" or consulta =="si":
                multa_car = int(input("\nIngrese el monto de la multa: $"))
                fecha_multa_car = input("\nFecha de la multa: ")
        
            else:
                print("")
        
            fecha_registro_car = input("\nFecha del registro del vehiculo: ")
            dueño_car = input("\nDueño del vehiculo: ")  
            lista = "Tipo de auto: ",tipo_car,"Patente del vehiculo: ",patente_car,"Marca del vehiculo: ",marca_car,"Valor del vehiculo: ",valor_car, multa_car, fecha_multa_car,"Fecha del registro: ",fecha_registro_car,"Dueño del vehiculo:",dueño_car
            print("Los datos ingresados son los siguientes: ",)
        #//////////////////////////////////////////////////////////////////////////
        
        elif opcion == 2 :
            print("\n Ha seleccionado la opción: Buscar")
            buscar_patente = input("INGRESE PATENTE: ")   
            if buscar_patente == patente_car:
                print(lista)
            else:
                print("Esa patente no esta registrada ")
            
        
        #////////////////////////////////////////////////////////////////////////
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
            print("\n Ha seleccionado la opción: Salir \n¡Vuelva Pronto!")
            break
        #////////////////////////////////////////////////////////////////////////////
        else:
            print("\nSelección invalida, Intente denuevo.")
            
    except ValueError:
        print("\nPor favor ingrese números enteros")
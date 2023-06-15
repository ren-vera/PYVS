def calcular_iva(numro1:int):
    return numro1 * 0.19




menu = True
try:
    while menu:
        try:
            print("\n----- CALCULADORA -----")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Calcular IVA")
            print("6. Calcular Descuento % ")
            print("7. Calcular IMC")
            print("8. SALIR ")
            
            opcion = int(input("\nSeleccione una opción: "))
            #/////////////////////////////////////////////////////////////////////////
            if opcion == 1 :
                print("\nHa seleccionado la opción Sumar")
                def sumar(a, b):
                    suma = a + b
                    return(suma)
                num1 = int(input("\nIngrese el primer número: "))
                num2 = int(input("\nIngrese el segundo número: "))
                print(f"El resultado de la suma es: ", sumar(num1, num2))
            #/////////////////////////////////////////////////////////////////////////
            elif opcion == 2:
                print("\nHa seleccionado la opción Restar")
                def restar(a, b):
                    resta = a - b
                    return(resta)
                numro1 = int(input("\nIngrese el primer número: "))
                numro2 = int(input("\nIngrese el segundo número: "))
                print(f"El resultado de la resta es: ", restar(numro1, numro2))
            #///////////////////////////////////////////////////////////////////////////////
            elif opcion == 3:
                print("\nHa seleccionado la opción Multiplicar")
                def multiplicacion (a, b):
                    multiplicar = a * b
                    return(multiplicar)
                num11 = int(input("\nIngrese el primer número: "))
                num22 = int(input("\nIngrese el segundo número: "))
                print(f"El resultado de la multiplicación es: ", multiplicacion(num11, num22))
            #///////////////////////////////////////////////////////////////////////////////////
            elif opcion == 4:
                print("\nHa seleccionado la opción Dividir")
                def division(a, b):
                    dividir = a // b
                    return(dividir)
                num111 = int(input("\nIngrese el primer número: "))
                num222 = int(input("\nIngrese el segundo número: "))
                print(f"El resultado de la división es: ", division(num111, num222))
            #//////////////////////////////////////////////////////////////////////////////////
            
            elif opcion == 5:
                print("Ha seleccionado Calcular IVA")
                producto = int(input("Ingrese un valor: "))
                print("El valor es: ",calcular_iva(producto))

            #//////////////////////////////////////////////////////////////////////////////////
            elif opcion == 6:
                print("\nHa seleccionado Calcular Descuento")
                def calculo_desc(precio):
                    calcular_desc = precio * 0.30  # Calcula el monto del descuento
                    return calcular_desc
                precio = float(input("Ingrese el precio: "))  
                descuento = calculo_desc(precio)
                monto_final = precio - descuento  # Calcula el monto final a pagar
                print(f"El monto final a pagar es: {monto_final}")
            #//////////////////////////////////////////////////////////////////////////////////////////////
            elif opcion == 7:
                print("Ha seleccionado Calcular IMC")
            
            
            
            
            
            
            #////////////////////////////////////////////////////////////////////////////////////////////////
            elif opcion == 8:
                print("Ha seleccionado la opción Salir")
                print("Vuelva pronto...")
                menu = False
            #///////////////////////////////////////////////////////////////////////////////////////
            else:
                print("número invaldo")
        except ZeroDivisionError:
            print("NO PUEDE DIVIDIR POR 0")
except ValueError:
    print("SOLO PUEDE INGRESAR NÚMEROS ENTEROS")













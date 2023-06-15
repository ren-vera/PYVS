menu = True
try:
    while menu:
        try:
            print("\n----- CALCULADORA -----")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            
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
                print(f"El resultado de la divisió es: ", division(num111, num222))
            #//////////////////////////////////////////////////////////////////////////////////
            elif opcion == 5:
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













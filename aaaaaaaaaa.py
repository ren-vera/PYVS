falta_gravisima = 0
falta_grave = 0
falta_menos_grave = 0
falta_leve = 0






consulta = input("Tiene multas?: ")
if consulta == "SI" or consulta == "si":
    falta_gravisima = int(input("Cantidad de Faltas Gravisimas (1,5 a 3 UTM): "))
    falta_grave = int(input("Cantidad de Faltas Graves (1 a 1,5 UTM): "))
    falta_menos_grave = int(input("Cantidad de faltas Menos Graves( 0,5 a 1 UTM): "))
    falta_leve = int(input("Cantidad de faltas leves (0,2 a 0,5 UTM): "))
    f_gravisima_monto = 126526 * falta_gravisima
    f_grave_monto = 75915 * falta_grave
    f_menos_g_monto = 50610 * falta_menos_grave 
    f_leve_monto = 25305 * falta_leve 

    print("Monto aproximado por Faltas Gravisimas: $",f_gravisima_monto,"\nMonto aproximado por Faltas Graves: $",f_grave_monto,"\nMonto aproximado por Faltas Menos Graves: $",f_menos_g_monto,"\n" "Monto aproximado por Faltas Leves: $",f_leve_monto)
    
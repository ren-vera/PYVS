#def calcular_imc(peso:int, altura:int):
#    imc = peso / (altura ** 2)
#    return imc

#def peso_persona(imc):
#    if imc < 18.5:
#        return "Bajo peso"
#    elif 18.5 <= imc < 25.0:
#        return "Adecuado"
#    elif 25.0 <= imc < 30.0:
#        return "Sobrepeso"
#    elif 30.0 <= imc < 35.0:
#        return "Obesidad grado 1"
    #elif 35.0 <= imc < 40.0:
   #     return "Obesidad grado 2"
  #  else:
 #       return "Obesidad grado 3"




def calcular_IMC(peso,altura):
    estado = "No calculado"
    IMC = peso / altura **2
    if IMC < 18.5 :
        estado = "Bajo peso"
    elif IMC >= 18.5 and IMC <= 24.9:
        estado = "Adecuado"
    elif IMC >= 25.0 and IMC <= 25.9:
        estado = "Sobrepeso"
    elif IMC >= 30.0 and IMC <= 34.9:
        estado = "Obesidad grado 1"
    elif IMC >= 35.5 and IMC <= 39.9:
        estado = "Obesidad grado 2"
    else:
        print("Obesidad grado 3")
    return estado + "IMC=" + str(IMC)
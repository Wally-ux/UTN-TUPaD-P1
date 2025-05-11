#8.	Crear una función llamada calcular_imc(peso, altura) 
# que reciba el peso en kilogramos y la altura en metros,
#  y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#funciones
def calcular_imc(peso, altura): #iMC = peso (kg)/ estatura (m2)
    imc= peso/altura**2
    return imc

#programa principal
peso=float(input("por favor ingrese su peso en kilogramos por favor(NOTA:LOS NUMEROS DECIMALES VAN CON PUNTO): "))
altura=float(input("por favor ingrese su peso en altura en metros por favor(NOTA:LOS NUMEROS DECIMALES VAN CON PUNTO): "))

imc=calcular_imc(peso, altura) 

print ("el IMC de la persona es: " , imc , "kg/mts")
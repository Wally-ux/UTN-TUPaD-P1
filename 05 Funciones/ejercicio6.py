#6.	Crear una función llamada tabla_multiplicar(numero) 
# que reciba un número como parámetro y imprima la tabla 
# de multiplicar de ese número del 1 al 10. Pedir 
# al usuario el número y llamar a la función.

#funciones
def tabla_multiplicar(numero):
    for contador in range (1,11):
        tabla=numero*contador
        print("la tabla de multiplicar del numero" , numero , "es", tabla)

#programa principal
numero= int(input("porfavor ingrese un numero para saber su tabla de multiplicar: "))
tabla=tabla_multiplicar(numero)


#revisar ejercicio
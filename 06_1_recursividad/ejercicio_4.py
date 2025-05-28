#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
#unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 
#procedimiento: 
#1. Dividir el número por 2. 
#2. Guardar el resto (0 o 1). 
#3. Repetir el proceso con el cociente hasta que llegue a 0. 
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.


#funcion
def decimal_a_binario(n):
    if n == 0: #en caso que el usuario coloque como numero decimal 0 
        return "0"
    elif n ==1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    #dividimos por 2  obtenemos el resto + pasamos el numeor a cadena asi no suma el numero base 10
        #construmos un cadena en bas binaria
# Programa principal
numero = int(input("Ingresá un número decimal: "))
binario = decimal_a_binario(numero)
print( "el numero binario es: ", binario)



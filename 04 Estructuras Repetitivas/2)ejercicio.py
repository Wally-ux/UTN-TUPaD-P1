#2)	Desarrolla un programa que solicite al usuario
#  un número entero y determine la cantidad de dígitos que contiene. 

digitos=0
import math
numero= int(input("por favor escrbia un numero entero:"))

while numero != 0:
        numero=numero // 10  #divide el número entre 10 y descarta los decimales (división entera).
                        #Es como hacer una "división redondeada hacia abajo".
        digitos =digitos + 1  # Incrementamos el contador

# Si el número es 0, tiene 1 dígito
if numero == 0:
        digitos= 1

print ( digitos, "digitos")



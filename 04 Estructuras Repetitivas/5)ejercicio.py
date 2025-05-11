#5)	Crea un juego en el que el usuario deba adivinar 
#un número aleatorio entre 0 y 9. Al final, el programa 
#debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random
numero_secreto= random.randint(0,9)

numero = int(input("ingrese un numero del 0 al 9 para adivinarlo "))
intentos=1

if numero== numero_secreto:
        print ("adivinaste, el numero sevreto es el  " , numero_secreto, ", tuvistes" , intentos,"intentos")

else:
    while numero != numero_secreto:
        intentos += 1
        numero=int(input("ingrese un numero del 0 al 9 para adivinarlo "))
    print ("excelente, adivinaste!!!el numero secreto es", numero_secreto, "tuvistes" , intentos, "intentos")
    
                
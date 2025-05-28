##5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es. 
#     Requisitos: 
#La solución debe ser recursiva. 
#No se debe usar [::-1] ni la función reversed(). 

#Una palabra que se lee igual de izquierda a derecha que de derecha a izquierda, como:

#funcion 
# palindormo :Una palabra que se lee igual de izquierda 
# a derecha que de derecha a izquierda

#funcion
def es_palindromo(palabra):
    if len(palabra) <= 1: 
        return True
    elif palabra [0] != palabra[-1]: #comparamos la 1ra palabra con la ultima palabra si son distintas, no es palindromo
        return False
    
    return es_palindromo(palabra[1:-1])


#programa principal 
palabra = (input("Ingresá una palabra sin espacios ni tildes: ")).lower()

if es_palindromo(palabra) == True:
    print(f"La Palabra {palabra} Es un palíndromo")
else:
    print(f"{palabra} No es un palíndromo")
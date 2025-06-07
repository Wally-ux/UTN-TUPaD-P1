#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra. 


frase = input("Ingresá una frase: ")
palabras = frase.split() #separa ñas palabras con espacios

unicas = set(palabras) #convierte las lista en set asi eliminados los dupplicados
print("Palabras únicas:", unicas)

recuento = {} #Crear o definir un diccionario para ver cuantass veces aparece la palabra
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Recuento:", recuento)

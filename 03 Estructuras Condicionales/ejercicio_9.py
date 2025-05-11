#9)Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#*Menor que 3:** "Muy leve" (imperceptible).
#*Mayor o igual que 3  y menor que 4:** "Leve" (ligeramente perceptible).
#*Mayor o igual que 4  y menor que 5:** "Moderado" (sentido por personas, pero generalmente no causa daños).
#*Mayor o igual que 5  y menor que 6:** "Fuerte" (puede causar daños en estructuras débiles).
#*Mayor o igual que 6  y menor que 7:** "Muy Fuerte" (puede causar daños significativos).
#*Mayor o igual que 7:** "Extremo" (puede causar graves daños a gran escala).

# Pedimos al usuario que ingrese la magnitud del terremoto
magnitud_terremoto = float(input("Por favor, ingrese la magnitud del terremoto según la escala de Ritcher: "))

# Si la magnitud del terremoto es menor que 3, imprimimos "Muy leve"
if magnitud_terremoto < 3:
    print("Muy leve")
# Si la magnitud del terremoto es mayor o igual que 3 y menor que 4, imprimimos "Leve"
elif 3 <= magnitud_terremoto < 4:
    print("Leve")
# Si la magnitud del terremoto es mayor o igual que 4 y menor que 5, imprimimos "Moderado"
elif 4 <= magnitud_terremoto < 5:
    print("Moderado")
# Si la magnitud del terremoto es mayor o igual que 5 y menor que 6, imprimimos "Fuerte"
elif 5 <= magnitud_terremoto < 6:
    print("Fuerte")
# Si la magnitud del terremoto es mayor o igual que 6 y menor que 7, imprimimos "Muy fuerte"
elif 6 <= magnitud_terremoto < 7:
    print("Muy fuerte")
# En cualquier otro caso, imprimimos "Extremo". Esto en este caso equivale a decir
# elif magnitud_terremoto >= 7 porque es el único caso que no está cubierto hasta el momento
else:
    print("Extremo")
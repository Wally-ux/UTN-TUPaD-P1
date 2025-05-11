#Escribir un programa que solicite al usuario su edad e 
# imprima por pantalla a cuál de las siguientes categorías pertenece:
#*Niño/a:** menor de 12 años.
#*Adolescente:** mayor o igual que 12 años y menor que 18 años.
#*Adulto/a joven:** mayor o igual que 18 años y menor que 30 años.
#*Adulto/a:** mayor o igual que 30 años.

edad= int(input("por favor ingrese su edad: "))

#adulto joven
if edad >= 30:
    print ("adulto")
elif edad >= 18 and edad < 30:
    print("adulto joven")
elif edad >= 12:
    print("adolescente")

else:
    print ("niño")



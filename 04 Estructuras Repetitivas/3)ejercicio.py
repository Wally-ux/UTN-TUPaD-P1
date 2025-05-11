#3)	Escribe un programa que sume todos los números enteros comprendidos entre 
#dos valores dados por el usuario, excluyendo esos dos valores. 

valor1= int(input("ingrese el 1er valor, tiene que ser menor al 2do numero "))
valor2= int(input("ingrese el 2do valor,tiene que ser mayor al 1ro"))

# Determinar los límites en orden ascendente usando loops
if valor1 < valor2:
    inicio = valor1 + 1
    fin = valor2
else:
    inicio = valor2 + 1
    fin = valor1

# Calcular la suma usando un bucle
suma = 0
for numero in range(inicio, fin):
    suma += numero #suma = suma + numero
#suma = sum(range(inicio, fin))  Hace exactamente lo mismo, pero usando la función incorporada sum() de Python, que es más rápida y concisa. Esa línea reemplaza completamente al bucle anterior.
#Nota: No es necesario usar ambas; una sola de las dos alcanza.

print(f"La suma de los números entre {valor1} y {valor2}, excluyéndolos, es: {suma}")


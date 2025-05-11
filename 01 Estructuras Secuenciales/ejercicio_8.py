#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#-modo:


peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros(ejemplo:1.7): "))

# Realizamos el cálculo del IMC Redondeamos a 2 decimales
#roudn una función incorporada (built-in), por lo tanto no necesitas importar
imc = round(peso / altura**2, 2)

# Imprimimos por pantalla el resultado
print(f"Su IMC es de: {imc}.")

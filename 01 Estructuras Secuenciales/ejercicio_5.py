#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))

# Realizamos la conversión de segundos a horas, sabiendo que una hora equivale a 3600 segundos
cantidad_horas = round(cantidad_segundos / 3600, 2)

# Imprimimos el resultado por pantalla
print(f"El equivalente a {cantidad_segundos} segundos son {cantidad_horas} horas.")
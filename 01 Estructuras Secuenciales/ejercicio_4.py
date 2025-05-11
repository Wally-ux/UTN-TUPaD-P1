#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro.
# imprtamos math 
import math


radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))

# Realizamos el cálculo del área del círculo
# A=PI.R**2
area_circulo = math.pi * (radio_circulo)**2

# Realizamos el cálculo del perímetro del círculo
#Perímetro = 2 * π * r
perimetro_circulo = 2 * math.pi * radio_circulo

# Imprimimos ambos resultados por pantalla
print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.") 
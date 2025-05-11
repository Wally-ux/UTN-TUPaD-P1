#4.	Crear dos funciones: calcular_area_circulo(radio) 
# que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro
#  y devuelva el perímetro del círculo. Solicitar el radio al usuario 
# y llamar ambas funciones para mostrar los resultados


import math
#funcion recibe el radio como parametro y devuelve area de circulo
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)#formula
    return area
#funcion recibe el radio como parametro y devuele el perimetro del circulo
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio #formula
    return perimetro

# programa principal, pedimos datos al usuario,llamamos a la funcion
#para que nos devuelba radio y area, imprimimos
radio = float(input("Introduce el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo con radio {radio} es: {area:.2f}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro:.2f}")
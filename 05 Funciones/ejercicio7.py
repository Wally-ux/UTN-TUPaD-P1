
#7.	Crear una función llamada operaciones_basicas(a, b) 
# que reciba dos números como parámetros y devuelva una 
# tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

#funciones  
def operaciones_basicas(a, b):
    suma = a + b  #0
    resta = a - b    #1
    multiplicacion = a * b  #2
    # Manejo de división por cero
    if b != 0:               #3S
        division = a / b
    else:
        division = "No es posible (división por cero)"
    
    return (suma, resta, multiplicacion, division)

# Solicitar números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Llamar a la función y obtener los resultados
resultados = operaciones_basicas(num1, num2)

# Mostrar los resultados de forma clara
print(f"Resultados de operaciones con {num1} y {num2}:")
print(f"Suma: {num1} + {num2} = {resultados[0]}")
print(f"Resta: {num1} - {num2} = {resultados[1]}")
print(f"Multiplicación: {num1} x {num2} = {resultados[2]}")
print(f"División: {num1} ÷ {num2} = {resultados[3]}")
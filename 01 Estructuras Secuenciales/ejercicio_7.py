#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

numero_a = float(input("Por favor, ingrese un número distinto de 0: "))
numero_b = float(input("Por favor, ingrese otro número distinto de 0: "))

# Realizamos la suma y la almacenamos en la variable suma_a_b
suma_a_b = numero_a + numero_b

# Realizamos la división y la almacenamos en la variable division_a_b. Redondeamos a 2 decimales.
division_a_b = round(numero_a / numero_b, 2)

# Realizamos la multiplicación y la almacenamos en la variable multiplicacion_a_b
multiplicacion_a_b = numero_a * numero_b

# Realizamos la resta y la almacenamos en la variable resta_a_b
resta_a_b = numero_a - numero_b

# Imprimimos el resultado por pantalla. En este caso hacemos una impresión de varias líneas por lo que usamos comillas triples
print(f"""
  Resultado de la suma: {suma_a_b}
  Resultado de la división: {division_a_b}
  Resultado de la multiplicación: {multiplicacion_a_b}
  Resultado de la resta: {resta_a_b}
      """)
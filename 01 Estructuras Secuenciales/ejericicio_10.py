 #10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números. 
numero_a = float(input("Por favor, ingrese el primer número: "))
numero_b = float(input("Por favor, ingrese el segundo número: "))
numero_c = float(input("Por favor, ingrese el tercer número: "))

# Realizamos la suma y la almacenamos en la variable suma_a_b_c
suma_a_b_c = numero_a + numero_b + numero_c

# Calculamos promedio_a_b_c. Redondeamos a 2 decimales.
promedio_a_b_c = round(suma_a_b_c/3, 2)

print(f"El promedio de los números ingresados es {promedio_a_b_c}.")
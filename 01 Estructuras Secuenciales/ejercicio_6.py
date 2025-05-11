#6#) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número. 

numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))

# Realizamos las multiplicaciones correspondientes
numero_por_0 = numero_a_multiplicar * 0
numero_por_1 = numero_a_multiplicar * 1
numero_por_2 = numero_a_multiplicar * 2
numero_por_3 = numero_a_multiplicar * 3
numero_por_4 = numero_a_multiplicar * 4
numero_por_5 = numero_a_multiplicar * 5
numero_por_6 = numero_a_multiplicar * 6
numero_por_7 = numero_a_multiplicar * 7
numero_por_8 = numero_a_multiplicar * 8
numero_por_9 = numero_a_multiplicar * 9
numero_por_10 = numero_a_multiplicar * 10

# Imprimimos el resultado por pantalla.
#  En este caso hacemos una impresión de varias líneas por lo que usamos comillas triples
print(f"""
  {numero_a_multiplicar} x 0 = {numero_por_0}
  {numero_a_multiplicar} x 1 = {numero_por_1}
  {numero_a_multiplicar} x 2 = {numero_por_2}
  {numero_a_multiplicar} x 3 = {numero_por_3}
  {numero_a_multiplicar} x 4 = {numero_por_4}
  {numero_a_multiplicar} x 5 = {numero_por_5}
  {numero_a_multiplicar} x 6 = {numero_por_6}
  {numero_a_multiplicar} x 7 = {numero_por_7}
  {numero_a_multiplicar} x 8 = {numero_por_8}
  {numero_a_multiplicar} x 9 = {numero_por_9}
  {numero_a_multiplicar} x 9 = {numero_por_10}
      """)
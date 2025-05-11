#Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla 
# el mensaje "Ha ingresado un número par"; en caso contrario, 
# imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# Pedimos al usuario que ingrese un número
numero = int(input("Por favor, ingrese un número entero: "))

# Si se ingresa un número par, imprimimos "Ha ingresado un número par"
if numero % 2 == 0:
    print("Ha ingresado un número par")
# En caso contrario, imprimimos "Por favor, ingresar un número par"
else:
    print("Por favor, ingresar un número par")
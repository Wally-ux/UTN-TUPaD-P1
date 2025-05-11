#8)Escribir un programa que solicite al usuario que ingrese su nombre 
# y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

#El programa debe transformar el nombre ingresado de acuerdo a la 
# opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python 
# para convertir entre mayúsculas y minúsculas.


# Pedimos al usuario que ingrese su nombre
nombre = input("Por favor, ingrese su nombre: ")

# Imprimimos por pantalla las opciones posibles y pedimos al usuario que ingrese la opción que desea
print("""
En este programa puede realizar cualquiera de las siguientes operaciones:
1. Si quiere su nombre en mayúsculas.
2. Si quiere su nombre en minúsculas.
3. Si quiere su nombre con la primera letra mayúscula.
""")
opcion = int(input("Ingrese el número de operación que desea realizar: "))


# Si el usuario eligió la opción 1, imprimimos su nombre en mayúsculas
if opcion == 1:
    nombre_mayuscula = nombre.upper() #convierte todas las letras de una cadena (string) a mayúsculas.

    print(nombre_mayuscula)
# Si el usuario eligió la opción 2, imprimimos su nombre en minúsculas
elif opcion == 2:
    nombre_minuscula = nombre.lower() #convierte a minuscula
    print(nombre_minuscula)
# Si el usuario eligió la opción 3, imprimimos su nombre con la primera letra en mayúscula
elif opcion == 3:
    nombre_title = nombre.title() #1er letra mayuscula
    print(nombre_title)
# Si el usuario eligió otro número de opción, imprimimos "Por favor, ingrese únicamente 1, 2 o 3"
else:
    print("Por favor, ingrese únicamente 1, 2 o 3")
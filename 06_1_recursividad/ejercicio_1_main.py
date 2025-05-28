#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

from ejercicio_1 import factorial_num # importamos la funcion facltorial_num que esta en ejercicio_1

num = int (input ("Ingrese un número para mostrar los factoriales desde 1 hasta ese número: "))

# Recorremos desde 1 hasta num +1 para ilcuir el numero dado
for i in range(1, num + 1):
    print(f"Factorial de {i} es {factorial_num(i)}")

    #factorial_num(i): llamamos a la función recursiva para calcular el factorial de ese número.



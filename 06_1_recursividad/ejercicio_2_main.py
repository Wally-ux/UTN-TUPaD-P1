#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 
#retunr valor de fibo en la posicion indicada
#valor         0 1 1 2 3 5 8  13  21
#psicion       0 1 2 3 4 5 6   7   8 

#importamos la funcion fibo_recursivo  del  archivo ejericio 2 
from ejercicio_2 import fibonacci_recursivo

num=int(input("ingrese un numero para saber la posicion que ocupa en la serie de fibonaccio: "))

for i in range (num):
    print (f"En la posicion {i}, tenemos el valor de fibonacci: {fibonacci_recursivo(i)}")
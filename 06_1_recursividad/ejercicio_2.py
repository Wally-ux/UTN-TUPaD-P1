#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 

#retunr valor de fibo en la posicion indicada
#valor         0 1 1 2 3 5 8 11 
#psicion       0 1 2 3 4 5 6 7 
def fibonacci_recursivo(posicion):
    if posicion ==0:
        return 0
    elif posicion==1:
        return 1
    else:
        return fibonacci_recursivo(posicion -1)+ fibonacci_recursivo(posicion-2)

if __name__=="__main__":
    print (fibonacci_recursivo(6))

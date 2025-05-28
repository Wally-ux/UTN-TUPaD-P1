#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

#definicion de funciones
def factorial_num(n):
    if n== 0:
        return 1   #caso base devuelve 1
    else:
        return n * factorial_num(n-1)
    
if __name__== "__main__":
    print (factorial_num(2))




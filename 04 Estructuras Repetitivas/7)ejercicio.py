#7)	Crea un programa que calcule la suma de todos 
# los números comprendidos entre 0 y un número entero 
#positivo indicado por el usuario. 


numero= int(input("por favor ingrese un numero entero positivo: "))
cont=0
acumulador=0
for cont in range (0,numero+1):
    acumulador += cont #acumulador += valor     equivale a acumular
    print(cont)
print ("la suma de todos los numeros es: ", acumulador)

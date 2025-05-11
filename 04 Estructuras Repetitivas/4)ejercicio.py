#4Elabora un programa en  que permita al usuario ingresar números enteros y los sume en secuencia. .
#El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.



sumatoria=0
numero=int(input("ingrese un numero entero, (para cortar el programa ingrese el numero cero): "))
if numero == 0 :
    print("el numero es cero")

else: 
    while numero !=0:
        sumatoria += numero
        numero=int(input("ingrese un numero entero, (para cortar el programa ingrese el numero cero): "))
    
    print("la sumatoria de los numeros entero es: " , sumatoria)
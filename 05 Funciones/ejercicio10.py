#10.Crear una función llamada calcular_promedio(a, b, c) 
# que reciba tres números como parámetros y devuelva 
# el promedio de ellos. Solicitar los números al usuario 
# y mostrar el resultado usando esta función.

#funcion
def calcular_promedio (a,b,c):
    promedio= (a+b+c)/3
    return promedio
    


#funcion principal
a=int(input("ingrese el primer numero : "))
b=int(input("ingrese el segundo numero : "))
c=int(input("ingrese el tercer numero : "))

promedio=calcular_promedio (a,b,c)

print(f"el promedio de los 3 numero ingresados es {promedio}" )


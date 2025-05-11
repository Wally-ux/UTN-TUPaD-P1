#Elabora un programa que permita al usuario ingresar 
# 100 números enteros y luego calcule la media de esos valores.
#  (Nota: puedes probar el programa con una cantidad menor, 
# pero debe poder procesar 100 números cambiando solo un valor). 


acumu= 0
contador = 0
media= 0

# Repetimos 10 veces para solicitar los números
for cont in range(10):
    numero = int(input(f"Ingrese el número {cont + 1} de 10: "))
    contador += 1 #contador += 1  # Equivalente a: contador = contador + 1
    acumu += numero #acumulador += valor  # Equivalente a: acumulador = acumulador + valor suma los numers
print("/////////////////////////////////")
print(f"el promedio de los numero ingresados es {(acumu/contador)} ")

print("/////////////////////////////////")

#ejercicios autoevaluacion
x=0
for i in range (1,6):
    x+=i
    print(i)
    if x >10:
        break
print (x)

print ("///////////////")
for i in range (1,10,2):
    print(i)

print ("///////////////")
for i in range (0,10,2):
    if i % 3 == 0 :
        print(i)

print ("///////////////")
nums= [1,2,3,4,5]
result = 1
for num in nums:
    result *= num
    if result >10:
        break

print (result)
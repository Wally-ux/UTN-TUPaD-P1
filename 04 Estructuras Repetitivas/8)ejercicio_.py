#Escribe un programa que permita al usuario 
# ingresar 100 números enteros. Luego, 
# el programa debe indicar cuántos de estos números son pares
# , cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, 
# pero debe estar preparado para procesar 100 números con un solo cambio). 


pares = 0
impares = 0
negativos = 0
positivos = 0

# Repetimos 10 veces para solicitar los números
for cont in range(100):
    numero = int(input(f"Ingrese el número {cont + 1} de 10: "))
    
    # Contar si el número es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contar si el número es negativo o positivo
    if numero < 0:
        negativos += 1 #numero=numero + 1 es equivalente a contar
    elif numero > 0:
        positivos += 1
    # Si el número es 0, no se cuenta como positivo ni negativo

print("/////////////////////////////////")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números positivos: {positivos}")
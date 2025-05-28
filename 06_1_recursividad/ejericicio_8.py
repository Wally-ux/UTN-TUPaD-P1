#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número. 
#      Ejemplos: 
#contar_digito(12233421, 2)   → 3   
#contar_digito(5555, 5)       → 4   
#contar_digito(123456, 7)     → 0   

# Función contar digitoo
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        # comparamos y sacamos mod
        ultimo = numero % 10
        
        # Si coincide con el dígito buscado, sumamos 1
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Programa principal
numero = int(input("Ingresá un número entero positivo: "))
digito = int(input("Ingresá el dígito que querés contar (0 a 9): "))

resultado = contar_digito(numero, digito)

print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
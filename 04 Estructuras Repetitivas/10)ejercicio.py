numero = int(input("Ingrese un número entero: "))
reverso = 0
original=numero

while original > 0:
    ultimo_digito = original % 10  # Obtener último dígito
    reverso = reverso * 10 + ultimo_digito  # Construir número invertido
    original = original // 10  # Eliminar último dígito
    
    

print("Número invertido:", reverso)
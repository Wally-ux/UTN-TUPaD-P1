#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

# Crear diccionario vacío para almacenar los contactos
agenda_telefonica = {}

# Cargar 5 contactos
print(" Cargar 5 contactos en la agenda:")
i=1
for i in range(1,6):
    nombre = input(f"Ingresá el nombre del contacto {i}: ")
    numero_telefono = int(input(f"Ingresá el número telefónico de {nombre}: "))
    agenda_telefonica[nombre] = numero_telefono

print (agenda_telefonica)

ver_agenda= input(f"ingrese el nombre de la persona el cual necesita el numero telefonico, nombre: ")
print (f"el numero de {ver_agenda} es: {agenda_telefonica[ver_agenda]}")

consulta = input("Ingresá el nombre del contacto a consultar: ")

if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print("Contacto no encontrado.")

 
#definicion de funciones
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre_usuario = input("Introduce tu nombre: ")
mensaje = saludar_usuario(nombre_usuario)
print(mensaje)

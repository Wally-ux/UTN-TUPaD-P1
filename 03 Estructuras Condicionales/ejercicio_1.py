#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.  

# Pedimos al usuario que ingrese su edad
edad = int(input("Por favor, ingrese su edad en años: "))

# Si la edad es mayor que 18, imprimimos "Es mayor de edad"
if edad > 18:
  print("Es mayor de edad")
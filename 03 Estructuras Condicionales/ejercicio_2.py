#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”.  

# Pedimos al usuario que ingrese su nota
nota = float(input("Por favor, ingrese su nota: "))

# Si la nota es mayor o igual que 6, imprimimos "Aprobado"
if nota >=6:
  print("Aprobado")
# En caso contrario, imprimimos "Desaprobado"
else:
  print("Desaprobado")
#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 

temperatura_celsius = float(input("Por favor, una temperatura en °C: "))

#convertimos  celsius a fahrenheit y redondeamos el decimal
temperatura_fahrenheit = round((9/5)*temperatura_celsius+32, 2)

# Imprimimos por pantalla el resultado
print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F.")
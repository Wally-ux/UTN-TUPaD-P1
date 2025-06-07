#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno. 
#Ejemplo: 
#alumnos={
#"Sofía": (10, 9, 8),
#"Luis": (6,7,7)}

alumnos = {}

for i in range(3):
    nombre = input(f"vuelta {i},Ingresá el nombre del alumno {i+1}: ")
    print(f"Ingresá 3 notas para {nombre}:")
    
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    notas = (nota1, nota2, nota3)  # tupla de 3 notas
    alumnos[nombre] = notas

print(" Promedios por alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
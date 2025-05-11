 #Crear una función llamada informacion_personal(nombre, apellido,
 #edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 #[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#gresados


def informacion_personal(nombre, apellido, edad, residencia):
    return f"soy {nombre} {apellido} , tengo {edad} años y vivo en {residencia}"


#programa principal
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
residencia = input("Introduce tu lugar de residencia: ")
datos=informacion_personal(nombre, apellido, edad, residencia)

print(datos)


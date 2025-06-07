#0) Dado un diccionario que mapea nombres de países
#  con sus capitales, construí un nuevo 
#dccionario donde: 
# Las capitales sean las claves. 
# Los países sean los valores. 
#ejemplo:
original={"argentina":"buenos aires"}

invertir={}

for pais,capital in original.items():# Recorrer con for
    invertir [capital]=pais

print (f"el diccionario orignal de paises y capitales es: {original}")
print (f"el diccionario invertido de paises y capitales es: {invertir}")



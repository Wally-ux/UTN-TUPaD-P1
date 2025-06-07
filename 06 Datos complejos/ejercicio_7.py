#7)Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

# Intersección &
ambos = parcial1 & parcial2 

#Diferencia simétrica ^ 
# Devuelve los elementos que  están en uno de los dos , pero no en los dos.
solo_uno = parcial1 ^ parcial2 

#Unión se representa con barra vertical | 
al_menos_uno = parcial1 | parcial2# 

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

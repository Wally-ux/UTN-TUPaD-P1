#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#-algoritmo general. 

#fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1)  
#             n   *   n(m-1)
# n elevado a la m=
# n=base es una sola vez el número que se multiplica.
# potencia(base, exponente - 1) calculamos el resto de las multiplicaciones.
#n y m determina el usuario 

from ejercicio_3 import potencia 

num_1=int(input("Ingrese la base del numero: ")) #pedimos la base al usuario
num_2=int(input("Ingrese la potencia: ")) #pedimos la pontecia al usuario


print(f"La pontencia del numero {num_1} es {potencia(num_1,num_2)}")
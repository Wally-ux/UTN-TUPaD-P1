#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#-algoritmo general. 

#fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1)  
#             n   *   n(m-1)
# n elevado a la m=
# n=base es una sola vez el número que se multiplica.
# potencia(base, exponente - 1) calculamos el resto de las multiplicaciones.
#n y m determina el usuario 

#funcion
def potencia(n,m):
    if m==0: #exponente es ==0 es el caso base
        return 1 

    else:    
        return n*potencia(n,m-1)

#programa principal
if __name__=="__main__":
    print (potencia(2,3))


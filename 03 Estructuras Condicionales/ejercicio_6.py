# Importamos todas los paquetes y funciones que necesitamos utilizar
import random
from statistics import mode, median, mean

# Generamos una lista de 50 números de forma aleatoria
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos la moda, la mediana y la media de la lista numeros_aleatorios
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Si la media es mayor que la mediana y la mediana es mayor que la moda, imprimir "Sesgo positivo o a la derecha"
if media > mediana > moda:
  print("Sesgo positivo o a la derecha")
# Si la media es menor que la mediana y la mediana es menor que la moda, imprimir "Sesgo negativo o a la izquierda"
elif media < mediana < moda:
  print("Sesgo negativo o a la izquierda")
# Si la media, la mediana y la moda son iguales, imprimir "Sin sesgo"
elif media == mediana == moda:
  print("Sin sesgo")
# Si no se cumple ninguna de las condiciones anteriores, imprimir "No se puede determinar si esta distribución tiene sesgo o no"
else:
  print("No se puede determinar si esta distribución tiene sesgo o no")
#8) Armá un diccionario donde las claves sean nombres de productos 
# y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 

productos= {"arroz":5,"fideos":4, "atun":7}

producto = input("Ingresá el nombre del producto: ")

if producto in productos:
    # Sumamos esa cantidad al stock actual
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {productos[producto]}")
else:
    # sini Lo agregamos al diccionario con ese stock
    nuevo_stock = int(input("Producto nuevo. Ingresá el stock inicial: "))
    productos[producto] = nuevo_stock
    # Confirmamos que el producto fue agregado
    print(f"Producto {producto} agregado con {nuevo_stock} unidades.")


def agregar_producto(productos):

    nombre = input("Ingrese nombre del producto: ").strip()
    stock = int(input("Ingrese stock del producto: "))
    precio = int(input("Ingrese precio del producto: "))

    # En vez de una lista, guardas un mini-diccionario con etiquetas claras
    productos[nombre] = {
        "stock": stock,
        "precio": precio
    }
    print("Producto agregado exitosamente.")

def mostrar_productos(productos):

    if len(productos) == 0:
        print("No hay productos registrados.")
    else:

        for nombre, datos in productos.items():

            print(f"Productos: {nombre} / stock: {datos['stock']} / precio: {datos['precio']}")

def buscar_producto(productos):

    if len(productos) == 0:
        print("No hay productos registrados.")
    else:

        buscado = input("Que producto desea buscar: ").strip()

        if buscado in productos:
            print(f"Producto encontrado {buscado} / stock: {productos[buscado]['stock']} / precio: {productos[buscado]['precio']}")
        else:
            print("Producto no encontrado.")

def producto_mas_caro(productos):

    if len(productos) == 0:
        print("No hay productos registrados.")
    else:

        precioMayor = -1
        nombreProducto = ""

        for nombre, datos in productos.items():

            if precioMayor < datos["precio"]:
                precioMayor = datos["precio"]
                nombreProducto = nombre

        print(f"El producto mas caro es {nombreProducto} y el precio mayor es: {precioMayor}")
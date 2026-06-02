def agregar_productos(productos):

    nombre = input("Ingrese el nombre del producto: ")
    stock = int(input("Ingrese el stock del producto: "))
    precio = int(input("Ingrese el precio del producto: "))

    productos[nombre] = [stock, precio]
    print("Producto agregado con éxito.")

def mostrar_productos(productos):

    if len(productos) == 0:
        print("No hay productos registrados en el inventario.")
    else:
        print("=== LISTA DE PRODUCTOS ===")
        for nombre, datos in productos.items():

            print(f"Producto: {nombre} / Stock: {datos[0]} / Precio: {datos[1]}")

def buscar_productos(productos):

    if len(productos) == 0:
        print("No hay productos registrados en el inventario.")
    else:
        nombreBuscar = input("Ingrese el producto que desea buscar: ")

        if nombreBuscar in productos:
            datos = productos[nombreBuscar]
            print(f"Producto encontrado -> Stock: {datos[0]} / Precio: {datos[1]}")
        else:
            print("El producto no existe en el inventario.")

def producto_mas_caro(productos):

    if len(productos) == 0:
        print("No hay productos registrados en el inventario.")
    else:

        nombre_mayor = ""
        precio_mayor = -1

        for nombre, datos in productos.items():

            precio_actual = datos[1]

            if precio_actual > precio_mayor:
                precio_mayor = precio_actual
                nombre_mayor = nombre

        print(f"El producto más caro es: {nombre_mayor} con un precio de ${precio_mayor}")

productos = {}

while True:

    print("=== MENU ===")
    print("1. Agregar Producto")
    print("2. Mostrar Productos")
    print("3. Buscar Producto")
    print("4. Producto mas caro")
    print("5. Salir")

    while True:
        try:
            opcionMenu = int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print("Opcion no valida, debe ser una opcion entre (1-5)")


    match opcionMenu:

        case 1:
            agregar_productos(productos)

        case 2:
            mostrar_productos(productos)

        case 3:
            buscar_productos(productos)

        case 4: 
            producto_mas_caro(productos)

        case 5:
            break

        case _:
            print("Opcion no valida, Debe ser una opcion entre (1-5)")

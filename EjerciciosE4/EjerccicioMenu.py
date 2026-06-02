def agregar_productos(productos):

    while True:
        # .strip() elimina espacios vacíos que el usuario pueda escribir al inicio o final
        nombre = input("Ingrese el nombre del producto: ").strip()

        if nombre == "":
            print("El nombre no debe estar vacio")
        elif nombre in productos: # 'in' revisa si la clave ya existe en el diccionario
            print("El producto ya esta registrado.")
        else:
            break
    
    while True:
        try:
            stock = int(input("Ingrese el stock del producto: "))

            if stock >= 0:
                break
            else:
                print("El stock debe ser mayor o igual a 0")
        except ValueError:
            print("Debe ingresar un valor numerico")
    
    while True:
        try:
            precio = int(input("Ingrese el precio del producto: "))

            if precio > 0:
                break
            else:
                print("El precio debe ser mayor a 0")
        except ValueError:
            print("Debe ingresar un valor numerico")

    # Guardar en el diccionario: la clave es el 'nombre' y el valor es la lista [stock, precio]
    productos[nombre] = [stock, precio]
    print("Producto agregado con éxito.")

def mostrar_productos(productos):

    # Validamos si el diccionario no tiene elementos
    if len(productos) == 0:
        print("No hay productos registrados en el inventario.")
    else:
        print("=== LISTA DE PRODUCTOS ===")

        # .items() nos permite extraer la Clave (nombre) y el Valor (datos) al mismo tiempo
        for nombre, datos in productos.items():

            print(f"Producto: {nombre} / Stock: {datos[0]} / Precio: {datos[1]}")

def buscar_productos(productos):

    if len(productos) == 0:
        print("No hay productos registrados en el inventario.")
    else:
        nombreBuscar = input("Ingrese el producto que desea buscar: ")

        # 'in' verifica si el nombre ingresado existe como una clave en el diccionario
        if nombreBuscar in productos:
            datos = productos[nombreBuscar]# Trae la lista [stock, precio] de ese producto
            print(f"Producto encontrado -> Stock: {datos[0]} / Precio: {datos[1]}")
        else:
            print("El producto no existe en el inventario.")

def producto_mas_caro(productos):

    if len(productos) == 0:
        print("No hay productos registrados en el inventario.")
    else:

        # Variables para guardar el nombre y precio del producto más caro encontrado
        nombre_mayor = ""
        precio_mayor = -1 # Empezamos en -1 para que cualquier precio real sea mayor

        #recorremos el diccionario buscando el mas caro
        for nombre, datos in productos.items():

            precio_actual = datos[1] #precio está en la posición 1 de la lista 'datos'

            # Si el precio del producto actual supera al máximo que conocemos
            if precio_actual > precio_mayor:
                precio_mayor = precio_actual # Actualizamos el precio más alto
                nombre_mayor = nombre        # Guardamos el nombre del nuevo producto más caro

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

import funciones as fn

productos = {}

while True:

    print("=== MENU ===")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto mas caro")
    print("5. Salir")

    try:
        opcionMenu = int(input("Ingrese una opcion del menu: "))
    except ValueError:
        print("Error, debe ingresar un valor numerico.")
        continue
        
    match opcionMenu:

        case 1:
            fn.agregar_producto(productos)
        case 2:
            fn.mostrar_productos(productos)
        case 3:
            fn.buscar_producto(productos)
        case 4:
            fn.producto_mas_caro(productos)
        case 5:
            break
        case _:
            print("Error, opcion invalida debe ser entre (1-5)")

    

  

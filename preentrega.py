# Lista principal para guardar los productos
productos = []

while True:
    print("\n--- Sistema de gestión de productos ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Elegí una opción (1-5): ").strip()
    
    # 1. AGREGAR PRODUCTO
    if opcion == "1":
        print("\n--- Agregar producto ---")
        
        nombre = input("Nombre del producto: ").strip()
        while nombre == "":
            print("Error: El nombre no puede estar vacío.")
            nombre = input("Nombre del producto: ").strip()
            
        categoria = input("Categoría: ").strip()
        while categoria == "":
            print("Error: La categoría no puede estar vacía.")
            categoria = input("Categoría: ").strip()
            
        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("Error: Ingresá solo números positivos.")
            precio_str = input("Precio (sin centavos): ").strip()
            
        precio = int(precio_str)
        
        # Guardamos como sublista dentro de la lista principal
        productos.append([nombre, categoria, precio])
        print("¡Producto agregado con éxito!")

    # 2. MOSTRAR PRODUCTOS
    elif opcion == "2":
        print("\n--- Lista de productos ---")
        
        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"{i + 1}. Nombre: {productos[i][0]} | Categoría: {productos[i][1]} | Precio: ${productos[i][2]}")

    # 3. BUSCAR PRODUCTO
    elif opcion == "3":
        print("\n--- Buscar producto ---")
        
        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            busqueda = input("Nombre del producto a buscar: ").strip().lower()
            
            encontrados = 0
            for i in range(len(productos)):
                if busqueda in productos[i][0].lower():
                    print(f"[{i + 1}] {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")
                    encontrados = encontrados + 1
                    
            if encontrados == 0:
                print("No se encontraron resultados.")

    # 4. ELIMINAR PRODUCTO
    elif opcion == "4":
        print("\n--- Eliminar producto ---")
        
        if len(productos) == 0:
            print("Todavía no hay productos para eliminar.")
        else:
            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i][0]}")
                
            num_str = input("Número de producto a eliminar: ").strip()
            
            if num_str.isdigit():
                posicion = int(num_str) - 1
                if posicion >= 0 and posicion < len(productos):
                    eliminado = productos.pop(posicion)
                    print(f"Se eliminó el producto: {eliminado[0]}")
                else:
                    print("Error: El número de producto no existe.")
            else:
                print("Error: Tenés que ingresar un número válido.")

    # 5. SALIR
    elif opcion == "5":
        print("¡Gracias por usar el sistema!")
        break
        
    else:
        print("Opción no válida. Elegí entre 1 y 5.")
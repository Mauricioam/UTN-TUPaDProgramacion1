def alta_nuevo_producto(inventario):
    print("======= ALTA NUEVO PRODUCTO =======")

    nuevo_nombre = input("Ingresa el nombre del producto: ")
    nuevo_nombre = nuevo_nombre.strip()
#validaciones de entrada de usuario
    if not len(nuevo_nombre):
        raise ValueError("No ingresaste ningún nombre")

    if not nuevo_nombre.isalpha():
        raise ValueError("El nombre no debe contener números. Solo letras.")
# validación para evitar nombre duplicado
    for n in range(len(inventario)):
        if inventario[n]["herramientas"] == nuevo_nombre.lower():
            raise ValueError("El artículo ya esta en el inventario.")
    cantidad_producto = input(f"Ingresa la cantidad para producto {nuevo_nombre}: ")

    if not len(cantidad_producto):
                raise ValueError("No puede estar vacio")

    if not cantidad_producto.isdecimal():
                raise ValueError("Debe ingresar un número")

    if int(cantidad_producto) < 0:
                raise ValueError("El número debe ser mayor o igual que 0")

    cantidad_producto = int(cantidad_producto)
    
    inventario.append({"herramienta": nuevo_nombre.lower(), "cantidad": cantidad_producto})
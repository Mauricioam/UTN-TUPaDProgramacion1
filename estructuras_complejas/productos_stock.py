inventario = {
    "Manteca": 0,
    "Arroz": 3
}

def consultar_producto(dic_inventario):
    # consulta de producto.
    # retorna mensaje de producto con sus unidades.
    # caso no exista, envia mensaje de error
    producto_consultar = input("Ingresar el producto a consultar: ")

    if producto_consultar in dic_inventario:
        return (f"{producto_consultar} : {dic_inventario[producto_consultar]}")
    else:
        return f"Error: no existe {producto_consultar} en inventario"

def agregar_producto(dic_inventario):
    # fn para agregar productos nuevos o mas unidades
    # retorna mensaje de producto/unidades agregadas.

    producto_agregar = input("Ingresa el nombre del producto a ingresar: ")

    if  producto_agregar not in dic_inventario:
        print("Producto nuevo")
        unidades_producto = input(f"Ingresa las unidades de producto {producto_agregar}: ")
        dic_inventario[producto_agregar] = int(unidades_producto)
        return f"Nuevo producto {producto_agregar} : {dic_inventario[producto_agregar]} unidades"
    else:
        print(f"Producto {producto_agregar} : {dic_inventario[producto_agregar]} unidades")
        agregar_unidades = input(f"Ingresa cuantas unidades adicionales para producto {producto_agregar}: ")
        dic_inventario[producto_agregar] += int(agregar_unidades)
        return f"Agregaste {agregar_unidades} unidades al {producto_agregar}: total {dic_inventario[producto_agregar] }"


def menu_inventario(dic_inventario):
    # fn para centralizar menu y opciones de usuario
    # no retorna, sino imprime resultado de funciones accesorias
    print("Inventario consultas / agregar productos")
    print(dic_inventario)
    print("====================")
    print("Ingresa opcion")
    print("1) Consultar producto")
    print("2) Agregar unidades / Agregar producto nuevo")
    seleccion_menu = input()

    match seleccion_menu:
        case "1":
            print(consultar_producto(dic_inventario))
        case "2":
            print(agregar_producto(dic_inventario))
        case _:
            print("Opción inválida")


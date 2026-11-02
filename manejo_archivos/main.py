ARCHIVO = "productos.txt"

import os
# aca primero creo el archivo con modo w. Uso os para verificar que exista el archivo
def crear_archivo_inicial(archivo):
    if os.path.exists(archivo):
        return  # ya existe: 
    with open(archivo, "w", encoding="utf-8") as arc:
        arc.write("Lapicera,120.5,30\n")
        arc.write("Cuaderno,200.0,10\n")
        arc.write("Lápiz,20.0,30\n")


def mostrar_archivo(archivo):
    # funcion que no retorna, solo muestra el producto en un formato
    try:
        with open(archivo,"r",encoding="utf-8") as arc:
            for linea in arc:
                item = linea.strip().split(",")
                print(f"Producto: {item[0]} | Precio: ${item[1]} | Cantidad: {item[2]}")
    except FileNotFoundError:
        print(f"Error: el archivo no se encontró {archivo}")
    except IndexError:
        print("Error: indice incorrecto se espera nombre, precio y cantidad en orden")


def cargar_productos(archivo):
    productos = []
    # función que carga diccionario de productos en una lista iterable con validaciónes.
    # retorna la lista de productos
    try:
        with open(archivo,"r",encoding="utf-8") as arc:
            for linea in arc:
                item = linea.strip().split(",")
                items_dic = {
                    "nombre": item[0],
                    "precio": float(item[1]),
                    "cantidad": int(item[2])
                }
                productos.append(items_dic)
    except FileNotFoundError:
        print(f"Error: el archivo no se encontró {archivo}")
    except IndexError:
        print("Error: indice incorrecto se espera nombre, precio y cantidad en orden")
    except ValueError:
        print("Error: el valor puede ser decimal para precio aunque la cantidad debe ser número entero")
    except Exception as e:
        print(f"Error: ocurrió un error {e}")
    return productos

def agregar_producto(productos):
    print(" ==== Ingresar nuevo producto ====")
    nombre = input("Ingrese nombre: ").strip()
    precio = input("Ingrese precio: ").strip()
    cantidad = input("Ingrese cantidad: ").strip()

    if not nombre:
        print("Error: nombre vacio")
        return
    try:
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })
        print("Producto agregado correctamente")
    except ValueError:
        print("Error: precio debe ser un número y cantidad un número entero")

def buscar_producto(productos):
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            return

    print(f"Error: no se encontró el producto '{nombre_buscado}'.")


def guardar_productos(archivo, lista):
    try:
        with open(archivo, "w", encoding="utf-8") as arc:
            for p in lista:
                arc.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
        print("Productos guardados correctamente")
    except OSError as e:
        print(f"Error al guardar el archivo: {e}")

# aqui el flujo para el programa


crear_archivo_inicial(ARCHIVO)
productos = cargar_productos(ARCHIVO)

mostrar_archivo(ARCHIVO)

agregar_producto(productos)
buscar_producto(productos)
guardar_productos(ARCHIVO, productos)
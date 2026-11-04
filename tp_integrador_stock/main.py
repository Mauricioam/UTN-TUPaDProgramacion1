import cargar_herramientas as fn_cargar_herramientas
def main():
    inventario = []
    # fn_cargar_herramientas(inventario)
    visualizar_inventario(inventario)

def visualizar_inventario(inventario):

    try:
        if(not len(inventario)):
            raise ValueError("No se tiene ningun elemento en la lista.")

        print("===== STOCK ACTUAL =====\n")
        for item in range(len(inventario)):
            nombre_herramienta = inventario[item]["herramienta"]
            cantidad_herramienta = inventario[item]["cantidad"]
            print(f"Herramienta: {nombre_herramienta} = {cantidad_herramienta}\n")

    except ValueError as error:
        print(print(f"Error: {error}\n"))   

main()
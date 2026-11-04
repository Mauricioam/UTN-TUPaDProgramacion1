def visualizar_inventario(inventario):

    try:
        if(not len(inventario)):
            raise ValueError("No se tiene ningun elemento en la lista.")

        print("===== STOCK ACTUAL =====\n")
        for item in range(len(inventario)):
            nombre_herramienta = inventario[item]["herramienta"]
            cantidad_herramienta = inventario[item]["cantidad"]
            print(f"{nombre_herramienta} = {cantidad_herramienta}\n")

    except ValueError as error:
        print(print(f"Error: {error}\n"))   
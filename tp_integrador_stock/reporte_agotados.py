def reporte_agotados(inventario):
    lista_agotados = []
    try:
        if not len(inventario):
            raise ValueError("El inventario esta vacio")

        for itm in range(len(inventario)):
            if inventario[itm]["cantidad"] == 0:
                lista_agotados.append(inventario[itm]["herramienta"])

        if not len(lista_agotados):
            print("Níngun producto esta agotado actualmente.")
            return
        print("===== LISTA DE AGOTADOS ======\n")
        for art in range(len(lista_agotados)):
            print(f"{art + 1} : {lista_agotados[art]}")

    except ValueError as err:
        print(f"Error: {err}")
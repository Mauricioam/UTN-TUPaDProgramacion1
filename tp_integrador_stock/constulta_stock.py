
def consulta_stock(inventario):
    print("==== CONSULTA DE STOCK =====\n")
    if not len(inventario):
        raise ValueError("No se tiene cargada ninguna herramienta.")

    consulta_herramienta = input("Ingresa nombre de herramienta a consultar: ")
    consulta_herramienta = consulta_herramienta.strip()

    if not len(consulta_herramienta):
        raise ValueError("No ingresaste ningún nombre")

    if not consulta_herramienta.isalpha():
        raise ValueError("El nombre no debe contener números. Solo letras.")

    for itm in range(len(inventario)):
        if inventario[itm]["herramienta"].lower() == consulta_herramienta.lower():
            print(f"{inventario[itm]["herramienta"]} = {inventario[itm]["cantidad"]}")
            break
        else:    
            print(f"El artículo {consulta_herramienta} no esta disponible.")
            break

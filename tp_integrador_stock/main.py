import cargar_herramientas as fn_cargar_herramientas
def main():
    inventario = []

    print("==== CONTROL DE STOCK ====\n")
    while True:
        print("1. Cargar inventario inicial")
        print("2. Visualizar inventario")
        print("3. Opcion 3")
        print("4. Opcion 4")
        print("5. Opción 5")
        print("6. Opcion 6")
        print("7. Salir")
        try:
            opcion_usuario = input("Ingrese una opción del menu: ")
            # estructura de selección de opciones 
            match opcion_usuario:
                case "1":
                    fn_cargar_herramientas(inventario)
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "7":
                    pass
                case _:
                    pass
            fn_cargar_herramientas(inventario)
            visualizar_inventario(inventario)
        except ValueError as error:
            print(f"Error: {error}. intente nuevamente \n")

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

stock_prueba = [{'herramienta': 'Martillo', 'cantidad': 3}, {'herramienta': 'Pala', 'cantidad': 2}]

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


    

consulta_stock(stock_prueba)
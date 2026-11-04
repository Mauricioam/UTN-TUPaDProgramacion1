import cargar_herramientas as fn_cargar_herramientas
import visualizar_inventario as fn_visualizar_inventario
import constulta_stock as fn_consulta_stock
def main():
    inventario = []

    print("==== CONTROL DE STOCK ====\n")
    while True:
        print("1. Cargar inventario inicial")
        print("2. Visualizar inventario")
        print("3. Consulta stock")
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
                    fn_visualizar_inventario(inventario)
                case "3":
                    fn_consulta_stock(inventario)
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "7":
                    print("Has elegido salir\n")
                    break
                case _:
                    pass
            
            
        except ValueError as error:
            print(f"Error: {error}. intente nuevamente \n")


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

prueba = []
reporte_agotados(prueba)
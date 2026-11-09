import cargar_herramientas as fn_cargar_herramientas
import visualizar_inventario as fn_visualizar_inventario
import constulta_stock as fn_consulta_stock
import reporte_agotados as fn_reporte_agotados
import alta_nuevo_producto as fn_alta_producto
def main():
    inventario = []

    print("==== CONTROL DE STOCK ====\n")
    while True:
        print("1. Cargar inventario inicial")
        print("2. Visualizar inventario")
        print("3. Consulta stock")
        print("4. Reporte agotados")
        print("5. Alta nuevo producto")
        print("6. Actualización de stock (venta/ingreso)")
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
                    fn_reporte_agotados(inventario)
                case "5":
                    fn_alta_producto(inventario)
                case "6":
                    pass
                case "7":
                    print("Has elegido salir\n")
                    break
                case _:
                    pass
            
            
        except ValueError as error:
            print(f"Error: {error}. intente nuevamente \n")





def venta_ingreso_stock(inventario):
    # debe ingresar reposición de mercaderia
    # debe disminuir stock por venta
    # no retorna nada. Actualiza lista de argumento inventario

    #verificamos si inventario tiene algo
    try:
        if(not len(inventario)):
            raise ValueError("No se tiene ningun elemento en la lista.")

        print("===== VENTA/INGRESO DE STOCK =====")        

        nombre_ingresado = input("Ingresa nombre de la herramienta: ")

        if not len(nombre_ingresado):
            raise ValueError("No has ingresado ninún nombre")

        if not nombre_ingresado.isalpha():
            raise("Solo se puede ingresar nombres con letras.")

        # vamos a colocar en lower y sacar espacios con strip() ya que todo ingreso esta realizado asi.
        nombre_ingresado = nombre_ingresado.strip().lower()

        

    except ValueError as err:
        print(f"Error: {err}")




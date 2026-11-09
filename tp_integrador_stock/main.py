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
            print(f"Error: {error}. Intente nuevamente \n")





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

        # buscamos la herramienta solo si la encuentra avanzamos.
        for itm in range(len(inventario)):
            if not nombre_ingresado == inventario[itm]["herramienta"]:
                raise ValueError("La herramienta ingresada no existe")
            else:
                pos_producto = itm
                break
        # aqui empezaremos el menu de operaciones
        print("==== INGRESE TIPO DE OPERACIÓN ====")
        print("1: VENTA")
        print("2: INGRESO\n")
        # todas las opciones se validan
        opcion_usuario = input("Ingrese su selección: ")

        if not len(opcion_usuario):
            raise ValueError("No ingresó ninguna opción")

        opcion_usuario = int(opcion_usuario)

        if not opcion_usuario == 1 or opcion_usuario == 2:
            raise ValueError("Opción inválida.")

        match opcion_usuario:
            case 1:
                if not inventario[pos_producto]["cantidad"] > 0:
                    raise ValueError("No hay stock suficiente")

                unidades_vendidas = input("Ingrese cantidad de venta: ")

                if not len(unidades_vendidas):
                    raise ValueError("No ingresó ningún numero")

                unidades_vendidas = int(unidades_vendidas)

                if unidades_vendidas == 0:
                    raise ValueError("Las unidades vendidas no puede ser 0 o negativos.")

                inventario[pos_producto]["cantidad"] -= unidades_vendidas

                print(f"Registrado venta de {inventario[pos_producto]["herramienta"]} cantidad: {unidades_vendidas}. Stock: {inventario[pos_producto]["cantidad"]}")



        

        



    except ValueError as err:
        print(f"Error: {err}")



test_invent = [{'herramienta': 'martillo', 'cantidad': 10}, {'herramienta': 'pala', 'cantidad': 3}]

venta_ingreso_stock(test_invent)
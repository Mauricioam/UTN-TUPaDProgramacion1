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


def alta_nuevo_producto(inventario):
    print("======= ALTA NUEVO PRODUCTO =======")

    nuevo_nombre = input("Ingresa el nombre del producto: ")
    nuevo_nombre = nuevo_nombre.strip()
#validaciones de entrada de usuario
    if not len(nuevo_nombre):
        raise ValueError("No ingresaste ningún nombre")

    if not nuevo_nombre.isalpha():
        raise ValueError("El nombre no debe contener números. Solo letras.")
# validación para evitar nombre duplicado
    for n in range(len(inventario)):
        if inventario[n]["herramientas"] == nuevo_nombre.lower():
            raise ValueError("El artículo ya esta en el inventario.")
    cantidad_producto = input(f"Ingresa la cantidad para producto {nuevo_nombre}: ")

    if not len(cantidad_producto):
                raise ValueError("No puede estar vacio")

    if not cantidad_producto.isdecimal():
                raise ValueError("Debe ingresar un número")

    if int(cantidad_producto) < 0:
                raise ValueError("El número debe ser mayor o igual que 0")

    cantidad_producto = int(cantidad_producto)
    
    inventario.append({"herramienta": nuevo_nombre, "cantidad": cantidad_producto})

    
        




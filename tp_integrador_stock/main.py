def main():
    inventario = []
    cargar_herramientas(inventario)
    print(inventario)

def cargar_herramientas(inventario):
    print("==== CARGA DE STOCK INICIAL ====")
    print("="*24)
    # bloque de validación de la carga inicial de las herramientas a cargar.
    # cada validación tiene un raise para capturar error.
    while True:
        carga_inicial = input("Ingrese la cantidad de herramientas distintas a cargar: (número entero):  ")
        # se evalua:
        # string vacio
        # validar tipo de dato que necesitamos
        # validación extra: (mayor q 0)
        try:
            if not len(carga_inicial):
                raise ValueError("No puede estar vacio")

            if not carga_inicial.isdecimal():
                raise ValueError("Debe ingresar un número")

            if int(carga_inicial) <= 0:
                raise ValueError("El número debe ser mayor o igual que 0")

            carga_inicial = int(carga_inicial)
            
            break
        
        except ValueError as error:
            print(f"Error: {error}. Intenta nuevamente \n")
            
    
    for n in range(carga_inicial):
        while True:
            try:
                nombre = input(f"Ingrese nombre de la herramienta {n+1}: ")

                if not len(nombre):
                    raise ValueError("Debe ingresar un nombre válido")

                nombre = nombre.strip()

                if not nombre.isalpha():
                    raise ValueError("El nombre debe contener solo letras sin números")

                # validar si nombre existe. Sacar afuera a una función
                nombre = nombre.lower()
                if len(inventario) > 0:
                    for itm in range(len(inventario)):
                    
                        if inventario[itm]["herramienta"] == nombre:
                            raise ValueError("El nombre igresado esta duplicado")

                break

            except ValueError as error:
                print(f"Error: {error} Intenta nuevamente \n")

        while True:
            try:
                cargar_cantidad = input(f"Ingrese la cantidad para {nombre}: ")

                if not len(cargar_cantidad):
                    raise ValueError("Debe ingresar número.")

                if not cargar_cantidad.isdecimal():
                    raise ValueError("Debe ingresar un número decimal entero positivo")

                cargar_cantidad = int(cargar_cantidad)


                break

            except ValueError as error:
                print(f"Error: {error} Intenta nuevamente \n")
        # si no se ha capturado ningun error, se agrega la herramienta.
        inventario.append({"herramienta": nombre, "cantidad": cargar_cantidad})
    

main()
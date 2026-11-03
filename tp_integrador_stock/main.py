def main():
    inventario = []
    pass

def cargar_herramientas(inventario):
    print("==== CARGA DE STOCK INICIAL ====")
    print("="*24)
    carga_inicial = input("Ingrese la cantidad de herramientas distintas a cargar: (número entero)")
    while True:
        try:
            if not len(carga_inicial):
                raise ValueError("Debe ingresar un número")


            if carga_inicial <= 0:
                raise ValueError("El número debe ser mayor o igual que 0")

            carga_inicial = int(carga_inicial)
            break
        except ValueError as error:
            print(f"Error: {error}. Intenta nuevamente \n")
    
    for n in range(carga_inicial):
        while True:
            try:
                nombre = input("Ingrese nombre de la herramienta: ")

                if not len(nombre):
                    raise ValueError("Debe ingresar un nombre válido")

                nombre = nombre.strip()

                if not nombre.isalpha():
                    raise ValueError("El nombre debe contener solo letras sin números")
                
                break

            except ValueError as error:
                print(f"Error: {error} Intenta nuevamente \n")
        
    



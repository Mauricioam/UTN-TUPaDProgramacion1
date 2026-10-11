
def cargar_agenda():
    # fn para cargar agenda.
    # retorna dicc de nombres y números
    nombre_tel = {}
    for n in range(5):
        # no tiene validación. Se asume camino feliz. Sino deberiamos validar el ingreso
        print(f"Carga de datos. Nombre y tel. Contacto {n + 1}")
        nombre = input("Ingresa el nombre: ")
        tel = input("Ingresa el número de teléfono: ")
        nombre_tel[nombre] = tel
    return nombre_tel

def buscar_nombre(agenda):
    # busca el nombre
    # tiene un argumento agenda que es un diccionario
    nombre_a_buscar = input("Ingresa el nombre a buscar: ")
    if agenda.get(nombre_a_buscar):
        return agenda[nombre_a_buscar]
    else:
        return "Error: el nombre a buscar no existe."

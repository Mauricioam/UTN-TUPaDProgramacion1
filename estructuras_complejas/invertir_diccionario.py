

def invertir_diccionario(diccionario):
    # recibe un diccionario clave y valor.
    # retorna un nuevo diccionario invirtiendo valores
    resultado_invertido = {}

    for pais,capital in diccionario.items():
        resultado_invertido[capital] = pais

    return resultado_invertido




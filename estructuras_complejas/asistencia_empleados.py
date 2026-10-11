
def contar_asistencia(lista_text):
    recuento_palabras = {}
    for n in range(len(lista_text)):
        if recuento_palabras.get(lista_text[n]):
            recuento_palabras[lista_text[n]] += 1
        else:
            recuento_palabras[lista_text[n]] = 1
    return recuento_palabras




def palabras_unicas(frase):
    txt_minuscula = lista_texto_minusculas(frase)
    return set(txt_minuscula)

def lista_texto_minusculas(oracion):
    oracion = oracion.split(" ")
    list_frase = []
    for word in range(len(oracion)):
        list_frase.append(oracion[word].lower())
    return list_frase

def contar_palabras(texto):
    recuento_palabras = {}
    lista_txt_minus = lista_texto_minusculas(texto)
    for n in range(len(lista_txt_minus)):
        if recuento_palabras.get(lista_txt_minus[n]):
            recuento_palabras[lista_txt_minus[n]] += 1
        else:
            recuento_palabras[lista_txt_minus[n]] = 1
    return recuento_palabras


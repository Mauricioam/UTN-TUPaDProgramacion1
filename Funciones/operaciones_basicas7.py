

def operaciones_basicas(a,b):
    #operaciones básicas con validación de división por 0
        
    sumar = a + b
    restar = round(a - b,2)
    multiplicar = a * b

    if b == 0:
        dividir = ("No se puede dividir por 0")
    else:
        dividir = round(a / b,2)
    resultados = ("Suma:",sumar,"Resta:",restar,"Multiplicación:",multiplicar,"División:",dividir)
    return resultados


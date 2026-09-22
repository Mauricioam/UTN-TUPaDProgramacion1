import aux_funcion as auxfn

def operaciones_basicas(a,b):
    #operaciones básicas con validación de división por 0
    if  (not type(a) == int or not type(a) == float) and (not type(b) == int or not type(b) == float):
        print("Error: no ingresaste un valor númerico")
        return
        
    sumar = a + b
    restar = round(a - b,2)
    multiplicar = a * b

    if b == 0:
        dividir = ("No se puede dividir por 0")
    else:
        dividir = round(a / b,2)
    resultados = ("Suma:",sumar,"Resta:",restar,"Multiplicación:",multiplicar,"División:",dividir)
    # mostrar resultados en for 1 por linea
    print(f"Números ingresados {a} y {b}")
    for n  in range(0,len(resultados),1):
        print(resultados[n])



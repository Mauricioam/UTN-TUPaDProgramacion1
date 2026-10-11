def ingresar_alumno_nota():
    alumnos = {}
    for n in range(3):
        nombre_alumno = input(f"Ingresar nombre de alumno {n+1}: ")
        alumnos[nombre_alumno] = None
        notas = []
        for i in range(3):
            nota_alumno = input(f" Ingresar nota {i+1} para alumno {nombre_alumno}: ")
            notas.append(int(nota_alumno))
        alumnos[nombre_alumno] = tuple(notas)
    return alumnos


def promedio_alumnos(alumnos):
    result = {}
    for clave,valor in alumnos.items():
        result[clave] = None
        suma_notas = 0
        for n in range(len(valor)):
            suma_notas += valor[n]
        result[clave] = round(suma_notas/len(valor),2)

    return result        


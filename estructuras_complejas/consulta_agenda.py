agenda = {
    ("lunes","8:00"): "Entregar trabajo",
    ("martes", "10:00") : "Ir al dentista" 
}

def consulta_agenda(agenda):
    # funcion de consulta
    # retorna la actividad con fecha y hora
    # estructura a recibir:
    # ("dia","hora"): "actividad"
    dia = input("Ingresa el dia que quieres consultar: (ejemplo lunes):  ")
    hora = input("Ingresa la hora a consultar: (Ejemplo 10:00):  ")

    if (dia,hora) in agenda:
        return f"Para el dia {dia} hora {hora} esta la actividad {agenda[(dia,hora)]}"
    
    return f"No se encontró actividad en {dia} y hora {hora}"

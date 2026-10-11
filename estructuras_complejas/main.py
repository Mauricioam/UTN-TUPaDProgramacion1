import nombre_tel as fntel
import frase_usuario as fn_frase_usuario
import alumnos_tupla as fn_alumnos_tupla
import asistencia_empleados as fn_asistencia_empleados
import productos_stock as fn_productos_stock
import consulta_agenda as fn_consulta_agenda
import invertir_diccionario as fn_invertir_diccionario

### 1) Diccionario de frutas.
## añadir  frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

### 2) Actualizar los precios
print("----------------------")

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

### 3 ) crear lista con los keys-

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

### 4 ) Programa para almacenay y consultar numeros tel


nombres = fntel.cargar_agenda()

resultado_nombre = fntel.buscar_nombre(nombres)

print(resultado_nombre)

## 5 Frase del usuario. Imprimir palabras unicas y contar cantidad de cada palabra

texto_usuario = input("Ingresa la frase: ")

frases_unicas = fn_frase_usuario.palabras_unicas(texto_usuario)
print(f"Palabras únicas: {frases_unicas}")

contar_palabras = fn_frase_usuario.contar_palabras(texto_usuario)
print(f"Recuento: {contar_palabras}")

## 6 ) Ingresar nombre de 3 alumnos y para cada uno una tupla de 3 notas. Mostrar promedio de cada alumno

alumnos = fn_alumnos_tupla.ingresar_alumno_nota()
print(f"Los alumnos ingresados {alumnos}")
promedio_alumnos = fn_alumnos_tupla.promedio_alumnos(alumnos)

print(f"El promedio de cada alumno: {promedio_alumnos}")

## 7) Lista original de asistencias. Hacer un set y mostrar empleados que asistieron al menos una vez

asistencias = ["Mauri", "Martin","Mauri","Luis","Ana","Martin","Ana", "Luis"]
print(f"La lista original: {asistencias}")
# crear set y mostrar nombres
asistencias_set = set(asistencias)

print(f"Lista sin repetir nombres {asistencias_set}")

numero_asistencia = fn_asistencia_empleados.contar_asistencia(asistencias)

print(f"Veces que asistieron cada empleado {numero_asistencia}")

## 8) Programa stock inventario. Consulta, agregar unidades y agregar nuevo producto

inventario = {
    "Manteca": 2,
    "Arroz": 3
}

fn_productos_stock.menu_inventario(inventario)

## 9 ) Crear agenda donde claves sean tuplas ( dia, hora ) y valores eventos. Permiti consultar 

agenda = {
    ("lunes","8:00"): "Entregar trabajo",
    ("martes", "10:00") : "Ir al dentista" 
}

consulta = fn_consulta_agenda.consulta_agenda(agenda)

print(consulta)

## 10) Contruir diccionario nuevo invirtiendo el original

original_paises = {
    "Uruguay" : "Montevideo",
    "Paraguay" : "Asunción",
    "Brasil" : "Brasilia",
    "Argentina" : "Buenos Aires"
}

print(fn_invertir_diccionario.invertir_diccionario(original_paises))
import hola_mundo as fn
import saludar_usuario as fn
import aux_funcion as auxfun
import info_personal as fn
# Ejercicio 1: imprimir hola mundoS

fn.imprimir_hola_mundo()

#Ejercicio 2: Saludo personalizado del usuario

fn.saludar_usuario("Mauricio")

# Ejercicio 3: información personal. Se pide datos al usuario y muestra en pantalla

nombre,apellido,residencia,edad = auxfun.pedir_datos()

fn.informacion_personal(nombre,apellido,residencia,edad)
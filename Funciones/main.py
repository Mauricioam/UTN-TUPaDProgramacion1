import hola_mundo_1 as fn1
import saludar_usuario_2 as fn2
import aux_funcion as auxfun
import info_personal_3 as fn3
import area_circulo_4 as fn4
import segundos_horas5 as fn5
import tabla_multiplicar6 as fn6
# Ejercicio 1: imprimir hola mundoS

fn1.imprimir_hola_mundo()

#Ejercicio 2: Saludo personalizado del usuario

fn2.saludar_usuario("Mauricio")

# Ejercicio 3: información personal. Se pide datos al usuario y muestra en pantalla

nombre,apellido,residencia,edad = auxfun.pedir_datos()

fn3.informacion_personal(nombre,apellido,residencia,edad)

#Ejercicio 4: area y perimetro de un circulo con el ingreso del usuario.
radio = fn4.request_radio()

fn4.calcular_perimetro_circulo(radio)

fn4.calcular_area_circulo(radio)

#Ejercicio 5: segundos a horas

segundos = fn5.user_input_seconds()

fn5.segundos_a_horas(segundos)

# Ejercicio 6: tabla de multiplicar. El usuario lo debe ingresar

num_multiplicar = fn6.num_input()

fn6.tabla_multiplicar(num_multiplicar)


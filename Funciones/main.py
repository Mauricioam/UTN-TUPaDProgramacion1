import hola_mundo_1 as fn1
import saludar_usuario_2 as fn2
import info_personal_3 as fn3
import area_circulo_4 as fn4
import segundos_horas5 as fn5
import tabla_multiplicar6 as fn6
import operaciones_basicas7 as fn7
import calcular_imc8 as fn8
import celcius_farenheit as fn9
import calcular_promedio as fn10


# Ejercicio 1: imprimir hola mundo
fn1.imprimir_hola_mundo()

#Ejercicio 2: Saludo personalizado del usuario
user_name = input("Ingrese su nombre: ")
print(fn2.saludar_usuario(user_name))

# Ejercicio 3: información personal. Se pide datos al usuario y muestra en pantalla
user_name_2 = input("Ingresa tu nombre: ")
user_lastname = input("Ingresa tu appellido: ")
user_age = input("Ingresa tu edad: ")
user_residence_city = input("Ingresa la ciudad donde vives: ")

print(fn3.informacion_personal(user_name_2,user_lastname,user_residence_city,user_age))

#Ejercicio 4: area y perimetro de un circulo con el ingreso del usuario.

num_radio = float(input("Ingresa el radio para calculo de área y perimetro: "))

print(f"El perímetro es igual a  {fn4.calcular_perimetro_circulo(num_radio)} y el área del circulo {fn4.calcular_area_circulo(num_radio)}")



#Ejercicio 5: segundos a horas


user_seconds = int(input("Ingresa la cantidad de segundos a convertir a horas: "))

print(f"La cantidad de segundos corresponde a {fn5.segundos_a_horas(user_seconds)} horas")



# Ejercicio 6: tabla de multiplicar. El usuario lo debe ingresar
multiply_num = int(input("Ingresa un número para ver su tabla de multiplicación: "))

print(fn6.tabla_multiplicar(multiply_num))

# Ejercicio 7: operaciones básicas sin ingreso de usuario
num_1 = int(input("Ingrese el número 1: "))
num_2 = int(input("Ingrese el número 2: "))
result = fn7.operaciones_basicas(num_1,num_2)
# mostrar resultados en forma clara
for n in range(len(result)):
    print(result[n])


# Ejercicio 8: calculadora de imc con función que solicita datos al usuario
user_height = float(input("Ingresa tu altura en metros: "))
user_weigth = float(input("Ingresa tu altura en kilogramos: "))

print(fn8.calcular_imc(user_weigth,user_height))


# Ejercicio 9: Convertidor de celcius a fahrenheit pidiendo el dato al usuario:
user_celcius_temp = float(input("Ingrese el valor de en grados Celcius: "))
print(f"La tempertura es {fn9.celcius_fahrenheit(user_celcius_temp)} F°")

# Ejercicio 10: promedio de 3 números
user_num_1 = int(input("Ingresa la nota 1: "))
user_num_2 = int(input("Ingresa la nota 2: "))
user_num_3 = int(input("Ingresa la nota 3: "))


print(f"El promedio de los números es {fn10.calcular_promedio(user_num_1,user_num_2,user_num_3)}")

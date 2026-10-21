# Ejercicio 1
#a = 10

#b = input("Introduce un número: ")

#result = a / b
# b = string TypeError no permite división


#numbers = [1,2,3]

#print(numbers[5])

# IndexError: no se tiene index de 5. Solo hasta 2

#=========================================

# Ejercicio 2: arreglar ejercicio 1 sin usar try-except

a = 10

b = input("Introduce un número: ")

result = a / float(b)

print(f"Resultado {result}")

numbers = [1,2,3]

print(numbers[0])


#=========================================

# Ejercicio 3,4 y 5: 

a = 10

b = input("Introduce un número: ")

try:
    result = a / b
    print(f"Resultado {result}")
    
    numbers = [1,2,3]

    print(numbers[5])
except TypeError as e_type: # error causado por división con string
    print(f"Se debe ingresar un valor de tipo número: {e_type}")
except IndexError as e_index: # error causado por fuera de indice
    print(f"Se ha ingresado un indice fuera de rango: {e_index}")
except:
    print("Se ha encontrado un error")
else:
    print("Entra cuando se ejecuta try")
finally:
    print("Se ejecuta siempre")
#

#=========================================
print("\n")

# Ejercicio 6: que un usuario ingrese un número



try:
    ingreso_user = int(input("Ingrese un número: "))
    print(f"Número ingresado: {float(ingreso_user)}")
except ValueError as e_value:
    print(f"El ingreso no es un número: {e_value}")

except:
    print("Se produjo un error inesperado")

print("\n")

#=========================================

# Ejercicio 7: que un usuario ingrese un número


while True:
    try:
        ingreso_user = int(input("Ingrese un número: "))
        print(f"Número ingresado: {ingreso_user}")
        break
    except ValueError as e_value:
        print(f"El ingreso no es un número: {e_value}")

    except Exception as e_exception:
        print(f"Se produjo un error inesperado: {e_exception}")







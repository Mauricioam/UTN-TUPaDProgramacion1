import aux_funcion as auxfun

def request_radio():

    # función para tomar el dato del radio con validaciones.
    # retorna el valor del radio en tipo float
    valid_data = False
    while not valid_data:
        print("Ingresa el radio del círculo: ")
        user_radio = input()
        if auxfun.check_num_data(user_radio):
            valid_data = True
            user_radio = float(user_radio)
        else:
            print("Error: Ingrese un número valido positivo.")
    return user_radio

radio = request_radio()

def calcular_area_circulo(radio):
    print(f"El área del circulo es: {(3.14 * radio):.2f}") 

def calcular_perimetro_circulo(radio):
    print(f"El perímetro del circulo es: {(2 * 3.14 * radio):.2f}") 

# P = 2 * PI * R
# A = PI * R
import aux_funcion as auxfun

def request_radio():
    print("Ingresa el radio del círculo: ")
    user_radio = input()
    # aca falta validar el dato de q sea un float
    valid_data = False
    while not valid_data:
        if auxfun.check_num_data(user_radio):
            valid_data = True
        else:
            print("Error: Ingrese un número valido positivo.")
    return user_radio

radio = request_radio()

def calcular_area_circulo(radio):
    return 2 * 3.14 * radio
# P = 2 * PI * R
# A = PI * R

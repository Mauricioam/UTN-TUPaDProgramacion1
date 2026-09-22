import aux_funcion as auxfn
def imc_input():
    # funcion para tomar datos de usuario
    # tiene validaciones 
    # retorna
    valid_data = False
    while not valid_data:
        print("Ingresa tu peso en kilogramos")
        user_weight = input()
        if auxfn.check_text_num_data(user_weight) and float(user_weight) > 0:
            print(f"Has ingresado:{user_weight} kg.")
            valid_data = True
            user_weight = float(user_weight)
        else:
            print("Error: el valor ingresado no es numérico o menor que 0")
    valid_data = False
    while not valid_data:
        print("Ingresa tu altura en metros")
        user_height = input()
        if auxfn.check_text_num_data(user_height) and float(user_height) > 0:
            print(f"Has ingresado {user_height} metros")
            valid_data = True
            user_height = float(user_height)
        else:
            print("Error: el valor ingresado no es numérico o menor que 0")
    return user_weight,user_height

def calcular_imc(weigth,height):
    result = weigth / (height*height)
    print(f"El IMC es igual a {result:.2f}")

import aux_funcion as auxfn

def user_input_seconds():
    #función para solicitar segundos
    # retorna un int.
    valid_data = False
    while not valid_data:
        print("Ingresa los segundos en números positivos")
        user_input = input()
        if auxfn.check_num_data(user_input) and not user_input.count("."):
            valid_data = True
            user_input = int(user_input)
        else:
            print("Error: el número ingresado no es válido. Debe ser positivo sin comas.")
    return user_input



def segundos_a_horas(seconds):
    # toma los segundos y los pasa a las horas que corresponde.
    # no retorna nada, solo muestra el dato
    num = seconds/3600
    print(f"Los {seconds} segundos, corresponden a {num:.2f} hora/s")

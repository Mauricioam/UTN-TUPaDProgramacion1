import aux_funcion as auxfn
def num_input():
    # función para solicitar al usuario y validar su entrada.
    # no acepta num negativos.
    valid_data = False
    while not valid_data:
        print("Ingresa un número positivo")
        user_num_input = input()
        if auxfn.check_num_data(user_num_input):
            valid_data = True
            user_num_input = int(user_num_input)
        else:
            print("Error: el número no es correcto")
    return user_num_input

def tabla_multiplicar(num):
    print("=== Tabla multiplicar ===")
    for n in range(1,11):
        print(f"{n} x {num} = {n*num}")




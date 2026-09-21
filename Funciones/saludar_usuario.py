import aux_funcion as auxfn

def saludar_usuario(user):
    auxfn.check_data(user)
    print(f"Hola {user}!!")
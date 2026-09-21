import aux_funcion as auxfun

def pedir_datos():
    
    valid_data = False
    while(not valid_data):
        print("Ingrese su nombre:")
        user_name  = input()
        
        if(auxfun.check_data(user_name)):
            valid_data = True
    valid_data = False
    while(not valid_data):
        print("Ingresa tu apellido")
        user_lastname = input()
        if(auxfun.check_data(user_lastname)):
            valid_data = True

    valid_data = False
    while( not valid_data):
        print("Ingresa tu lugar de residencia")
        user_residence = input()

        if(auxfun.check_data(user_residence)):
            valid_data = True

    valid_data = False
    while(not valid_data):
        print("Cuantos años tienes ")
        user_age = input()
        if(auxfun.check_num_data(user_age)):
            valid_data = True

    return user_name,user_lastname,user_residence,user_age

nombre,apellido,residencia,edad = pedir_datos()

def informacion_personal(user_name,user_lastname,user_residence, user_age):

    
    print(f"Hola soy {user_name} {user_lastname}, tengo {user_age} años y vivo en {user_residence}")
    

informacion_personal(nombre,apellido,residencia,edad)


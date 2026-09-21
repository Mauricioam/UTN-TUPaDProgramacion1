def check_data(text_input):
    # función para corroborar input correcto del usuario.
        if(len(text_input) and text_input.isalpha()):
            return True
        else:
            print("Error: El dato ingresado no es correcto")

def check_num_data(num_input):
        #funcion para corroborar entradas númericas
        if(len(num_input) and num_input.isdigit()):
            return True
        else:
            print("Error: El dato ingresado no es correcto")

def pedir_datos():
    
    valid_data = False
    while(not valid_data):
        print("Ingrese su nombre:")
        user_name  = input()
        
        if(check_data(user_name)):
            valid_data = True
    valid_data = False
    while(not valid_data):
        print("Ingresa tu apellido")
        user_lastname = input()
        if(check_data(user_lastname)):
            valid_data = True

    valid_data = False
    while( not valid_data):
        print("Ingresa tu lugar de residencia")
        user_residence = input()

        if(check_data(user_residence)):
            valid_data = True

    valid_data = False
    while(not valid_data):
        print("Cuantos años tienes ")
        user_age = input()
        if(check_num_data(user_age)):
            valid_data = True

    return user_name,user_lastname,user_residence,user_age
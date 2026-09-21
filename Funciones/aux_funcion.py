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
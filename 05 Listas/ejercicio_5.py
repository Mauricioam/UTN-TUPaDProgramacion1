student_list = ["Matute","Cucho","Benito","Panza","Demóstenes","Arabella","Jazz","Tom"]
for num in range(len(student_list)):
    print(f"{num + 1} : {student_list[num]}")

valid_option = False

while not valid_option:
    print("1) Agregar nombre 2) Remover nombre")
    user_option = input()
    if(len(user_option) and user_option.isdecimal()):
        user_option = int(user_option)
        if user_option > 0 and user_option < 3:
            valid_option = True

            match user_option:
                case 1:
                    valid_name = False
                    while not valid_name:
                        print("Ingrese nuevo nombre:")
                        add_new_name = input()
                        if(len(add_new_name) and add_new_name.isalpha()):
                            valid_name = True
                            student_list.append(add_new_name)
                        else:
                            print("Error: No ingresaste nombre válido.")
                
                case 2:
                    # ya no hice validaciones aca para avanzar mas rápido. Asumo camino feliz
                    print("Que nombre quiere borrar:")
                    for n in range(len(student_list)):
                        print(f"{n + 1}: {student_list[n]}")
                    user_num_option = input()
                    user_num_option = int(user_num_option) - 1
                    print(f"Borrado {student_list[user_num_option]}")
                    student_list.pop(user_num_option)
    

                case _:
                    print("Error")
        else:
            print("Error: Fuera de rango. Opciones 1 o 2")
    else:
        print("Error: No ingresaste nada o ingresaste letras. Solo números")

print("La lista actualizada:\n")

for num in range(len(student_list)):
    print(f"{num + 1} : {student_list[num]}")
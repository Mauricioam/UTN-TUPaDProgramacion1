## 1 ) Lista de 10 estudiantes
student_grades = [5,10,8,2,1,9,6,3,4,7]
total = 0
for num in student_grades:
    total += num
print(f"El promedio es {total/len(student_grades)}")
print(f"El max es {max(student_grades)} el min {min(student_grades)}")

#2 5 productos mas eliminar uno

product_list = []



for item in range(1,6):
    valid_input = False
    while not valid_input:
        print(f"Ingrese producto {item} de 5")
        user_input = input()
        if(len(user_input) and user_input.isalpha()):
            valid_input = True
            product_list.append(user_input.lower())
        else:
            print("Error: No ingresó valor / ingreso valor erróneo. Solo ingrese letras")

print("La lista ingresada es:\n")
product_list.sort()

valid_num = False
while not valid_num:
    for i in range(len(product_list)):
        product_list[i] = product_list[i].capitalize()
        print(f"Producto {i+1}: {product_list[i]}")

    print("Que producto desea eliminar: Ingrese 1 al 5")
    user_num_delet = input()

    if(len(user_num_delet) and user_num_delet.isdecimal()):
        
        user_num_delet = int(user_num_delet)
        if(user_num_delet > 0 and user_num_delet < 6):
            valid_num = True
            user_num_delet = user_num_delet - 1
            print(f"Se ha borrado el item {product_list[user_num_delet]}")
            product_list.pop(user_num_delet)
        else:
            print("Error: Ingrese número del 1 al 5")
    else:
        print("Error: No ingresó valor / ingreso valor erróneo. Solo ingrese números")   

print("La lista actualizada\n")
for i in range(len(product_list)):
    product_list[i] = product_list[i].capitalize()
    print(f"Producto {i+1}: {product_list[i]}")
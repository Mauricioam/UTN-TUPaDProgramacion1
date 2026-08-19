## Caja del kiosco - 1
valid_name = False
while not valid_name:
    buyer_name = input(" Ingresa tu nombre para comprar: ")
# Valido que no este vacio ni tampoco ingrese números
    if len(buyer_name) and buyer_name.isalpha():

        valid_name = True
        valid_products = False

    else:
        print("Debe ingresar un nombre válido para continuar  ")

while not valid_products:
# Valido que no este vacio ni tampoco ingrese números
            product_amount = input("Ingrese la cantidad de productos: ")

            #valido q no este vacio y sea un numero enterp
            
            if(len(product_amount) and product_amount.isdigit()):

                valid_products = True
                product_amount = int(product_amount)

            else:
                print("No ingresó productos o ingresó un valor erróneo. Ingrese cantidad de productos en números enteros.")


    # declaro valores iniciales en 0
price_w_discount = 0
total_no_discounts = 0
total_w_discount = 0

#itereación por cada producto
for item in range(1,product_amount+1):
    valid_price = False
    #validación de precio
    while not valid_price:
        product_price = input(f"Ingrese el precio del producto {item}: ")

        if(len(product_price) and product_price.isdigit()):
            valid_price = True
        else:
            print("Valor vacio o incorrecto. Ingrese números enteros")
    product_price = int(product_price)
    
    #validación del descuento
    valid_discount = False
    while not valid_discount:
        has_discount = input("Ingrese si este producto tiene descuento: S/N ")
        if(len(has_discount) and len(has_discount) < 2 and has_discount.isalpha()):
            has_discount = has_discount.lower()
            #tenemos q validar solo las dos letras s o n
            if(has_discount == "s" or has_discount == "n"):
                valid_discount = True
            else:
                print("Solo se permite s o n")
        else:
            print("Ingrese valor válido.")

    total_no_discounts += product_price
    if(has_discount == "s"):
        product_price = product_price * 0.9
    total_w_discount += product_price

    print("\n")
    print(f"Cliente: {buyer_name}")
    print(f"Cantidad de productos: {product_amount}")
    print("\n")
    print(f"Producto {item} - Precio: {product_price} Descuento (S/N): {has_discount}")
    print(f"Total sin descuento: {total_no_discounts:.2f}")
    print(f"Total con descuento: {total_w_discount:.2f}")
    print(f"Ahorro: {total_no_discounts - total_w_discount:.2f}")
    print(f"Promedio por producto: {total_w_discount/product_amount:.2f}")

########################################################
## Ejercicio 2 Acceso Campus

### acceso al campus y menu
user_correct = "alumno"
pass_correct = "python123"
max_try = 3

valid_access = False

while max_try > 0 :

    print(f"Tenes {max_try} intento/s")
    print("Ingrese su usuario")
    user_input = input()
    print("Ingrese su contraseña")
    user_pass = input()
    
    if( user_input == user_correct and user_pass == pass_correct):
        valid_access = True
        break
    else:
        print("Usuario y/o clave incorrecta")
    max_try = max_try - 1

if(valid_access):
    end_session = False
    while not end_session:
        print("=== BIENVENIDO AL CAMPUS ===")
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) salir")
        user_option = input()
        if(len(user_option) and user_option.isdigit()):
            user_option = int(user_option)
            match user_option:
                case 1:
                    print("Estado: Inscripto")
                case 2:

                    change_pass_succesful = False
                    while not change_pass_succesful:
                        print("Ingrese su nueva clave. Minimo 6 caracteres")
                        user_new_pass = input()
                        if(len(user_new_pass) >= 6):
                            print("Ingrese nuevamente su clave")
                            user_pass_confirmation = input()
                            if(user_new_pass == user_pass_confirmation):
                                print("Cambiaste tu clave con éxito")
                                change_pass_succesful = True
                            else:
                                print("No coinciden las claves.")
                        else:
                            print("La clave debe tener al menos 6 caracteres")
                case 3:
                    print("Aca va frase motivacional")
                case 4:
                    print("Seleccionado Salir \n"
                    "Gracias")
                    end_session = True
                case _:
                    print("opción fuera de rango")
        else:
            print("Error: Ingrese un número válido")


else:
    print("Cuenta bloqueada denegado")
##Ejercicio 3


#Agenda turnos

monday = 4 
tuesday = 3

valid_operator_name = False

while not valid_operator_name:
    print("Ingrese nombre del operador")
    operator_input_name = input()
    if(len(operator_input_name) and operator_input_name.isalpha()):
        valid_operator_name = True

    else:
        print("Error: Vacio o ingresó números/símbolos. Ingrese el nombre solo letras.")

valid_option_menu = False

#catalogo de lugares libres por dia
monday_1 = ""
monday_2 = ""
monday_3 = ""
monday_4 = ""

tuesday_1 = ""
tuesday_2 = ""
tuesday_3 = ""


end_session = False
while not end_session:
    valid_option_menu = False

    while not valid_option_menu:
        print("\n")
        print("==== AGENDAMIENTO DE TURNOS ====")
        print("\n")
        print(f"Operador: {operator_input_name}")
        print("Ingrese opción del menu:")
        print("1) Resevar turno 2) Cancelar turno 3) Ver agenda del dia 4) Ver resumen general 5) Cerrar sistema")
        operator_option = input()
        if(len(operator_option) and operator_option.isdigit()):
            operator_option = int(operator_option)
            if(operator_option > 0 and operator_option < 6):
                valid_option_menu = True
            else:
                print("Error: fuera de rango. Ingrese numero del 1 al 5")
        else:
            print("Error: Vacio o ingresó letras. Solo ingrese números del 1 al 5")
    # casos para cada opción de menu
    match operator_option:
        #RESERVAR TURNO
        case 1:
            print("RESERVAR TURNO")
            valid_day = False
            #verificar opción de días válidos
            while not valid_day:
                print("1: Lunes 2: Martes")
                input_day = input()
                if(input_day == "1" or input_day == "2"):
                    valid_day = True
                else:
                    print("Error: Ingrese 1 para Lunes o 2 para Martes")
            # Verificar nombre valido del paciente 
            valid_patient_name = False
            while not valid_patient_name:
                print("Ingrese el nombre del paciente")
                patient_name = input()
                # validación del nombre
                if(len(patient_name) and patient_name.isalpha()):
                    valid_patient_name = True
                    lower_patient_name = patient_name.lower()
                else:
                    print("Error: Vacio o ingresó números/símbolos. Solo ingresar letras")
            # verificación de espacios por dia
            match input_day:
                case "1":
                    #verificar si no esta repetido
                    if(
                    lower_patient_name == monday_1 or 
                    lower_patient_name == monday_2 or 
                    lower_patient_name == monday_3 or 
                    lower_patient_name == monday_4):
                        print(f"El paciente {patient_name} ya esta agendado para el Lunes")
                        continue

                    # agendamiento para cada dia
                    if(monday_1 == ""):
                        monday_1 = lower_patient_name
                        monday = monday - 1
                        print(f"Turno reservado para {patient_name} el dia Lunes")
                        
                    elif(monday_2 == ""):
                        monday_2 = lower_patient_name
                        monday = monday - 1
                        print(f"Turno reservado para {patient_name} el dia Lunes")
                        
                    elif(monday_3 == ""):
                        monday_3 = lower_patient_name
                        monday = monday - 1
                        print(f"Turno reservado para {patient_name} el dia Lunes")
                        
                    elif(monday_4 == ""):
                        monday_4 = lower_patient_name
                        monday = monday - 1
                        print(f"Turno reservado para {patient_name} el dia Lunes")
                        
                    else:
                        print("No hay lugares libres el Lunes")
                case "2":
                    if(
                    lower_patient_name == tuesday_1 or 
                    lower_patient_name == tuesday_2 or 
                    lower_patient_name == tuesday_3):
                        print(f"El paciente {patient_name} ya esta agendado para el Martes")
                        continue

                    if(tuesday_1 == ""):
                        tuesday_1 = lower_patient_name
                        tuesday = tuesday - 1
                        print(f"Turno reservado para {patient_name} el dia Martes")
                        continue
                    elif(tuesday_2 == ""):
                        tuesday_2 = lower_patient_name
                        tuesday = tuesday - 1
                        print(f"Turno reservado para {patient_name} el dia Martes")
                        continue
                    elif(tuesday_3 == ""):
                        tuesday_3 = lower_patient_name
                        tuesday = tuesday - 1
                        print(f"Turno reservado para {patient_name} el dia Martes")
                    else:
                        print("No hay lugares libres el Martes")
        # CANCELAR TURNO
        case 2:
            print("CANCELAR TURNO")
            valid_day = False
            #verificar opción de días válidos
            while not valid_day:
                print("Ingrese día 1: Lunes 2: Martes")
                input_day = input()
                if(input_day == "1" or input_day == "2"):
                    valid_day = True
                else:
                    print("Error: Ingrese 1 para Lunes o 2 para Martes")
            # Verificar nombre valido del paciente 
            valid_patient_name = False
            while not valid_patient_name:
                print("Ingrese el nombre del paciente")
                patient_name = input()
                # validación del nombre
                if(len(patient_name) and patient_name.isalpha()):
                    valid_patient_name = True
                    lower_patient_name = patient_name.lower()
                else:
                    print("Error: Vacio o ingresó números/símbolos. Solo ingresar letras")

            match input_day:
                case "1":

                    # agendamiento para cada dia
                    if(monday_1 == lower_patient_name):
                        monday_1 = ""
                        print(f"Turno cancelado para {patient_name} el dia Lunes")
                        monday = monday + 1
                        
                    elif(monday_2 == lower_patient_name):
                        monday_2 = ""
                        monday = monday + 1
                        print(f"Turno cancelado para {patient_name} el dia Lunes")
                        
                    elif(monday_3 == lower_patient_name):
                        monday_3 = ""
                        monday = monday + 1
                        print(f"Turno cancelado para {patient_name} el dia Lunes")
                        
                    elif(monday_4 == lower_patient_name):
                        monday_4 = ""
                        monday = monday + 1
                        print(f"Turno cancelado para {patient_name} el dia Lunes")
                        
                    else:
                        print("Paciente no esta agendado para el Lunes")

                case "2":

                    if(tuesday_1 == lower_patient_name):
                        tuesday_1 = ""
                        tuesday = tuesday + 1
                        print(f"Turno cancelado para {patient_name} el dia Martes")
                        
                    elif(tuesday_2 == lower_patient_name):
                        tuesday_2 = ""
                        tuesday = tuesday + 1
                        print(f"Turno cancelado para {patient_name} el dia Martes")
                        
                    elif(tuesday_3 == lower_patient_name):
                        tuesday_3 = ""
                        tuesday = tuesday + 1
                        print(f"Turno cancelado para {patient_name} el dia Martes")
                        
                    else:
                        print("Paciente no esta agendado para el Martes")
        case 3:
            print("AGENDA DEL DIA")
            valid_day = False
            #verificar opción de días válidos
            while not valid_day:
                print("Ingrese dia a verificar día 1: Lunes 2: Martes")
                input_day = input()
                if(input_day == "1" or input_day == "2"):
                    valid_day = True
                else:
                    print("Error: Ingrese 1 para Lunes o 2 para Martes")

            match input_day:
                case "1":
                    if len(monday_1): print(f"TURNO 1: {monday_1}")
                    else: print("TURNO 1: LIBRE")
                    if len(monday_2): print(f"TURNO 2: {monday_2}")
                    else: print("TURNO 2: LIBRE")
                    if len(monday_3): print(f"TURNO 3: {monday_3}")
                    else: print("TURNO 3: LIBRE")
                    if len(monday_4): print(f"TURNO 4: {monday_4}")
                    else: print("TURNO 4: LIBRE")

                case "2":
                    if len(tuesday_1): print(f"TURNO 1: {tuesday_1}")
                    else: print("TURNO 1: LIBRE")
                    if len(tuesday_2): print(f"TURNO 2: {tuesday_2}")
                    else: print("TURNO 2: LIBRE")
                    if len(tuesday_3): print(f"TURNO 3: {tuesday_3}")
                    else: print("TURNO 3: LIBRE")

        case 4:
            print("RESUMEN GENERAL")
            print("\n")
            print(f"TURNOS LIBRES LUNES: {monday}")
            print(f"TURNOS LIBRES MARTES: {tuesday}")

            if(monday > tuesday):
                print("Dia con mas turnos disponibles: Lunes")
            elif( monday == tuesday ):
                print("Ambos dias con misma cantidad de turnos")
            else:
                print("Dia con mas turnos disponibles: Martes ")

        case 5:
            print("Gracias por usar nuestro servicio")
            end_session = True 
        case _:
            print("Error")
#==================================================
#Ejercicio 4: Boveda:

## Ejercicio cerraduras
energy = 100
time = 12
locks_opened = 0
alarm = False
partial_code = ""
letter_code = "ABCD"

valid_usarname = False
#validar user name 
while not valid_usarname:
    print("Ingrese el nombre del agente!")
    username_input = input()

    if(len(username_input) and username_input.isalpha()):
        valid_usarname = True
    else:
        print("Error: Debe ingresar un nombre válido solo con letras")
# aca tendremos el contador de forzar cerradura option
count_forced_tries = 0
# tenemos q almacenar la opción anterior para seguir la racha de forzar cerraduras
prev_option = 0
is_first_round = True

blocked_alarm = False
while energy > 0 and time > 0 and locks_opened < 3:
    #caso de bloqueo de alarma
    if(alarm == True and time <= 3):
        blocked_alarm = True
        break


    valid_option_num = False
    while not valid_option_num:

        print(f"==== ESTADO ====")
        print(f"Agente: {username_input}")
        print(f"Energía: {energy} Tiempo: {time} Cerraduras abiertas: {locks_opened}/3")
        print("Ingrese opción válida del menu")
        print("1) Forzar cerradura 2) Hackear panel 3) Descansar")
        print("\n")
        user_option_menu = input()
        #validaciones del input de número del usuario:
        if(len(user_option_menu) and user_option_menu.isdigit()):
            user_option_menu = int(user_option_menu)

            if(user_option_menu > 0 and user_option_menu < 4):
                valid_option_num = True
                # aca haremos la validación antispam donde vamos a guardar el valor seleccionado e iremos comparando en cada ronda.
                if(is_first_round and user_option_menu == 1):# caso de primera ronda
                    count_forced_tries = count_forced_tries + 1
                elif(prev_option == 1 and user_option_menu == 1):# caso de las siguientes rondas
                    count_forced_tries = count_forced_tries + 1
                elif(prev_option == 1 and user_option_menu != 1): # caso para cortar la racha
                    count_forced_tries = 0

                is_first_round = False
                prev_option = user_option_menu
            else:
                print("Error: El valor debe ser del 1 al 3")

        else:
            print("Debes ingresar un número válido del 1 al 3")
    match user_option_menu:
        case 1:
            #costo
            energy = energy - 20
            time = time - 2
            #caso tercera vez que usa opción 1
            if(alarm == True):
                print("LA ALARMA ESTA ACTIVADA. NO ABRES CERRADURA")
                continue
            if(count_forced_tries == 3):
                print("Es la tercera vez que fuerzas la cerradura")
                print("\n")
                print("🚨🚨 ALARMA ON 🚨🚨")
                alarm = True
                continue
            # caso 
            if(energy < 40 and count_forced_tries < 3):
                print("Riesgo de alarma!")
                valid_try = False
                while not valid_try:
                    print("Ingrese numero del 1 al 3")
                    force_alarm_try = input()
                    if(len(force_alarm_try) and force_alarm_try.isdigit()):
                        force_alarm_try = int(force_alarm_try)
                        if( force_alarm_try > 0 and force_alarm_try < 4):
                            if(force_alarm_try == 3):
                                print("Se ha activado la alarma")
                                alarm = True
                            else:
                                locks_opened = locks_opened + 1
                        else:
                            print("Error: El valor debe ser del 1 al 3")
                    else:
                        print("No ingresaste un valor válido. Ingrese numero del 1 al 3")
            else:
                print("Has desbloqueado una cerradura!")
                locks_opened = locks_opened + 1
        

        case 2:
            #costo
            energy = energy - 10
            time = time - 3
            #proceso
            for n in range(len(letter_code)):
                partial_code = partial_code + letter_code[n]
                print(partial_code)
                print(f"Has descifrado una letra, te faltan {8 - len(partial_code)} para desbloquear una cerradura")

                if(len(partial_code) >= 8):
                    print("Has desbloqueado una clave!")
                    locks_opened = locks_opened + 1
                    partial_code = ""
            
        case 3:
            print("Has seleccionado descansar")
            #costo
            time = time - 1
            if(alarm == True):
                energy = energy - 10
                print("Pierdes 10 de energía, la alarma esta encendida!")
                continue
            if(energy > 85):
                energy = 100
            else:
                energy = energy + 15
                
            print(f"Has recuperado {energy} energía")
        
                                    
        case _:
            print("Debe seleccionar opción válida del 1 al 3")

# RESULTADOS CADA CASO
if(locks_opened == 3 and time > 0):
    print("Has ganado!")
elif( energy <= 0):
    print("Se te terminó la energia")
    print("HAS PERDIDO")
elif(time <= 0 ):
    print("Se te acabó el tiempo!")
    print("HAS PERDIDO")
elif( blocked_alarm == True):
    print("ALARMA BLOQUEADA")
    print("HAS PERDIDO")


##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
## Ejercicio 5 Escape Room Arena del Gladiador

# Config del personaje
valid_player_name = False
print("--- BIENVENIDO A LA ARENA ---")
print("\n")
while not valid_player_name:
    player_name = input("Ingrese el nombre de su guerrero: ")
# validar si esta vacio o es un numero
    if(len(player_name)):
        if(player_name.isalpha()):
            valid_player_name = True
        else:
            print("Error: Solo se permite letras")
    else:
        print("Error: No ingreso nada. Ingrese un nombre")

## Config de estadisticas
player_health = 100 
enemy_health = 100 
health_potions = 3
base_damage_heavy_attack = 15 
base_damage_enemy_attack = 12 
player_turn = True 

# ciclo de combate
# mientras la salud de ambos sea mayor a 0
# para el primer turno uso bandera. En el segundo comienza con NUEVO TURNO
is_first_turn = True
print("=== INICIO DEL COMBATE ====")
while player_health > 0 and enemy_health > 0:

    if(is_first_turn):
        print(f"{player_name} : (HP: {player_health}) vs Enemigo (HP:{enemy_health}) | Pociones: {health_potions}")
        print("\n")
        is_first_turn = False
    else:
        print("\n")
        print("=== NUEVO TURNO ===")
        print(f"{player_name} : (HP: {player_health}) vs Enemigo (HP:{enemy_health}) | Pociones: {health_potions}")
        print("\n")
    # solicitar opción de juego. Validos que las opciones sean correctas
    valid_option = False
    while not valid_option:
        print("1 : Ataque pesado")
        print("2 : Ráfaga veloz")
        print("3 : Curar")
        #validación del input
        print("\n")
        player_option = input("Elige una opción: ")
        if(len(player_option)):
            if(player_option.isdigit()):
                player_option = int(player_option)
                if(player_option > 0 and player_option < 4):
                    valid_option = True
                else:
                    print("Error: El valor debe ser 1, 2 o 3")
            else:
                print("Error: Debe ingresar valor numérico 1,2 o 3")
        else:
                print("Error: Debe ingresar algún valor")
        # Caralogo de ataques! una vez validado pasamos aca:
    match player_option:
        case 1:
            if(enemy_health < 20):
                enemy_health = enemy_health - (base_damage_heavy_attack * 1.5)
                print(f"Atacaste al enemigo por {base_damage_heavy_attack *1.5} puntos de daño ")
            else:
                enemy_health = enemy_health - base_damage_heavy_attack
                print(f"Atacaste al enemigo por {base_damage_heavy_attack} puntos de daño ")
        case 2:
            for n in range(3):
                enemy_health = enemy_health - 5
                print("> Golpe conectado por 5 de daño")
        case 3:
            if(player_option == 3):
                if(health_potions >0):
                    # aca para evitar sobrepasar el limite de 100:
                    if player_health > 70:
                        player_health = 100
                        health_potions = health_potions -1
                        print(f"Has bebido una poción!. Salud {player_health}")
                    else:
                        player_health = player_health + 30
                        health_potions = health_potions - 1
                        print(f"Has bebido una poción!. Salud {player_health}")
                else:
                    print("No te quedan pociones!")
        case _:
            print("Otro día")
                


    if(enemy_health > 0):
        print("\n")
        print("TURNO DEL ENEMIGO")
        player_health = player_health - 12
        print("El enemigo te ataca por 12 puntos del daño")
        print("\n")
print("\n")
if(player_health > 0):
    print(F"¡VICTORIA! {player_name} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate")
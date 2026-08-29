# ta-te-ti
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
#mostrar el tablero

# jugador por turnos
# Que ingrese fila y columna
# q pasa si esta ocupado?
valid_game = False
print("=========== JUEGO TA TE TI ===========")
while not valid_game:
    for item in range(len(board)):
        print(board[item])

    print("Player 1 : X")
    print("Player 2 : O")
    player_1_turn = True
    while player_1_turn:
        print("Jugador 1 : Ingrese fila. Ej: 1,2,3 ")
        player_1_row = input()
        print("Jugador 1 : Ingrese columna. Ej: 1,2,3 ")
        player_1_col = input()
        player_1_row = int(player_1_row) - 1
        player_1_col = int(player_1_col) - 1

        if(player_1_row >= 0 and player_1_row < 4 and player_1_col >= 0 and player_1_col < 4):
            if(board[player_1_row][player_1_col] == "-"):
                board[player_1_row][player_1_col] = "X"
                player_1_turn = False
            else:
                print("Error: Ese lugar ya esta ocupado")
        else:
            print("Error: Los números deben ser del 1 a 3")

    # condicion para terminar juego: filas
    if(board[0][0] == board[0][1] == board[0][2] and board[0][0] != "-"):
        if(board[0][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[1][0] == board[1][1] == board[1][2] and board[1][0] != "-"):
        if(board[1][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[2][0] == board[2][1] == board[2][2] and board[2][0] != "-"):
        if(board[2][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True

# condicion para ganar columnas
    elif(board[0][0] == board[1][0] == board[2][0] and board[0][0] != "-"):
        if(board[0][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[0][1] == board[1][1] == board[2][1] and board[0][1] != "-"):
        if(board[0][1] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[0][2] == board[1][2] == board[2][2] and board[0][2] != "-"):
        if(board[0][2] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
# condición para diagonales
    elif(board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-"):
        if(board[0][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-"):
        if(board[0][2] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    else: # condición de empate
        count = 0
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == "-":
                    count += 1

        if( count == 0):
            print("Juego empatado")
            valid_game = True

    if valid_game:
        break

    for item in range(len(board)):
        print(board[item])

    player_2_turn = True
    while player_2_turn:
        print("Jugador 2 : Ingrese fila. Ej: 1,2,3 ")
        player_2_row = input()
        print("Jugador 2 : Ingrese columna. Ej: 1,2,3 ")
        player_2_col = input()
        player_2_row = int(player_2_row) - 1
        player_2_col = int(player_2_col) - 1

        if(player_2_row >= 0 and player_2_row < 4 and player_2_col >= 0 and player_2_col < 4):
            if(board[player_2_row][player_2_col] == "-"):
                board[player_2_row][player_2_col] = "O"
                player_2_turn = False
            else:
                print("Error: Ese lugar ya esta ocupado")
        else:
            print("Error: Elegir números 1,2 o 3")

    # No puedo modularizar en funciones entonces tengo q repetir los bloques para validar el juego
    # condicion para terminar juego: filas
    if(board[0][0] == board[0][1] == board[0][2] and board[0][0] != "-"):
        if(board[0][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[1][0] == board[1][1] == board[1][2] and board[1][0] != "-"):
        if(board[1][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[2][0] == board[2][1] == board[2][2] and board[2][0] != "-"):
        if(board[2][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True

# condicion para ganar columnas
    elif(board[0][0] == board[1][0] == board[2][0] and board[0][0] != "-"):
        if(board[0][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[0][1] == board[1][1] == board[2][1] and board[0][1] != "-"):
        if(board[0][1] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[0][2] == board[1][2] == board[2][2] and board[0][2] != "-"):
        if(board[0][2] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
# condición para diagonales
    elif(board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-"):
        if(board[0][0] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    elif(board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-"):
        if(board[0][2] == "X"):
            print("Gana jugador 1")
            valid_game = True
        else:
            print("Gana jugador 2")
            valid_game = True
    else: # condición de empate
        count = 0
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == "-":
                    count += 1

        if( count == 0):
            print("Juego empatado")
            valid_game = True


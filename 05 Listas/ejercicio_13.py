# puntajes video juego
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

#mostrar puntaje mas alto y mas bajo
max_points = max(puntajes)
min_points = min(puntajes)
#mostrar ranking
down_sorted = sorted(puntajes,key=None,reverse=True)
print("==== POSICIONES ====")
for n in range(len(down_sorted)):
    print(f"{n +1 }: {down_sorted[n]}")
    if(down_sorted[n] == 990):
        pos = n + 1
#mostrar posición del ranking 990
print(f"Puntaje 990 en posición {pos}")
print(f"Puntaje mas alto {max_points}")
print(f"Puntaje mas bajo {min_points}")

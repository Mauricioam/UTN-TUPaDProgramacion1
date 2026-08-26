# matriz 7 x 2 para temp
# fila materia columna estudiantes

week_temp = [[32,21],[34,21],[34,21],[29,20],[30,20],[23,16],[24,13]]
sum_max = 0
sum_min = 0
first_loop = True
for row in range(len(week_temp)):
    sum_max += week_temp[row][0]
    sum_min += week_temp[row][1]

    if first_loop:
        first_loop = False
        termic_amplitude = week_temp[row][0] - week_temp[row][1]
        continue
    temp_diff = week_temp[row][0] - week_temp[row][1]
    if temp_diff > termic_amplitude:
        termic_amplitude = temp_diff
        day = row + 1


average_max = round(sum_max/ len(week_temp),2)
average_min = round(sum_min / len(week_temp),2)

print(f"El promedio de temperatura max es: {average_max}")
print(f"El promedio de temperatura min es: {average_min}")
print(f"El día {day} tuvo mayor amplitud: {termic_amplitude} grados")
#matriz de 5 x 3 promedio de cada estudiante y promedio de cada materia
# fila = estudiante ; col1,2,3 = materia 1 , 2 y 3
student_grades = [[5,6,7],[4,5,9],[8,8,9],[7,7,7],[8,3,6]]
grades_student = [0,0,0,0,0]
subjects_grades = [0,0,0]
materia_2 = 0
materia_3 = 0
for row in range(len(student_grades)):
    subjects_grades[0] = student_grades[row][0] + subjects_grades[0]
    subjects_grades[1] = student_grades[row][1] + subjects_grades[1]
    subjects_grades[2] = student_grades[row][2] + subjects_grades[2]
    for item in range(len(student_grades[row])):
        match row:
            case 0:
                grades_student[row] = student_grades[row][item] + grades_student[row] 
            case 1:
                grades_student[row] = student_grades[row][item] + grades_student[row] 
            case 2:
                grades_student[row] = student_grades[row][item] + grades_student[row] 
            case 3:
                grades_student[row] = student_grades[row][item] + grades_student[row] 
            case 4:
                grades_student[row] = student_grades[row][item] + grades_student[row] 
# promedio de estudiantes en las 3 materias
for n in range(len(grades_student)):
    grades_student[n] = round(grades_student[n]/len(student_grades[row]),2)
# promedio por materia
for subject in range(len(subjects_grades)):
    subjects_grades[subject] = round(subjects_grades[subject]/len(student_grades),2)
# mostrar cada promedio
for n in range(len(grades_student)):
    print(f"El estudiante {n+1} tiene un promedio de {grades_student[n]}")

for n in range(len(subjects_grades)):
    print(f"La materia {n+1} tiene un promedio de {subjects_grades[n]}")


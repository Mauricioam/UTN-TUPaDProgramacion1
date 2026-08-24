## 1 ) Lista de 10 estudiantes
student_grades = [5,10,8,2,1,9,6,3,4,7]
total = 0
for num in student_grades:
    total += num
print(f"El promedio es {total/len(student_grades)}")
print(f"El max es {max(student_grades)} el min {min(student_grades)}")
# lista con 10 estudiantes
studen_names = [
    "Ana",
    "Carlos",
    "Elena",
    "Javier",
    "Lucia",
    "Marcos",
    "Sofia",
    "Tomás",
    "Valeria",
    "Mateo"
]
print(studen_names)


print("Ingrese el nombre del estudiante a buscar")
user_input = input()
user_input = user_input.lower()
for name in range(len(studen_names)):
    studen_names[name] = studen_names[name].lower()

if studen_names.count(user_input) > 0:
    print("El nombre se encuentra en la lista")
    for name in range(len(studen_names)):
        if studen_names[name] == user_input:
            pos = name
    print(f"Se encuenta en la posición {pos}")
else:
    print("El nombre no esta en la lista")


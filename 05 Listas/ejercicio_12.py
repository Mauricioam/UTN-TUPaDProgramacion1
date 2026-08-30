# usuario debe ingresar 8 numero int
# mostrar lista
# mostrar lista ordenada decreciente
# mostrar lista ordenada creciente

user_num = []
for n in range(8):
    print(f"Ingresa un número entero: {n+1} de 8")
    user_input = input()
    user_input = int(user_input)
    user_num.append(user_input)
#lista original
sorted_up = sorted(user_num)
sorted_down = sorted(user_num,key=None,reverse=True)

## sorted puede devolver la lista de forma creciente y decreciente. Devuelve una lista nueva y no modifica la original
## importante no modificar lista original cuando se trabajen con datos reales. Lo ideal es nunca modificar datos

print(f"Lista ordenada creciente: {sorted_up}")
print(f"Lista ordenada decreciente: {sorted_down}")
print(f"Lista original { user_num}")
# 3 generar 15 números y separar por par e impar
import random
random_num = []
odd_num = []
even_num = []
for n in range(15):
    random_num.append(random.randint(1, 100))
    if(random_num[n] % 2 == 0):
        even_num.append(random_num[n])
    else:
        odd_num.append(random_num[n])


print(f"Lista completa: {random_num}")
print(f"Números pares: {even_num}")
print(f"Números impares: {odd_num}")
# ventas de 4 productos durante 7 dias
# matriz 4x7
product_sales = [
    [12, 15, 8, 20, 25, 30, 10],   # Producto 1
    [5, 8, 12, 14, 19, 22, 7],     # Producto 2
    [30, 25, 40, 35, 50, 60, 45],  # Producto 3
    [3, 4, 6, 2, 8, 10, 5]         # Producto 4
]

# total vendido por cada producto
product_total = []
for product in range(len(product_sales)):
    temp = sum(product_sales[product])  
    product_total.append(temp)

print(product_total)
# mostrar el total vendido y el producto mas vendido
most_saled = 0
for product in range(len(product_total)):
    print(f"El producto {product + 1} vendió un total de {product_total[product]}")
    if product == 0:
        temp_most_saled = product_total[product]
    elif product_total[product] > temp_most_saled:
        most_saled = product + 1
        temp_most_saled = product_total[product]


# dia con mayores ventas
daily_sale = []

for row in range(len(product_sales)):
    for col in range(len(product_sales[row])):
        if row == 0:
            daily_sale.append(product_sales[row][col])
        else:
            daily_sale[col] += product_sales[row][col]

higher_day_sales = 0
for day in range(len(daily_sale)):
    if day == 0:
        temp_higher_day = daily_sale[day]
    elif daily_sale[day] > temp_higher_day:
        temp_higher_day = daily_sale[day]
        higher_day_sales = day + 1

print("\n")
print(f"El dia con mayores ventas fué el dia : {higher_day_sales}")
print(f"El producto mas vendido fué el producto {most_saled} ")

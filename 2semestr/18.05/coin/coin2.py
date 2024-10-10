products = {
    "молоко": 30,
    "хлеб": 15,
    "сыр": 40,
    "масло": 30,
    "яйца": 25,
    "яблоки": 50,
    "бананы": 35,
    "вода": 10,
    "сок": 45,
    "кофе": 60
}

coins = [20, 15, 10, 5, 1]
coins_count = {20: 10, 15: 10, 10: 10, 5: 10, 1: 10}

print("Список продуктов:")
for i, (product, price) in enumerate(products.items(), 1):
    print(f"{i}. {product} - {price}р")

choice = int(input("Выберите продукт (введите номер): ")) - 1
product_name = list(products.keys())[choice]
product_price = products[product_name]

payment = int(input(f"Введите сумму, которую даёте (цена продукта {product_price}р): "))
change = payment - product_price
print(f"Сдача составляет: {change}р")

result = []
for coin in coins:
    while change >= coin and coins_count[coin] > 0:
        change -= coin
        coins_count[coin] -= 1
        result.append(coin)

if change == 0:
    print(f"Сдача будет выдана монетами: {result}")
else:
    print("Недостаточно монет для сдачи.")

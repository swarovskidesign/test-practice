products = {
    "молоко": 20,
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

coins = [15, 10, 7, 5, 1]

def get_min_coins(change):
    result = []
    for coin in coins:
        while change >= coin:
            change -= coin
            result.append(coin)
    return result

print("Список продуктов:")
for i, (product, price) in enumerate(products.items(), 1):
    print(f"{i}. {product} - {price}р")

choice = int(input("Выберите продукт (введите номер): ")) - 1
product_name = list(products.keys())[choice]
product_price = products[product_name]

payment = int(input(f"Введите сумму, которую даёте (цена продукта {product_price}р): "))
change = payment - product_price
print(f"Сдача составляет: {change}р")

change_coins = get_min_coins(change)
print(f"Сдача будет выдана монетами: {change_coins} (количество монет: {len(change_coins)})")

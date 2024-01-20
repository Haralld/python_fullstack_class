import json

with open('inventory.json', 'r') as json_file:
    json_data = json.load(json_file)

def product_quantity(data):
    """функция проверяет наличие товаров и сосволяет список покупок"""

    shop_list = {}

    for material in data['inventory']:
        item = material['item']
        quantity = material['quantity']
        min_required = material['minimum_required']
        required = min_required - quantity

        if item not in shop_list:
            if quantity < min_required:
                shop_list[item] = required
        
    return shop_list

# вызов функции 
result = product_quantity(json_data)

# вывод результата
for item, required in result.items():
    print(f"Необходимо закупить: {item} {required} шт.")
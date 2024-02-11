import json

# чтение данных из файла
with open('sales.json', 'r', encoding="utf-8") as json_file:
    json_data= json.load(json_file)


def  calculation_revenue(data):
    """Функция обходит данные файла и складывает выручку одинаковых категорий товаров"""
    
    end_info = {}

    for sale in data['sales']:
        category = sale['category']
        total_price = sale['total_price'] * sale['quantity']

        if category not in end_info:    
            end_info[category] = total_price
        else:
            end_info[category] += total_price
    
    return end_info

# вызов функции для подсчёта выручки из файла
result = calculation_revenue(json_data)

# вывод резальтата
for category, total_prise in result.items():
    print(f"Выручка по категории: {category}: {total_prise}")
    

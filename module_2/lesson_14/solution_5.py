from collections import Counter

def inventory_counter(items):
    type_counts = Counter(map(lambda item: item[1], items))
    return dict(type_counts)


items_list_1 = [('Рубашка', 'Одежда'), ('Кружка', 'Посуда')]   
items_list_2 = [('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')]  
items_list_3 = [('Ручка', 'Канцелярия'), ('Тетрадь', 'Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')]

result_1 = inventory_counter(items_list_1)
result_2 = inventory_counter(items_list_2)
result_3 = inventory_counter(items_list_3)

print(result_1)
print(result_2)
print(result_3)

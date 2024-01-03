from collections import Counter

def inventory_counter(items):
    type_counts = Counter(map(lambda item: item[1], items))
    return dict(type_counts)

# Пример использования
items_list = [("item1", "electronics"), ("item2", "clothing"), ("item3", "electronics"), ("item4", "clothing"), ("item5", "books")]

result = inventory_counter(items_list)
print(result)

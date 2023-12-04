products_list_1 = ['fruit', 'toy', 'fruit', 'toy']
product_1 = 'toy'

products_list_2 = ['clothes', 'clothes', 'clothes']
product_2 = 'clothes'

def count_specific_items_with_while(product, product_list):
    
    while product in product_list:
        product_count = product_list.count(product)
        print(f"Количество {product}: {product_count}")
        break

count_specific_items_with_while(product_1, products_list_1)        
count_specific_items_with_while(product_2, products_list_2)

"""
Описание:

В магазинах Романа есть различные категории товаров. 
Необходимо написать функцию `count_specific_items_with_while`, 
которая с помощью цикла `while` подсчитывает количество товаров определенной категории в переданном списке.



Примеры входных и выходных данных:



Ограничения:

- Использовать только цикл `while`
"""
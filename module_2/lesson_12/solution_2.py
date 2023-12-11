order_1 = {'id': 1, 'items': ['book', 'pen']}
order_2 = {'id': 2, 'items': []}

def check_order(order):   # проверка
    return bool(order.get('items'))

def package_order(order):  # упаковка
    return bool(order)

def send_order(check_function, package_function, order):  # Отправка
    if check_function(order): 
        return f"Отправка: Упакован заказ {order['id']}" if package_function(order) else "Отправка: Нечего упаковывать"
    else:
        return f"Отправка: Заказ {order['id']} пуст"

print(send_order(check_order, package_order, order_1))
print(send_order(check_order, package_order, order_2))


"""
Задача 2: Композиция функций для обработки заказов

Описание:  

В рамках оптимизации работы интернет-магазина Роман хочет создать функционал для комплексной обработки заказов.
 Разработайте три функции: `check_order`, `package_order` и `send_order`. 
 Функция `send_order` должна принимать `check_order` и `package_order` и применять `package_order` к результату выполнения `check_order`.


Примечание:

`check_order` проверяет заказ, `package_order` упаковывает его, `send_order` координирует процесс и инициирует отправку. 
Функиция `send_order` не должна начинать упаковку заказа, если он пустой!


В нашем примере вызов функции должен выглядеть так:

order1 = {'id': 1, 'items': ['book', 'pen']}

order2 = {'id': 2, 'items': []}


print(send_order(check_order, package_order, order1))

print(send_order(check_order, package_order, order2))
"""

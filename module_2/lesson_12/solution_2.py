order_1 = {'id': 1, 'items': ['book', 'pen']}
order_2 = {'id': 2, 'items': []}

def check_order(order):   # проверка
    if order and 'items' in order and len(order['items']) > 0:
        return "Успешная проверка"
    else:
        return f"Заказ {order['id']} пуст"

def package_order(order):  # упаковка
    if order:
        return "Успешная упаковка"
    else:
        return "Нечего упаковывать"

def send_order(check_function, package_function, order):  # Отправка
    checked_result = check_function(order)

    if "Успешная" in checked_result:
        packaged_result = package_function(order)
        if "Успешная" in packaged_result:
            return f"Отправка: Упакован заказ {order['id']}"
        else:
            return f"Отправка: {packaged_result}"
    else:
        return f"Отправка: {checked_result}"


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
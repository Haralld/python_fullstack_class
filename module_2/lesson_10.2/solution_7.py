input_prices = input("Список цен: ")
prices = [float(x) for x in input_prices.split(', ')]

def calculate_discount(prices, index=0, previous_price=None):
    end_prices = []

    if index < len(prices):
        current_price = prices[index] 
        current_discount = previous_price * 0.1 if previous_price is not None else 0
        discount_price = current_price - current_discount if previous_price is not None else current_price
        end_prices.append(discount_price)
        end_prices += calculate_discount(prices, index + 1, current_price)

    return end_prices

result = calculate_discount(prices)
result_int = [int(x) for x in result]

print("Выходные данные:", result_int)






"""
Задача 7: Расчет скидок

Описание:

В дизайн-студии Романа каждый новый заказ получает скидку, размер которой равен 10% от стоимости предыдущего заказа. 
Напишите рекурсивную функцию `calculate_discount`,
которая принимает на вход список стоимостей заказов и возвращает список стоимостей заказов уже со скидками.


"""

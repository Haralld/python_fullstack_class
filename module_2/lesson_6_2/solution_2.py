price_list = []
price = ''

while price != 0:
    price = int(input("Введите цены(для окончания введите 0):"))
    if price != 0:
        price_list.append(price)

print(f"Цены без скидки: {price_list[1::2]}")


"""
Задание 2: Скидки на определенные товары

Описание:

Роман хочет ввести скидки на определенные товары. 
Напишите программу, которая выводит все товары, на которые скидка не распространяется. 
Эти товары будут являться нечетными числами в списке цен.
"""
length = float(input("Введите длину помещения: "))
width = float(input("Введите ширину помещения: "))

square = float(length * width)
round_square = round(square, 2)

print(f"Площадь помещения ровна: {round_square}")

"""
Задача 2: Площадь магазина

Описание:

Роману нужно узнать площадь своего магазина для оптимизации расстановки товаров. 
Магазин представляет собой прямоугольник.

Реализуйте программу, которая принимает на вход длину и ширину магазина в метрах и выводит его площадь. 
Площадь должна быть в виде float значения, убедитесь, что возвращаете всегда значение нужного типа.
"""
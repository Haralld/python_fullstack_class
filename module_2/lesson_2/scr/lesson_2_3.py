books = int(input("Введите колличесво книг: "))
stationery = int(input("Введите колличесво канцтоваров: "))
toys = int(input("Введите колличесво игрушек: "))

volume_books = books * 2
volume_stationary = stationery * 1.5
volume_toys = toys * 3

total_volume = volume_books + volume_stationary + volume_toys

print(f"Общий объём для хранени всех товаров равен {total_volume} m2")
"""
Задача 3: Расчет объема товаров для магазина "Гладиолус"

Описание:

Роман хочет определить, сколько коробок он должен закупить для хранения товаров в своем магазине "Гладиолус". 
У него есть три типа товаров: книги, канцтовары и игрушки.



Для книг требуется 2 м², для канцтоваров — 1.5 м², а для игрушек — 3 м².

Реализуйте программу, которая принимает количество каждого типа товара и вычисляет общий объем в м², 
который потребуется для хранения всех товаров.
"""
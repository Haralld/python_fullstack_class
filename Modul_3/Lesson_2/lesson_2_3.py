
class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * (9/5)) + 32
        print(f"Температура в градусах Фаренгейта: {fahrenheit}")


    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * (5/9)
        print(f"Температура в градусах Цельсия: {celsius}")


Temperature.celsius_to_fahrenheit(10)
Temperature.celsius_to_fahrenheit(32)

Temperature.fahrenheit_to_celsius(50)
Temperature.fahrenheit_to_celsius(54.5)



"""
Задание 3: Конвертация единиц
Создайте класс Temperature с методами для конвертации температуры между градусами Цельсия и Фаренгейта.
Реализуйте статические методы celsius_to_fahrenheit и fahrenheit_to_celsius.
"""
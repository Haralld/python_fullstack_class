class Greenhouse:
    def __init__(
            self,
            temperature=25,
            humidity=50,
            light_level=65
    ):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__light_level = light_level

    @property
    def temperature(self):  # геттер
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):  # сеттер
        if not 15 <= temperature <= 30:  # температура в градусах Цельсия
            print(f"Недопустимая температура: {temperature}")
        else:
            self.__temperature = temperature
            print("Текущая температура:", greenhouse.temperature)

    @property
    def humidity(self):  # геттер
        return self.__humidity

    @humidity.setter
    def humidity(self, humidity):  # сеттер
        if not 50 <= humidity <= 60:  # влажность в процентах
            print(f"Недопустимый уровень влажности: {humidity}")
        else:
            self.__humidity = humidity
            print("Текущий уровень влажности:", greenhouse.humidity)

    @property
    def light_level(self):  # геттер
        return self.__light_level

    @light_level.setter
    def light_level(self, light_level):  # сеттер
        if not 25 <= light_level <= 65:  # интенсивность свечения в Вт/м2
            print(f"Недопустимый уровень освещенности: {light_level}")
        else:
            self.__light_level = light_level
            print("Текущий уровень освещенности:", greenhouse.light_level)


greenhouse = Greenhouse()

greenhouse.temperature = 28
greenhouse.humidity = 55
greenhouse.light_level = 80



"""
Задание 2: Автоматизация управления теплицей (Инкапсуляция)

Создайте класс Greenhouse с приватными атрибутами для температуры, влажности и уровня света.

Добавьте публичные методы для установки и получения этих атрибутов, включая проверки на допустимые значения 
(например, температура должна быть между 15 и 30 градусами).

В программе создайте объект Greenhouse и продемонстрируйте установку и получение атрибутов с помощью методов.


"""

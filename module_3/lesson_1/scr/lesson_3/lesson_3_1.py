from abc import ABC, abstractmethod


class Fountain(ABC):

    @abstractmethod
    def spray_water(self):
        pass


class SimpleFountain:
    def spray_water(self):
        print("Простой фонтан брызгает воду.")


class MusicalFountain:
    def spray_water(self):
        print("Музыкальный фонтан брызгает водой под музыку")


class LightedFountain:
    def spray_water(self):
        print("Освещаемый фонтан брызгает водой и светится")


fountains = [SimpleFountain(), MusicalFountain(), SimpleFountain()]

for fountain in fountains:
    fountain.spray_water()

"""
Задание 1: Управление фонтанами (Полиморфизм)

Создайте абстрактный класс Fountain с методом spray_water.

Создайте подклассы SimpleFountain, MusicalFountain, и LightedFountain, которые переопределяют метод spray_water, выводя уникальное сообщение о том, как каждый фонтан брызгает воду.

В программе создайте список объектов типа Fountain и вызовите метод spray_water для каждого элемента списка.
"""

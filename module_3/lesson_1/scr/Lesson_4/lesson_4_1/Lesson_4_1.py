from abc import ABC, abstractmethod
import pygame
import time


class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


class Guitar(Instrument):
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(
            'sound/guitar.mp3')
        pygame.mixer.music.set_volume(100)
        print("Так звучит гитара")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.stop()


class Piano(Instrument):
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(
            'sound/piano.mp3')
        pygame.mixer.music.set_volume(100)
        print("Так звучит пианино")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.stop()


class Flute(Instrument):
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(
            'sound/flute.mp3')
        pygame.mixer.music.set_volume(100)
        print("Так звучит флейта")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.stop()


guitar = Guitar()
piano = Piano()
flute = Flute()

piano.play()
guitar.play()
flute.play()

"""
Задание 1: Школа музыки (Наследование от абстрактного класса)
Создайте абстрактный класс Instrument с абстрактным методом play().
Создайте подклассы Guitar, Piano, и Flute, каждый из которых переопределяет метод play.
В каждом подклассе должен быть своя реализация метода для воспроизведения звука инструмента.
В главной программе создайте список объектов типа Instrument и вызовите для каждого метод play.
"""

from abc import ABC, abstractmethod
import pygame
import time
import cv2


class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


class Guitar(Instrument):
    def play(self):
        cap = cv2.VideoCapture('sound/guitar.mp4')

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow('video_guitar', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()


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
        print("Звук флейты - словно легкий воздушный вздох, наполняющий пространство нежностью и покоем.")

        time.sleep(5)


guitar = Guitar()
piano = Piano()
flute = Flute()

# flute.play()
# piano.play()
guitar.play()

"""
Задание 1: Школа музыки (Наследование от абстрактного класса)
Создайте абстрактный класс Instrument с абстрактным методом play().
Создайте подклассы Guitar, Piano, и Flute, каждый из которых переопределяет метод play.
В каждом подклассе должен быть своя реализация метода для воспроизведения звука инструмента.
В главной программе создайте список объектов типа Instrument и вызовите для каждого метод play.
"""

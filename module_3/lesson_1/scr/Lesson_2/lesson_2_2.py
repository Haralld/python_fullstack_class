import datetime


class Person:
    population = 0

    def __init__(
            self,
            name: str,
            age: int
    ):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def from_birth_year(cls,
                        name,
                        birth_year
                        ):
        today = datetime.date.today()
        current_year = today.year
        age = current_year - birth_year
        return cls(name, age)

    @classmethod
    def current_population(cls):
        print(f"Текущая популяция: {cls.population}")


person_1 = Person.from_birth_year("Михаил", 1988)

Person.current_population()

person_2 = Person.from_birth_year("Татьяна", 1983)

Person.current_population()

person_3 = Person.from_birth_year("Харальд", 2000)
person_4 = Person.from_birth_year("Торвальд", 2005)

Person.current_population()
"""
Задание 2: Работа с атрибутами класса
Добавьте в класс Person атрибут класса population, который будет отслеживать количество созданных экземпляров.
Обновите методы __init__ и from_birth_year так, чтобы они увеличивали population на 1 при создании нового экземпляра.
Создайте метод класса, который выводит текущую популяцию.

"""
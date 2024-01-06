import datetime


class Person:
    def __init__(
            self,
            name: str,
            age: int
    ):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls,
                        name,
                        birth_year
                        ):
        today = datetime.date.today()
        current_year = today.year
        age = current_year - birth_year
        return cls(name, age)


person = Person.from_birth_year("Михаил", 1988)

print(f"Имя: {person.name}, Возраст: {person.age} лет")

"""
Задание 1: Альтернативные конструкторы
Создайте класс Person с атрибутами name и age.
Реализуйте метод __init__ для инициализации этих атрибутов.
Создайте класс метод from_birth_year для создания экземпляра Person на основе года рождения.
Выведите информацию о персоне, созданной через этот альтернативный конструктор.
"""

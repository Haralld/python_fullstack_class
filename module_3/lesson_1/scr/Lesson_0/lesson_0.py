from typing import Literal


class Animal:
    def __init__(
            self,
            animal_type: str,
            animal_noises: str,
            feeding: Literal["хищное", "травоядное", "всеядное"]
    ):
        self.animal_type = animal_type
        self.animal_noises = animal_noises
        self.feeding = feeding

    def __str__(self) -> str:
        return f"Это {self.feeding} животное {self.animal_type}."

    def sound(self) -> str:
        return f"{self.animal_type} издает следующие звуки {self.animal_noises}."


lion = Animal("Лев", "ррр", "хищное")
rabbit = Animal("Кролик", "Хрум-хрум", "травоядное")
bear = Animal("Медведь", "гррр", "всеядное")

print(lion, lion.sound())
print(rabbit, rabbit.sound())
print(bear, bear.sound())


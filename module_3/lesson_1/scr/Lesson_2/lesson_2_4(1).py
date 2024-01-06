from enum import Enum


class VehicleType(Enum):
    CAR = "car"
    BOAT = "boat"


class Moveable:
    def move(self) -> None:
        pass


class Vehicle:
    total_vehicles = 0

    def __init__(
            self,
            speed: float
    ) -> None:
        self.speed = speed
        Vehicle.total_vehicles += 1

    @classmethod
    def create_vehicle(cls, vehicle_type: VehicleType, speed: float) -> 'Vehicle':
        if vehicle_type == VehicleType.CAR:
            return Car(speed)
        elif vehicle_type == VehicleType.BOAT:
            return Boat(speed)
        else:
            raise ValueError("Неизвестный тип транспортного средства")

    @staticmethod
    def convert_speed_to_kmh(speed_mph: float) -> float:
        return speed_mph * 1.60934

    @classmethod
    def display_total_vehicles(cls) -> None:
        print(f"Всего было создано {cls.total_vehicles} экземпляров таранспортных средств")


class Car(Vehicle, Moveable):
    def move(self) -> None:
        current_speed = Vehicle.convert_speed_to_kmh(self.speed)
        print(f"Скорость машины {current_speed} км/час")


class Boat(Vehicle, Moveable):
    def move(self) -> None:
        print(f"Скорость лодки {self.speed} морских миль")


def move_any_vehicle(vehicle: Moveable) -> None:
    vehicle.move()


car_1 = Vehicle.create_vehicle(VehicleType.CAR, 60)
boat_1 = Vehicle.create_vehicle(VehicleType.BOAT, 25)

move_any_vehicle(car_1)
move_any_vehicle(boat_1)

Vehicle.display_total_vehicles()

"""
Задание 4: Фабричный метод
Используя пример с классом Vehicle, добавьте еще один тип транспортного средства, например, Bike.
Добавьте в класс Vehicle поддержку этого нового типа.
Убедитесь, что ваш фабричный метод корректно создает новый тип транспортного средства.
"""

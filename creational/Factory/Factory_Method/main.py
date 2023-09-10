"""
    Factory Method
     - Provides an interface for creating objects in a superclass,
    but allows subclasses to alter the type of objects that will be created.
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_customer(self) -> None: pass


class CarLuxury(Vehicle):
    def get_customer(self) -> None:
        print('Luxury car is looking for the customer...')


class CarEconomy(Vehicle):
    def get_customer(self) -> None:
        print('Economy car is looking for the customer...')


class MotorcycleLuxury(Vehicle):
    def get_customer(self) -> None:
        print('Luxury motorcycle is looking for the customer...')


class MotorcycleEconomy(Vehicle):
    def get_customer(self) -> None:
        print('Economy motorcycle is looking for the customer...')


class VehicleFactory(ABC):
    def __init__(self, type) -> None:
        self.vehicle = self.get_vehicle(type)

    @staticmethod
    @abstractmethod
    def get_vehicle(type: str) -> Vehicle: pass

    def get_customer(self):
        self.vehicle.get_customer()


class VehicleFactoryNorth(VehicleFactory):
    @staticmethod
    def get_vehicle(type: str) -> Vehicle:  # Factory Method
        vehicle: Vehicle
        if type == 'car_luxury':
            vehicle = CarLuxury()
        elif type == 'car_economy':
            vehicle = CarEconomy()
        elif type == 'motorcycle_luxury':
            vehicle = MotorcycleLuxury()
        elif type == 'motorcycle_economy':
            vehicle = MotorcycleEconomy()
        else:
            raise ValueError('Vehicle does not exists')

        return vehicle


class VehicleFactorySouth(VehicleFactory):
    @staticmethod
    def get_vehicle(type: str) -> Vehicle:
        vehicle: Vehicle
        if type == 'car_economy':
            vehicle = CarEconomy()
        else:
            raise ValueError('Vehicle does not exists')

        return vehicle


if __name__ == '__main__':
    from random import choice
    north_available_vehicles = [
        'car_luxury', 'car_economy',
        'motorcycle_luxury', 'motorcycle_economy',
    ]

    south_available_vehicles = ['car_economy']
    print('NORTH REGION')
    for i in range(10):
        vehicle1 = VehicleFactoryNorth(choice(north_available_vehicles))
        vehicle1.get_customer()
    print()
    print('SOUTH REGION')
    for i in range(3):
        vehicle2 = VehicleFactorySouth(choice(south_available_vehicles))
        vehicle2.get_customer()

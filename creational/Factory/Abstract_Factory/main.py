"""
    Abstract Factory
    - Lets you produce families of related objects without specifying their
    concrete classes.
"""
from abc import ABC, abstractmethod


class VehicleLuxury(ABC):
    @abstractmethod
    def get_customer(self) -> None: pass


class VehicleEconomy(ABC):
    @abstractmethod
    def get_customer(self) -> None: pass


class CarLuxuryNorth(VehicleLuxury):
    def get_customer(self) -> None:
        print('North luxury car is looking for the customer...')


class CarEconomyNorth(VehicleEconomy):
    def get_customer(self) -> None:
        print('North economy car is looking for the customer...')


class MotorcycleLuxuryNorth(VehicleLuxury):
    def get_customer(self) -> None:
        print('North luxury motorcycle is looking for the customer...')


class MotorcycleEconomyNorth(VehicleEconomy):
    def get_customer(self) -> None:
        print('North economy motorcycle is looking for the customer...')


class CarLuxurySouth(VehicleLuxury):
    def get_customer(self) -> None:
        print('South luxury car is looking for the customer...')


class CarEconomySouth(VehicleEconomy):
    def get_customer(self) -> None:
        print('South economy car is looking for the customer...')


class MotorcycleLuxurySouth(VehicleLuxury):
    def get_customer(self) -> None:
        print('South luxury motorcycle is looking for the customer...')


class MotorcycleEconomySouth(VehicleEconomy):
    def get_customer(self) -> None:
        print('South economy motorcycle is looking for the customer...')


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_car_luxury() -> VehicleLuxury: pass

    @staticmethod
    @abstractmethod
    def get_car_economy() -> VehicleEconomy: pass

    @staticmethod
    @abstractmethod
    def get_motorcycle_luxury() -> VehicleLuxury: pass

    @staticmethod
    @abstractmethod
    def get_motorcycle_economy() -> VehicleEconomy: pass


class VehicleFactoryNorth(VehicleFactory):
    @staticmethod
    def get_car_luxury() -> VehicleLuxury:
        return CarLuxuryNorth()

    @staticmethod
    def get_car_economy() -> VehicleEconomy:
        return CarEconomyNorth()

    @staticmethod
    def get_motorcycle_luxury() -> VehicleLuxury:
        return MotorcycleLuxuryNorth()

    @staticmethod
    def get_motorcycle_economy() -> VehicleEconomy:
        return MotorcycleEconomyNorth()


class VehicleFactorySouth(VehicleFactory):
    @staticmethod
    def get_car_luxury() -> VehicleLuxury:
        return CarLuxurySouth()

    @staticmethod
    def get_car_economy() -> VehicleEconomy:
        return CarEconomySouth()

    @staticmethod
    def get_motorcycle_luxury() -> VehicleLuxury:
        return MotorcycleLuxurySouth()

    @staticmethod
    def get_motorcycle_economy() -> VehicleEconomy:
        return MotorcycleEconomySouth()


class Branch:
    def get_customers(self):
        for factory in [VehicleFactoryNorth, VehicleFactorySouth]:
            car_economy = factory.get_car_economy()
            car_economy.get_customer()

            car_luxury = factory.get_car_luxury()
            car_luxury.get_customer()

            motorcycle_economy = factory.get_motorcycle_economy()
            motorcycle_economy.get_customer()

            motorcycle_luxury = factory.get_motorcycle_luxury()
            motorcycle_luxury.get_customer()


if __name__ == '__main__':
    b = Branch()
    b.get_customers()

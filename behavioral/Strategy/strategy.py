"""
    Strategy
     - Lets you define a family of algorithms, put each of them into a separate
     class, and make their objects interchangeable.
"""

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercentDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercentDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float) -> None:
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


if __name__ == '__main__':
    twenty_percent = TwentyPercentDiscount()
    fifty_percent = FiftyPercentDiscount()
    no_discount = NoDiscount()
    custom_discount = CustomDiscount(5)

    order = Order(1000, twenty_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, fifty_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, no_discount)
    print(order.total, order.total_with_discount)

    order = Order(1000, custom_discount)
    print(order.total, order.total_with_discount)

"""
    Composite
     - Lets you compose objects into tree structures and then work with these
     structures as if they were individual objects.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class BoxStructure(ABC):
    """Component"""

    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    """Composite"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: list[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """Leaf"""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    # Leaf
    shirt_1 = Product('Shirt 1', 49.90)
    shirt_2 = Product('Shirt 2', 29.99)
    shirt_3 = Product('Shirt 3', 75.65)

    # Composite
    box_of_shirts = Box('Box of Shirts')
    box_of_shirts.add(shirt_1)
    box_of_shirts.add(shirt_2)
    box_of_shirts.add(shirt_3)

    # Leaf
    smartphone_1 = Product('iPhone 15', 1100.00)
    smartphone_2 = Product('S23 Ultra', 950.00)

    # Composite
    box_of_smartphones = Box('Box of Smartphones')
    box_of_smartphones.add(smartphone_1)
    box_of_smartphones.add(smartphone_2)

    # Composite
    big_box = Box('Big box')
    big_box.add(box_of_shirts)
    big_box.add(box_of_smartphones)
    big_box.print_content()

    print('')

    print(big_box.get_price())

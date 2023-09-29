from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.5


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 2.0


@dataclass
class Cheese(Ingredient):
    price: float = 4.29


@dataclass
class MashedPotato(Ingredient):
    price: float = 5.80


@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.99


class Hotdog:
    _name: str
    _ingredients: list[Ingredient]

    @property
    def price(self) -> float:
        return round(
            sum([ingredient.price for ingredient in self.ingredients]),
            2,
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> list[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price}) -> {self.ingredients}'


class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'Simple Hotdog'
        self._ingredients = [
            Bread(),
            Sausage(),
            PotatoSticks(),
        ]


class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'Special Hotdog'
        self._ingredients = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            PotatoSticks(),
            MashedPotato(),
            Cheese(),
        ]


# Dynamic Decorator
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog

        self._ingredient = ingredient
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> list[Ingredient]:
        return self._ingredients


if __name__ == '__main__':
    simple_hotdog = SimpleHotdog()
    print(simple_hotdog)
    print('')

    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())
    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())
    print(egg_bacon_simple_hotdog)

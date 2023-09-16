"""
    Template Method
     - Defines the skeleton of an algorithm in the superclass but lets
     subclasses override specific steps of the algorithm without changing its
     structure.
"""

from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self) -> None:
        """Template method"""
        self.hook_before_add_ingredients()
        self.add_ingredients()
        self.hook_after_add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: cutting')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: serving')

    def hook_before_add_ingredients(self) -> None: pass

    def hook_after_add_ingredients(self) -> None: pass

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class Margherita(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: checking expiry dates')

    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: adding tomatoes, olive oil, '
              f'mozzarella')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: cooking for 2min in oven')


class Hawaiian(Pizza):
    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: adding oregan, pineapple, ham, '
              f'mozzarella')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: cooking for 7min in oven')


if __name__ == '__main__':
    margherita = Margherita()
    margherita.prepare()

    print('')

    hawaiian = Hawaiian()
    hawaiian.prepare()

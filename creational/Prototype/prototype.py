"""
    Prototype
     - Lets you copy existing objects without making your code dependent on
     their classes.
"""

from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


class Person(StringReprMixin):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.addresses: list[Address] = []

    def add_address(self, address: Address):
        leo.addresses.append(address)

    def clone(self):
        return deepcopy(self)


if __name__ == '__main__':
    leo = Person('Leonardo', 'Reis')
    address_leo = Address('Av. Brasil', '250A')
    leo.add_address(address_leo)

    mom = leo.clone()
    mom.first_name = 'Vania'

    print(leo)
    print(mom)

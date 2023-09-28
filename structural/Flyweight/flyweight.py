"""
    Flyweight
     - Lets you fit more objects into the available amount of RAM by sharing
     common parts of state between multiple objects instead of keeping all of
     the data in each object.
"""

from __future__ import annotations


class Customer:
    """Context"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: list = []

        # extrinsic address data
        self.address_number: str
        self.address_complement: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(
                self.address_number,
                self.address_complement
            )


class Address:
    """Flyweight"""

    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(
            self, address_number: str, address_complement: str
    ) -> None:
        print(
            self._street, address_number, self._neighborhood,
            address_complement, self._zip_code
        )


class AddressFactory:
    _addresses: dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Address found!')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Address created!')

        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()
    a1 = address_factory.get_address(
        street='Av. Brasil',
        neighborhood='Downtown',
        zip_code='111222-000'
    )

    a2 = address_factory.get_address(
        street='Av. Brasil',
        neighborhood='Downtown',
        zip_code='111222-000'
    )

    print('')

    leo = Customer('Leonardo')
    leo.address_number = '450'
    leo.address_complement = 'Flat 3'
    leo.add_address(a1)
    leo.list_addresses()

    print('')

    fernando = Customer('Fernando')
    fernando.address_number = '231'
    fernando.address_complement = 'Flat 1'
    fernando.add_address(a2)
    fernando.list_addresses()

    print('')

    print(a1 == a2)

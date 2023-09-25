"""
    Proxy
     - Lets you provide a substitute or placeholder for another object. A proxy
     controls access to the original object, allowing you to perform something
     either before or after the request gets through to the original object.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep


class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> list[dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> dict: pass


class User(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # simulating a request
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> list[dict]:
        sleep(2)  # simulating a request
        return [
            {'street': 'Av. Brasil', 'number': 500},
        ]

    def get_all_user_data(self) -> dict:
        sleep(2)  # simulating a request
        return {
            'cpf': '111.111.111-11',
            'rg': 'AB11222333'
        }


class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._user: User  # lazy instantiation

        self._cached_addresses: list[dict]  # lazy instantiation
        self._all_user_data: dict  # lazy instantiation

    def get_user(self) -> None:
        if not hasattr(self, '_user'):
            self._user = User(self.firstname, self.firstname)

    def get_addresses(self) -> list[dict]:
        self.get_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> dict:
        self.get_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._user.get_all_user_data()

        return self._all_user_data


if __name__ == '__main__':
    leo = UserProxy('Leonardo', 'Reis')

    print(leo.firstname)
    print(leo.lastname)
    print('')

    # takes 6 sec
    print(leo.get_all_user_data())
    print(leo.get_addresses())
    print('')

    # respond instantaneously
    print('CACHED DATA:')
    print(leo.get_all_user_data())
    print(leo.get_addresses())

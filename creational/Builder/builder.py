"""
    Builder
     - Lets you construct complex objects step by step. The pattern allows you 
     to produce different types and representations of an object using the same 
     construction code.
"""

from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None
        self.age = None
        self.phones: list = []
        self.addresses: list = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_first_name(self, first_name): pass

    @abstractmethod
    def add_last_name(self, last_name): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_address(self, address): pass


class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        data = self._result
        self.reset()
        return data

    def add_first_name(self, first_name):
        self._result.first_name = first_name
        return self

    def add_last_name(self, last_name):
        self._result.last_name = last_name
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone):
        self._result.phones.append(phone)
        return self

    def add_address(self, address):
        self._result.addresses.append(address)
        return self


class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder

    def with_age(self, first_name, last_name, age):
        self._builder.add_first_name(first_name) \
            .add_last_name(last_name) \
            .add_age(age)
        return self._builder.result

    def with_address(self, first_name, last_name, address):
        self._builder.add_first_name(first_name) \
            .add_last_name(last_name) \
            .add_address(address)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Leonardo', 'Reis', 20)
    print(user1)

    user2 = user_director.with_address('Leonardo', 'Reis', 'Brazil, 30 Street')
    print(user2)

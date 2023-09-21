"""
    Mediator
     - Lets you reduce chaotic dependencies between objects. The pattern
     restricts direct communications between the objects and forces them to
     collaborate only via a mediator object.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Colleague(ABC):
    def __init__(self) -> None:
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    @abstractmethod
    def direct(self, msg: str) -> None: pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None: pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None: pass


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.colleagues: list[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return

        print(f'{colleague.name} broadcasted: {msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: list[Colleague] = [
            collaegue for collaegue in self.colleagues
            if collaegue.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} to {receiver_obj[0].name}: {msg}'
        )


if __name__ == '__main__':
    chat = ChatRoom()

    leo = Person('Leonardo', chat)
    vania = Person('Vania', chat)
    fernando = Person('Fernando', chat)
    pedro = Person('Pedro', chat)
    babi = Person('Barbara', chat)

    chat.add(leo)
    chat.add(vania)
    chat.add(fernando)
    chat.add(pedro)

    fernando.broadcast('Hello world!')
    vania.broadcast('Helloo! XD')
    babi.broadcast('Anyone here??')

    print('')

    leo.send_direct('Vania', 'How is Nala today?')
    vania.send_direct('Leonardo', 'As always... messing around XD')

"""
    Chain Of Responsibility - COR
     - Lets you pass requests along a chain of handlers. Upon receiving a
     request, each handler decides either to process the request or to pass
     it to the next handler in the chain.
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.successor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters = 'A', 'B', 'C'
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{self.__class__.__name__}: handled {letter}'
        return self.successor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters = 'D', 'E', 'F'
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{self.__class__.__name__}: handled {letter}'
        return self.successor.handle(letter)


class HandlerUnhandled(Handler):
    def handle(self, letter: str) -> str:
        return f'{self.__class__.__name__}: unhandled {letter}'


if __name__ == '__main__':
    handler_unsolved = HandlerUnhandled()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))
    print(handler_abc.handle('I'))

"""
    Iterator
     - Lets you traverse elements of a collection without exposing its
     underlying representation (list, stack, tree, etc.).
"""

from collections.abc import Iterator, Iterable


class MyIterator(Iterator):
    def __init__(self, collection: list) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
        except IndexError:
            raise StopIteration

        return item


class MyIteratorReverse(Iterator):
    def __init__(self, collection: list) -> None:
        self._collection = collection
        self._index = -1

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
        except IndexError:
            raise StopIteration

        return item


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: list = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iter(self) -> Iterator:
        return MyIteratorReverse(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == '__main__':
    mylist = MyList()
    mylist.add('Leonardo')
    mylist.add('Vania')
    mylist.add('Fernando')

    print(f'{mylist}\n')

    for value in mylist:
        print(value)

    print('')
    for value in mylist.reverse_iter():
        print(value)

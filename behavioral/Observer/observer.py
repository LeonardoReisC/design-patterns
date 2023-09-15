"""
    Observer
     - Lets you define a subscription mechanism to notify multiple
     objects(Observers) about any events that happen to the object they're
     observing(Observable).
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class IObservable(ABC):
    """Observable"""

    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


class WeatherStation(IObservable):
    """Observable"""

    def __init__(self) -> None:
        self._observers: list[IObserver] = []
        self._state: dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: dict) -> None:
        new_state: dict = {**self._state, **state_update}

        if new_state != self.state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} the object {observable_name} '
              f'has just been updated -> {self.observable.state}')


class Notebook(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def show(self):
        state = self.observable.state

        print(f'{self.name} updated data -> {state}')

    def update(self) -> None:
        self.show()


if __name__ == '__main__':
    weather_station = WeatherStation()
    smartphone1 = Smartphone('iPhone 15', weather_station)
    smartphone2 = Smartphone('S23', weather_station)
    notebook = Notebook('Dell G715', weather_station)

    weather_station.add_observer(smartphone1)
    weather_station.add_observer(smartphone2)
    weather_station.add_observer(notebook)

    weather_station.state = {'temperature': '25', }
    print('')
    weather_station.state = {'humidity': '89', }
    print('')

    weather_station.remove_observer(smartphone2)
    weather_station.reset_state()

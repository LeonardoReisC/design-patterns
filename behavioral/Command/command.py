"""
    Command
     - Turns a request into a stand-alone object that contains all information
     about the request. This transformation lets you pass requests as a method
     arguments, delay or queue a request's execution, and support undoable
     operations.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Light:
    """Receiver"""

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'default'

    def on(self) -> None:
        print(f'Light {self.name} in {self.room_name} is now ON')

    def off(self) -> None:
        print(f'Light {self.name} in {self.room_name} is now OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'Light {self.name} in {self.room_name} is now {self.color}')


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOn(ICommand):
    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColor(ICommand):
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    """Invoker"""

    def __init__(self) -> None:
        self._buttons: dict[str, ICommand] = {}
        self._undos: list[tuple[str, str]] = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_activate(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))

    def button_deactivate(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self._undos:
            print('Empty history')
            return None

        button_name, action = self._undos.pop()

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()


if __name__ == '__main__':
    bedroom_light = Light('LED', 'bedroom')
    bathroom_light = Light('LED', 'bathroom')

    bedroom_light_on = LightOn(bedroom_light)
    bathroom_light_on = LightOn(bathroom_light)

    bedroom_light_blue = LightChangeColor(bedroom_light, 'blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'red')

    remote = RemoteController()

    remote.button_add_command('bedroom light', bedroom_light_on)
    remote.button_add_command('bathroom light', bathroom_light_on)
    remote.button_add_command('bedroom light blue', bedroom_light_blue)
    remote.button_add_command('bedroom light red', bedroom_light_red)

    remote.button_activate('bedroom light')
    remote.button_activate('bathroom light')
    remote.button_activate('bedroom light blue')
    remote.button_activate('bedroom light red')
    print('')

    remote.button_deactivate('bedroom light')
    remote.button_deactivate('bathroom light')
    remote.button_deactivate('bedroom light red')
    remote.button_deactivate('bedroom light blue')
    print('')

    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()

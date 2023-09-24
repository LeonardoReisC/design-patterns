"""
    Adapter
     - Allows objects with incompatible interfaces to collaborate.
"""
from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


class Control(IControl):
    def top(self) -> None:
        print('moving top...')

    def down(self) -> None:
        print('moving down...')

    def right(self) -> None:
        print('moving right...')

    def left(self) -> None:
        print('moving left...')


class NewControl:
    def move_top(self) -> None:
        print('moving top...')

    def move_down(self) -> None:
        print('moving down...')

    def move_right(self) -> None:
        print('moving right...')

    def move_left(self) -> None:
        print('moving left...')


class ControlAdapter:
    """Adapter Object"""

    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def down(self) -> None:
        self.new_control.move_down()

    def right(self) -> None:
        self.new_control.move_right()

    def left(self) -> None:
        self.new_control.move_left()


class ControlAdapter2(Control, NewControl):
    """Adapter Class"""

    def top(self) -> None:
        self.move_top()

    def down(self) -> None:
        self.move_down()

    def right(self) -> None:
        self.move_right()

    def left(self) -> None:
        self.move_left()


if __name__ == '__main__':
    # Control - Adapter object
    new_control = NewControl()
    control_obj = ControlAdapter(new_control)

    control_obj.top()
    control_obj.down()
    control_obj.right()
    control_obj.left()

    print('')

    # Control - Adapter class
    control_class = ControlAdapter2()
    control_class.top()
    control_class.down()
    control_class.right()
    control_class.left()

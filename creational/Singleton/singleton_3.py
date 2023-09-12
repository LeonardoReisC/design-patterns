# using a metaclass
class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.theme = 'Dark'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.theme = 'Light'

    as2 = AppSettings()

    print(as1.theme)
    print(as2.theme)

# using a class decorator

def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class()
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


@singleton
class Test:
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()
    print(as1)
    print(as2)

    t1 = Test()
    t2 = Test()
    print(t1 == t2)

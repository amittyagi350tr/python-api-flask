#a py file can be used in 2 ways:
    #a) to execute something

    #MODULE IS MADE FOR SECOND REASON!
    #b) it could act as a source of ready-made functionalities for others to import


def square(number : int) -> int:
    return number * number


__version__ = "1.0.0"


class DataGenerator:

    def __init__(self, counter) -> None:
        self.counter_limit = counter
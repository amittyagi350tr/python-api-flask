__version__ = "1.0.0"

def display_greeting(name : str, msg: str)->None:
    print(f"Hello, {name}. {msg}")


def display_pretty_print(msg: str)->None:
    print("######################")
    print(msg)
    print("######################")

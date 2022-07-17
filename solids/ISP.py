from abc import ABC, abstractmethod

"""
Many client-specific interfaces are better than one general-purpose interface


In the contest of classes, an interface is considered,
all the methods and properties “exposed”,
thus, everything that a user can interact with that belongs to that class.
"""


class Walker(ABC):
    @abstractmethod
    def walk() -> bool:
        return print("can walk")


class Swimmer(ABC):
    @abstractmethod
    def swim() -> bool:
        return print("can swim")


class Man(Walker, Swimmer):
    def walk():
        return print("man can walk")

    def swim():
        return print("man can swim")


class Fish(Swimmer):
    def swim():
        return print("fish can swim")


if __name__ == "__main__":
    Man.swim()
    Man.walk()

    Fish.swim()

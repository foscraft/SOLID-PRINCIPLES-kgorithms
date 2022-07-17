"""
The Single-responsibility principle (SRP)
"""


from typing import Any


class SSR:
    def __init__(self) -> None:
        self.__name = None
        self.__age = None
        self.__height = None
        self.__weight = None

    def set_name(self, name: Any) -> None:
        self.__name = name

    def set_age(self, age: Any) -> None:
        self.__age = age

    def set_height(self, height: Any) -> None:
        self.__height = height

    def set_weight(self, weight: Any) -> None:
        self.__weight = weight

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_height(self) -> Any:
        return self.__height

    def get_weight(self) -> Any:
        return self.__weight

    def __str__(self) -> str:
        return f"Name: {self.__name}, Age: {self.__age}, Height: {self.__height}, Weight: {self.__weight}"


class Main:
    def __init__(self) -> None:
        self.ssr = SSR()

    def run(self) -> Any:
        self.ssr.set_name("John")
        self.ssr.set_age(20)
        self.ssr.set_height(1.75)
        self.ssr.set_weight(75)
        print(self.ssr)


if __name__ == "__main__":
    Main().run()

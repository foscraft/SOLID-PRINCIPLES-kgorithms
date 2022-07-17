from abc import ABC, abstractmethod
from typing import Any

import numpy as np

"""
The Open–closed principle (OCP)


If now we want to add a new operation e.g.: median, we will
only need to add a class “Median” inheriting from the class “Operations”.
The newly formed sub-class will be immediately picked up by __subclasses__()
and no modification in any other part of the code needs to happen.
"""


class OpenClosedPrinciple(ABC):
    @abstractmethod
    def operations() -> Any:
        pass


class Mean(OpenClosedPrinciple):
    def operation(self) -> Any:
        return np.mean(self)


class Median(OpenClosedPrinciple):
    def operation(self) -> Any:
        return np.median(self)


class Max(OpenClosedPrinciple):
    def operation(self) -> Any:
        return np.max(self)


class Main:
    @abstractmethod
    def get_operations(self) -> None:
        for operation in OpenClosedPrinciple.__subclasses__():
            return print(operation.operation(self))  # type: ignore[attr-defined]


if __name__ == "__main__":
    Main.get_operations([56, 7, 88, 90, 2, 344, 56, 78, 99, 100])  # type: ignore[arg-type]

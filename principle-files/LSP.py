from abc import ABC, abstractmethod




class LiskovSubstitutionPrincipleBase(ABC):
"""
The Liskov substitution principle (LSP)
"""

"""
Functions that use pointers or references to base
classes must be able to use objects of derived
classes without knowing it

!TODO
n (maybe) simpler words, if a subclass redefines a function also present in the parent class,
a client-user should not be noticing any difference in behaviour, and it is a substitute for the base class.
For example, if you are using a function and your colleague change the base class,
you should not notice any difference in the function that you are using.

Among all the SOLID principle, this is the most abstruse to understand and to explain.
For this principle, there is no standard “template-like” solution where it must be applied,
and it is hard to offer a “standard example” to showcase.
"""
    @abstractmethod
    def operation(self) -> bool:
        pass


class LiskovSubstitutionPrinciple(LiskovSubstitutionPrincipleBase):
    def operation(self) -> bool:
        return "LiskovSubstitutionPrincipleBase"


class LiskovSubstitutionPrincipleDerived(LiskovSubstitutionPrincipleBase):
    def operation(self) -> bool:
        return "LiskovSubstitutionPrincipleDerived"


class Main:
    def get_operations(self) -> None:
        for operation in LiskovSubstitutionPrincipleBase.__subclasses__():
            print(operation.operation())  # type: ignore[call-arg]


if __name__ == "__main__":
    Main().get_operations()

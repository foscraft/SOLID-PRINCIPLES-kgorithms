'''
 The Dependency Inversion Principle (DIP)

 Abstractions should not depend on details. 
 Details should depend on abstraction. 
 High-level modules should not depend on low-level modules. 
 Both should depend on abstractions

 !TODO
 Taking an example of a PageLoader class that uses a MySqlConnection class
  to load pages from a database we might create the classes so that the 
  connection class is passed to the constructor of the PageLoader class.

!TODO
This structure means that we are essentially stuck with using MySQL for our database layer. 
What happens if we want to swap this out for a different database adaptor? 
We could extend the MySqlConnection class in order to create a connection to Memcache or something, 
but that would contravene the Liskov Substitution principle. 
Chances are that alternate database managers might be used to load the pages so we need to find a way to do this.

The solution here is to create an interface called DbConnectionInterface and then implement this interface in 
the MySqlConnection class. Then, instead of relying on a MySqlConnection object being passed to the PageLoader 
class, we instead rely on any class that implements the DbConnectionInterface interface
'''

from re import sub
from subprocess import call
from typing import Any


class DbConnectionMeta(type):
    def __instancecheck__(self, __instance: Any) -> bool:
        return self.__subclasscheck__(type(__instance))

    def __subclasscheck__(self, __subclass: type) -> bool:
        return (hasattr(__subclass, 'connect') and call(__subclass.connect))

class DbConnectionInterface(metaclass=DbConnectionMeta):
    pass

class MysqlConnection(DbConnectionInterface):
    def connect(self) -> bool:
        pass

class MemCacheConnection(DbConnectionInterface):
    def connect(self) -> bool:
        pass
        
class PageLoader():
    def __init__(self, db_connection: DbConnectionInterface):
        self.db_connection = db_connection

    def load_page(self, url: str) -> str:
        return self.db_connection.connect() 
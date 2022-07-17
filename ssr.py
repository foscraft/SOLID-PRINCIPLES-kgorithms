'''
The Single-responsibility principle (SRP)
'''

class SSR:
    def __init__(self):
        self.__name = None
        self.__age = None
        self.__height = None
        self.__weight = None

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}, Height: {self.__height}, Weight: {self.__weight}'

class Main:
    def __init__(self):
        self.ssr = SSR()

    def run(self):
        self.ssr.set_name('John')
        self.ssr.set_age(20)
        self.ssr.set_height(1.75)
        self.ssr.set_weight(75)
        print(self.ssr)


if __name__ == '__main__':
    Main().run()
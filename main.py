#!/usr/bin/python3
"""
    Creating Class Objects
"""
class animals:
    """
        General Class
    """
    def __init__(self, name="", species="", age=0):
        self.name = name
        self.species = species
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def setname(self, value):
        if type(value) is not str:
            raise TypeError("Name must be a string")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def setspecies(self, value):
        if type(value) is not str:
            raise TypeError("Species must be a string")
        self.__species = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def setage(self, value):
        if type(value) is not int:
            raise TypeError("Age must be an int")
        if value <= 0:
            raise ValueError("Age must be bigger than cero")
        self.__age = value

    def move(self, position=""):
        if type(position) is not str:
            raise TypeError("Position must be a string")
        print(f"Direction: {position}")

    def show(self):
        print(f"I'm {self.__name}")
        print(f"My Specie is: {self.__species}")
        print(f"I'm {self.__age} years old")

    def sound(self, sound=""):
        if type(sound) is not str:
            raise TypeError("Sound must be a string")
        print(f"My sound is: {sound}")

    """
    Subclass terrestrial animals
    """
    def terrestrial_animal(animals):
        """
        this is subclass
        """
        def __init__(self, name="", species="", age=0):
            animals.__init__(self, name="", species="", age=0)

        def move(self, position=""):
            animals.move(self, position="")
            if type(position) is not str:
                raise TypeError("Position must be a string")
            print(f"Movement: {position}")

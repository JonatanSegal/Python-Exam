class Person:

    def __init__(self, name:str, age:int) :
        self.name = name #self.name is now the setter @name.setter
        self.age = age

    @property
    def name(self):
        return self.__name #Private variable

    @name.setter
    def name(self, value:str):
        self.__name = value
        


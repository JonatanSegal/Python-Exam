class Fruit:
    def __init__(self, name: str):
        self.__name = name
    
    def get_name(self):
        print("Getting fruit name")
        return self.__name

    def set_name(self, new_name:str):
        print("Setting new name")
        self.__name = new_name




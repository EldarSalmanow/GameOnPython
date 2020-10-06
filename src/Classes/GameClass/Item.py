from src.Classes.GameClass.GameItems import Types


# класс элемента для использования игроком
class Item:
    # конструктор для оружия
    def __init__(self, typeOfWeapon):
        self.__itemType = Types.WEAPON
        self.__typeOfWeapon = typeOfWeapon

    # конструктор для всяких расходников
    def __init(self, typeOfСonsumable, col):
        self.__itemType = Types.CONSUMABLE
        self.__typeOfСonsumable = typeOfСonsumable
        self.__col = col

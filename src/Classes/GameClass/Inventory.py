# класс инвентаря игрока
class Inventory:
    def __init__(self):
        self.__size = 5
        self.__items = []

    # def addItem(self, type, subtype, col=0):
    #     if type in Types:
    #         typeOfItem = Types.CONSUMABLES
    #     else:
    #         raise GameTypeException("Типа '" + type + "' не существует!")

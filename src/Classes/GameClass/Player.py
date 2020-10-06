from src.Classes.GameClass.Inventory import Inventory
from src.Classes.GameClass.GameObject import GameObject


# класс игрока
class Player(GameObject):
    def __init__(self, name):
        super().__init__(0, 0, 100, 15)
        self.__name = name
        self.__inventory = Inventory()

    def inp_com(self, commandFromPlayer):
        move_com = ['w', 's', 'a', 'd']
        if commandFromPlayer in move_com:
            self.__move(commandFromPlayer)
        else:
            print(f"Команды {commandFromPlayer} не существует!")
            print("Список доступных команд: " + str(move_com))

    def __move(self, commandPlayer):
        if commandPlayer == 'w':
            self.x += 1
        elif commandPlayer == 's':
            self.x -= 1
        elif commandPlayer == 'a':
            self.y += 1
        elif commandPlayer == 'd':
            self.y -= 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

from src.Classes.GameClass.GameObject import GameObject


# класс врага
class Enemy(GameObject):
    def __init__(self, x, y, level):
        super().__init__(x, y, 0, 0)
        self.__level = level
        self.__initLevel()

    def __initLevel(self):
        if self.__level == 1:
            self.health = 40
            self.attack = 10
        elif self.__level == 2:
            self.health = 60
            self.attack = 15
        elif self.__level == 3:
            self.health = 80
            self.attack = 20

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

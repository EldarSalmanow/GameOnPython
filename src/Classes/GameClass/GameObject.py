# шаблон класса для создания класса игрока и врага
class GameObject:
    def __init__(self, x, y, health, attack):
        self.__x = x
        self.__y = y
        self.__health = health
        self.__attack = attack
        self.__flag = True

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, flag):
        self.__flag = flag

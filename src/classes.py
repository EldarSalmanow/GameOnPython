# шаблон класса для создания класса игрока и врага
class GameObject:
    def __init__(self, x, y, health, attack):
        self.__x = x
        self.__y = y
        self.__health = health
        self.__attack = attack
        self.__flag = 'notNull'

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


# класс игрока
class Player(GameObject):
    def __init__(self, name):
        super().__init__(0, 0, 100, 15)
        self.__name = name

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

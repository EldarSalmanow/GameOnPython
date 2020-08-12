# шаблон класса для создания класса игрока и врага
class GameObject:
    def __init__(self, x, y, health, attack):
        self.__x = x
        self.__y = y
        self.__health = health
        self.__attack = attack

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


# класс игрока
class Player(GameObject):
    def __init__(self, name):
        super().__init__(x=0, y=0, health=100, attack=15)
        self.__name = name

    def inp_com(self):
        move_com = ['вперёд', 'назад', 'вниз', 'вверх']
        command = str(input("Введите команду для игрока: "))
        if command in move_com:
            self.move(command)
        else:
            print(f"Команды {command} не существует!")

    def move(self, command):
        if command == 'вперёд':
            self.__x += 1
        elif command == 'назад':
            self.__x -= 1
        elif command == 'вверх':
            self.__y += 1
        elif command == 'вниз':
            self.__y -= 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


# класс врага
class Enemy(GameObject):
    def __init__(self, x, y, level):
        super().__init__(x, y, health=0, attack=0)
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

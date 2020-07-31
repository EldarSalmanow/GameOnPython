# шаблон класса для создания класса игрока и врага
class GameObject:
    def __init__(self, x, y, health, attack):
        self.x = x
        self.y = y
        self.health = health
        self.attack = attack


# класс игрока
class Player(GameObject):
    def __init__(self, name):
        super().__init__(x=0, y=0, health=100, attack=15)
        self.name = name

    def inp_com(self):
        move_com = ['вперёд', 'назад', 'вниз', 'вверх']
        command = str(input("Введите команду для игрока: "))
        if command in move_com:
            self.move(command)
        else:
            print(f"Команды {command} не существует!")

    def move(self, command):
        if command == 'вперёд':
            self.x += 1
        elif command == 'назад':
            self.x -= 1
        elif command == 'вверх':
            self.y += 1
        elif command == 'вниз':
            self.y -= 1


# класс врага
class Enemy(GameObject):
    def __init__(self, x, y, health, attack):
        super().__init__(x, y, health, attack)

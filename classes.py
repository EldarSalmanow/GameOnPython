# создаём класс для игрока
class player:
    def __init__(self, name, x=0, y=0, health=100):
        self.name = name
        self.x = x
        self.y = y
        self.health = health

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def inp_com(self, com):
        move_com = ['вперёд', 'назад', 'вниз', 'вверх']
        attack_com = ['атака']
        if com in move_com:
            self.move(com)
        elif com in attack_com:
            self.attack()
        else:
            print(f"Команды {com} не существует!")

    def move(self, com):
        if com == 'вперёд':
            self.x += 1
        elif com == 'назад':
            self.x -= 1
        elif com == 'вверх':
            self.y += 1
        elif com == 'вниз':
            self.y -= 1
        self.print_pos()

    def attack(self):
        pass

    def print_pos(self):
        print(f"Игрок {self.name} передвинулся на позицию {self.x, self.y}.")


class enemy:
    def __init__(self, health, attack_enemy, cord_x, cord_y):
        self.health = health
        self.attack_enemy = attack_enemy
        self.cord_x = cord_x
        self.cord_y = cord_y

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

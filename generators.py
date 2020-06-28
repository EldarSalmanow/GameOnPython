from classes import player, enemy
import random


class generators:
    # параметры для регистрации игроков(players)
    col_players = 1
    dct_players = {}
    lst_players_name = []
    # параметры для создания врагов(enemies)
    col_enemies = random.randint(2, 5)
    dct_params_enemies = {}
    lst_params_enemy = []

    def __init__(self, class_generator):
        self.class_generator = class_generator

    def init_class(self):
        if self.class_generator == 'player':
            self.reg_players()
        elif self.class_generator == 'enemy':
            self.generator_enemies()

    def reg_players(self):
        self.col_players = int(input("Введите количество игроков: "))
        for i in range(1, self.col_players + 1):
            name = str(input(f"Введите имя для {i} игрока: "))
            self.lst_players_name.append(name)
            self.dct_players[i] = name
            self.dct_players[i] = player(self.dct_players[i])
            print(f"Игрок с именем {name} успешно создан!")

    def generator_enemies(self):
        for i in range(1, self.col_enemies + 1):
            health = random.randint(20, 40)
            attack_enemy = random.randint(15, 25)
            cord_x = random.randint(-10, 10)
            cord_y = random.randint(-10, 10)
            self.lst_params_enemy.append(health)
            self.lst_params_enemy.append(attack_enemy)
            self.lst_params_enemy.append(cord_x)
            self.lst_params_enemy.append(cord_y)
            self.dct_params_enemies[i] = self.lst_params_enemy
            self.dct_params_enemies[i] = enemy(self.lst_params_enemy[0], self.lst_params_enemy[1],
                                               self.lst_params_enemy[2], self.lst_params_enemy[3])

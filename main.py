# импортируем класс generators(класс, для создания врагов и регистрации игроков)
from generators import generators
from supportClass import supportClass

# созадём генератор врагов(enemies)
obj_enemy = generators('enemy')
obj_enemy.init_class()
# создаём регистратор игроков(players)
obj_player = generators('player')
obj_player.init_class()

# переменная для начала и завершения главного цикла игры
game = 1
# главный цикл игры
while game == 1:
    # цикл для задания очерёдности игроков
    for n in range(1, obj_player.col_players + 1):
        # приём команды для определённого игрока
        com = str(input(f"Введите команду для игрока {obj_player.lst_players_name[n - 1]}: "))
        # уменьшение команды на случай, если игрок напишет большие буквы
        com.lower()
        # проверка на конец игры
        if com == 'конец':
            # уведомление игроков о том, что игра закончена
            print("Игра завершена!")
            # изменение переменной game на 0, чтобы закончить игру
            game = 0
            # прерывание цикла
            break
        # передача команды, введённой игроком, к обьекту игрока
        obj_player.dct_players[n].inp_com(com)
        # цикл проверки соприкосновения координат игрока с координатами одного из врагов
        for i in range(1, obj_enemy.col_enemies + 1):
            support = supportClass(obj_player.dct_players[n].x, obj_player.dct_players[n].y)
            status = support.checkCord(obj_enemy.dct_params_enemies[i].cord_x, obj_enemy.dct_params_enemies[i].cord_y)
            if status == "Yes":
                lst_dct = support.attack(obj_player.dct_players, obj_enemy.dct_params_enemies, n, i)
                obj_enemy.dct_params_enemies = lst_dct[1]
                obj_player.dct_players = lst_dct[0]
            else:
                continue

        if obj_player.dct_players == {}:
            print("Вы проиграли! Игра окончена!")
            game = 0
            break
        elif obj_enemy.dct_params_enemies == {}:
            print("Вы выиграли! Игра окончена!")
            game = 0
            break

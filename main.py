# импортируем класс generators(класс, для создания врагов и регистрации игроков)
from generators import generators

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
    for n in range(0, obj_player.col_players):
        # приём команды для определённого игрока
        com = str(input(f"Введите команду для игрока {obj_player.lst_players_name[n]}: "))
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
        obj_player.dct_players[n + 1].inp_com(com)

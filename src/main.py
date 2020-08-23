# импорт генераторов
from src.generators import genPlayers, genEnemies

# импорт функции атаки
from src.supportFuncs import attack

# регистрация игроков
players = genPlayers()

# генерация врагов
enemies = genEnemies()

# статус игры
statusGame = True

# итерация цикла игры
iteration = 0

# главный цикл игры
while statusGame:
    iteration += 1
    # игровой процесс
    for step in range(0, len(players)):
        command = str(input(f"Введите команду для игрока {players[step].name}: "))
        players[step].inp_com()
        # проверка на совпадение координат игрока и врага
        for colEnemy in range(0, len(enemies)):
            if players[step].x == enemies[colEnemy].x and players[step].y == enemies[colEnemy].y:
                attack(players[step], enemies[colEnemy])
    # вопрос для игроков о том, закончить ли игру досрочно
    if iteration % 7 == 0:
        commandGame = int(input("Если хотите закончить игру, напишите '0', если продолжить, напишите '1': "))
        if commandGame == 0:
            statusGame = False
            print("Игра окончена!")
        else:
            continue

# импорт генераторов
from src.generators import genPlayers, genEnemies

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
    # вопрос для игроков о том, закончить ли игру досрочно
    if iteration % 7 == 0:
        commandGame = int(input("Если хотите закончить игру, напишите '0', если продолжить, напишите '1': "))
        if commandGame == 0:
            statusGame = False
            print("Игра окончена!")
        else:
            continue

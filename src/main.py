# импорт генераторов
from src.generators import genPlayers, genEnemies

# импорт функции атаки
from src.supportFuncs import attack

# импорт доп. модулей
import time

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
    for step in range(0, len(players)):
        if players[step] == 'null':
            continue
        command = str(input(f"Введите команду для игрока {players[step].name}: "))
        players[step].inp_com(command)
        # проверка на совпадение координат игрока и врага
        check = True
        colEnemy = 0
        while check:
            if enemies[colEnemy] == 'null':
                colEnemy += 1
                continue
            if players[step].x == enemies[colEnemy].x and players[step].y == enemies[colEnemy].y:
                check = False
                win = attack(players[step], enemies[colEnemy])
                if win == 'player':
                    enemies[colEnemy] = 'null'
                elif win == 'enemy':
                    players[step] = 'null'
            if colEnemy >= len(enemies) - 1:
                check = False
            colEnemy += 1
            if len(enemies) <= 0:
                print("Поздравляю!!!")
                time.sleep(2.0)
                print("Игра окончена! Игроки победили всех монстров!")
                time.sleep(2.0)
                print("Спсаибо, что сыграли в эту игру.")
                print("Ссылка на исходный код: https://github.com/EldarSalmanow/GameOnPython")
            elif len(players) <= 0:
                time.sleep(2.0)
                print("Увы, вы проиграли...")
                time.sleep(2.0)
                print("Монстры убили всех игроков...")
                time.sleep(2.0)
                print("Конец!!!")
                time.sleep(2.0)
                print("Спсаибо, что сыграли в эту игру.")
                print("Ссылка на исходный код: https://github.com/EldarSalmanow/GameOnPython")

    # вопрос для игроков о том, закончить ли игру досрочно
    if iteration % 7 == 0:
        commandGame = int(input("Если хотите закончить игру, напишите '0', если продолжить, напишите '1': "))
        if commandGame == 0:
            statusGame = False
            print("Игра окончена!")
        else:
            continue

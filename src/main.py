# импорт генераторов
from src.generators import genPlayers, genEnemies

# импорт функции атаки
from src.supportFuncs import attack

# импорт доп. модулей
import time


# проверка количества игроков и врагов
def checkColEnemiesAndPlayers():
    if len(enemies) <= 0:
        print("Поздравляю!!!")
        time.sleep(2.0)
        print("Игра окончена! Игроки победили всех монстров!")
        time.sleep(2.0)
        print("Спасибо, что сыграли в эту игру.")
        print("Ссылка на исходный код: https://github.com/EldarSalmanow/GameOnPython")
        return 'end'
    elif len(players) <= 0:
        time.sleep(2.0)
        print("Увы, вы проиграли...")
        time.sleep(2.0)
        print("Монстры убили всех игроков...")
        time.sleep(2.0)
        print("Конец!!!")
        time.sleep(2.0)
        print("Спасибо, что сыграли в эту игру.")
        print("Ссылка на исходный код: https://github.com/EldarSalmanow/GameOnPython")
        return 'end'
    return 'notEnd'


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
        # пропуск игроков помеченных флагом 'null'
        if players[step].flag == 'null':
            continue
        command = str(input(f"Введите команду для игрока {players[step].name}: "))
        players[step].inp_com(command)
        # проверка на совпадение координат игрока и врага
        check = True
        enemyIndex = 0
        while check:
            if enemies[enemyIndex].flag == 'null':
                enemyIndex += 1
                continue
            else:
                # если координаты врага и координаты игрока совпали, начать битву
                if players[step].x == enemies[enemyIndex].x and players[step].y == enemies[enemyIndex].y:
                    check = False
                    win = attack(players[step], enemies[enemyIndex])
                    # пометка флагом 'null' в зависимости от того, кто выиграл
                    if win == 'player':
                        enemies[enemyIndex].flag = 'null'
                    elif win == 'enemy':
                        players[step].flag = 'null'
                if enemyIndex >= len(enemies) - 1:
                    check = False
                enemyIndex += 1
                # проверка количества игроков и врагов
                status = checkColEnemiesAndPlayers()
                if status == 'end':
                    statusGame = False

    # вопрос для игроков о том, закончить ли игру досрочно
    if iteration % 7 == 0:
        commandGame = int(input("Если хотите закончить игру, напишите '0', если продолжить, напишите '1': "))
        if commandGame == 0:
            statusGame = False
            print("Игра окончена!")
        else:
            continue

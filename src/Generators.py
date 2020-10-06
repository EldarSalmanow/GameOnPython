# импорт классов игрока и врага
from src.Classes.GameClass.Player import Player
from src.Classes.GameClass.Enemy import Enemy

# импорт доп. модулей из стандартной библиотеки
import random


# регистраор игроков
def genPlayers():
    lstPlayers = []
    col = int(input("Введите количество игроков: "))
    if 1 <= col <= 5:
        for i in range(1, col + 1):
            name = str(input(f"Введите имя для {i} игрока: "))
            lstPlayers.append(Player(name))
        return lstPlayers


# генератор врагов
def genEnemies():
    lstEnemies = []
    colEnemies = random.randint(3, 7)
    # списки для проверки на совпадение координат при генерации
    xLst = []
    yLst = []
    # генерация
    enemy = True
    while enemy:
        x = random.randint(-15, 15)
        if x in xLst:
            continue
        xLst.append(x)
        y = random.randint(-15, 15)
        if y in yLst:
            continue
        yLst.append(y)
        level = random.randint(1, 3)
        lstEnemies.append(Enemy(x, y, level))
        if len(lstEnemies) == colEnemies:
            enemy = False
    return lstEnemies

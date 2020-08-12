# импорт классов игрока и врага
from src.classes import Player, Enemy

# импорт доп. модулей
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
    for col in range(1, colEnemies + 1):
        x = random.randint(-15, 15)
        y = random.randint(-15, 15)
        level = random.randint(1, 3)
        lstEnemies.append(Enemy(x, y, level))
    return lstEnemies

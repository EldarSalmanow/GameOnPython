from classes import Player, Enemy
import random


def genPlayers():
    lstPlayers = []
    col = int(input())
    if 1 <= col <= 5:
        for i in range(1, col + 1):
            name = str(input())
            lstPlayers.append(Player(name))
        return lstPlayers


def genEnemies():
    lstEnemies = []
    colEnemies = random.randint(3, 7)
    for col in range(1, colEnemies + 1):
        x = random.randint(-15, 15)
        y = random.randint(-15, 15)
        level = random.randint(1, 3)
        lstEnemies.append(Enemy(x, y, level))

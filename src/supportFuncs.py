from src.classes import Player, Enemy

# импорт доп. модулей
import time


# функция для создания битвы между игрокком и врагом
def attack(player, enemy):
    print(f"Игрок {player.name} был атакован монстром!\n"
          "Вот краткие характеристики монстра:\n"
          f"Уровень: {enemy.level}")
    battle = True
    while battle:
        step = True
        while step:
            player.health = player.health - enemy.attack
            time.sleep(2.0)
            print(f"Монстр атаковал игрока {player.name}! У него осталось {player.health} жизней!")
            if checkHealth(player):
                print(f"Битва окончена! Игрок {player.name} победил монстра!")
                battle = False
                break
            enemy.health = enemy.health - player.attack
            time.sleep(2.0)
            print(f"Игрок {player.name} атаковал монстра! У монстра осталось {enemy.health} жизней!")
            if checkHealth(enemy):
                print(f"Битва окончена! Монстр победил игрока {player.name}!")
                battle = False
                break
            step = False


def checkHealth(gameObject):
    if gameObject.health <= 0:
        return True
    else:
        return False


attack(Player('eldar'), Enemy(0, 0, 1))

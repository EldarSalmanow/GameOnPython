# import time
#
#
# class supportClass:
#     player_cord_x = 0
#     player_cord_y = 0
#
#     def __init__(self, player_x, player_y):
#         self.player_cord_x = player_x
#         self.player_cord_y = player_y
#
#     def checkCord(self, cord_enemy_x, cord_enemy_y):
#         if self.player_cord_x == cord_enemy_x and self.player_cord_y == cord_enemy_y:
#             return "Yes"
#         else:
#             return "No"
#
#     def attack(self, dct_players, dct_enemies, player_while, enemy_while):
#         lst_return = []
#         attack_player = 20
#         attack_enemy = dct_enemies[enemy_while].attack_enemy
#         print(f"Игрока {dct_players[player_while].name} атаковал монстр! Сейчас начнётся битва!")
#         status_attack = True
#         win = ''
#         time.sleep(3.0)
#         while status_attack:
#             dct_enemies[enemy_while].set_health(dct_enemies[enemy_while].health - attack_player)
#             if dct_enemies[enemy_while].health <= 0:
#                 win = 'player'
#                 break
#             dct_players[player_while].set_health(dct_players[player_while].health - attack_enemy)
#             if dct_players[player_while].health <= 0:
#                 win = 'enemy'
#                 break
#         if win == 'enemy':
#             print(f"Игрок {dct_players[player_while].name} програл! Он выбывает из игры!")
#             dct_players.pop(player_while)
#             print(dct_players)
#             lst_return.append(dct_players)
#             lst_return.append(dct_enemies)
#             return lst_return
#         elif win == 'player':
#             print(f"Игрок {dct_players[player_while].name} победил монстра! Поздравляем!")
#             dct_enemies.pop(enemy_while)
#             print(dct_players[player_while].health)
#             lst_return.append(dct_players)
#             lst_return.append(dct_enemies)
#             return lst_return

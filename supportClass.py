class supportClass:
    player_cord_x = 0
    player_cord_y = 0

    def __init__(self, player_x, player_y):
        self.player_cord_x = player_x
        self.player_cord_y = player_y

    def checkCord(self, cord_enemy_x, cord_enemy_y):
        if self.player_cord_x == cord_enemy_x and self.player_cord_y == cord_enemy_y:
            return "Yes"
        else:
            return "No"

    def __del__(self):
        print("Удаление экземпляра...")

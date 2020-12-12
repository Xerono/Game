from ClassFiles import Player
import Map


def new_player(name, x, y, direction):
    for obj in Map.Objects:
        if obj.clas == "Player":
            Tile = obj
    if obj:
        player = Player.Player(name, x, y, direction, obj)
    else:
        print("Error - No tile found for object 'Player'")
    return player
    

from ClassFiles import Player
from ClassFiles import Monsters
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
    
def new_monster(species, Level):
    for obj in Map.Objects:
        if obj.name == species:
            Tile = obj
    if Tile:
        Monster = Monsters.new_monster(species, Level, Tile)
    else:
        print("Error - No tile found for object '" + str(species) + "'")
    return Monster


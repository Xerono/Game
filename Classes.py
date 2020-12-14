from ClassFiles import Player
from ClassFiles import Monsters
import Map


def new_player(name, id, mapid, x, y, direction, journey):
    for obj in Map.Objects:
        if obj.clas == "Player":
            Tile = obj
    if obj:
        player = Player.Player(name, id, mapid, x, y, direction, obj, journey)
    else:
        print("Error - No tile found for object 'Player'")
    return player
    
def new_monster(species, Level):
    Tile = ""
    for obj in Map.Objects:
        if obj.name == species:
            Tile = obj
    if Tile:
        Monster = Monsters.new_monster(species, Level, Tile)
    else:
        print("Error - No tile found for object '" + str(species) + "'")
    return Monster

def catch_monster(Monster, Player, Nick, Loc, DT):
    cMonster = Monsters.caught(Monster, Player, Nick, Loc, DT)
    return cMonster

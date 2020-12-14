import Tile
import random
import pygame


Tiles = Tile.load_tiles()
Objects = Tile.load_objects()

Block_Size = 0
FieldSizeX = 0
FieldSizeY = 0

def create_random_map(Height, Width, Blocksize):
    global Block_Size
    global FieldSizeX
    global FieldSizeY
    Block_Size = Blocksize
    FieldSizeX = int(Height/Blocksize)
    FieldSizeY = int(Width/Blocksize)
    Field = []
    for x in range(FieldSizeX):
        Field.append([])
        for y in range(FieldSizeY):
            Field[x].append(y)
    for x in range(FieldSizeX):
        for y in range(FieldSizeY):    
            if random.random() <= 0.75:
                Field[x][y] = (Tiles[0], "")
            else:
                Field[x][y] = (Tiles[1], "")
    return Field

def print_map(Field):
    for y in range(FieldSizeY):
        for x in range(FieldSizeX):
            print(Field[x][y][0].desc, end = " ")
        print()


def set_player(Field, Player):
    x = Player.Position[0]
    y = Player.Position[1]
    for xc in range(FieldSizeX):
        for yc in range(FieldSizeY):
            if Field[xc][yc][0].desc == "P":
                print("Error - There already is a player on (" + str(xc) + ", " + str(yc) + ").")
                return Field
            if Field[xc][yc][0].passable:
                Possible_Passable = Field[xc][yc]
    # In case initial placement is on inpassable terrain
    if (not Field[x][y][0].passable):
            Field[x][y] = Possible_Passable
    for object_tile in Objects:
        if object_tile.name == "Player":
            Player.Last_Tile = Field[x][y]
            Field[x][y] = (object_tile, Player)
    return (Field, Player)


def draw_tile(Screen, x, y, Field):
    rect = pygame.Rect(x*Block_Size, y*Block_Size, Block_Size, Block_Size)
    pygame.draw.rect(Screen, Field[x][y][0].color, rect, 0)


def draw_map(Screen, Field):
    for x in range(FieldSizeX):
        for y in range(FieldSizeY):
            draw_tile(Screen, x, y, Field)
    pygame.display.update()

def set_monster(Field, x, y, Direction, Monster):
    if Field[x][y][0].passable:
        Monster.OldTile = Field[x][y]
        Monster.Position = (x,y)
        Monster.Direction = Direction
        Field[x][y] = (Monster.Tile, Monster)
    return Field
    
    

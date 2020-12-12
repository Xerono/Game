import Tile
import random
import pygame


Tiles = Tile.load_tiles()
Objects = Tile.load_objects()

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
                Field[x][y] = Tiles[0]
            else:
                Field[x][y] = Tiles[1]
    return Field

def print_map(Field):
    for y in range(FieldSizeY):
        for x in range(FieldSizeX):
            print(Field[x][y].desc, end = " ")
        print()


def set_player(Field,x,y):
    global Last_Tile
    for xc in range(FieldSizeX):
        for yc in range(FieldSizeY):
            if Field[xc][yc].desc == "P":
                print("Error - There already is a player on (" + str(xc) + ", " + str(yc) + ").")
                return Field
            if Field[xc][yc].passable:
                Possible_Passable = Field[xc][yc]
    # In case initial placement is on inpassible terrain
    if (not Field[x][y].passable):
            Field[x][y] = Possible_Passable
    for object_tile in Objects:
        if object_tile.name == "Player":
            Last_Tile = Field[x][y]
            Field[x][y] = object_tile
    return Field


def draw_tile(Screen, x, y, Field):
    rect = pygame.Rect(x*Block_Size, y*Block_Size, Block_Size, Block_Size)
    pygame.draw.rect(Screen, Field[x][y].color, rect, 0)


def draw_map(Screen, Field):
    for x in range(FieldSizeX):
        for y in range(FieldSizeY):
            draw_tile(Screen, x, y, Field)
    pygame.display.update()

def get_last_tile():
    return Last_Tile

def set_last_tile(tile):
    Last_Tile = tile
    
    

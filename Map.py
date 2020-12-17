import Tile
import random
import pygame
import os
import Classes

Tiles = Tile.load_tiles()
Objects = Tile.load_objects()

Mapfilesfolder = os.getcwd() + "/Maps/"

Block_Size = 0
FieldSizeX = 0
FieldSizeY = 0

def init_map(Height, Width, Blocksize):
    global Block_Size
    global FieldSizeX
    global FieldSizeY
    Block_Size = Blocksize
    FieldSizeX = int(Height/Blocksize)
    FieldSizeY = int(Width/Blocksize)

def create_random_map():
    Field = []
    for x in range(FieldSizeX):
        Field.append([])
        for y in range(FieldSizeY):
            Field[x].append(y)
    for x in range(FieldSizeX):
        for y in range(FieldSizeY):    
            if random.random() <= 0.75:
                Field[x][y] = (Tiles[0], None)
            else:
                Field[x][y] = (Tiles[1], None)
    return Field

def print_map(Field):
    for y in range(FieldSizeY):
        for x in range(FieldSizeX):
            print(Field[x][y][0].desc, end = " ")
        print()


def set_player(Field, Player, targetmapid, x, y):
    if Player.Current_Map == targetmapid:
        for xc in range(FieldSizeX):
            for yc in range(FieldSizeY):
                if Field[xc][yc][0].desc == "P":
                    print("Error - There already is a player on (" + str(xc) + ", " + str(yc) + ").")
                    return (Field, Player)
        for object_tile in Objects:
            if object_tile.name == "Player":
                Player.Last_Tile = Field[x][y]
                Player.Position = (x,y)
                Field[x][y] = (object_tile, Player)
        
    else:
        PlayerLoc = (x,y)
        Field = load_map(Player, PlayerLoc, targetmapid)
        Player.Current_Map = targetmapid
        (Field, Player) = set_player(Field, Player, targetmapid, x, y)
        
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

def set_portal(Field, x, y, tmid, tx, ty):
    if Field[x][y][0].passable:
        if Field[x][y][1] == None:
            Field[x][y] = (Field[x][y][0], ("Portal", tmid, tx, ty))
        else:
            print("Portalfield not empty")
    else:
        print("Portalfield not passable")
    return Field

def load_map(Player, PlayerLoc, mapid):
    Mapfiles = os.listdir(Mapfilesfolder)
    MapFound = False
    TargetMap = ""
    
    for mapfile in Mapfiles:
        split = mapfile.split(".")
        if len(split)>1:
            if split[1] == "map":
                try:
                    mid = int(split[0])
                    if mid == mapid:
                        MapFound = True
                        TargetMap = Mapfilesfolder + mapfile
                except:
                    print("Error in load_map: " + str(mapfile) + " has no map id as filename")
    Field = []
    for x in range(FieldSizeX):
        Field.append([])
        for y in range(FieldSizeY):
            Field[x].append(y)
    if MapFound:
        all_lines = []
        with open(TargetMap, "r") as mapfile:
            for line in mapfile.readlines():
                all_lines.append(line.rstrip())
        try:
            for y in range(FieldSizeY):
                line = all_lines[y].split("|")
                for x in range(FieldSizeX):
                    for tile in Tiles:
                        if tile.desc == line[x]:
                            Field[x][y] = (tile, None)
                    if not Field[x][y]:
                        print("Error in loading tile " + str(x) + str(y) + "(" + str(line[x]) + ") from mapid " + str(mapid))
                        Field[x][y] = False
            if len(all_lines)>FieldSizeY:
                Monsterlist = []
                for k in range(len(all_lines)-FieldSizeY):
                    CurLine = all_lines[FieldSizeY+k].split("|")
                    if len(CurLine)>=1:
                        Target = CurLine[0]
                        if Target == "M":
                            try:
                                # Unique:
                                # (Type, Species, Level, X, Y, Direction)
                                # Non-Unique:
                                # (Type, Species, LevelMin, LevelMax, Spawnchance)
                                mon = int(CurLine[1])
                                lvl = int(CurLine[2])
                                NewMon = Classes.new_monster(mon, lvl)
                                Monsterlist.append((NewMon, CurLine))    
                            except:
                                print("Malformed monster in Map file " + str(mapid))
                        if Target == "P":
                            # (Type, Portal_X, Portal_Y, NewMapID, NewX, NewY)
                            Field = set_portal(Field, int(CurLine[1])-1, int(CurLine[2])-1, int(CurLine[3]), int(CurLine[4])-1, int(CurLine[5])-1)
                for (NewMon, CurLine) in Monsterlist:
                    if NewMon.Unique == True:
                        if NewMon.MonsterID not in Player.Defeated_Monsters:
                            Field = set_monster(Field, int(CurLine[3])-1, int(CurLine[4])-1, CurLine[5], NewMon)
                    else:
                        dirs = ["Up", "Down", "Left", "Right"]
                        mon = int(CurLine[1])
                        for x in range(FieldSizeX):
                            for y in range(FieldSizeY):
                                if (x,y) != PlayerLoc:
                                    if Field[x][y][1] == None:
                                        SpawnChance = random.randint(0, 100)
                                        if SpawnChance < int(CurLine[4]):
                                            lvl = random.randint(int(CurLine[2]), int(CurLine[3]))
                                            NewMon = Classes.new_monster(mon, lvl)

                                            direction = random.choice(dirs)
                                            set_monster(Field, x, y, direction, NewMon)
        except:
            print("Error in Map file " + str(mapid))
    else:
        print("Error: No Map with MapID " + str(mapid) + " found.")
    return Field                

    
    
    

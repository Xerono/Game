import os

class tile():
    def __init__(self, name, clas, color, desc, passable):
        self.name = name
        self.clas = clas
        self.color = color
        self.desc = desc
        self.passable = passable



Path_To_Tiles = os.getcwd() + "/Tiles"

def load_tiles():
    Marker = "T"
    Tilefiles = os.listdir(Path_To_Tiles)
    TilesData = []
    Namelist = []
    for TileFile in Tilefiles:
        if TileFile.split("_")[0] == Marker:
            with open(Path_To_Tiles + "/" + TileFile, "r") as file:
                all_lines = []
                for line in file.readlines():
                    all_lines.append(line.rstrip())
                for (TF, name) in Namelist:
                    if name == all_lines[0]:
                        print("Error in tile loading: File " + TileFile + " has a duplicate name (same as " + str(TF) + "): " + name)
                        break
                else:
                    Tile = tile(all_lines[0], all_lines[1], (int(all_lines[2]), int(all_lines[3]), int(all_lines[4])), all_lines[5], "True" == all_lines[6])
                    Namelist.append((TileFile, all_lines[0]))
                    TilesData.append(Tile)
    return TilesData

def load_objects():
    Marker = "O"
    Tilefiles = os.listdir(Path_To_Tiles)
    TilesData = []
    Namelist = []
    for TileFile in Tilefiles:
        if TileFile.split("_")[0] == Marker:
            with open(Path_To_Tiles + "/" + TileFile, "r") as file:
                all_lines = []
                for line in file.readlines():
                    all_lines.append(line.rstrip())
                for (TF, name) in Namelist:
                    if name == all_lines[0]:
                        print("Error in tile loading: File " + TileFile + " has a duplicate name (same as " + str(TF) + "): " + name)
                        break
                else:
                    Tile = tile(all_lines[0], all_lines[1], (int(all_lines[2]), int(all_lines[3]), int(all_lines[4])), all_lines[5], "True" == all_lines[6])
                    Namelist.append((TileFile, all_lines[0]))
                    TilesData.append(Tile)
    return TilesData    
    

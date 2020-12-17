import os

class tile():
    def __init__(self, name, clas, color, desc, passable):
        self.name = name
        self.clas = clas
        self.color = color
        self.desc = desc
        self.passable = passable



Path_To_Tiles = os.getcwd() + "/Tiles"

def load_objects():
    Monsterdata = load_monster()
    objectdata = load_object()
    TilesList = Monsterdata + objectdata
    return TilesList


def load_tiles():
    Filepath = Path_To_Tiles + "/Ground/"
    Tilefiles = os.listdir(Filepath)
    TilesData = []
    Namelist = []
    for TileFile in Tilefiles:
        split = TileFile.split(".")
        if len(split)>1:
            if split[1] == "tile":
                try:
                    with open(Filepath + TileFile, "r") as file:
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
                except:
                    print("Error in loading tile file" + str(TileFile))
    return TilesData

def load_object():
    Filepath = Path_To_Tiles + "/Objects/"
    Tilefiles = os.listdir(Filepath)
    TilesData = []
    Namelist = []
    for TileFile in Tilefiles:
        with open(Filepath + TileFile, "r") as file:
            all_lines = []
            for line in file.readlines():
                all_lines.append(line.rstrip())
            Tile = tile(all_lines[0], all_lines[1], (int(all_lines[2]), int(all_lines[3]), int(all_lines[4])), all_lines[5], "True" == all_lines[6])
            TilesData.append(Tile)
    return TilesData

def load_monster():
    Filepath = Path_To_Tiles + "/Monster/"
    TileFiles = os.listdir(Filepath)
    TilesData = []
    Namelist = []
    for TileFile in TileFiles:
        with open(Filepath + TileFile, "r") as file:
            all_lines = []
            for line in file.readlines():
                all_lines.append(line.rstrip())
            Tile = tile(all_lines[0], all_lines[1], (int(all_lines[2]), int(all_lines[3]), int(all_lines[4])), all_lines[5], "True" == all_lines[6])
            TilesData.append(Tile)
    return TilesData

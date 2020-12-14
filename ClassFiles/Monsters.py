import os

NumberOfAttacks = 4


class Monster:
    def __init__(self, Species, MonsterID, Type1, Type2, HP, Atk, Def, MAtk, MDef, Speed, Attacks, Level, Tile):
        self.Species = Species
        self.MonsterID = MonsterID
        self.Type1 = Type1
        if Type2 == "":
            self.Type2 = None
        else:
            self.Type2 = Type2
        self.Position = ""
        self.Direction = ""
        self.Stats = (HP, Atk, Def, MAtk, MDef, Speed)
        self.CurrentHP = HP
        self.Attacks = Attacks
        self.Level = Level
        CurAts = []
        for Att in Attacks:
            (ALevel, Attack) = Att
            if ALevel <= Level:
                CurAts.append(Attack)
        self.CurrentAttacks = CurAts[-NumberOfAttacks:]
        self.Tile = Tile
        self.OldTile = ""

class CaughtMonster(Monster):
    def __init__(self, Monster, Player, Nickname, LocationID, Datetime):
        self.Species = Monster.Species
        self.MonsterID = Monster.MonsterID
        self.Type1 = Monster.Type1
        self.Type2 = Monster.Type2
        self.Stats = Monster.Stats
        self.CurrentHP = Monster.CurrentHP
        self.Attacks = Monster.Attacks
        self.CurrentAttacks = Monster.CurrentAttacks
        self.Tile = Monster.Tile
        self.Nickname = Nickname
        self.CaughtLoc = LocationID
        self.CaughtTime = Datetime
        self.Catched_By = (Player.Name, Player.ID)
        
    

Path_To_Monsters = os.getcwd() + "/ClassFiles/Monster"
Path_To_Attacks = Path_To_Monsters + "/Attacklist"


def load_monsters():
    Monsterlist = []
    ClassFiles = os.listdir(Path_To_Monsters)
    ClassFiles.remove("Attacklist")
    for ClassFile in ClassFiles:
        Attacks = []
        with open(Path_To_Monsters + "/" + ClassFile, "r") as file:
            All_Lines = file.readlines()
            Species = All_Lines[0].rstrip()
            MonsterID = All_Lines[1].rstrip()
            Type1 = All_Lines[2].rstrip()
            Type2 = All_Lines[3].rstrip()
            HP = All_Lines[4].rstrip()
            Atk = All_Lines[5].rstrip()
            Def = All_Lines[6].rstrip()
            MAtk = All_Lines[7].rstrip()
            MDef = All_Lines[8].rstrip()
            Speed = All_Lines[9].rstrip()
        with open(Path_To_Attacks + "/" + ClassFile, "r") as attfile:
            for att in attfile.readlines():
                attspl = att.rstrip()
                attack = attspl.split("#")[1]
                lvl = attspl.split("#")[0]
                Attacks.append((int(lvl), attack))
        Monster = (Species, MonsterID, Type1, Type2, int(HP), int(Atk), int(Def), int(MAtk), int(MDef), int(Speed), Attacks)
        Monsterlist.append(Monster)
    return Monsterlist


Monsterlist = load_monsters()

def new_monster(MonsterSpecies, Level, Tile):
    for (Species, M_ID, Type1, Type2, HP, Atk, Def, MAtk, MDef, Speed, Attacks) in Monsterlist:
        if Species == MonsterSpecies:
            MonsterRet = Monster(Species, M_ID, Type1, Type2, HP, Atk, Def, MAtk, MDef, Speed, Attacks, Level, Tile)
            break
    return MonsterRet

def caught(Monster, Player, Nick, Loc, DT):
    cCaughtMonster = CaughtMonster(Monster, Player, Nick, Loc, DT)
    return cCaughtMonster

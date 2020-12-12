import os

NumberOfAttacks = 4

class Monster:
    def __init__(self, Species, Typ1, Typ2, Atk, Def, MAtk, MDef, Speed, Attacks, Level, Tile):
        self.Species = Species
        self.Typ1 = Typ1
        if Typ2 == "":
            self.Typ2 = None
        else:
            self.Typ2 = Typ2
        self.Position = ""
        self.Direction = ""
        self.Atk = Atk
        self.Def = Def
        self.MAtk = MAtk
        self.MDef = MDef
        self.Speed = Speed
        self.Attacks = Attacks
        self.Level = Level
        self.Name = ""
        CurAts = []
        for Att in Attacks:
            (ALevel, Attack) = Att
            if ALevel <= Level:
                CurAts.append(Attack)
        self.CurrentAttacks = CurAts[-NumberOfAttacks:]
        self.Tile = Tile

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
            Type1 = All_Lines[1].rstrip()
            Type2 = All_Lines[2].rstrip()
            Atk = All_Lines[3].rstrip()
            Def = All_Lines[4].rstrip()
            MAtk = All_Lines[5].rstrip()
            MDef = All_Lines[6].rstrip()
            Speed = All_Lines[7].rstrip()
        with open(Path_To_Attacks + "/" + ClassFile, "r") as attfile:
            for att in attfile.readlines():
                attspl = att.rstrip()
                attack = attspl.split("#")[1]
                lvl = attspl.split("#")[0]
                Attacks.append((int(lvl), attack))
        Monster = (Species, Type1, Type2, int(Atk), int(Def), int(MAtk), int(MDef), int(Speed), Attacks)
        Monsterlist.append(Monster)
    return Monsterlist


def new_monster(MonsterSpecies, Level, Tile):
    for (Species, Type1, Type2, Atk, Def, MAtk, MDef, Speed, Attacks) in load_monsters():
        if Species == MonsterSpecies:
            MonsterRet = Monster(Species, Type1, Type2, Atk, Def, MAtk, MDef, Speed, Attacks, Level, Tile)
            break
    return MonsterRet

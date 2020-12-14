class Player():
    def __init__(self, name, id, mapid, x, y, direction, Tile, JStart):
        self.Name = name
        self.ID = id
        self.Current_Map = mapid
        self.Position = (x,y)
        self.Direction = direction
        self.Tile = Tile
        self.Last_Tile = Tile
        self.Journey_Start = JStart
        self.Party = []
        self.Box = []
        self.Saves = 0

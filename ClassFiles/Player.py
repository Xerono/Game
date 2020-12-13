class Player():
    def __init__(self, name, x, y, direction, Tile):
        self.Name = name
        self.Position = (x,y)
        self.Direction = direction
        self.Tile = Tile
        self.Party = []

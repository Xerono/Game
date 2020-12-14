import pygame

def create_battle_screen(Player, Monsterlist, Blocksize, FieldsizeX, FieldsizeY):
    Height = int(FieldsizeX*Blocksize)
    Width = int(FieldsizeY*Blocksize)
    Battlescreen = pygame.display.set_mode((Height, Width))

    pygame.display.update()

def Start_battle(Screen):
    pass

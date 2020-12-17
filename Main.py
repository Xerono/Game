import Map
import Movement
import Classes
import Monster
import Saves

import pygame

import random
import time
import pickle


Screen_Height = 1000
Screen_Width = 800
Blocksize = 100
Map.init_map(Screen_Height, Screen_Width, Blocksize)


def naming():
    print("Enter your name:")
    Namecheck = False
    PlayerName = input()
    while "_" in PlayerName:
        PlayerName.remove("_")
        Namecheck = True
    print("Name the first monster:")
    StarterName = input()
    if Namecheck:
        print("I will call you " + Playername + ". Is that okay? y/n")
        okcheck = input()
        if okcheck == "n":
            return naming()
    return (PlayerName, StarterName)
    
def game_first_start():
    if True:
        (PlayerName, StarterName) = naming()
    else:
        PlayerName = "PlayerDefault"
        StarterName = "Starty"
        
    Journey_Start = time.time()   
    
    PlayerX = 2
    PlayerY = 2
    MapID = 1

    PlayerID = random.randint(0, 9999999999)
    MonsterID = 1
    MonsterLvl = 1
    
    Player = Classes.new_player(PlayerName, PlayerID, MapID, PlayerX, PlayerY, "Up", Journey_Start)
    Starter = Classes.catch_monster(Classes.new_monster(MonsterID, MonsterLvl), Player, StarterName, 1, Journey_Start)
    Player = Monster.put_monster_in_party(Starter, Player)

    Field = Map.load_map(Player, (PlayerX, PlayerY), MapID)
    try:
        (Field, Player) = Map.set_player(Field, Player, MapID, PlayerX, PlayerY)
    except:
        print("Error: Setting of Player on Map " + str(MapID) + " failed.")
        sys.exit()
    Saves.save_game(Field, Player)
    return (Player, Field)

def game_init_screen(Field):
    Map.Block_Size = Blocksize
    Map.FieldSizeX = int(Screen_Height/Blocksize)
    Map.FieldSizeY = int(Screen_Width/Blocksize)
    MapScreen = pygame.display.set_mode((Screen_Height, Screen_Width))
    Map.draw_map(MapScreen, Field)
    pygame.key.set_repeat(200)
    return MapScreen

def main(MapScreen, Field, Player):
    CurScreen = MapScreen
    Running = True
    UDLR = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:
                if CurScreen == MapScreen:
                    if event.key in UDLR:
                        (Field, Player) = Movement.move_player(Field, Player, event.key)
                        Map.draw_map(MapScreen, Field)
                    if event.key == pygame.K_s:
                        Saves.save_game(Field, Player)

    pygame.quit()
    exit()





def game_init():
    saves = Saves.get_num_of_saves()
    if saves == 0:
        (Player, Field) = game_first_start()
    else:
        print("New game or load old save? new/old")
        neworold = input()
        if neworold == "new":
            (Player, Field) = game_first_start()
        else:
            PF = Saves.load_game()
            if PF:
                (Player, Field) = PF
            else:
                game_init()
    Screen = game_init_screen(Field)
    main(Screen, Field, Player)

game_init()

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
    
    PlayerX = 1
    PlayerY = 0
    PlayerID = random.randint(0, 9999999999)
    MapID = 1
    Player = Classes.new_player(PlayerName, PlayerID, MapID, PlayerX, PlayerY, "Up", Journey_Start)
    Starter = Classes.catch_monster(Classes.new_monster("Starter", 1), Player, StarterName, 1, Journey_Start)
    Player = Monster.put_monster_in_party(Starter, Player)

    Field = Map.create_random_map(Screen_Height, Screen_Width, Blocksize)
    (Field, Player) = Map.set_player(Field, Player)
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
                    if event.key == pygame.K_a:
                        #Debug
                        try:
                            Field = Map.set_monster(Field, 2, 2, "Up", Classes.new_monster("Monster1", 1))
                            Map.draw_map(MapScreen, Field)
                        except:
                            print("Error in creating Monster after a press")
                    if event.key == pygame.K_b:
                        #Debug
                            BattleScreen = pygame.display.set_mode((Screen_Height, Screen_Width))
                            Map.draw_map(BattleScreen, Field)

    pygame.quit()
    exit()




saves = Saves.get_num_of_saves()
if saves == 0:
    (Player, Field) = game_first_start()
else:
    print("New game or load old save? new/old")
    neworold = input()
    if neworold == "new":
        (Player, Field) = game_first_start()
    else:
        (Player, Field) = Saves.load_game()
Screen = game_init_screen(Field)
main(Screen, Field, Player)

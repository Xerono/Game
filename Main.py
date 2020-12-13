import Map
import Movement
import Classes

import Monster

import pygame


def main():
    Screen_Height = 1000
    Screen_Width = 800
    Blocksize = 100
    PlayerX = 1
    PlayerY = 0

    Running = True

    Monsters_on_Map = {}
    
    Field = Map.create_random_map(Screen_Height, Screen_Width, Blocksize)
    Field = Map.set_player(Field, PlayerX, PlayerY)
    #import Monster
    Player = Classes.new_player("Playername", PlayerX, PlayerY, "Up")
    Player.Party = Monster.put_monster_in_party(Classes.catch_monster(Classes.new_monster("Starter", 1), "Starty", 1, 0), Player.Party)
    
    MapScreen = pygame.display.set_mode((Screen_Height, Screen_Width))
    
    Map.draw_map(MapScreen, Field)
    pygame.key.set_repeat(200)
                          
    CurScreen = MapScreen
    
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:
                if CurScreen == MapScreen:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        (Field, Player) = Movement.move_player(Field, Player, event.key)
                        Map.draw_map(MapScreen, Field)
                    if event.key == pygame.K_a:
                        #Debug
                        try:
                            (Field, SeenMonster) = Map.set_monster(Field, 2, 2, "Up", Classes.new_monster("Monster1", 1))
                            Monsters_on_Map[SeenMonster.Position] = SeenMonster
                            Map.draw_map(MapScreen, Field)
                        except:
                            print("Error in creating Monster after a press")
                    if event.key == pygame.K_b:
                        #Debug
                            Screen2 = pygame.display.set_mode((Screen_Height, Screen_Width))
                            Map.draw_map(Screen2, Map.set_player(Map.create_random_map(Screen_Height, Screen_Width, Blocksize), PlayerX, PlayerY))

    pygame.quit()
    exit()
    
main()

import Map
import Movement
import Classes

import pygame


def main():
    Screen_Height = 1000
    Screen_Width = 800
    Blocksize = 10
    PlayerX = 1
    PlayerY = 0
    Running = True


    Field = Map.create_random_map(Screen_Height, Screen_Width, Blocksize)
    Field = Map.set_player(Field, PlayerX, PlayerY)

    Player = Classes.new_player("Player", PlayerX, PlayerY, "Up")
    Screen = pygame.display.set_mode((Screen_Height, Screen_Width))
    Map.draw_map(Screen, Field)
    
    View = "Map"
    
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:
                if View == "Map":
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        (Field, Player) = Movement.move_player(Field, Player, event.key)
                        Map.draw_map(Screen, Field)
    pygame.quit()
    exit()
    
main()

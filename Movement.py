import pygame
import Map

def move_player(Field, Player, key):
    (PlayerX, PlayerY) = Player
    if key == pygame.K_UP:
        NewX = PlayerX
        NewY = PlayerY - 1
    else:
        if key == pygame.K_DOWN:
            NewX = PlayerX
            NewY = PlayerY + 1
        else:
            if key == pygame.K_LEFT:
                NewX = PlayerX - 1
                NewY = PlayerY
            else:
                if key == pygame.K_RIGHT:
                    NewX = PlayerX + 1
                    NewY = PlayerY
                else:
                    pass
                        
    if NewY < 0 or NewY >= len(Field[0]) or NewX < 0 or NewX >= len(Field) or (not Field[NewX][NewY].passable):
        pass
    else:
        LastTile = Map.get_last_tile()
        Map.set_last_tile(Field[NewX][NewY])
        Field[PlayerX][PlayerY] = LastTile
        Field = Map.set_player(Field, NewX, NewY)       
        Player = (NewX, NewY)
    return (Field, Player)
        
                
    

import pygame
import Map
import Battle

def move_player(Field, Player, key):
    (PlayerX, PlayerY) = Player.Position
    if key == pygame.K_UP:
        NewX = PlayerX
        NewY = PlayerY - 1
        NewDir = "Up"
    else:
        if key == pygame.K_DOWN:
            NewX = PlayerX
            NewY = PlayerY + 1
            NewDir = "Down"
        else:
            if key == pygame.K_LEFT:
                NewX = PlayerX - 1
                NewY = PlayerY
                NewDir = "Left"
            else:
                if key == pygame.K_RIGHT:
                    NewX = PlayerX + 1
                    NewY = PlayerY
                    NewDir = "Right"
                else:
                    # Should never happen
                    print("Something went wrong: move_player, " + str(key))
                    return (Field, Player)
    if NewY < 0 or NewY >= len(Field[0]) or NewX < 0 or NewX >= len(Field):
        #OOB
        pass
    else:
        if Field[NewX][NewY][0].clas == "Ground":
            # Target tile contains ground
            if (not Field[NewX][NewY][0].passable):
                #Non-passable terrain
                pass
            else:
                LastTile = Player.Last_Tile
                Player.Position = (NewX, NewY)
                Player.direction = NewDir
                Field[PlayerX][PlayerY] = LastTile
                (Field, Player) = Map.set_player(Field, Player)

        else:
            if Field[NewX][NewY][0].clas == "Monster":
                OldTile = Field[NewX][NewY][1].OldTile
                BattleScreen = Battle.create_battle_screen(Player, [Field[NewX][NewY]], Map.Block_Size, Map.FieldSizeX, Map.FieldSizeY)
                Battle.Start_battle(BattleScreen)
                Field[NewX][NewY] = OldTile
    return (Field, Player)
        
                
    

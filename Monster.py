Allowed_Monsters_in_Party = 6

def put_monster_in_party(Monster, Player):
    if len(Player.Party) >= Allowed_Monsters_in_Party:
        print("Error: Party is full")
    else:
        Player.Party.append(Monster)
    return Player

def remove_monster_from_party(Monster, Player):
    if Monster in Player.Party:
        Player.Party.remove(Monster)
        Player.Box.append(Monster)
    else:
        print("Error: Monster not in party")
    return Player


def swap_monster(MonsterOut, MonsterIn, Player):
    PlayerOut = remove_monster_from_party(MonsterOut, Player)
    PlayerIn = put_monster_in_party(MonsterIn, PlayerOut)
    return PlayerIn

def put_monster_in_box(Monster):
    Box.append(Monster)

def get_monster_out_box(num, Player):
    if num<=Player.Box.length:
        mon = Player.Box.pop(num)
        return mon
    else:
        print("Error: get_monster_out_box num not in range")
    

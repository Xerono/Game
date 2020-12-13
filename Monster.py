Allowed_Monsters_in_Party = 6

Box = []

def put_monster_in_party(Monster, Party):
    if len(Party) >= Allowed_Monsters_in_Party:
        print("Error: Party is full")
    else:
        Party.append(Monster)
    return Party

def remove_monster_from_party(Monster, Monsterlist):
    if Monster in Monsterlist:
        Monsterlist.remove(Monster)
        Box.append(Monster)
    else:
        print("Error: Monster not in party")
    return Monsterlist


def swap_monster(MonsterOut, MonsterIn, Monsterlist):
    Monsterlist = remove_monster_from_party(MonsterOut, Monsterlist)
    Monsterlist = put_monster_in_party(MonsterIn, Monsterlist)
    return Monsterlist

def put_monster_in_box(Monster):
    Box.append(Monster)

def get_monster_out_box(num):
    if num<=Box.length:
        mon = Box.pop(num)
        return mon
    else:
        print("Error: get_monster_out_box num not in range")
    

import os
import pickle
import time

Num_Of_Saves_Per_Player = 10

def get_num_of_saves():
    Savepath = os.getcwd() + "/Saves/"
    Saves = {}
    i = 0
    for Savefolder in os.listdir(Savepath):
        i+=1
    return i

def which_file_to_load(PlayerAndID, Savefile, Saves):
        [Player, ID] = PlayerAndID.split("_")
        print("Which file to load from "+ str(Player) + " (" + str(ID) + ")? ('c' to cancel)")
        Saves.sort(reverse=True)
        for i in range(len(Saves)):
            itoprint = str(i+1)
            if len(itoprint)<2:
                itoprint = "0" + itoprint
            print(itoprint + ": " + str(Saves[i]) + " | " + str(time.ctime(int(Saves[i].split(".")[0]))))
        sf = input()
        if sf == 'c':
            return False
        try:
            sfn = int(sf)
        except:
            print("Please enter a number between 1 and " + str(i+1))
            return which_file_to_load(Saves)
        if sfn > len(Saves) or sfn < 1:
            print("Please enter a number between 1 and " + str(i+1))
            which_file_to_load(PlayerAndID, Savefile, Saves)
        else:
            Chosen_File = Saves[sfn-1]
            NewestFile = Savefile + "/" + str(Chosen_File)
            print("Loading File " + str(sfn) + "...")
            with open(NewestFile, "rb") as save:
                savedict = pickle.load(save)
                return (savedict["Player"], savedict["Field"])
            
def load_game():
    Savepath = os.getcwd() + "/Saves/"
    Saves = {}
    i = 1
    for Savefolder in os.listdir(Savepath):
        sname, sid = Savefolder.split("_")
        Saves[i] = (sname, sid)
        i+=1
    savenum = 1
    if i>2:
        print("Load which save? 'c' to cancel")
        for key in Saves.keys():
            print(str(key) + ": " + str(Saves[key][0]) + " (" + str(Saves[key][1]) + ")")
        savenuminput = input()
        if savenuminput == "c":
              return False
        try:
            savenum = int(savenuminput)
        except:
            print("Please enter a number between 1 and " + str(i))
            savenum = 0
        if savenum > i or savenum < 1:
            print("Please enter a number between 1 and " + str(i))
            savenum = 0
        if savenum == 0:
            return load_game()
    if savenum > 0:
        PlayerAndID = str(Saves[savenum][0]) + "_" + str(Saves[savenum][1])
        Savefilepath = Savepath + PlayerAndID

        Newest = 0
        Saves = []
        for Savefile in os.listdir(Savefilepath):
            Saves.append(Savefile)
            if int(Savefile.split(".")[0]) > Newest:
                Newest = int(Savefile.split(".")[0])
        yn = "i<0"
        if len(Saves)>1:
            print("Load newest file? y/n ('c' to cancel)")
            yn = input()
        if yn == 'c':
            return False
        if yn != "n":
            print("Loading newest file...")
            NewestFile = Savefilepath + "/" + str(Newest) + ".sav"
            with open(NewestFile, "rb") as save:
                savedict = pickle.load(save)
            return (savedict["Player"], savedict["Field"])
        else:
            return which_file_to_load(PlayerAndID, Savefilepath, Saves)

        
    


def save_game(Field, Player):
    save = {}
    save["Field"] = Field
    save["Player"] = Player
    LongID = str(Player.ID).zfill(10)
    Savetime = str(time.time()).split(".")[0]
    PName = str(Player.Name)

    StrLID = str(LongID)
    Savepath = os.getcwd() + "/Saves/"
    if not os.path.exists(Savepath):
        os.mkdir(Savepath)
    
    SaveFolder = Savepath + PName + "_" + StrLID + "/"
    Filename =  Savetime + ".sav"
    Player.Saves += 1
    
    Oldest = str(time.time())

    if not os.path.exists(SaveFolder):
        os.mkdir(SaveFolder)

    Savecount = 0
    for Savefile in os.listdir(SaveFolder):
        stime = Savefile.split(".")[0]
        Savecount += 1
        if stime < Oldest:
            Oldest = stime   
    if Savecount < Num_Of_Saves_Per_Player:
        with open(SaveFolder + Filename, "wb") as file:
            pickle.dump(save, file)       
        print("Saved")
    else:
        print(str(Num_Of_Saves_Per_Player) + " savefiles detected.")
        print("Your oldest savefile will be overwritten. Proceed? y/n")
        yn = input()
        if yn != "y":
              print("Nothing saved.")
        else:
            os.remove(SaveFolder + Oldest + ".sav")
            print("Oldest savefile deleted. Saving now...")
            save_game(Field, Player)

           

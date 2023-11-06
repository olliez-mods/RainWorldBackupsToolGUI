import pathlib
import shutil
import sys
from datetime import datetime
import subprocess
import os



def ext():
    input(" ")
    sys.exit()


print("\n")

appdataRoaming = os.environ.get("APPDATA")
appdataLocalLow = os.path.normpath(appdataRoaming + "\\..\\LocalLow\\Videocult\\Rain World\\")
rainWorldSaveDir = pathlib.Path(appdataLocalLow)
#rainWorldSaveDir = pathlib.Path("")  #pathlib.Path(appdataLocalLow)

if(not rainWorldSaveDir.exists()):
    print("We could not find \""+str(rainWorldSaveDir)+"\" please make sure you have Rain World installed")
    ext()

savsDir = rainWorldSaveDir.joinpath("RWCPsavs")
backupsDir = savsDir.joinpath("backups")
currSavNameDir = rainWorldSaveDir.joinpath("RWCPselectedSav.txt")
currSavFileDir = rainWorldSaveDir.joinpath("sav")


print("Using path:", rainWorldSaveDir, "\n")

# Check if all requird directories and files exist in the rain world folder
def doesSavFileExist():
    return currSavFileDir.is_file()
def doesSaveDirExist():
    return savsDir.is_dir()
def doesBackupsDirExist():
    return backupsDir.is_dir()
def doesCurrSaveNameFileExist():
    return currSavNameDir.is_file()
def createSavesDir():
    savsDir.mkdir(parents=False, exist_ok=False)
    backupsDir.mkdir(parents=False, exist_ok=False)
def createBackupsdir():
    backupsDir.mkdir(parents=False, exist_ok=False)
def createCurrsaveNameFile():
    currSavNameDir.touch(exist_ok=False)
    file = open(currSavNameDir, "w")
    file.write("default")
    file.close()

def getRainWorldFolderDirectory():
    global rainWorldSaveDir
    return rainWorldSaveDir


def getCurrSaveName():
    file = open(currSavNameDir, "r")
    saveName = file.read()
    file.close()
    return saveName

def getSavesNames():
    l = savsDir.glob('*.RWCPsav')
    itemsNames = []
    for item in l:
        itemName = item.name.split(".")[0]
        itemsNames.append(itemName)
    return itemsNames

def getallSavesList():
    curr = getCurrSaveName()
    savesList = getSavesNames()
    savesList.insert(0, curr)
    return savesList


# =====================
# Create backup, very important

def createBackup():
    # we assume that all required files and folders exist
    currDate = str(datetime.now().strftime("%Y-%m-%d [%H-%M-%Ss]"))
    newBackupDir = backupsDir.joinpath(currDate)
    newBackupDir.mkdir(parents=False, exist_ok=False)
    names = getSavesNames()
    currSaveName = getCurrSaveName()

    for fileName in names: # copy saves in storage
        shutil.copy2(savsDir.joinpath(fileName + ".RWCPsav"), newBackupDir)
    shutil.copy2(currSavFileDir, newBackupDir.joinpath(currSaveName + ".RWCPsav")) # copy main file
        
#createBackup() # we have this in a function so we dont pollute the main function with variables


# ===================



def printMainMenu():
    print("Saves:")
    print("-  " + getCurrSaveName() + " *Selected*")
    names = getSavesNames()
    for n in names:
        print("-  " + n)
    print("\nMain Menu (Use \"help <number>\" for more info on a command):")
    print("1 - Load a Save")
    print("2 - Copy Selected Save")
    print("3 - Delete a Save")
    print("4 - Override Selected With a Stored Save")
    print("5 - Rename Selected Save")
    print("6 - Open Rain World folder\n")

def isValidSave(saveName, includecurrent = False):
    l = getSavesNames()
    if(includecurrent):
        l.append(getCurrSaveName())
    return (saveName in l)

def clear():
    print("\n"*100)

def pause(msg = "\n -> Press \"Enter\" to continue <-"):
    input(msg)

def getFileString(saveName):
    # if it doesnt exist at all
    if(not isValidSave(saveName) and saveName != getCurrSaveName()):
        print("not valid save")
        ext()

    if(saveName == getCurrSaveName()):
        with open(rainWorldSaveDir.joinpath('sav'), 'r') as file:
            fileString = file.read()
    else:
        with open(savsDir.joinpath(saveName + ".RWCPsav")) as file:
            fileString = file.read()
    return fileString
    

# loads a save from the savs folder into rain world folder
def loadSave(saveName):
    if(not isValidSave(saveName)):
        print("not valid save in loadSave()")
        ext()

    # Get name of current save
    currSaveName = getCurrSaveName()

    # now copy it into the savs folder
    shutil.move(currSavFileDir, savsDir.joinpath(currSaveName + ".RWCPsav"))

    #now move the new sav into the main dir
    shutil.move(savsDir.joinpath(saveName + ".RWCPsav"), rainWorldSaveDir.joinpath("sav"))

    #update txt file to reflect new name
    file = open(currSavNameDir, "w")
    file.write(saveName)
    file.close()

    return saveName
   
def duplicateSelectedSave(newName):
    #copy into sav folder with new name
    shutil.copy2(currSavFileDir, savsDir.joinpath(newName + ".RWCPsav"))

def duplicateSave(saveName, newName):
    if(saveName == getCurrSaveName()):
        duplicateSelectedSave(newName)
        return
    #copy into sav folder with new name
    shutil.copy2(savsDir.joinpath(saveName + ".RWCPsav"), savsDir.joinpath(newName + ".RWCPsav"))

def deleteSave(saveName):
    if(not savsDir.joinpath(saveName + ".RWCPsav").is_file()):
        print("Error in deleteSave() we just saved your life ;)")
        ext()
    
    savsDir.joinpath(saveName + ".RWCPsav").unlink()

# delete current save and copy another save into it
def loadBackup(saveName):
    if(not savsDir.joinpath(saveName + ".RWCPsav").is_file()):
        print("Error in loadbackup() we just saved your life ;)")
        ext()
    # delete current save
    rainWorldSaveDir.joinpath("sav").unlink()

    # copy and select new save
    shutil.copy2(savsDir.joinpath(saveName + ".RWCPsav"), rainWorldSaveDir.joinpath("sav"))

# rename the currently selected save
def renameSelectedSave(newName):
    file = open(currSavNameDir, "w")
    file.write(newName)
    file.close()

def renameSave(saveName, newName):
    if(not savsDir.joinpath(saveName + ".RWCPsav").is_file()):
        print("Error in renameSave() [saveName].RWCPsav could not be found")
        ext()
    shutil.move(savsDir.joinpath(saveName + ".RWCPsav"), savsDir.joinpath(newName + ".RWCPsav"))
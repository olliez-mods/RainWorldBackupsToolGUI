import tkinter as tk
import sys
from tkinter import messagebox
import fileTools as fTools
import saveFileParser as saveParser
import loadImages
import os
import webbrowser



print(os.path.dirname(os.path.abspath(__file__)))


# Confirm folders and files exist
if(not fTools.doesSavFileExist()):
    messagebox.showinfo(title="Missing save file", message=f"It seems like there isn't a save file in the directory:\n{fTools.getRainWorldFolderDirectory()}\nPlease make sure this path is correct.")
    sys.exit()
if(not fTools.doesSaveDirExist()):
    a = messagebox.askyesno(title="Missing Folder", message=f'Missing folder "RWCPsavs" in the Rain World folder at \n"{str(fTools.getRainWorldFolderDirectory())}"\nWould you like to create this folder?')
    if(not a):
        sys.exit()
    print("Creating saves directory")
    fTools.createSavesDir()
if(not fTools.doesBackupsDirExist()):
    a = messagebox.askyesno(title="Missing Folder", message=f'Missing folder "RWCPsavs/backups" in the Rain World folder at \n"{str(fTools.getRainWorldFolderDirectory())}"\nWould you like to create this folder?')
    if(not a):
        sys.exit()
    print("Creating backups directory")
    fTools.createBackupsdir()
if(not fTools.doesCurrSaveNameFileExist()):
    a = messagebox.askyesno(title="Missing File", message=f'Missing file "RWCPselectedSav.txt" in the Rain World folder at \n{str(fTools.getRainWorldFolderDirectory())}\nWould you like to create this folder?')
    if(not a):
        sys.exit()
    print("Creating Curr save name file")
    fTools.createCurrsaveNameFile()


fTools.createBackup()


window = tk.Tk()


loadImages.loadSlugImages()


WIDTH = 800
HEIGHT = 500


window.geometry("")


window.title("Rain World Backups Tool")
window.resizable(False,False)

viewedSave = ""
currentSave = ""


outerFrame = tk.Frame(window, borderwidth=5, bg="#8eff61")
outerFrame.pack(fill="both", expand=True)

innerFrame = tk.Frame(outerFrame)
innerFrame.pack(fill="both", expand=True)

savesListFrame = tk.Frame(innerFrame, background="#c7c7c7")
savesListFrame.pack(side="left", fill="y")

topInfoFrame = tk.Frame(innerFrame, bg="#a3a3a3")
topInfoFrame.pack(side="top", fill="x")


viewedSaveNameLabel = tk.Label(topInfoFrame, text="Selected Save", font=("Arial", 30))
viewedSaveNameLabel.grid(column=0, row=0, rowspan=2)


def changeSaveBFunc():
    global viewedSave, currentSave
    if(not fTools.isValidSave(viewedSave)):
        return
    currentSave = fTools.loadSave(viewedSave)
    updateSavesList()
changeSaveButton = tk.Button(topInfoFrame, text="Select Save", font=("Arial", 10), command=changeSaveBFunc)
changeSaveButton.grid(column=1, row=0)

def deleteSaveBFunc():
    global viewedSave, currentSave

    if(viewedSave == currentSave):
        messagebox.showinfo(title="Incorrect Usage", message="You cannot delete the currently selected save.")
    # if it's the current save it will return
    if(not fTools.isValidSave(viewedSave)):
        return
    answer = messagebox.askyesno(title=f'Delete "{viewedSave}" save', message=f'Are you sure you want to delete "{viewedSave}"?')
    if(answer):
        fTools.deleteSave(viewedSave)
        updateSavesList()
        setViewedSave(currentSave)
deleteSaveButton = tk.Button(topInfoFrame, text="Delete Save", font=("Arial", 10), command=deleteSaveBFunc)
deleteSaveButton.grid(column=1, row=1, sticky=tk.EW)

copySaveInputHintLabel = tk.Label(topInfoFrame, text="Name:", font=("Arial", 8))
copySaveInputHintLabel.grid(column=2, row=1, sticky=tk.EW)

copySaveInput = tk.Entry(topInfoFrame)
copySaveInput.grid(column=3, row=1, sticky=tk.EW)


def copySaveBFunc():
    global viewedSave, currentSave
    if(not fTools.isValidSave(viewedSave, True)):
        return
    if(copySaveInput.get() == ""):
        messagebox.showinfo(title="Save must have name", message="Please type a name for the new save into the input field")
        return
    if(copySaveInput.get() == currentSave):
        messagebox.showinfo(title="Incorrect Usage", message='You can\'t name a copy the same name as the currently selected save.\n Try using "Override Selected"')
        return
    if(fTools.isValidSave(copySaveInput.get())):
        answer = messagebox.askyesno(title=f'Override "{copySaveInput.get()}"', message=f'Creating this copy will override "{copySaveInput.get()}", are you sure?')
        if(answer == False):
            return
    fTools.duplicateSave(viewedSave, copySaveInput.get())
    updateSavesList()
    copySaveInput.delete(0, tk.END)  # Clear any existing text
copySaveButton = tk.Button(topInfoFrame, text="  Copy Save  ", font=("Arial", 10), command=copySaveBFunc)
copySaveButton.grid(column=2, row=0, columnspan=1, sticky=tk.EW)

def renameSaveBFunc():
    global viewedSave, currentSave
    if(copySaveInput.get() == ""):
        messagebox.showinfo(title="Save must have name", message="Please type a name into the input field")
        return
    if(fTools.isValidSave(copySaveInput.get(), True)):
        messagebox.showinfo(title=f'Can\'t rename to an existing save', message=f'you can\'t rename "{viewedSave}" to "{copySaveInput.get()}" because there is already a save by that name')
        return
    # we have a different function to rename the selected save
    if(viewedSave == currentSave):
        fTools.renameSelectedSave(copySaveInput.get())
    else:
        fTools.renameSave(viewedSave, copySaveInput.get())
    updateSavesList()
    setViewedSave(copySaveInput.get())
    copySaveInput.delete(0, tk.END)  # Clear any existing text
renameSaveButton = tk.Button(topInfoFrame, text="rename Save", font=("Arial", 10), command=renameSaveBFunc)
renameSaveButton.grid(column=3, row=0, columnspan=1, sticky=tk.EW)


def overrideSelectedBFunc():
    global viewedSave, currentSave
    answer = messagebox.askyesno(title=f'Override "{currentSave}"', message=f'Creating this copy will override "{currentSave}" with "{viewedSave}".\n(the name, "{currentSave}" will be kept).\nare you sure?')
    if(answer):
        fTools.loadBackup(viewedSave)
OverrideSelectedButton = tk.Button(topInfoFrame, text="Override\nSelected", font=("Arial", 10), command=overrideSelectedBFunc)
OverrideSelectedButton.grid(column=4, row=0, rowspan=2, sticky=tk.NSEW)


areaCodeToReadable = {"SU":"Outskirts", "HI":"Industrial Complex", "DS":"Drainage System", "CC":"Chimney Canopy", "GW":"Garbage Wastes", "SH":"Shaded Citadel", "VS":"Pipeyard", 
                    "SL":"Shoreline", "SI":"Sky Islands", "LF":"Farm Arrays", "UW":"The Exterior", "SS":"Five Pebbles", "SB":"Subterranean", "OE":"Outer Expanse", 
                    "MS": "Submerged Superstructure", "LM":"Waterfront Facility", "LC":"Metropolis", "RM":"The Rot", "DM":"Looks To The Moon", "UG":"Undergrowth", 
                    "VS":"Barren Conduits", "CL":"Silent Construct", "HR":"Rubicon"}


savs = fTools.getallSavesList()


viewedSaveSlugsFrames = []



def createButton(saveName, i):
    def b_command():
        setViewedSave(saveName)

    fileString = fTools.getFileString(saveName)
    saveStr = saveParser.getSaveStringFromFileString(fileString)
    currSlug = saveParser.getNextValueGivenTerm(saveStr, "CURRENTSLUGCAT")
    try:
        img = loadImages.slugImages[f"{currSlug}_icon"]
    except:
        img = loadImages.slugImages["no_icon"]

    b = tk.Button(savesListFrame, text=saveName, image=img, compound="right", command=b_command)
    b.pack(fill="x")

    if(i==0):
        b.config(bg="#919191")

def updateSavesList():
    global savs
    savs = fTools.getallSavesList()
    for child in savesListFrame.winfo_children():
        child.destroy()
    i = 0
    for saveName in savs:
        createButton(saveName, i)
        i += 1
    
    

def viewedSaveCreateMapButton(frame, slugName, areaCode, lastDen):
    openMapButton = tk.Button(frame, text="Open Map", command=lambda: webbrowser.open(f"https://rain-world-map.github.io/map.html?slugcat={str(slugName).lower()}&region={areaCode}&room={lastDen}"))
    openMapButton.pack(anchor="ne", side="top")

def setViewedSave(saveName):
    global viewedSave, currentSave
    if(viewedSave == saveName and saveName != currentSave):
        return
    fileString = fTools.getFileString(saveName)
    saveStr = saveParser.getSaveStringFromFileString(fileString)
    
    viewedSave = saveName

    slugCats = saveParser.getSlugCats(saveStr)

    for i in range(len(viewedSaveSlugsFrames)):
        viewedSaveSlugsFrames[i].destroy()
    viewedSaveSlugsFrames.clear()

    for slugName in slugCats:
        slugcat = slugCats[slugName]
        viewedSaveSlugsFrames.append(tk.Frame(innerFrame, bg="#c7c7c7"))
        viewedSaveSlugsFrames[-1].pack(fill="x", pady=3, padx=5)
        try:
            slugImg = loadImages.slugImages[f"{slugName}_portrait"]
        except:
            #print(f"no {slugName}")
            slugImg = loadImages.slugImages[f"no_portrait"]


        slugImageLabel = tk.Label(viewedSaveSlugsFrames[-1], image=slugImg, compound="top", text=slugName, bg="#c7c7c7")
        slugImageLabel.pack(side="left")

        if(slugcat["selected"]):
            viewedSaveSlugsFrames[-1].config(bg="#5c5c5c")
            slugImageLabel.config(bg="#5c5c5c")

        karmaLabel = tk.Label(viewedSaveSlugsFrames[-1], text=f"Karma: {int(slugcat['karma'])+1}")
        karmaLabel.pack(anchor="nw")

        foodLabel = tk.Label(viewedSaveSlugsFrames[-1], text=f"Food: {slugcat['food']}")
        foodLabel.pack(anchor="sw")

        lastDen = slugcat["denPos"]
        areaCode = lastDen.split("_")[0]
        areaReadable = areaCodeToReadable[areaCode]
        areaLabel = tk.Label(viewedSaveSlugsFrames[-1], text=f"Area: {areaReadable}")
        areaLabel.pack(anchor="sw")

        denLabel = tk.Label(viewedSaveSlugsFrames[-1], text=f"Den Code: {lastDen}")
        denLabel.pack(anchor="sw")

        viewedSaveCreateMapButton(viewedSaveSlugsFrames[-1], slugName, areaCode, lastDen)



    viewedSaveNameLabel.config(text=saveName.capitalize())

    window.geometry("")

currentSave = fTools.getCurrSaveName()
updateSavesList()
setViewedSave(fTools.getCurrSaveName())
window.mainloop()
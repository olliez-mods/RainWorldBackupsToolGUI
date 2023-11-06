# RainWorld Backups Tool GUI
A tool for RainWorld that allows you to easily create/load/edit/copy your save file. You can have different save files for personal, friends, siblings, etc.


This Python program is based on [RainWorldcheckpointTool](https://github.com/olliez-mods/RainWorldCheckPointTool) also made by me but adds more features such as a functional GUI, and more information on each save and slugcat.
<br/><br/>

## Download: [RainWorldBackupsTool Latest](https://github.com/olliez-mods/RainWorldBackupsToolGUI/releases/latest)
Click [here](https://github.com/olliez-mods/RainWorldBackupsToolGUI/releases/latest) to download the latest version as an EXE.
<br/><br/>

## How to use

When you run the program for the first time it will prompt you to create some files and folders, make sure the path leads to your Rainworld folder (if it doesn't you're out of luck for now).
  
Once you have the window open, you should see the left bar should have one save (probably called "Default") right now you only have one save file, you can rename this if you want, here are the different things you can do with your save.

### Rename A Save
- To rename a save, put the desired name into the text entry box next to the label "Name:", then press "Rename Save"

### Copying A Save
- To create a copy of a save, put the name of the new save into the text box and press "Copy Save" This will create a new save on the left side of the screen, you can click it and view it (Although it will be the same as the other one since it's a copy)
- This is useful if you are at a point that you might want to reload to later if you lose too much karma or key items, etc.

### Select/Load A Save
- NOTE: Please close Rainworld before performing this action since Rainworld could decide to override your save with something else. IMPORTANT.
- This will change the selected save, you can do this by clicking on the save you want to load (the top save in the left-hand menu will always be shaded dark to signify that it's the currently selected one) and then press "Select Save" this will switch out the save.
- Once you select a new save, make sure you restart RainWorld to see this take effect.

### Deleting A Save
- It's as simple as clicking on the save you want to delete (it can't be the currently loaded one) and pressing "Delete Save".

### Override Selected Save
- IMPORTANT: Close Rainworld before using this!
- NOTE: This is a relatively dangerous option so pay attention!
- This option will take the save you are looking at (can't be the loaded save) and will copy itself into the currently loaded save.
- It will override the currently loaded save but will keep the same name.
- This is useful if you want to "quick load" a save repeatedly in a hard section of the game.

### Backups
- Every time "RainWorld Backups Tool" opens it creates a copy of all of your saves and stores it in a backups folder.
- I currently have no plans to create a tutorial on how to restore a backup, please open a discussion if this is urgent.
- The backups folder is located in your Rain World folder (NOT the steam one, but the one in "appdata/Videocult") go to "RWCPsavs/backups" to see all the backups

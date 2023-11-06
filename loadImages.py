from PIL import Image,ImageTk
import sys
import os


def resource_path(relative_path):
    return str(os.path.dirname(sys.executable))+"/"+str(relative_path)


slugImages = {}

def loadSlugImages():
    #icons
    image = Image.open(resource_path("images/survivor_icon.png"))
    image = image.resize((25, 25))
    slugImages["White_icon"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/monk_icon.png"))
    image = image.resize((25, 25))
    slugImages["Yellow_icon"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/hunter_icon.png"))
    image = image.resize((25, 25))
    slugImages["Red_icon"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/gourmand_icon.png"))
    image = image.resize((25, 25))
    slugImages["Gourmand_icon"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/artificer_icon.png"))
    image = image.resize((25, 25))
    slugImages["Artificer_icon"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/rivulet_icon.png"))
    image = image.resize((25, 25))
    slugImages["Rivulet_icon"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/spear_icon.png"))
    image = image.resize((25, 25))
    slugImages["Spear_icon"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/saint_icon.png"))
    image = image.resize((25, 25))
    slugImages["Saint_icon"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/noslug_icon.png"))
    image = image.resize((25, 25))
    slugImages["no_icon"] = ImageTk.PhotoImage(image)


    # portraits
    image = Image.open(resource_path("images/monk_portrait.png"))
    image = image.resize((50, 50))
    slugImages["Yellow_portrait"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/survivor_portrait.png"))
    image = image.resize((50, 50))
    slugImages["White_portrait"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/hunter_portrait.png"))
    image = image.resize((50, 50))
    slugImages["Red_portrait"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/artificer_portrait.png"))
    image = image.resize((50, 50))
    slugImages["Artificer_portrait"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/gourmand_portrait.png"))
    image = image.resize((50, 50))
    slugImages["Gourmand_portrait"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/rivulet_portrait.png"))
    image = image.resize((50, 50))
    slugImages["Rivulet_portrait"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/spear_portrait.png"))
    image = image.resize((50, 50))
    slugImages["Spear_portrait"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/saint_icon.png"))
    image = image.resize((50, 50))
    slugImages["Saint_portrait"] = ImageTk.PhotoImage(image)

    image = Image.open(resource_path("images/noslug_icon.png"))
    image = image.resize((50, 50))
    slugImages["no_portrait"] = ImageTk.PhotoImage(image)
import xml.etree.ElementTree as ET
import re

# looks at the index and finds the next value seperated by <mpdB> or smthng
def getNextValueGivenIndex(saveStr, index):
    nextGT = saveStr.find(">", index)
    thenLT = saveStr.find("<", nextGT)
    return str(saveStr[nextGT+1:thenLT])

def getNextValueGivenTerm(saveStr, str, start_index = 0):
    loc = saveStr.index(">" + str + "<", start_index)+1
    return getNextValueGivenIndex(saveStr, loc)

def getTermLocations(saveStr, term, start_index = 0):
    term = ">" + str(term) + "<"
    locations = []
    while start_index < len(saveStr):
        index = saveStr.find(term, start_index)
        if index == -1:
            break
        locations.append(index+1)
        start_index = index + 1
    return locations

def getSlugCatLocs(saveStr):
    return getTermLocations(saveStr, "SAV STATE NUMBER")
def getSlugCats(saveStr):
    locs = getSlugCatLocs(saveStr)
    slugcats = {}

    curr = getNextValueGivenTerm(saveStr, "CURRENTSLUGCAT")
    for slugLoc in locs:
        name = getNextValueGivenIndex(saveStr, slugLoc)
        food = getNextValueGivenTerm(saveStr, "FOOD", slugLoc)
        denPos = getNextValueGivenTerm(saveStr, "DENPOS", slugLoc)
        karma = getNextValueGivenTerm(saveStr, "KARMA", slugLoc)
        cycleNum = getNextValueGivenTerm(saveStr, "CYCLENUM", slugLoc)
        isSelected = (curr == name)
        
        slugcats[name] = {"slugName":name, "food":food, "denPos":denPos, "karma":karma, "cycleNum":cycleNum, "selected":isSelected}
    return slugcats



def remove_non_ascii(input_string):
    return re.sub(r'[^a-zA-Z0-9_\s.,?!@#$%^&*()_+-=:;\'"<>]+', '', input_string)

def getSaveStringFromFileString(fileString):
    fileString = remove_non_ascii(fileString)
    root = ET.fromstring(fileString)  
    saveStr = ""
    nextIsSave = False
    for element in root.iter():
    #print(f"\n\n{element.tag}: {str(element.text)[:1000]}")

        if(nextIsSave):
            nextIsSave = False
            saveStr = str(element.text)

        if(element.text == "save"):
            nextIsSave = True
    return saveStr

def getSaveStringFromFilePath(path):
    with open(path, 'r') as file:
        xml_data = file.read()
    
    xml_data = remove_non_ascii(xml_data)
    print(xml_data[:100])

    saveString = getSaveStringFromFileString(xml_data)
    return saveString



# locs = getTermLocations("SAV STATE NUMBER")
# print("Selected:", getNextValueGivenTerm("CURRENTSLUGCAT"), "\n")
# for loc in locs:
#     print(getNextValueGivenIndex(loc))
#     print("FOOD:", getNextValueGivenTerm("FOOD", loc))
#     print("KARMA:", getNextValueGivenTerm("KARMA", loc))
#     print("DEN", getNextValueGivenTerm("DENPOS", loc), "\n")
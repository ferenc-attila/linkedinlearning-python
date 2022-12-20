import os

currentDir = os.getcwd()
newDir = "/result" # Erre jo lenne valami szebb, platformfuggetlen megoldas (Windows-on most nem is helyesen mukodik)
resultFileName = currentDir + newDir + "/result.txt"

listOfFiles = os.listdir(currentDir)
for nameOfFileOrFolder in listOfFiles:
    if os.path.isdir(currentDir + "/" + nameOfFileOrFolder):
        listOfFiles.remove(nameOfFileOrFolder)

listOfFilesString = ""
totalByteCount = 0

for fileName in listOfFiles:
    totalByteCount += os.stat(fileName).st_size
    fileName += "\n"
    listOfFilesString += fileName

content = "Total bytecount:" + str(totalByteCount) + "\nFiles list:\n--------------\n" + listOfFilesString

try:
    os.mkdir(currentDir + newDir)
except FileExistsError as fee: # Ezt egy egyszeru ellenorzessel ki lehet kerulni, es abban az esetben elegendo a fajl letrehozasa
    print("Directory exists!")
except FileNotFoundError as fnfe:
    print("Parent directory doesn't exists!")

resultFile = open(resultFileName, "w+")
if resultFile.mode == "w+":
    resultFile.write(content)
    resultFile.close()

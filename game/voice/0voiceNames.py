import os

voiceFolder = "temp/"
nameFile = open("names.txt")
names = [n[:-1] for n in nameFile]

def main():
    for i, filename in enumerate(os.listdir(voiceFolder)):
        newName = names[i] + ".ogg"
        os.rename(voiceFolder + "/" + filename, newName)
main()

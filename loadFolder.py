import os
from os import listdir

    # !  Problem
    #   Select a folder, and get all the .ext files in there, 
    #   and print them in console
    # ?   What this does
    #   This class methods loads all the files in a 
    #   folder with the current extension
    #   and return them as an array

    #  Will also load all subfolders and its files


class Folder(object):

    def __init__(self,path,ext):
        
        self.items = []
        self.itemsPath = []
        self.path = path
        self.ext = ext

        self.allFoldersList = []
        self.allFoldersPath = []
        self.trackedFolderList = False
        
    # Load all subfolders in the entered path
    # this includes the folder name and the folder path
    # and a variable that becomes true if the method was executed
    def loadAllSubfolders(self):
               
        for folder in os.walk(self.path):

            # index 0 prints the full path of folder
            # index 1 prints the full path of subfolders in folder
            # index 2 prints the files in folder

            # print(folder[0]) 
               
            # last ocurrence of \, be said, the folder name, not full path
            getStart = folder[0].rfind('\\')

            # this is a int with the number of chars to the last \
            # print(getStart) 

            # getStart + 1 would be the start of folder name
            # print(folder[0][(getStart + 1):])

            currentFolder = folder[0][(getStart + 1):]

            # if (CHARS.find(currentFolder) == -1):
            self.allFoldersList.append(currentFolder)
            self.allFoldersPath.append(folder[0])
            
            self.trackedFolderList = True 

    # Load all items in the selected folder with the extension of the class
    # Also affects the length property
    def loadItemsSingleFolder(self, selectedPath):

        try:
            for item in os.listdir(selectedPath):
                if(item.endswith(self.ext)):
                    self.items.append(item)
                    self.itemsPath.append(os.path.join(selectedPath, item))

            self.length = len(self.items)
        
        except:
            for item in os.listdir("C:/"):
                if(item.endswith(self.ext)):
                    self.items.append(item)
                    self.itemsPath.append(os.path.join(selectedPath, item))

            self.length = len(self.items)

    # Load all items in all subfolders of the class path
    def loadItemsFolderSubFolders(self):

        self.items.clear()

        if (self.trackedFolderList == True):

            for folderPath in self.allFoldersPath:

                self.loadItemsSingleFolder(folderPath)
        
        else:

            print("Warning: The class method loadAllSubfolders() hasn't been executed, please run it once at least.")

    # Show info of the class
    def showInfo(self):
        print("Extension: " + self.ext)
        print("Path: " + self.path)
        print("Length: " + str(self.length))

        sel = input("Show all items listed? y/n.")

        if (sel == "y" or sel == "Y"):

            print("Items: ")

            for item in self.items:

                print(item)

    # Update the current properties running all the class methods
    def update(self):
            self.loadAllSubfolders()
            self.loadItemsFolderSubFolders()

    # Change the path and the extension
    def changeSettings(self,newPath,newExt):

        self.path = newPath
        self.ext = newExt
        #
        self.update()



# test = Folder("D:\Temp Music", ".mp3")

# test.update()

# test.showInfo()
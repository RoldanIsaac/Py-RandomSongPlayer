import random, os
from importlib.machinery import SourceFileLoader
module = SourceFileLoader("loadFolder","loadFolder.py")

# Set our constants > Our music library folder and the type of files we have in mostly
musicDir = 'D:\Music\Music Library'
ext = '.mp3' 

# Import the class for scanning the library folder
loadFolder = module.load_module()

# Initialize the music library
myMusicLibrary = loadFolder.Folder(musicDir, ext)

# Scan. 
# This methods fetch all files in all subfolders and store 
# them temporary in the class property
myMusicLibrary.update()

# Get all songs in an array 
allSongs = myMusicLibrary.items
# print(len(allSongs))

# Generate a random number from 1 to the length of all songs
# This allows us to select any song randomly
randomSongNumber = random.randint(0, len(allSongs))
print("Random selected song: ", allSongs[randomSongNumber])

# Execute the file with this os method
# Also the items path previously stored all the full paths 
# So passing an index it gives us the full path of the song picked
os.startfile(myMusicLibrary.itemsPath[randomSongNumber])
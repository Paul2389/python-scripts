from tkinter.filedialog import askdirectory
from tkinter import Tk
from importlib.resources import path
import hashlib
import shutil
import time
import os

Tk().withdraw() # File selector popup without full GUI
path = askdirectory(title= "Select A Folder")
destination = os.path.expanduser('~/Desktop/Duplicates/')
duplicateDetected = False

filesDict = dict()
duplicateDict = dict()
pathList = list()
x = 1

# List all folders and files
for folder, sub, file in os.walk(path):
    for filename in file:
        # List the full path of every file
        absolutePath = os.path.join(folder, filename)
        fileHash = hashlib.md5(open(absolutePath, 'rb').read()).hexdigest()
        # Assign key and value to Dictionary
        filesDict[absolutePath] = fileHash

# Take key, value of filesDict and reverse the order to a new Dictionary
for filepath, hash in filesDict.items():
    # If no duplicate just reverse the order
    if hash not in duplicateDict:
        duplicateDict[hash] = [filepath]
    else:
        # If there is duplicate has create a list of path's
        duplicateDict[hash].append(filepath)

# Find the list values of the dictionary
for key, value in duplicateDict.items():
    # If the list contains more than one element
    if len(value) > 1:
        duplicateDetected = True
        pathList.append(value)

# Find if duplicates are present
if len(pathList) > 0 and duplicateDetected == True:
    print('----------------------------------')
    print('Duplicate Files Found.')

    # Folder Creation
    if os.path.exists(destination) is True:
        print('Folder Already Exists. Continue...')
        print('----------------------------------')
    else:
        os.makedirs(destination)
        print('Creating New Folder:', destination)
        print('----------------------------------')

    # Break down 2D list to different lists
    for innerList in pathList:
        # Break down to single list
        for plainFilePath in innerList:
            # Seperate filepath, filename and extension
            filename = str(plainFilePath).split('\\')[-1]
            filePhrase = str(filename).split('.')[0]
            extension = str(filename).split('.')[-1]
            
            # If the same filename exists in destination procceed to rename
            if os.path.isfile(destination + filename):
                print('Same Filename Found in Destination')
                # Start loop of renaming until filename doesn't exist in destination
                while os.path.isfile(destination + filename):
                    rename = filePhrase + '-' + str(x) + '.' + extension
                    print('Filename:', filename, 'Already Exists in:', destination)
                    print('Renaming File To:', rename)
                    time.sleep(1)
                    # If the renaming is successfull break the loop
                    if os.path.isfile(destination + rename) is False:
                        shutil.move(plainFilePath , destination + '/' + rename)
                        print('Moving File To:', plainFilePath , destination + '/' + rename)
                        print('Success!')
                        print('----------------------------------')
                        break
                    x +=1
            else:
                shutil.move(plainFilePath, destination)
                print('Moving file:', plainFilePath, 'To:', destination + filename)
                print('Success!')
                print('----------------------------------')
                continue
else:
    print('----------------------------------')
    print('No Duplicate Files Found. Exiting.')
    print('----------------------------------')
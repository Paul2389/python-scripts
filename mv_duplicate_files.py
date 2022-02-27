from importlib.resources import path
import os
import hashlib

path = (os.path.expanduser('~/Desktop'))
destination = os.path.expanduser('~/Desktop/Duplicates')
duplicateDetected = False

filesDict = dict()
duplicateDict = dict()

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
        # print(value)
        

# FOLDER CREATION
if duplicateDetected == True:
    if os.path.exists(destination) is True:
        print('Duplicates folder already exists in:', destination)

    else:
        os.makedirs(destination)
        print('New Folder Created in:', destination)
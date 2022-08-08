# run this script when you want to copy / move the files from one directory to another directory

destinationDirectory = str(input("Enter the destination directory: "))

# folders to move 
import os 
currentWD = os.getcwd()

folders = os.listdir(currentWD)
# remove .git folder and python transfer script 
folders.remove('.git')
folders.remove('pythonTransferScript.py')

# add the currentWD to each of the files in the folders list
for i in range(len(folders)):
    folders[i] = currentWD + '/' + folders[i]

# based on folders, create a dictionary that determines if each is a FILE or a FOLDER
fileDict = {}
for folder in folders:
    if os.path.isfile(folder):
        fileDict[folder] = 'FILE'
    else:
        fileDict[folder] = 'FOLDER'

# keep only keys that are folders in a new folder list
folderList = []
for key in fileDict:
    if fileDict[key] == 'FOLDER':
        folderList.append(key)

# keep only keys that are files in a new file list
fileList = []
for key in fileDict:
    if fileDict[key] == 'FILE':
        fileList.append(key)

# move each of the FILES in the fileList to the destination directory
for file in fileList:
    os.system('mv ' + file + ' ' + destinationDirectory)
    print('moved ' + file)

# move all of the files within each FOLDER in the folderList to the destination directory
for folder in folderList:
    os.system('mv ' + folder + '/* ' + destinationDirectory)
    print('moved ' + folder)

print('...succesfully transfered everything to: ' + destinationDirectory)
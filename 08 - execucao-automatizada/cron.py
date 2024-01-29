import os

types = ['txt', 'xlsx']

base_path = 'C:\\Sharepoint\\OneDrive\\Downloads'

cwd = os.chdir(base_path)

fileList = os.listdir(cwd)

for type_ in types:
    if type_ not in fileList:
        os.mkdir(type_)

for file in fileList:
    for type_ in types:
        if '.' + type_ in file:
            oldPath = os.path.join(base_path, file)
            newPath = os.path.join(base_path, type_, file)
            os.replace(oldPath, newPath)

import os

#note that there only have to be pictures and folders in your directory

#note that backslashes in path has to be doubled
PATH = 'C:\\Users\\Ines\\Documents\\MartinDokumente\\projects\\Pictures'

#change working directory to PATH
os.chdir(PATH)
print(os.getcwd())

#get elements, what is folder & what is picture?
def getelements():
    elements = (os.listdir())
    pictures = []
    folders = []
    for e in elements:
        try:
            os.chdir(PATH + '\\' + e)
            folders.append(e)
        except NotADirectoryError:
            pictures.append(e)
    return pictures, folders

print(getelements())

#change last element name
#os.rename(elements[-1], 'Zehleabend2016')

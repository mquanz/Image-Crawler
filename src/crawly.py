import os

#note that backslashes in path have to be doubled
PATH = 'C:\\Users\\Ines\\Documents\\MartinDokumente\\projects\\Pictures'

def main():
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

if __name__ == '__main__':
    main()

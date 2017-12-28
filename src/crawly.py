import os
from PIL import Image

#note that backslashes in path have to be doubled
PATH = 'C:\\Users\\Ines\\Documents\\MartinDokumente\\projects\\Pictures'

def main():
    #change working directory to PATH
    os.chdir(PATH)
    print('The PATH is:')
    print(os.getcwd())

    #get elements, what is folder & what is picture?
    def getelements():
        elements = (os.listdir())
        pictures = []
        folders = []
        for e in elements:
            try:
                Image.open(PATH + '\\' + e)
                pictures.append(e)
            except IOError:
                folders.append(e)
        return pictures, folders
    
    #get exif of pictures
    def getexif():
        pic_info = []
        for e in pictures:
            im = Image.open(PATH + '\\' + e)
            pic_info.append(im.format + str(im.size) + im.mode + ' ' + im._getexif()[36867])
        return pic_info

    #change last element name
    #os.rename(elements[-1], 'Zehleabend2016')
   
    pictures, folders = getelements()
    print('\nPictures')
    print(pictures)
    print('\nFolders')
    print(folders)

    print('\nEXIFs:')
    print(getexif())

if __name__ == '__main__':
    main()

import os
from PIL import Image
from collections import Counter


def main():
    #note that backslashes in PATH have to be doubled
    PATH = 'C:\\Users\\Ines\\Documents\\MartinDokumente\\projects\\Pictures'
    
    #change working directory to PATH
    def change_directory():
        os.chdir(PATH)
        print('The working directory is changed to:')
        print(os.getcwd())

    #get elements in PATH, what is folder & what is picture?
    def getelements():
        pictures = []
        folders = []
        for e in os.listdir():
            try:
                Image.open(PATH + '\\' + e)
                pictures.append(e)
            except IOError:
                folders.append(e)
#        for e in folders:
#            try:
#                os.chdir(PATH + '\\' + e)
#            except NotADirectoryError:
#                print(e + ' is not a folder.')
        return pictures, folders

    #get exif of unsorted pictures in PATH
    def getexif(picture_list):
        pic_info = []
        for e in picture_list:
            im = Image.open(PATH + '\\' + e)
            pic_info.append((im._getexif()[36867], im.format, im.size, im.mode))
        return pic_info

    #arrange unsorted pictures to folder
    def arrange(pic_info, picture_list):
        #when there are no unsorted pictures code wont be executed
        if picture_list != []:
            years = []
            for e in pic_info:
                years.append(int(e[0][0:e[0].find(':')]))
            #get most common year in years
            folder_name = str(Counter(years).most_common(1)[0][0])
            #create new folder
            if not os.path.exists(PATH + '\\' + folder_name):
                os.makedirs(PATH + '\\' + folder_name)
            for e in picture_list:
                os.rename(PATH + '\\' + e, PATH + '\\' + folder_name + '\\' + e)
    
    #change last element name
    #os.rename(elements[-1], 'newname')

    #Test
    change_directory()
    print('\nPictures')
    print(getelements()[0])
    print('\nFolders')
    print(getelements()[1])
    print('\nEXIFs:')
    print(getexif(getelements()[0]))
#    arrange(getexif(getelements()[0]), getelements()[0])

if __name__ == '__main__':
    main()

import os
from PIL import Image
from collections import Counter


def main():
    #note that backslashes in START_PATH have to be doubled
    START_PATH = 'C:\\Users\\Ines\\Documents\\MartinDokumente\\projects\\Pictures'
    
    #change working directory to START_PATH
    def change_directory():
        os.chdir(START_PATH)
        print('The working directory is changed to:')
        print(os.getcwd())

    #get elements in PATH, what is folder & what is picture?
    def getelements(PATH):
        pictures = []
        folders = []
        for e in os.listdir():
            try:
                Image.open(PATH + '\\' + e)
                pictures.append(e)
            except IOError:
                if os.path.isdir(PATH + '\\' + e):
                    folders.append(e)
        return pictures, folders

    #get exif of unsorted pictures in PATH
    def getexif(PATH, picture_list):
        pic_info = []
        for e in picture_list:
            im = Image.open(PATH + '\\' + e)
            pic_info.append((im._getexif()[36867], im.format, im.size, im.mode))
        return pic_info

    #arrange unsorted pictures to folder
    def arrange(PATH, pic_info, picture_list):
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
    pictures = getelements(START_PATH)[0]
    folders = getelements(START_PATH)[1]
    EXIFs = getexif(START_PATH, pictures)
    print('\nPictures:\n' + str(pictures))
    print('\nFolders:\n' + str(folders))
    print('\nEXIFs:\n' + str(EXIFs))
    
#    arrange(START_PATH, EXIFs, pictures)

if __name__ == '__main__':
    main()

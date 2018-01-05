import os
from PIL import Image
from collections import Counter


def main():
    #note that backslashes in PATH's have to be doubled
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
        for e in os.listdir(PATH):
            try:
                Image.open(PATH + '\\' + e)
                pictures.append(e)
            except IOError:
                if os.path.isdir(PATH + '\\' + e):
                    folders.append(e)
        return pictures, folders

    #get exif of pictures in PATH
    def getexif(PATH, picture_list):
        pic_info = []
        for e in picture_list:
            #opening image with PIL
            im = Image.open(PATH + '\\' + e)
            try:
                pic_info.append(im._getexif()[36867])
            #TypeError occurs, when picture dont have a recording date
            except TypeError:
                print(e + ' has a TypeError, the picture doesn´t have a recording date.')
            #KeyError occurs, wheb fotos taken by some new cameras having different exif location
            except KeyError:
                print(e + ' has a KeyError! Program doesn´t find the EXIF location.')
        return pic_info

    #arrange unsorted pictures to folder named by most common year of recording date
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
                
    #list all files starting with PATH (normally START_PATH)
    def crawl(PATH):
        for root, dirs, files in os.walk(PATH):
            #sort unsorted pictures in START_PARH
            if root is START_PATH:
                pictures = getelements(root)[0]
                EXIFs = getexif(root, pictures)
                arrange(root, EXIFs, pictures)
            else:
                pictures = getelements(root)[0]
                print('\n' + root)
                print(pictures)
                print(getexif(root, pictures))

    
    #change last element name
    #os.rename(elements[-1], 'newname')

    #Test
    change_directory()
    crawl(START_PATH)
#    pictures = getelements(START_PATH)[0]
#    folders = getelements(START_PATH)[1]
#    EXIFs = getexif(START_PATH, pictures)
#    print('\nPictures:\n' + str(pictures))
#    print('\nFolders:\n' + str(folders))
#    print('\nEXIFs:\n' + str(EXIFs))
    
#    arrange(START_PATH, EXIFs, pictures)

if __name__ == '__main__':
    main()

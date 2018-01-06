import os
import re
from PIL import Image
from collections import Counter


def main():
    #note that backslashes in PATH's have to be doubled
    START_PATH = 'C:\\Users\\Ines\\Documents\\MartinDokumente\\projects\\Pictures'

    ERRORS = []
    
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
        picture_info = []
        for e in picture_list:
            #opening image with PIL
            im = Image.open(PATH + '\\' + e)
            try:
                picture_info.append(im._getexif()[36867])
            #TypeError occurs, when picture dont have a recording date
            except TypeError:
                ERRORS.append('\n' + e + ' has a TypeError, the picture doesn´t have a recording date.')
            #KeyError occurs, wheb fotos taken by some new cameras having different exif location
            except KeyError:
                ERRORS.append('\n' + e + ' has a KeyError! Program doesn´t find the EXIF location.')
        return picture_info

    #arrange unsorted pictures to folder named by most common year of recording date
    def arrange(PATH, picture_info, picture_list):
        #when there are no unsorted pictures code wont be executed
        if picture_list != []:
            years = []
            for e in picture_info:
                #most EXIFs using : as separator for dates, other will be ignored
                try:
                    years.append(int(e[:e.find(':')]))
                except ValueError:
                    ERRORS.append('\n' + e + 'has a strange separator and will be ignored.')
            #get most common year in years
            folder_name = str(Counter(years).most_common(1)[0][0])
            #create new folder
            if not os.path.exists(PATH + '\\' + folder_name):
                os.makedirs(PATH + '\\' + folder_name)
            for e in picture_list:
                os.rename(PATH + '\\' + e, PATH + '\\' + folder_name + '\\' + e)

    def rename_folder(PATH, picture_info, picture_list):
        #when there are no unsorted pictures or no EXIF´s code won´t be executed
        if picture_info != []:
            years = []
            for e in picture_info:
                #most EXIFs using : as separator for dates, other will be ignored
                try:
                    years.append(int(e[:e.find(':')]))
                except ValueError:
                    ERRORS.append('\n' + e + 'has a strange separator and will be ignored.')
            #get most common year in years
            year = str(Counter(years).most_common(1)[0][0])
            #look for date in old foldername and if there is no number rename folder
            old_name = os.path.basename(os.path.normpath(PATH))
            if not re.search('\d+', old_name):
                try:
                    os.rename(PATH, PATH + ' ' + year)
                except PermissionError:
                    ERRORS.append('Impossible to change name of ' + old_name + '. I don´t have the permission...')
                
    #crawl through directories starting with START_PATH                 
    def crawl():
        for root, dirs, files in os.walk(START_PATH):
            #sort unsorted pictures in START_PARH
            if root is START_PATH:
                pictures = getelements(root)[0]
                EXIFs = getexif(root, pictures)
                arrange(root, EXIFs, pictures)
            else:
                pictures = getelements(root)[0]
                EXIFs = getexif(root, pictures)
                rename_folder(root, EXIFs, pictures)
                

    #Test
    change_directory()
    crawl()

    print('\nERRORS:')
    for e in ERRORS:
        print(e)

if __name__ == '__main__':
    main()

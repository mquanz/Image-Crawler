import functions as f

def main():
    print('Hello, I´m Crawly & I will help you with organizing your pictures.')
    print('I do the following things: \n-move unsorted pictures in your start path into a new folder named by the most common recording date of those pictures and\n-rename folders (which don´t have a date yet) by the most common recording date of pictures in that folder.')
    print('You just need to enter a Path, where I´m going to start crawl. Please use Backslashes to separate the folders in your path.')

    USER_PATH = input('> ')
    while True:
        try:
            f.change_directory(USER_PATH)
            break
        except FileNotFoundError:
            print('Please try again')
            USER = input('> ')

    START_PATH = USER_PATH

    f.crawl(START_PATH)

    print('\nJust finished crawling! Check out the Errors.')

    print('\n\nERRORS:')
    for e in f.ERRORS:
        print(e)

if __name__ == '__main__':
    main()

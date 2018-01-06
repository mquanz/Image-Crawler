import functions as f

def main():
    #note that backslashes in PATH's have to be doubled
    START_PATH = 'C:\\Users\\Ines\\Documents\\MartinDokumente\\projects\\Pictures'

    #Test
    f.change_directory(START_PATH)
    f.crawl(START_PATH)

    print('\nERRORS:')
    for e in f.ERRORS:
        print(e)

if __name__ == '__main__':
    main()

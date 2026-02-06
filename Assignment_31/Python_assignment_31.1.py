'''
1. Design automation script which accepts directory name and file extension from user. 
Display all files with that extension.
- Usage: DirectoryFileSearch.py "Demo" ".txt"
- Demo is the name of the directory and .txt is the extension that we want to search.
'''

import sys
import logging
import os

def DirectoryFileSearch(DirectoryName , Extension):
    
    if os.path.exists(DirectoryName):

        if(os.path.isdir(DirectoryName)):

            logging.info("File Names ending with extension "+Extension+" are :")
            for folderName, subfolderName , FileName in os.walk(DirectoryName):

                for file in FileName:

                    if(file.endswith(Extension)):
                        logging.info(file)

        else:
            logging.critical(f"Given {DirectoryName} is not a directory")
            return
        
    else:
        logging.critical("Path does not exists")
        return
    
    
    
def setup_logging(filename="DirectoryFileSearch.log"):
    logging.basicConfig(filename=filename, 
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='a')
    

def main():
    setup_logging()

    if (len(sys.argv) != 3):
        logging.info("Invalid arguments")
        logging.info("--usage: command file_name.py directory_name extension ")
        return
    
    directory_name = sys.argv[1]
    extension = sys.argv[2]

    DirectoryFileSearch(directory_name,extension)

if __name__ == "__main__":
    main()  

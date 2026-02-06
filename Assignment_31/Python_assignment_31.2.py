'''
2. Design automation script which accept directory name and two file extensions from user. 
Rename all files with first file extension with the second file extenntion.

Usage: DirectoryRename.py "Demo" ".txt" ".doc"

Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
After execution this script each .txt file gets renamed as .doc.
'''

import sys
import os
import logging

def DirectoryRename(DirectoryName , OldExt , NewExt):

    if(os.path.exists(DirectoryName)):

        if(os.path.isdir(DirectoryName)):
            
            logging.info("from Directory: "+DirectoryName+" renaming the Extension: "+OldExt+" files with: "+NewExt)

            for FolderName, SubfolderName,fileName in os.walk(DirectoryName):

                for file in fileName:
                    
                    if(file.endswith(OldExt)):
                        oldpath = os.path.join(FolderName,file) 
                        logging.info({oldpath})
                        newfileName = file.replace(OldExt,NewExt)
                        newpath = os.path.join(FolderName,newfileName)
                        os.rename(oldpath,newpath)
                        logging.info(f"Renamed file {file} to {newfileName}")
            
            logging.info("Done with the renaming of extensions")


        else:
            logging.info(DirectoryName+" is not a Directory ")
            return 
        
    else:
        logging.info(DirectoryName+" This directory does not exixts")
        return
        
def setup_logging(filename="DirectoryRename.log"):
    logging.basicConfig(filename=filename, 
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='a')
            

def main():

    setup_logging()

    if(len(sys.argv) != 4):
        logging.info("Invalid arguments")
        logging.info("--usage: command file_name.py directory_name old_extension new_extension ")
        return
    
    directory_name = sys.argv[1]
    old_extension = sys.argv[2]
    new_extension = sys.argv[3]

    DirectoryRename(directory_name, old_extension , new_extension)

if __name__ == "__main__":
    main()
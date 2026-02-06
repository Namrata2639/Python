'''
Q.1 Design automation script which accept directory name and display checksum of all files.
Usage : DirectoryChecksum.py "Demo"
Demo is name of directory.
'''

import logging
import sys
import os
import hashlib


def CalculateChecksum(filename):

    if(os.path.exists(filename)):
        fobj = open(filename,'rb')

        hobj = hashlib.md5()

        buffer = fobj.read(1000)

        while len(buffer) > 0:
            hobj.update(buffer)
            buffer = fobj.read(1000)

        checksum = hobj.hexdigest()
        logging.info(f"Checksum of file {filename} is {checksum}")
        fobj.close()

    else:
        logging.info(filename+ "this does not exists")
        return
    
def DisplayChecksum(directory):
    if(os.path.exists(directory)):
        if(os.path.isdir(directory)):

            for FolderName, SubfolderName, FileName in os.walk(directory):

                for file in FileName:

                    filepath = os.path.join(FolderName,file)
                    CalculateChecksum(filepath)

            logging.info("Checksum calculation completed for all files")

        else:
            logging.info(directory+" is not a directory")
            return 


    else:
        logging.info(directory+ "this directory does not exists")
        return


def setup_logging(filename="DirectoryChecksum.log"):
    logging.basicConfig(filename=filename,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='a')
    
def main():

    setup_logging()

    if len(sys.argv) != 2:
        logging.warning("Invalid number of arguments")
        logging.info("Usage: filename.py <Directory_Name>")
        return
    

    DisplayChecksum(sys.argv[1])

if __name__ == "__main__":
    main()
    
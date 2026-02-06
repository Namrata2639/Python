'''
Q.2
Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt. 
Log.txt file should be created into current directory.
Usage : DirectoryDuplicate.py "Demo"
Demo is name of directory.
'''

import logging
import sys
import os
import hashlib

def calculate_checksum(filename):
    fobj = open(filename,'rb')

    hobj = hashlib.md5()
    buffer = fobj.read(1000)

    while len(buffer)>0 :
        hobj.update(buffer)
        buffer = fobj.read(1000)

    fobj.close()
    logging.info(f"Checksum calculated successfully for file {filename}")

    return hobj.hexdigest()

def Find_Duplicate(DirName):

    if (os.path.exists(DirName)):
        if (os.path.isdir(DirName)):

            duplicates = {}
            logging.info(f"Finding duplicate files in directory {DirName}")
            for FolderName,SubFolderName,FileName in os.walk(DirName):

                for Fname in FileName:

                    Fname = os.path.join(FolderName,Fname)
                    Checksum = calculate_checksum(Fname)

                    if  Checksum in duplicates:
                        duplicates[Checksum].append(Fname)

                    else:
                        duplicates[Checksum] = [Fname]

            logging.info("Duplicate files found successfully")

            return duplicates
                    
        else:
            logging.info(DirName+" is not a directory")
            return 
    else:
        logging.info(DirName+ "No such Directory Exists")
        return 

def Add_duplicates(DirName):

    Mydict = Find_Duplicate(DirName)
    # print(Mydict)

    Result = list(filter(lambda x : len(x)>1 ,Mydict.values()))
    # print(Result)

    count = 0

    for value in Result:
        for subvalue in value:
            count = count+1
            if count>1:
                fobj = open("Log.txt",'a')
                fobj.write(subvalue + "\n") 
                fobj.close()
                logging.info(f"Duplicate file {subvalue} added to log file successfully")
        count = 0



def setup_logging(filename="Duplicate.log"):
    logging.basicConfig(filename=filename,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='a')
     
def main():
    setup_logging()

    if len(sys.argv) != 2:
        logging.info("Invalid number of arguments")
        logging.info("Usage: DirectoryDuplicate.py <Directory_Name>")
        return

    DirName = sys.argv[1]

    Add_duplicates(DirName)


if __name__ == "__main__":
    main()
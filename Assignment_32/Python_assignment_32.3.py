'''
Q.3Design automation script which accept directory name and delete all duplicate files from that directory.
 Write names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory.
Usage : DirectoryDuplicateRemoval.py "Demo"
'''
import logging
import sys
import os
import hashlib

def calculate_checksum(filename):

    with open(filename,'r') as fobj:

        hobj = hashlib.md5()
        buffer = fobj.read(1000)

        while len(buffer)>0 :
            hobj.update(buffer.encode())
            buffer = fobj.read(1000) 
        fobj.close()
        logging.info(f"Checksum calculated successfully for file {filename}")
        
        return hobj.hexdigest()


def find_duplicate(DirName):

    if not os.path.exists(DirName):
        logging.info(DirName+ "No such Directory Exists")
        return
    
    if not os.path.isdir(DirName):
        logging.info(DirName+" is not a directory")
        return
    
    duplicates = {}
    logging.info(f"Finding duplicate files in directory {DirName}")
    for FolderName,SubFolderName,FileName in os.walk(DirName):

        for Fname in FileName:

            Fname = os.path.join(FolderName,Fname)
            Checksum = calculate_checksum(Fname)

            if  Checksum in duplicates:
                duplicates[Checksum].append(Fname) 

            else:
                duplicates[Checksum]= [Fname] 

    logging.info("Duplicate files found successfully")
    return duplicates

def delete_duplicate(DirName):
    my_dict = find_duplicate(DirName)

    Result = list(filter(lambda x : len(x)>1 ,my_dict.values()))
    
    count = 0
    for value in Result:
        for subvalue in value:
            count = count+1
            if count>1:
                fobj = open("Log.txt",'a')
                fobj.write(subvalue + "\n") 
                fobj.close()
                logging.info(f"Duplicate file {subvalue} added to log file successfully")
                os.remove(subvalue)
                logging.info(f"Duplicate file {subvalue} removed successfully")
        count = 0
    

def setup_logging(filename="DirectoryDuplicateRemoval.log"):
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'
    )

def main():

    setup_logging()

    if(len(sys.argv) != 2):
        logging.warning("Invalid number of arguments")
        logging.info("Usage: Filename.py <Directory_Name>")
        return

    Dir_name = sys.argv[1]

    delete_duplicate(Dir_name)

if __name__ == "__main__":
    main()
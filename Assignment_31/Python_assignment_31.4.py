'''
Q.4 Design automation script which accept two directory names and one file extension.
Copy all files with the specified extension from first directory into second directory.
Second directory should be created at run time.
Usage: DirectoryCopyExt.py "Demo" "Temp" ".exe"

Demo is name of directory which is existing and contains files in it.
 We have to create new Directory as Temp and copy all files with extension .exe from Demo to Temp.
 
'''


import logging
import sys      
import os

def CreateDirectory(SrcDict,DestDict,Extension):

    if(os.path.exists(SrcDict)):
        if(os.path.isdir(SrcDict)):

            for FolderName, SubfolderName, FileName in os.walk(SrcDict):

                for file in FileName:

                    if(file.endswith(Extension)):

                        srcpath = os.path.join(FolderName,file)
                        destpath = os.path.join(DestDict,file)

                        if not os.path.exists(DestDict):
                            os.mkdir(DestDict)
                            logging.info(f"Directory {DestDict} created successfully")

                        fobjsrc = open(srcpath,'r')
                        fobjdest = open(destpath,'w')

                        fobjdest.write(fobjsrc.read())
                        fobjdest.close()
                        fobjsrc.close()
                    
                        logging.info(f"File {file} copied successfully from {SrcDict} to {DestDict}")

            logging.info("All files copied successfully")

        else:
            logging.info(SrcDict+" is not a directory")
            return 


    else:
        logging.info(SrcDict+ "this directory does not exists")
        return

def setup_logging(filename="CreateDirectory1.log"):
    logging.basicConfig(filename=filename,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='a'
                        )

def main():
    setup_logging()

    if(len(sys.argv) != 4):
        logging.info("Invalid arguments")
        logging.info("--usage: command file_name.py source_directory destination_directory extension ")
        return

    srcdict = sys.argv[1]
    destdict = sys.argv[2]
    extension = sys.argv[3]

    CreateDirectory(srcdict,destdict,extension)


if __name__ == "__main__":
    main()
'''
Q3) Copy File Contents into a New File (Command Line)
Problem Statement:
Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.
Input (Command Line):
ABC.txt
Expected Output:
Create Demo.txt and copy contents of ABC.txt into Demo.txt.
'''
import sys
import os

def CopyContent(FileName):

    if os.path.exists(FileName):

        fobj1 = open(FileName,"r")
        Data1 = fobj1.read()

        fobj2 = open("Demo.txt",'w')
        fobj2.write(Data1)

    else:
        print(FileName," this file does not exists")
        return


def main():

    if ((len(sys.argv) > 2) | (len(sys.argv) <= 1) ):
        print("Invalid Number or argumnets")
        return
    
    fname = sys.argv[1]
    CopyContent(fname)

if __name__ == "__main__":
    main()
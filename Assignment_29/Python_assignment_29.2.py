'''
Q2) Display File Contents
Problem Statement:
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
Input:
Demo.txt
Expected Output:
Display contents of Demo.txt on console.
'''

import os

def readFile(FileName):

    if os.path.exists(FileName):
        fobj = open(FileName,'r')
        Data = fobj.read()

        print(f"Data from {FileName} is : {Data}")

    else:
        print("File does not exists")
        return


def main():
    
    fName = input("Enter FileName: ")

    readFile(fName)

if __name__ == "__main__":
    main()
'''
Q1) Check File Exists in Current Directory
Problem Statement:
Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
Input:
Demo.txt
Expected Output:
Display whether Demo.txt exists or not.
'''

import os

def ChkFileExists(FileName):
    return os.path.exists(FileName)

def main():

    filename = input("Eneter File name: ")

    ret = ChkFileExists(filename)

    if ret == True:
        print(filename," Exists")

    else:
        print(filename," does not Exists")

if __name__ == "__main__":
    main()


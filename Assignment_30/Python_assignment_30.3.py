'''
Q3) Display File Line by Line
Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
Input:
Demo.txt
Expected Output:
Display each line of Demo.txt one by one.
'''

import os 

def Disply_lines(Fname):

    if os.path.exists(Fname):

        fobj = open(Fname,'r')

        for lines in fobj:
            print(lines,end=" ")

    else:
        print("File does not exists")
        return

def main():

    Fname = input("Enter The file name: ")
    Disply_lines(Fname)

if __name__ == "__main__":
    main()
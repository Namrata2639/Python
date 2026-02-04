'''
Q1) Count Lines in a File
Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file.
Input:
Demo.txt
Expected Output:
Total number of lines in Demo.txt

'''

import os 

def Count_number_lines(Fname):

    if(os.path.exists(Fname)):

        fobj = open(Fname,'r')
        count = 0
        for line in fobj:
            count = count + 1

        return count

    else:
        print("File does not exists")
        return 


def main():

    Fname = input("Enter file Name: ")
    number_lines = Count_number_lines(Fname)
    print(f"Total number of lines in {Fname} is: {number_lines}")

if __name__ == "__main__":
    main()




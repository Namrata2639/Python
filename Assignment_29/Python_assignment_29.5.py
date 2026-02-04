'''
Q5) Frequency of a String in File
Problem Statement:
Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
Input:
Demo.txt Marvellous
Expected Output:
Count how many times "Marvellous" appears in Demo.txt.

'''

import os

def countOccurences(Fname,string):

    if os.path.exists(Fname):

        fobj = open(Fname,"r")
        count  = 0

        for line in fobj:
            words = line.split()
            for word in words:
                if word == string:
                    count = count + 1
                
        print(f"Occurences of {string} in {Fname} are: {count}")
    

    
    else:
        print("File does not exists")


def main():

    FileName = input("Enter the FileName: ")
    str = input("Enter a string to find occurences: ")
    
    countOccurences(FileName,str)

    

if __name__ == "__main__":
    main()




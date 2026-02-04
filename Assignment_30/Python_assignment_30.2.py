'''
Q2) Count Words in a File
Problem Statement:
Write a program which accepts a file name from the user and counts the total number of words in that file.
Input:
Demo.txt
Expected Output:
Total number of words in Demo.txt.

'''

import os 

def Count_words(Fname):

    if(os.path.exists(Fname)):

        fobj = open(Fname,'r')
        count = 0
        for line in fobj:
            words = line.split()
            print(type(words))
            for word in words :
                count = count + 1

        return count

    else:
        print("File does not exists")
        return 


def main():

    Fname = input("Enter file Name: ")
    numberof_words = Count_words(Fname)
    print(f"Total number of lines in {Fname} is: {numberof_words}")

if __name__ == "__main__":
    main()

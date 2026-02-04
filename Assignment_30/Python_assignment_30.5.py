'''
Q5) Search a Word in File
Problem Statement:
Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
Input:
Demo.txt Marvellous
Expected Output:
Display whether the word Marvellous is found in Demo.txt or not.
'''

import os

def Search_word(Filename,GivenWord):

    if(os.path.exists(Filename)):

        fobj = open(Filename,"r")

        for lines in fobj:
            words = lines.split()

            for word in words:
                if word == GivenWord:
                    return True
            
        return False

                
    else:
        print("File does not exists")
        return


def main():
    
    Fname = input("Enter the file Name: ")
    word = input("Enter the word to search in file: ")

    found = Search_word(Fname,word)

    if(found == True):
        print(f"Word {word} is found in file {Fname}")   

    elif(found == False):
        print(f"Word {word} is not found in file {Fname}")
    

if __name__ == "__main__":
    main()
'''
Q4) Copy File Contents into Another File
Problem Statement:
Write a program which accepts two file names from the user.
- First file is an existing file
- Second file is a new file
Copy all contents from the first file into the second file.
Input:
ABC.txt Demo.txt
'''
import os

def Copy_data(File1,File2):

    if os.path.exists(File1):

        fobj1 = open(File1,'r')
        data = fobj1.read()
        
        fobj2 = open(File2,'w')
        fobj2.write(data)
        print(f"Data copying from {File1} to {File2} is completed")

    else:
        print("File does not exists")
        return 

def main():

    file1 = input("Enter Existing file name: ")
    file2 = input("Enetr the file name where you want to copy the data: ")

    Copy_data(file1,file2)


if __name__ == "__main__":
    main()
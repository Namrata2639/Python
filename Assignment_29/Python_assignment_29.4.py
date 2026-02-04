'''
Q4) Compare Two Files (Command Line)
Problem Statement:
Write a program which accepts two file names through command line arguments and compares the contents of both files.
- If both files contain the same contents, display Success
- Otherwise display Failure
Input (Command Line):
Demo.txt Hello.txt
Expected Output:
Success OR Failure

'''
import sys
import os

def CompareFiles(File1,File2):

    if(os.path.exists(File1) & os.path.exists(File2)):

        fobj1 = open(File1,"r")
        Data1 = fobj1.read()

        fobj2 = open(File2,"r")
        Data2 = fobj2.read()

        if Data1 == Data2:
            return True
        
        else:
            return False
        
    else:
        print("File does not exists")
        return
    
def main():

    if ((len(sys.argv) >= 4) | (len(sys.argv) <= 1) | (len(sys.argv) == 2) ):
        print("Invalid Number of arguments")
        return 
    
    elif (len(sys.argv) == 3):
        
        FileName1 = sys.argv[1]
        FileName2 = sys.argv[2]

        Ans = CompareFiles(FileName1,FileName2)

        if(Ans == True):
            print("SUCCESS: Contents of both the files is same ")

        elif( Ans ==False):
            print("Failure: Contents of both of the files is different ")

if __name__ == "__main__":
    main()

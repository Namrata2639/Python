# Write a program which accept one character and checks whether it is voewl or consonant
# Input : a
# Output: Voewl

def CheckChar(char):

    if(char in ['a','e','i','o','u','A','E','I','O','U']):
        return True
    else:
        return False

def main():

    value = " "
    Ans = False

    print("Enter a Character: ")
    value = input()

    Ans = CheckChar(value)
    
    if(Ans == True):
        print(value, "is a voewl")
    else:
        print(value,"is a consonant")
        
if __name__ == "__main__":
    main()
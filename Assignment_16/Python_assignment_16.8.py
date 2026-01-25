# Write a program which accepts a number from user and prints that number of * on screen.
# Example:
# #Input : 5  
# Output : *  *  *  *  *

def Pattern(Num):
    for i in range(Num):
        print("*",end=" ")

def main():
    Value = 0

    Value = int(input("Enter a Number: "))

    Pattern(Value)

if __name__ == "__main__":
    main()
'''
2. Write a program which accepts one number and displays the below pattern.
Example:
Input : 5
Output :
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

def Pattern(Num):
    for i in range(Num):
        for j in range(Num):
            print("*",end=" ")
        print()


def main():
    Value = 0

    Value = int(input("Enter a Number: "))

    Pattern(Value)

if __name__ == "__main__":
    main()
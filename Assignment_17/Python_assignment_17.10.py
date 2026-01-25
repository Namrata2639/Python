'''
10. Write a program which accepts a number from user and returns addition of digits in that number.
Example:
Input : 5187934
Output : 37
'''

def add_digits(Num):
    add = 0
    digit = 0

    while Num:
        digit = Num %10
        add = add + digit
        Num = int(Num/10)

    return add

def main():
    Value = 0
    Ret = 0

    print("Enter a Number")
    Value = int(input())

    Ret = add_digits(Value)
    print("Addition of Digits is: ",Ret)

if __name__ == "__main__":
    main()
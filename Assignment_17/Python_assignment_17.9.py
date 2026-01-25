'''
9. Write a program which accepts a number from user and returns number of digits in that number.
Example:
Input : 5187934
Output : 7
'''

def num_digits(Num):
    count = 0

    while Num:
        Num = int(Num/10)
        count += 1

    return count

def main():
    Value = 0
    Ret = 0

    print("Enter a Number")
    Value = int(input())

    Ret = num_digits(Value)
    print("Number of Digits are: ",Ret)

if __name__ == "__main__":
    main()
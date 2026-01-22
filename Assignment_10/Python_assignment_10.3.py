# write a program which accepts one number and print Factorial of that number.
# Input : 5
# Output: 120

def Factorial(Num):
    Ans = 1

    while(Num):
        Ans = Ans * Num
        Num = Num - 1

    return Ans

def main():
    Value = 0
    Res = 0

    print("Enter a number: ")
    Value = int(input())

    Res = Factorial(Value)
    print("Factorial is :",Res)

if __name__ == "__main__":
    main()
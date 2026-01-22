# write a program which accepts one number and print sum of first N natural numbers.
# Input : 5
# Output: 15

def SumNaturalNum(Num):
    Sum = 0

    while(Num):
        Sum = Sum + Num
        Num = Num - 1

    return Sum

def main():
    Value = 0
    Res = 0

    print("Enter a number: ")
    Value = int(input())

    Res = SumNaturalNum(Value)
    print("Sum is :",Res)

if __name__ == "__main__":
    main()
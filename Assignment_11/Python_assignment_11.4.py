# write a program which accept one number and prints reverse of that number.
# Input: 123
# Output: 321

def reverse(Num):

    Ans = 0
    digits = 0

    while(Num):
        digits = Num % 10
        Ans = Ans * 10 + digits
        Num = int(Num / 10)
    
    return Ans


def main():

    Value = 0
    Ret = 0

    print("enter a number: ")
    Value = int(input())

    Ret = reverse(Value)

    print("Reverse value of ",Value,"is: ",Ret)



if __name__ == "__main__":
    main()
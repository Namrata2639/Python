# write a program which accepts one number and checks whether is is palindrome or not .
# Input: 121
# Output: palindrome

def Palindrome(Num):

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

    Ret = Palindrome(Value)

    if(Ret == Value):
        print(Value,"is a palindrome")
    else:
        print(Value,"is not  a palindrome")

if __name__ == "__main__":
    main()
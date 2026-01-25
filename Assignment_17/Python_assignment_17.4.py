'''
4. Write a program which accepts one number from user and returns addition of its factors.
Example:
Input : 12
Output : 16   (1+2+3+4+6)
'''

def Add_factors(Num):
    ans = 0
    for i in range (1,(int(Num/2)+1)):
        if(Num % i == 0):
            ans = ans + i

    return ans

def main():
    Value = 0
    Res = 0

    Value = int(input("Enter a Number to find out the Addition of its factors: "))

    Res = Add_factors(Value)
    print("Addition of factors is : ",Res)

if __name__ == "__main__":
    main()





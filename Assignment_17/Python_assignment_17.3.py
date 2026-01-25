'''
3. Write a program which accepts one number from user and returns its factorial.
Example:
Input : 5
Output : 120
'''

def Factorial(Num):
    ans = 1

    for i in range (1,Num+1):
        ans = ans *i

    return ans

def main():
    Value = 0
    Res = 0

    Value = int(input("Enter a Number to find out its factorial: "))

    Res = Factorial(Value)
    print("Factorial is : ",Res)

if __name__ == "__main__":
    main()
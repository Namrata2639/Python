# Write a program which accepts one number and checks weather is prime number or not
# Input: 11
# output: Prime Number

# numbers which are less than or equal to 1 are not prime number

import math 

def Prime(Num):

    if(Num <= 1):
        return False
    
    for i in range(2,int(math.sqrt(Num))+1):
        if(Num % i == 0):
            return False
        
    return True 


def main():
    Value = 0
    Ret = False

    Value = int(input("Enter a number: "))

    Ret = Prime(Value)

    if(Ret == True):
        print(Value ,"is a prime number.")
    else:
        print(Value,"is not a prime number.")
    
if __name__ == "__main__":
    main()
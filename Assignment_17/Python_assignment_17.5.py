'''
5. Write a program which accepts one number from user and checks whether number is prime or not.
Example:
Input : 5
Output : It is Prime Number
'''

def Prime_num(Num):

    for i in range(2,Num):
        if(Num % i == 0 ):
            return False
        
    return True


def main():
    Value = 0
    Res = False

    Value = int(input("Enter a Number: "))

    Res = Prime_num(Value)

    if (Res == True):
        print(Value,"is prime number")
    
    else:
        print(Value,"not is prime number")

    

if __name__ == "__main__":
    main()

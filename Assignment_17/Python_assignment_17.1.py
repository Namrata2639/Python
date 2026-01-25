'''
1. Create one module named as Arithmetic which contains 4 functions:
- Add() for addition
- Sub() for subtraction
- Mult() for multiplication
- Div() for division
All functions accept two parameters as numbers and perform the operation.
Write one Python program which calls all the functions from Arithmetic module by accepting the parameters from user.
'''

import Arithematic

def main():
    Num1 = 0
    Num2 = 0

    print("Enter First Number: ")
    Num1 = int(input())

    print("Enter second Number: ")
    Num2 = int(input())

    add = Arithematic.Add(Num1,Num2)
    print("Addition of",Num1,"&",Num2,"Is : ",add)

    sub = Arithematic.Sub(Num1,Num2)
    print("Substraction of",Num1,"&",Num2,"Is : ",sub)

    mul = Arithematic.Mul(Num1,Num2)
    print("Multiplication of",Num1,"&",Num2,"Is : ",mul)

    div = Arithematic.Div(Num1,Num2)
    print("Division of",Num1,"&",Num2,"Is : ",div)

if __name__ == "__main__":
    main()
    

    

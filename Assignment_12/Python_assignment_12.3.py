# Write a program which accepts two numbers and prints addition , substraction ,Multiplication and Division

def Calculator(num1,num2):

    return num1+num2,num1-num2,num1*num2,num1/num2

def main():
    Value1 = 0
    Value2 = 0

    Value1 = float(input("Enter First Number: "))
    Value2 = float(input("Enter Second Number: "))
    

    Add,Sub,Mul,Div = Calculator(Value1,Value2)

    print("Addition of",Value1,",",Value2 ,"is:",Add)
    print("Substraction of",Value1,",",Value2 ,"is:",Sub)
    print("Multiplication of",Value1,",",Value2 ,"is:",Mul)
    print("Division of",Value1,",",Value2 ,"is:",Div)

if __name__ == "__main__":
    main()
    

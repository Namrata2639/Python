# Q.9: write a lambda function which accept two number and returns Multiplication.

Multiplication = lambda Num1,Num2 : Num1 * Num2

def main():
    Value1 = 0
    Value2 = 0
    Ans = 0

    try: 
        print("Enter first Number: ")
        Value1 = int(input())

        print("Enter second Number: ")
        Value2= int(input())

        Ans = Multiplication(Value1,Value2)

    except ValueError:
        print("Invalid input! Please enter a valid integer number.")
        return
    
    print("Multiplication of ",Value1,"&",Value2,"is: ",Ans)

if __name__ == "__main__":
    main()
# Q.10: write a lambda function which accept three number and returns Largest Number.

Large = lambda Num1,Num2,Num3 : Num1 if Num1>= Num2 and Num1>=Num3 else (Num2 if(Num2>=Num1 and Num2>=Num3) else Num3)

def main():
    Value1 = 0
    Value2 = 0
    Value3 = 0
    Ans = 0

    try: 
        print("Enter first Number: ")
        Value1 = int(input())

        print("Enter second Number: ")
        Value2= int(input())

        print("Enter Third Number: ")
        Value2= int(input())

        Ans = Large(Value1,Value2,Value3)

    except ValueError as vobj:
        print("Invalid input!",vobj)
        return
    
    print("Largest Number is : ",Ans)

if __name__ == "__main__":
    main()
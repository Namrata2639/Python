#Q.2 write a program which contains one function ChkGreater() that accepts two numbers and prints the grater number .
# Input: 10 20 
# Output: 20 is grater 
 
def ChkGreater(num1,num2):
    if( num1 > num2 ):
        print(num1,"is greater")
    else:
        print(num2,"is greater")

def main():
    value1 = 0
    value2 = 0

    print("enter Two numbers to comapre")
    value1 = int(input("Enter First Number: "))
    value2 = int(input("Enter Second Number: "))

    ChkGreater(value1,value2)

if __name__ == "__main__":
    main()


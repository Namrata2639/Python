'''
2. Lambda function with two parameters (multiplication)
Write a program which contains one lambda function that accepts two parameters and returns their multiplication.
- Input: 4  3  Output: 12
- Input: 6  3  Output: 18
'''

square =lambda num1 , num2 :num1 *num2

def main():
    num1 = 0
    num2 = 0

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    ans = square(num1, num2)

    print("square of",num1,"and",num2,"is: ",ans)
    
if __name__ == "__main__":
    main()

    



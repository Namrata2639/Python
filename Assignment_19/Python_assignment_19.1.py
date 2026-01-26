'''
Q.1 1. Lambda function with one parameter (power of two)
Write a program which contains one lambda function that accepts one parameter and returns power of two.
- Input: 4  Output: 16
- Input: 6  Output: 64
'''

square =lambda num :num**2

def main():
    num = 0

    num = int(input("Enter a number: "))

    ans = square(num)

    print("square of",num,"is: ",ans)

if __name__ == "__main__":
    main()

    
#Q.3 Write a program which contains one function named as Add().
# which accepts two numbers from user and returns addition of those two numbers.
# Input : 11   5   Output : 16

def Add(Num1,Num2):
    return Num1+Num2

def main():
    No1 = 0
    No2 = 0
    Ans = 0

    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))

    Ans = Add(No1,No2)

    print(Ans)

if __name__ == "__main__":
    main()

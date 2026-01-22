# Write a program which accepts one number and print all even numbers till that number.
# Input : 10
# Output: 2 4 6 8 10

def DisplayEven(Num):

    for i in range(1,Num+1):
        if(i % 2 == 0):
            print(i,end= " ")


def main():
    value = 0
    value = int (input("Enter a Number: "))

    DisplayEven(value)


if __name__ == "__main__":
    main()

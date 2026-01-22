# write a program which accepts one number and prints all odd numbers till that number.
# Input : 5
# Output: 1 3 5

def DisplyOdd(Num):
    for i in range(1,Num+1):
        if(i % 2 != 0):
            print(i,end= " ")


def main():
    Value = 0

    Value = int(input("Enter a number: "))

    DisplyOdd(Value)
    
if __name__ == "__main__":
    main()
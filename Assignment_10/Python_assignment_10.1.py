# Q.1 : write a program which accepts one number and prints multiplication table of that number.
# Inuput: 4
# Output: 4 8 12 16 20 24 28 32 36 40 

def Table(Num):

    for i in range(1,11):
        print(Num*i,end=" ")

def main():
    Value = 0

    Value = int(input("Enter a number: "))
    Table(Value)

if __name__ == "__main__":
    main()

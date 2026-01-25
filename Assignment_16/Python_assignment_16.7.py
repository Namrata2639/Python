# Q.7 Write a program which contains one function that accepts one number from user 
# and returns true if number is divisible by 5, otherwise returns false.

# Input : 8        Output : False
# Input : 25       Output : True

def is_divisible_by_5(Num):
    return Num % 5 == 0

def main():
    Value = 0
    Ret = False

    Value = int(input("Enter a Number: "))
    Ret = is_divisible_by_5(Value)

    print(Ret)

if __name__ == "__main__":
    main()

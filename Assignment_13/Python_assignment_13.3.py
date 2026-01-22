# write a program which accepts one number and checks weather it is perfect number or not
# Input : 6
# Output : Perfect Number

def perfectNumber(Num):
    sum = 0

    for i in range(1,Num):
        if(Num % i == 0):
            sum = sum + i

    return sum
    
def main():
    Value = 0
    Ret = False

    print("Enter the Number to check if it is perfect number or not:  ")
    Value = int(input())

    Ret = perfectNumber(Value)
    if(Ret == Value):
        print(Value,"is a Perfect number")
    else:
        print(Value,"is not a perfect number")
        
if __name__ == "__main__":
    main()
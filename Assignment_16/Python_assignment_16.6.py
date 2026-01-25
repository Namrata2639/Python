#Q.6 Write a program which accepts a number from user and checks whether that number is positive, negative, or zero.
# Input : 11       Output : Positive Number
# Input : -8       Output : Negative Number
# Input : 0        Output : Zero

def Num(num):
    
    if(num>0):
        print("Positive Number")

    elif(num<0):
        print("Negative Number")
    
    else:
        print("Zero")

def main():
    Value = 0

    Value= int(input("Enter a number: "))

    Num(Value)

if __name__ == "__main__":
    main()
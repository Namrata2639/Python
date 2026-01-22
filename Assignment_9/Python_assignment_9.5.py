#write a program which accepts one number and checks whether it is divisible by 3 and 5.
# Input: 15 
# Output: Divisible by 3 and 5 

def Divisible(Num):
    if((Num % 3 == 0) & (Num % 5 == 0 )):
        return True
    else:
        return False

def main():
    Value = 0
    Res = False
    
    print("Enter a number to check if it Divisible by 3 and 5 : ")
    Value = int(input())

    Res = Divisible(Value)

    if(Res == True):
        print(Value,"is Divisible by 3 and 5.")
    else:
        print(Value,"is  not Divisible by 3 and 5.")

if __name__ == "__main__":
    main()




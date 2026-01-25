#Q.2 - Write a program which contains one function named as ChkNum() which accepts one parameter as number.
# If number is even then it should display "Even number"
#  Otherwise display "Odd number" on console.

# Input : 11       Output : Odd Number
# Input : 8        Output : Even Number

def Chk_Num(Num):

    if(Num % 2 == 0):
        return True
    
    else:
        return False
    
def main():
    inum = 0
    Ret = False

    print("enter a number: ")
    inum = int(input())

    Ret = Chk_Num(inum)

    if(Ret==True):
        print("Even Number")
    
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()


    


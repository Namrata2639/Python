# write a program which accepts one ni=umber and prints binary equivalent.

def BinaryEquivalent(Num):
    Ans = ''

    while(Num):
        Ans = str (Num % 2) + Ans
        Num = int(Num / 2)

    return Ans
    
def main():
    Value = 0
    Ret = False

    print("Enter the Number:  ")
    Value = int(input())

    Ret = BinaryEquivalent(Value)
    print("Binary Equivalent of",Value,"is: ",Ret)
        
if __name__ == "__main__":
    main()
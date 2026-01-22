# write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def CountDigits(Num):
   count = 0

   while(Num):
       count = count + 1
       Num = int(Num / 10)
        
   return count

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter a number: "))

    Ret =  CountDigits(Value)
    print("Number of digits in ",Value," are : ",Ret)
    
if __name__ == "__main__":
    main()
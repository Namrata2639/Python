# write a program which accepts one number print sum of digits
# Input: 123
# Output: 6

def SumDigits(Num):
   sum = 0
   digits = 0

   while(Num):
       digits =Num % 10 
       sum = sum + digits
       Num= int(Num / 10)
        
   return sum

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter a number: "))

    Ret =  SumDigits(Value)
    print("Sum of digits in ",Value," are : ",Ret)
    
if __name__ == "__main__":
    main()
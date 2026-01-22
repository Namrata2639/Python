# write a program which accept one number and prints its factors
# Input: 12
# Output : 1 2 3 4 6 12 

def Factors(Num):

    for i in range(1,Num+1):
        if(Num % i == 0):
            print(i,end =" ")  

def main():
    Value = 0

    print("Enter a Number: ")
    Value = int(input())

    Factors(Value)
        
if __name__ == "__main__":
    main()
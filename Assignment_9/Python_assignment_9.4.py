#Q.2 write a program which Accepts one number and print Cube of that number.
# Input: 5
# Output: 125 
 
def Cube(num):
   return num**3 

def main():
    value = 0
    Res = 0
    
    print("Enter Number to find out Cube of that number: ")
    value = int(input())
   
    Res = Cube(value)
    print("Cube of ",value,"is :",Res)

if __name__ == "__main__":
    main()


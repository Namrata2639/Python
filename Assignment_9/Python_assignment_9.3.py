#Q.2 write a program which Accepts one number and print square of that number.
# Input: 5
# Output: 25 
 
def Square(num):
   return num**2 

def main():
    value = 0
    Res = 0

    print("Enter Number to find out Square of that number: ")
    value = int(input())
   
    Res = Square(value)
    print("Sqaure of ",value,"is :",Res)

if __name__ == "__main__":
    main()


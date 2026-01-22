# write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5
# Output: 1 2 3 4 5

def Display_numbers(Num):

    for i in range(1,Num+1):
        print(i,end = " ")

def main():
    Value = 0

    print("Enter a Number: ")
    Value = int(input())

    Display_numbers(Value)
        
if __name__ == "__main__":
    main()
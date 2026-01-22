# write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 5 4 3 2 1

def Display_rev_numbers(Num):

    for i in range(Num,0,-1):
        print(i,end = " ")

def main():
    Value = 0

    print("Enter a Number: ")
    Value = int(input())

    Display_rev_numbers(Value)
        
if __name__ == "__main__":
    main()
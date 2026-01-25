# Q.5 - Write a program which displays numbers from 10 to 1 on screen.
# Output:
# 10   9   8   7   6   5   4   3   2   1

def order(num):

    for i in range(num,0,-1):
        print(i)

def main():
     
     num = int(input("Enter a Number: "))
     order(num)

if __name__ == "__main__":
    main()
#Q.9. Write a program which displays the first 10 even numbers on screen.
# Example:
# Output : 2  4  6  8  10  12  14  16  18  20

def even_num(Num):

    for i in range(1,Num*2+1):
        if(i%2==0):
            print(i)

def main():
    Value = 0

    Value = int(input("Enetr the Number: "))

    even_num(Value)

if __name__ == "__main__":
    main()

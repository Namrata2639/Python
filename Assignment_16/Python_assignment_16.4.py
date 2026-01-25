#Q.4 write a program which displays "Marvellous" 5 times on screen.
# Output:
# Marvellous
# Marvellous
# Marvellous
# Marvellous
# Marvellous

def Display(Num,str):
    for i in range(Num):
        print(str)

def main():
    num = int(input("How many time you want to display the string: "))
    str = input("Enter a string to display on conole: ")

    Display(num,str)

if __name__ =="__main__":
    main()
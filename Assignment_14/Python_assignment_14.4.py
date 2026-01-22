# Q.3 write a lambda function which accepts two number and returns minimum number.

min = lambda No1,No2: No1 if No1<No2 else No2

def main():
    No1 = 0
    No2 = 0
    Res = 0

    try:
        No1 = int(input("Enter first number: "))
        No2 = int(input("Enter second number: "))

        Res = min(No1,No2)
        

    except ValueError as vobj:
        print("Exception Occured: ",vobj)

    print("Minimum number between",No1,"&",No2,"is: ",Res)

if __name__ == "__main__":
    main()
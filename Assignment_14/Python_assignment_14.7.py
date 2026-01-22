# Q.7: write a lambda function which accept one number and return True if it is devisible by 5.

Div= lambda x : x % 5 == 0

def main():
    Value = 0
    Ans = False

    try: 
        print("Enter a Number: ")
        Value = int(input())

        Ans = Div(Value)

    except ValueError:
        print("Invalid input! Please enter a valid integer number.")
        return
    
    if Ans == True:
        print(Value,"is Divisible by 5")
    else:
        print(Value,"is not Divisible by 5")

if __name__ == "__main__":
    main()
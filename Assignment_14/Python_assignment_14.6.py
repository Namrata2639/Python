# Q.6: write a lambda function which accept one number and return True if it Odd otherwise False

Even = lambda x : x % 2 != 0

def main():
    Value = 0
    Ans = False

    try: 
        print("Enter a Number: ")
        Value = int(input())

        Ans = Even(Value)

    except ValueError:
        print("Invalid input! Please enter a valid integer number.")
        return
    
    if Ans == True:
        print(Value,"is an Odd number")
    else:
        print(Value,"is an Even number")

if __name__ == "__main__":
    main()
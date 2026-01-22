# Q.1: Write a lambda function which accepts one number and returns square of that number.and
 
square = lambda x:x**2

def main():
    Value = 0
    Ans = 0

    try: 
        print("Enter a Number: ")
        Value = int(input())

        Ans = square(Value)
    except ValueError:
        print("Invalid input! Please enter a valid integer number.")
        return
    
    print(f"Square of {Value} is: {Ans}")

if __name__ == "__main__":
    main()


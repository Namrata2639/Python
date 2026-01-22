# Q.1: Write a lambda function which accepts one number and returns cube of that number.
 
cube = lambda x:x**3

def main():
    Value = 0
    Ans = 0

    try: 
        print("Enter a Number: ")
        Value = int(input())

        Ans = cube(Value)
    except ValueError:
        print("Invalid input! Please enter a valid integer number.")
        return
    
    print(f"Cube of {Value} is: {Ans}")

if __name__ == "__main__":
    main()


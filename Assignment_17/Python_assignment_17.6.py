'''
6. Write a program which accepts one number and displays the below pattern.
Example:
Input : 5
Output :
* * * * *
* * * *
* * *
* *
*
'''

def display_pattern(n):
    for i in range(n, 0, -1):
        print('* ' * i)     

def main():
    Value = 0

    Value = int(input("Enter a Number: "))

    display_pattern(Value)

if __name__ == "__main__":
    main()

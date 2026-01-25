'''
7. Write a program which accepts one number and displays the below pattern.
Example:
Input: 5
Output:     
Input : 5
Output :
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

def display_pattern(n):
    for i in range(1,n+1):
       for j in range(1,n+1):
           print(j,end =" ")
       print()
    

def main():
    num = 0

    num = int(input("Enter a Number: "))

    display_pattern(num)

if __name__ == "__main__":
    main()
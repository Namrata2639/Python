'''
5. Write a program which accepts N numbers from user and stores them into a List.Return addition of all prime numbers from that List.
Main Python file accepts N numbers from user and passes each number to ChkPrime() function which is part of our user-defined module named as MarvellousNum.
Name of the function from main Python file should be ListPrime().
Input: 11
Input Elements: 13 5 45 7 4 56 10 34 2 5 8
output: 32 (13+5+7+2+5)
'''

import MarvellousNum

def ListPrime(num_list):
    add = 0 

    for i in num_list:
        if(MarvellousNum.chkPrime(i)):
            add = add + i       

    return add

def main():
    size = 0
    number_list = []
    ans = 0

    print("Enter the number of elements: ")
    size = int(input())

    print("Enetr Elements") 
    for i in range(1,size+1):
        number_list.append(int(input()))

    ans = ListPrime(number_list)

    print("Addition of Prime numbers from ",number_list,"is  : ",ans)

if __name__ == "__main__":
    main()


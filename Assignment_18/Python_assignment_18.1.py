'''
Q.1. Write a program which accepts N numbers from user and stores them into a List.
Return addition of all elements from that List.

Input : Number of elements: 6
Input Elements : 13  5  45  7  4  56
Output : 130

'''

def addition_elements(num_list):
    addition = 0

    for i in num_list:
        addition = addition + i

    return addition

def main():
    size = 0
    element = 0
    number_list = []
    ans = 0

    print("Enter the number of elements: ")
    size = int(input())

    print("Enetr Elements") 
    for i in range(1,size+1):
        element = int(input())
        number_list.append(element)

    ans = addition_elements(number_list)

    print("Addition is: ",ans)

if __name__ == "__main__":
    main()

    

'''
2. Write a program which accepts N numbers from user and stores them into a List.
Return Maximum number from that List.
Example:
Input : Number of elements: 7
Input Elements : 13  5  45  7  4  56  34
Output : 56
'''

def Max_element(num_list):
    Max = 0

    for i in num_list:
        if(i>Max):
            Max = i

    return Max

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

    ans = Max_element(number_list)

    print("Maximum Number is  : ",ans)

if __name__ == "__main__":
    main()

'''
3. Write a program which accepts N numbers from user and stores them into a List.
Return Minimum number from that List.
Example:
Input : Number of elements: 4
Input Elements : 13  5  45  7  
Output : 5
'''

def Min_element(num_list):
    min = num_list[0]

    for i in num_list:
        if(i<min):
            min = i

    return min

def main():
    size = 0
    element = 0
    number_list = []
    ans = 0

    print("Enter the number of elements: ")
    size = int(input())

    print("Enetr Elements") 
    for i in range(size):
        element = int(input())
        number_list.append(element)

    ans = Min_element(number_list)

    print("Minimum Number is: ",ans)

if __name__ == "__main__":
    main()

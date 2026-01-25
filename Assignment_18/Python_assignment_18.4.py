'''
Q.4. Write a program which accepts N numbers from user and stores them into a List.
Accept one another number from user and return frequency of that number from List.
Input : Number of elements: 11
Input Elements : 13  5  45  7  4  56  5  34  2  5  65
Element to search : 5
Output : 3
'''

def Frequency_element(num_list,element):
    frequency = 0

    for i in num_list:
        if(i == element):
            frequency += 1

    return frequency

def main():
    size = 0
    element = 0
    number_list = []
    ans = 0

    print("Enter the number of elements: ")
    size = int(input())

    print("Enetr Elements") 
    for i in range(1,size+1):
        number_list.append(int(input()))

    print("Enter Element you want to search: ")
    element = int(input())

    ans = Frequency_element(number_list,element)

    print("freqency of Number in",number_list,"is  : ",ans)

if __name__ == "__main__":
    main()

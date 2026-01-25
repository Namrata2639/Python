# Q.10 Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

def is_even(no):
    return no %2 ==0

def main():
    size = 0
    numbers_list = []

    print("Enter the size of the list:")
    size = int(input())

    print("Enter the elements :")
    for i in range(size):
        num = int(input())
        numbers_list.append(num)

    even_num = list(filter(lambda x: x%2==0,numbers_list))
    count = len(even_num)
    #even_num = list(filter(is_even,numbers_list))
    # count = len(even_num)

    print("Count of even numbers are: ",count)

if __name__ == "__main__":
    main()

#Q.3- Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

def is_odd(no):
    return no % 2 != 0

def main():
    size = 0
    numbers_list = []

    print("Enter the size of the list:")
    size = int(input())

    print("Enter the elements :")
    for i in range(size):
        num = int(input())
        numbers_list.append(num)

    odd_num = list(filter(lambda x:x%2!=0,numbers_list))
    # odd_num = list(filter(is_odd,numbers_list))

    print(odd_num)

if __name__ == "__main__":
    main()
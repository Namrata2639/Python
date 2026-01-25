#Q.4Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

def increase(A,B):
    return A+B

def main():
    size = 0
    numbers_list = []

    print("Enter the size of the list:")
    size = int(input())

    print("Enter the elements :")
    for i in range(size):
        num = int(input())
        numbers_list.append(num)

    Addition = reduce(lambda X,Y:X+Y,numbers_list)
    # Addition = reduce(increase,numbers_list)

    print("Addition is: ",Addition)

if __name__ == "__main__":
    main()
#Q.5Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

def Max_element(A,B):
    if A>B:
        return A
    else:
        return B

def main():
    size = 0
    numbers_list = []

    print("Enter the size of the list:")
    size = int(input())

    print("Enter the elements :")
    for i in range(size):
        num = int(input())
        numbers_list.append(num)

    Max = reduce(lambda X,Y: X if (X>Y) else Y,numbers_list)
    # Max = reduce(Max_element,numbers_list)

    print("Maximum Number is: ",Max)

if __name__ == "__main__":
    main()
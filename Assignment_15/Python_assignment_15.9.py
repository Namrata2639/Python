#Q.9- Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

def product(A,B):
    return A*B

def main():
    size = 0
    numbers_list = []

    print("Enter the size of the list:")
    size = int(input())

    print("Enter the elements :")
    for i in range(size):
        num = int(input())
        numbers_list.append(num)

    Multiplication= reduce(lambda X,Y: X*Y,numbers_list)
    # Multiplication = reduce(product,numbers_list)

    print("Maximum Number is: ",Multiplication)

if __name__ == "__main__":
    main()
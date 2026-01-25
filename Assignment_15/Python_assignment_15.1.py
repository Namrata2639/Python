# Q.1 Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

def square(num):
    return num**2

def main():
    size = 0
    numbers_list = []

    print("Enter the size of the list:")
    size = int(input())

    print("Enter the elements :")
    for i in range(size):
        num = int(input())
        numbers_list.append(num)

    squares_list = list(map(lambda x:x**2,numbers_list))
    # squares_list = list(map(square,numbers_list))

    print(squares_list)

if __name__ == "__main__":
    main()



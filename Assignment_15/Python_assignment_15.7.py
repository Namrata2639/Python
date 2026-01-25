#Q.7: - Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

def is_greater(str):
    return len(str)>5

def main():
    size = 0
    str_list = []

    print("Enter the size of the list:")
    size = int(input())

    print("Enter the elements :")
    for i in range(size):
        str = input()
        str_list.append(str)

    str_length = list(filter(lambda x: (len(x)>5)  ,str_list))
    # str_length = list(filter(is_greater,str_list))

    print(str_length)

if __name__ == "__main__":
    main()
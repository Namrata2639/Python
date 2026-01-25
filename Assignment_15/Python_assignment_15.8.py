# Q.8 - Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5

def is_divisible(num):
    return (num%3==0 and num%5==0)

def main():
    size = 0
    num_list = []

    print("Enter the size of the list:")
    size = int(input())

    print("Enter the elements :")
    for i in range(size):
        num = int(input())
        num_list.append(num)

    Output = list(filter(lambda x: x % 3 == 0 and x % 5 == 0  ,num_list))
    # Output = list(filter(is_divisible,num_list))

    print(Output)

if __name__ == "__main__":
    main()
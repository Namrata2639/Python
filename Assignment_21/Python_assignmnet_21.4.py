'''
Q.4 Design a Python application that creates two threads.
- Thread 1 should compute the sum of elements from a list.
- Thread 2 should compute the product of elements from the same list.
- Return the results to the main thread and display them.
'''

import threading

# Shared directory to store results
Result = {}

def Compute_sum(numbers):
    global Result
    sum_result = 0

    for num in numbers:
        sum_result += num
    
    Result['Sum'] = sum_result

def Compute_product(numbers):
    global Result
    product_result = 1

    for num in numbers:
        product_result *= num

    Result['Product'] = product_result

def main():
    global Result
    size = 0
    Data = []

    print("Inside main Thread")    

    print("Enter the number of elements in the list: ")
    size = int(input())

    print("Enter the elements of the list: ")
    for i in range(size):
        Data.append(int(input()))

    # Creating threads
    Thread1 = threading.Thread(target=Compute_sum, args=(Data,))
    Thread2 = threading.Thread(target=Compute_product, args=(Data,))

    # Starting threads
    Thread1.start()
    Thread2.start()

    # Waiting for both threads to complete
    Thread1.join()
    Thread2.join()

    print("Sum of elements is:", Result['Sum'])
    print("Product of elements is:", Result['Product'])

if __name__ == "__main__":
    main()


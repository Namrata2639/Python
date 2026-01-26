''' 
Q.2 Design a Python application that creates two threads.
- Thread 1 should calculate and display the maximum element from a list.
- Thread 2 should calculate and display the minimum element from the same list.
- The list should be accepted from the user.
'''
import threading

def Max(numbers):
    max = numbers[0]

    for i in numbers:
        if i > max:
            max = i

    print("Maximum element is:", max)
    print("Thread id of Max_Thread is : ",threading.get_ident())
    print("Thread name of Max_Thread is: ",threading.current_thread().name)

def Min(numbers):
    min = numbers[0]

    for i in numbers:
        if i < min :
            min = i

    print("Minimum element is:", min)
    print("Thread id of Min_Thread is : ",threading.get_ident())
    print("Thread name of Min_Thread is: ",threading.current_thread().name)

def main():
    size = 0
    Data = []

    print("Inside main thread")

    print("Enter the number of elements in the list: ")
    size = int(input())

    print("Enter the elements of the list: ")
    for i in range(size):
        Data.append(int(input()))

    # Creating threads
    max_thread = threading.Thread(target=Max, args=(Data,))
    min_thread = threading.Thread(target=Min, args=(Data,))

    # Starting threads
    max_thread.start()
    min_thread.start()

    # Waiting for both threads to complete
    max_thread.join()
    min_thread.join()

    print("End of main thread")


if __name__ == "__main__":
    main()  

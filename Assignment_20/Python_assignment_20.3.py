'''
 3: Design a Python application that creates two threads named EvenList and OddList.
- Both threads should accept a list of integers as input.
- The EvenList thread should:
        Extract all even elements from the list.
        Calculate and display their sum.
- The OddList thread should:
    Extract all odd elements from the list.
    Calculate and display their sum.
- Threads should run concurrently.

'''

import threading

def Even_sum(Data):
    sum = 0

    for i in Data:
        if i%2 == 0:
            sum = sum + i

    print("Sum of even elements from the list: ",sum)

def Odd_sum(Data):
    sum = 0

    for i in Data:
        if i%2 != 0:
            sum = sum + i

    print("Sum of odd elements from the list: ",sum)

def main():
    size = 0
    Data = []

    print("Inside Main Thread")

    print("Enter the number of elements in list: ")
    size = int(input())

    print("Enter elements: ")
    for i in range(size):
        Data.append(int(input()))

    # creating threads for EvenList and OddList passing Data list as argument
    EvenList = threading.Thread(target=Even_sum,args=(Data,))
    OddList = threading.Thread(target=Odd_sum,args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

    print("End of main thread")

if __name__ == "__main__":
    main()

    

    
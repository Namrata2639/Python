'''
Problem 1
Design a Python application that creates two threads named Prime and NonPrime.
- Both threads should accept a list of integers.
- The Prime thread should display all prime numbers from the list.
- The NonPrime thread should display all non-prime numbers from the list.
'''

import threading

def chk_prime(no):

    for i in range(2,(int(no/2+1))):
        if(no%i == 0):
            return False

    return True   

def Prime_Thread(numbers):

    print("Inside prime thread")
    print("Prime numbers are: ")

    for i in numbers:
        if i>1 and chk_prime(i):
            print(" ",i,end="")
    print()
    print("Thread id of Prime_Thread is : ",threading.get_ident())
    print("Thread name of Prime_Thread is: ",threading.current_thread().name)

def NonPrime_Thread(numbers):

    print("Inside NonPrime thread")
    print("Non-Prime numbers are: ")

    for i in numbers:
        if i>1 and not(chk_prime(i)):
            print(" ",i,end="")
    print()

    print("Thread id of NonPrime_Thread is: ",threading.get_ident())
    print("Thread name of NonPrime_Thread is:  ",threading.current_thread().name)


def main():
    size = 0
    Data = []

    print("Inside main thread")

    print("Enter the number of elements in the list: ")
    size = int(input())

    print("Enter the elements of the list: ")
    for i in range(size):
        Data.append(int(input()))

    # Create threads 
    Prime = threading.Thread(target=Prime_Thread,args=(Data,))
    NonPrime = threading.Thread(target=NonPrime_Thread,args=(Data,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()

    print("End of main Thread")

if __name__ == "__main__":
    main()
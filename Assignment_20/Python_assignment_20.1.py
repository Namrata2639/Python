'''
1. Design a Python application that creates two separate threads named Even and Odd.
- The Even thread should display the first 10 even numbers.
- The Odd thread should display the first 10 odd numbers.
- Both threads should execute independently using the threading module.
- Ensure proper thread creation and execution.

'''
import threading

def Even_numbers(count):
    print("inside even number thread")
    print("Even numbers are: ")
    for i in range(0, (count*2),2):
        print(i,end=" ")
    print()

    
def Odd_numbers(count):
    print("inside odd number thread")
    print("Odd numbers are: ")
    for i in range(1, (count*2),2):
        print(i,end=" ")
    print()

def main():
    print("Inside main thread")
    print("How many even number you want to print: ")
    even_count = int(input())

    print("How many odd number you want to print: ")
    odd_count = int(input())

    # created a thread named Even which will execute Even_numbers function and pass even_count as argument to the even_numbers function
    Even = threading.Thread(target=Even_numbers,args=(even_count,))
    # this will start the execution of even thread
    Even.start()

    # created a thread named Odd which will execute Odd_numbers function and pass odd_count as argument to the odd_numbers function
    Odd = threading.Thread(target=Odd_numbers,args=(odd_count,))
    # this will start the execution of odd thread
    Odd.start()

    # Wait for both threads to complete
    Even.join()
    Odd.join()

    print("End of main thread")

if __name__  =="__main__":
    main()




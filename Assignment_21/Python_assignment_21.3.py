'''
Problem 3
Design a Python application where multiple threads update a shared variable.
- Use a Lock to avoid race conditions.
- Each thread should increment the shared counter multiple times.
- Display the final value of the counter after all threads complete execution
'''

import threading

# Shared variable
counter = 0
lock = threading.Lock()  # Create a lock object

def IncrementCounter():
    global counter

    for _ in range (200000000):
        #added a lock to critical section 
        with lock:
            counter  = counter + 1 #critical section where counter is accessible by both thread1 and thread2


def main():
    global counter

    print("Inside main Thread")

    Thread1 = threading.Thread(target=IncrementCounter)
    Thread2 = threading.Thread(target=IncrementCounter)

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print(counter)

if __name__ == "__main__":
    main()



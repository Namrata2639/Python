'''
Q.5.Design a Python application that creates two threads named Thread1 and Thread2.
- Thread1 should display numbers from 1 to 50.
- Thread2 should display numbers from 50 to 1 in reverse order.
- Ensure that:
- Thread2 starts execution only after Thread1 has completed.
- Use appropriate thread synchronization.
'''

import threading

def inorder(num):
    print("Inside inorder thread")

    for i in range(1,num+1,1):
        print(i,end=" ")

    print()

def reverseorder(num):
    print("Inside reverseorder thread")

    for i in range(num,0,-1):
          print(i,end=" ")

    print()


def main():
    print("Inside main Thread")

    Num = int(input("Enter the nUmber: "))

    Thread1 = threading.Thread(target=inorder,args=(Num,))
    Thread2 = threading.Thread(target=reverseorder,args=(Num,))

    # this will start the execution of Thread1
    Thread1.start()
    Thread1.join()

    # this will start the execution of Thread2 after the completion of Thread1 use of synchronization
    Thread2.start()
    Thread2.join()

    print("End of main thread")

if __name__ == "__main__":
    main()
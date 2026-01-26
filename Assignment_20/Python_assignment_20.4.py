'''
Problem 4
Design a Python application that creates three threads named Small, Capital, and Digits.
- All threads should accept a string as input.
- The Small thread should count and display the number of lowercase characters.
- The Capital thread should count and display the number of uppercase characters.
- The Digits thread should count and display the number of numeric digits.
- Each thread must also display:
- Thread ID
- Thread Name
'''
import threading

def Small_count(str):
    count = 0
    for i in str:
        if i.islower():
            count = count + 1

    print("Number of lowercase characters: ",count)
    print("Thread ID of Small thread: ",threading.get_ident()) 
    print("Thread Name of Small thread: ",threading.current_thread().name)

def Capital_count(str):
    count = 0

    for i in str:
        if i.isupper():
            count = count + 1

    print("Number of uppercase characters: ",count)
    print("Thread ID of Capital thread: ",threading.get_ident()) #used to get the id of current thread
    print("Thread Name of Capital thread: ",threading.current_thread().name) #used to get the name of current thread

def Digits_count(str):
    count = 0

    for i in str:
        if i.isdigit():
            count = count + 1

    print("Number of digits: ",count)
    print("Thread ID of Digits thread: ",threading.get_ident()) 
    print("Thread Name of Digits thread: ",threading.current_thread().name)

def main():

    print("Inside Main Thread")

    print("Enter a string: ")
    str = input()

    #target parameter is used to specify the function to be executed by the thread and args parameter is used to pass the arguments to that function
    Small = threading.Thread(target=Small_count,args=(str,))
    Capital = threading.Thread(target=Capital_count,args=(str,))
    Digits = threading.Thread(target=Digits_count,args=(str,))  

    # starting all threads
    Small.start()
    Capital.start()     
    Digits.start()

    # wait until all threads complete
    Small.join()
    Capital.join()  
    Digits.join()

    print("End of main thread")

if __name__ == "__main__":
    main()


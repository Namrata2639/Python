'''
2. Design a Python application that creates two threads named EvenFactor and OddFactor.
- Both threads should accept one integer number as a parameter.
- The EvenFactor thread should:
- Identify all even factors of the given number.
- Calculate and display the sum of even factors.
- The OddFactor thread should:
- Identify all odd factors of the given number.
- Calculate and display the sum of odd factors.
- After both threads complete execution, the main thread should display the message:
“Exit from main”
'''

import threading 

def Even_Factors(Num):
    Even_sum = 0

    for i in range(1,Num+1):
        if(Num % i == 0 and i%2 ==0):
            Even_sum = Even_sum + i

    print("Sum of Even Factors: ",Even_sum)

def Odd_Factors(Num):
    Odd_sum = 0

    for i in range(1,Num+1):
        if(Num % i == 0 and i%2 !=0):
            Odd_sum = Odd_sum + i

    print("Sum of Odd Factors: ",Odd_sum)
            

def main():
    Num = 0

    print("Inside main thread")
    
    print("Enter a number: ")
    Num = int(input())

    EvenFactor = threading.Thread(target=Even_Factors,args =(Num,))
    OddFactor = threading.Thread(target=Odd_Factors,args =(Num,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

    
if __name__  =="__main__":
    main()  




'''
5. Program using filter(), map(), and reduce() (prime numbers)
Write a Python application that contains one list of numbers (accepted from user).
- Filter: should filter out all prime numbers.
- Map: will multiply each number by 2.
- Reduce: will return the maximum number from those numbers.
(You can also use normal functions instead of lambda functions.)

- Input List = [2, 70, 11, 10, 17, 23, 31, 77]
- List after filter = [2, 11, 17, 23, 31]
- List after map = [4, 22, 34, 46, 62]
- Output of reduce = 62

'''

from functools import reduce

def isPrime(No):

    for i in range(2,int(No/2+1)):
        if(No%i==0):
            return False
    return True

is_prime = lambda x : not[True for i in range(2,int(x/2+1)) if x%i == 0]
square = lambda No: No * 2
Large = lambda A,B: A if(A>B) else B

def FilterX(Task,Data):
    Res = []
    for i in Data:
       if(Task(i) == True):
            Res.append(i)
        
    return Res

def MapX(Task,Data):
    Res = []

    for i in Data:
        Res.append(Task(i))
        
    return Res

def ReduceX(Task,Data):
    max = 0

    for i in Data:
        max = Task(max,i)

    return max

def main():
    size = 0
    Data = list()

    print("Enter The size of list: ")
    size = int(input())

    print("Enter the elements of list: ")
    for i in range(size):
        Data.append(int(input()))

        
    # fData = FilterX(is_prime,Data) 
    fData = list(filter(lambda x: not [True for i in range(2,int(x/2+1)) if x%i == 0],Data))
    print("List After Filter: ",fData)

    # mData = MapX(square,fData)
    mData = list(map(lambda x: x*2,fData))
    print("List After Map: ",mData)

    # rData = ReduceX(Large,mData)
    rData = reduce(lambda x,y:x if x>y else y,mData)
    print("output of reduce: ",rData)

if __name__ == "__main__":
    main()


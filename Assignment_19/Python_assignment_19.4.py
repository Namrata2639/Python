'''
4. Program using filter(), map(), and reduce() (even numbers)
Write a Python application that contains one list of numbers (accepted from user).
- Filter: should filter out all numbers which are even.
- Map: will calculate the square of each number.
- Reduce: will return the addition of all those numbers.
Example:
- Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
- List after filter = [2, 4, 4, 2, 8, 10]
- List after map = [4, 16, 16, 4, 64, 100]
- Output of reduce = 204
'''

from functools import reduce

is_even = lambda No: No %2 ==0 
square= lambda No: No **2
Addition = lambda A,B:A+B

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
    Add = 0

    for i in Data:
        Add = Task(Add,i)

    return Add

def main():
    size = 0
    Data = list()

    print("Enter The size of list: ")
    size = int(input())

    print("Enter the elements of list: ")
    for i in range(size):
        Data.append(int(input()))

    
    # fData = FilterX(is_even,Data)
    fData = list(filter(lambda x:x%2==0,Data))
    print("List After Filter: ",fData)

    # mData = MapX(square,fData)
    mData = list(map(lambda x: x**2,fData))
    print("List After Map: ",mData)
    
    # rData = ReduceX(Addition,mData)
    rData = reduce(lambda x,y:x+y,mData )
    print("output of reduce: ",rData)

if __name__ == "__main__":
    main()




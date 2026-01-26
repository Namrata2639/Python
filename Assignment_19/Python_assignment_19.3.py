'''
3. Program using filter(), map(), and reduce()
Write a Python application that contains one list of numbers (accepted from user).
- Filter: should filter out all numbers greater than or equal to 70 and less than or equal to 90.
- Map: will increase each number by 10.
- Reduce: will return the product of all those numbers.
Example:
- Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
- List after filter = [76, 89, 86, 90, 70]
- List after map = [86, 99, 96, 100, 80]
- Output of reduce = 6538752000
'''

from functools import reduce

is_greater = lambda No: True if (No>=70 and No<=90) else False
increment = lambda No: No + 10
product = lambda A,B:A*B

def FilterX(Task,Data):
    Res = []

    for i in Data:

        if(Task(i) == True):
            Res.append(i)
        
    return Res

def MapX(Task,Data):
    Res = []
    ans =0

    for i in Data:
        ans = Task(i)
        Res.append(ans)
        
    return Res

def ReduceX(Task,Data):
    mul = 1

    for i in Data:
        mul = Task(mul,i)

    return mul

def main():
    size = 0
    Data = list()

    print("Enter The size of list: ")
    size = int(input())

    print("Enter the elements of list: ")
    for i in range(size):
        Data.append(int(input()))

        
    # fData = FilterX(is_greater,Data) 
    fData = list(filter(lambda x: x>=70 and x<=90,Data))
    print("List After Filter: ",fData)

    # mData = MapX(increment,fData)
    mData = list(map(lambda x: x+10,fData))
    print("List After Map: ",mData)

    # rData = ReduceX(product,mData)
    rData = reduce(lambda x,y:x*y,mData)
    print("output of reduce: ",rData)

if __name__ == "__main__":
    main()



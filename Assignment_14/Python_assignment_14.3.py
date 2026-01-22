# Q.3 write a lambda function which accepts two number and returns maximum number.

# def max(No1,No2):
#     if(No1>No2):
#         return No1
#     else:
#         return No2
    
max = lambda No1,No2: No1 if No1>No2 else No2

def main():
    No1 = 0
    No2 = 0
    Res = 0

    try:
        No1 = int(input("Enter First Number: "))
        No2 = int(input("Enter second Number: "))

        Res = max(No1,No2)
        

    except Exception as eobj:
        print("Exception occured",eobj)
    
    print("Maximum number between",No1,"&",No2,"is :",Res)

if __name__ =="__main__":
    main()




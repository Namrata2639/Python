'''
3: Write a Python program to implement a class named Numbers with the following specifications:
- The class should contain one instance variable:
    Value
- Define a constructor (__init__) that accepts a number from the user and initializes Value.
- Implement the following instance methods:
    ChkPrime() – returns True if the number is prime, otherwise returns False
    ChkPerfect() – returns True if the number is perfect, otherwise returns False
    Factors() – displays all factors of the number
    SumFactors() – returns the sum of all factors
(You may use this method as a helper in ChkPerfect() if required)
- Create multiple objects and call all methods.

'''

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):

        if self.Value <= 1 :
            return False
        
        for i in range(2,int((self.Value/2)+1)):
            if self.Value % i == 0:
                return False
            
        return True
    
    def ChkPerfect(self):
        sum = 0

        if(self.Value <= 1):
            return False
        
        for i in range(1,int(self.Value/2)+1):
            if self.Value % i == 0:
                sum = sum + i

        if sum == self.Value:
            return True
        
    def Factors(self):

        for i in range(1,self.Value+1):
            if (self.Value % i == 0 ):
                print(i,end =" ")
        print()

    def SumFactors(self):
        sum = 0

        if self.ChkPrime() == True:
            print("No factors as given number id prime number")
            sum = 1
            return sum

        else:
            for i in range(1,self.Value+1):
                if(self.Value % i == 0):
                    sum = sum + i

            return sum
        
obj1 = Numbers()

is_prime = obj1.ChkPrime()
if is_prime==True:
    print(f"{obj1.Value} is a prime number")    
else:
    print(f"{obj1.Value} is not a prime number")

is_perfect =obj1.ChkPerfect()
if is_perfect==True:
    print(f"{obj1.Value} is a perfect number")
else:
    print(f"{obj1.Value} is not a perfect number")

obj1.Factors()

Sum = obj1.SumFactors()
print(f"Sum of factors of {obj1.Value} is {Sum}")
print("--------------------------------------------------")
        
obj2 = Numbers()
is_prime2 = obj2.ChkPrime()
if is_prime2:
    print(f"{obj2.Value} is a prime number")    
else:
    print(f"{obj2.Value} is not a prime number")

is_perfect2 = obj2.ChkPerfect()
if is_perfect2:
    print(f"{obj2.Value} is a perfect number")
else:
    print(f"{obj2.Value} is not a perfect number")

obj2.Factors()
sum2 = obj2.SumFactors()
print(f"Sum of factors of {obj2.Value} is {sum2}")
            
    


        

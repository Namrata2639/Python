'''
- Write a Python program to implement a class named Arithmetic with the following characteristics:
- The class should contain two instance variables: Value1 and Value2.
- Define a constructor (__init__) that initializes all instance variables to 0.
- Implement the following instance methods:
- Accept() - accepts values for Value1 and Value2 from the user.
- Addition() - returns the addition of Value1 and Value2.
- Subtraction() - returns the subtraction of Value1 and Value2.
- Multiplication() - returns the multiplication of Value1 and Value2.
- Division() - returns the division of Value1 and Value2 (handle division by zero properly).
- Create multiple objects of the Arithmetic class and invoke all the instance methods.

'''

class Arithematic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enetr First Number: "))
        self.Value2 = int(input("Enter second Number: "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try:
            return  self.Value1 / self.Value2

        except ZeroDivisionError:
            print("Division by zero is not allowed")
    

obj = Arithematic()
obj.Accept()
add = obj.Addition()
sub = obj.Substraction()
mul = obj.Multiplication()
div = obj.Division()   

print("Numbers: ",obj.Value1,",",obj.Value2)
print("Addition is: ",add)
print("Substraction is: ",sub)
print("Multiplication is: ",mul)
print("Division is: ",div)

obj1 = Arithematic()
obj1.Accept()
add = obj1.Addition()
sub = obj1.Substraction()
mul = obj1.Multiplication()
div = obj1.Division()    

print()
print("Numbers: ",obj1.Value1,",",obj1.Value2)
print("Addition is: ",add)
print("Substraction is: ",sub)
print("Multiplication is: ",mul)
print("Division is: ",div)



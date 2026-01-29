'''
Write a Python program to implement a class named BankAccount with the following requirements:
- The class should contain two instance variables:
    Name (Account holder name)
    Amount (Account balance)
- The class should contain one class variable:
    ROI (Rate of Interest), initialized to 10.5
- Define a constructor __init__ that accepts Name and initial Amount.
- Implement the following instance methods:
    -Display() – displays account holder name and current balance
    -Deposit() – accepts an amount from the user and adds it to balance
    -Withdraw() – accepts an amount from the user and subtracts it from balance
    (Ensure withdrawal is allowed only if sufficient balance exists)
    -CalculateInterest() – calculates and returns interest using formula:
    Interest = (  Amount * ROI)\100 
- Create multiple objects and demonstrate all methods.
'''

class BankAccount:
    ROI = 10.5

    def __init__(self,AName,ABalance):
        self.Name = AName
        self.Balance = float(ABalance)

    def Display(self):

        print(f"Account holder name is :{self.Name} & current balance is {self.Balance}")

    def Deposit(self):
        print("Enter an ammount you want to deposit:")
        ammount = float(input())
        self.Balance += ammount
        self.Display()

    def Withdraw(self):
        print("Enter an ammount you want to withdraw: ")
        ammount = float(input())
        if(self.Balance<ammount):
            print("Insufficient funds")
        else:
            self.Balance -= ammount
        self.Display()

    def CalculateInterest(self):
        Interest = (self.Balance * BankAccount.ROI)/100
        return Interest

obj1 = BankAccount("Nimmi",'130')
obj1.Display()
obj1.Deposit()
Interest = obj1.CalculateInterest()
print(f"Interest for obj1 is: {Interest}")  
obj1.Withdraw()

print()

obj2 = BankAccount("Nam",'1500')
obj2.Display()
obj2.Deposit()
Interest = obj2.CalculateInterest()
print(f"Interest for obj2 is: {Interest}")
obj2.Withdraw()

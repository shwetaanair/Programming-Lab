class account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the BANK ACCOUNT")
 
    def deposit(self):
        amount=int(input("Enter amount: "))
        self.balance += amount
        print("\n Deposited Current balance is:",amount)
 
    def withdraw(self):
        amount = int(input("Enter amount to be Withdrawn: "))
        if amount > self.balance :
            print("\n Insufficient balance \n Please Enter Valid Amount ")
        else:
            self.balance -=amount
            print("Withdrwan from your account",amount)
            
    def display(self):
        print("\n Current Balance is=",self.balance)
      
myaccount = account()

myaccount.deposit()
myaccount.withdraw()
myaccount.display()
 

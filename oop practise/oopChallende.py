#implemention of the oop challenge on educative

#challenge 1

class Account:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
    
    def getBalance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdrawl(self,amount):
        self.balance -= amount
        return self.balance
    

    

class SavingAccount(Account):
    def __init__(self, title, balance,interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmout(self):
        return self.balance * self.interestRate / 100
        
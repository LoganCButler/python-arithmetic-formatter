from enum import Enum

class EntryType(Enum):
    deposit = 1
    withdraw = 2

class Category:
    def __init__(self, name): 
        self.name = name
        self.ledger = []
        self.internalLedger = []

    def deposit(self, amount, description = None):
        description = description if description is not None else ""
        self.internalLedger.append(LedgerEntry(amount, EntryType.deposit, description))
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amountRequest, description = None): 
        completedWithdraw = False
        fundsAvailable = self.check_funds(amountRequest)
        description = description if description is not None else ""
        if fundsAvailable:
            completedWithdraw = True
            self.internalLedger.append(LedgerEntry(amountRequest, EntryType.withdraw, description, completedWithdraw))
            self.ledger.append({"amount": amountRequest * -1, "description": description})

        return completedWithdraw

    def get_balance(self):
        balance = 0
        for entry in self.internalLedger:
            if entry.entryType == EntryType.deposit:
                balance += entry.amount
            else:
                balance -= entry.amount
        return balance
    
    def transfer(self, amount, desinationCategory):
        sourceCategory = self
        transferIsSuccessful = False
        withdrawDetails = f'Transfer to {desinationCategory.name}'

        withDrawSuccess = sourceCategory.withdraw(amount, withdrawDetails)
        if withDrawSuccess:
            depositeDetails = f'Transfer from {sourceCategory.name}'
            desinationCategory.deposit(amount, depositeDetails)
            transferIsSuccessful = True
        
        return transferIsSuccessful

    def check_funds(self, amountRequest):
        return self.get_balance() >= amountRequest
            


class LedgerEntry:
    def __init__(self, amount, entryType, details = '', transactionCompleted = True):
        self.amount = amount
        self.entryType = entryType
        self.details = details,
        self.transactionCompleted = transactionCompleted
    
    def __str__(self):
        return f'amount: {self.amount}, description={self.details})'
        




def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(1000, "initial deposit")
clothing = Category("Clothing")
food.transfer(50, clothing)
print("food budget", food.get_balance())
print("clothing budget", clothing.get_balance())
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

    def __str__(self):
        finalString = ""
        finalString = self.addTitleHeader(finalString)
        finalString = self.addLineItmes(finalString)
        finalString += f'Total: {self.formatToDollar(self.get_balance())}'
        return finalString

    def addLineItmes(self, finalString):
        printHoriz = 30

        for lineItem in self.internalLedger:
            descriptiondisplay = lineItem.details[0][:23]
            amountDispay = f'{self.formatToDollar(lineItem.amount)}' if lineItem.entryType is EntryType.deposit else f'-{self.formatToDollar(lineItem.amount)}'

            internalSpacesCount = printHoriz - len(descriptiondisplay) - len(amountDispay)

            finalString += descriptiondisplay + " " * internalSpacesCount + amountDispay
            finalString += '\n'
        return finalString

    def addTitleHeader(self, finalString):
        printHoriz = 30
        titleOffset = int(((printHoriz / 2) - (len(self.name) / 2)) // 1)

        finalString += "*" * titleOffset
        finalString += self.name
        finalString += "*" * (printHoriz - len(finalString))
        finalString += '\n'
        return finalString
    
    def formatToDollar(self, amount):
        return '{:.2f}'.format(amount)
            


class LedgerEntry:
    def __init__(self, amount, entryType, details = '', transactionCompleted = True):
        self.amount = amount
        self.entryType = entryType
        self.details = details,
        self.transactionCompleted = transactionCompleted
    
    def __str__(self):
        return f'amount: {self.amount}, description={self.details})'
        




def create_spend_chart(categories):
    chartString = "Percentage spent by category\n"
    yInterval = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

    for interval in yInterval:
        displayLable = ''
        leadingSpaces = 3 - len(f'{interval}')

        displayLable += " " * leadingSpaces
        displayLable += f'{interval}|'

        # TODO: Add loop to add category data points


        chartString += displayLable + '\n'

    # botom of chart
    chartString += '    ' + ('---' * len(categories)) + '\n'

    # x-axis lables
    longestXTitle = 0
    for catagory in categories:
        catNameLeng = len(catagory.name)
        if catNameLeng > longestXTitle:
            longestXTitle = catNameLeng
    
    for i in range(0, longestXTitle):
        chartString += '    ' # starting offset
        for catagory in categories:
            character = catagory.name[i:i+1]
            displayChar = character if character is not '' else ' '

            chartString += ' ' + displayChar + ' '
        chartString += '\n'

    

    return chartString


food = Category("Food")
food.deposit(1000, "initial deposit")
food.deposit(1000, "second deposit with long description")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(create_spend_chart([food, clothing]))
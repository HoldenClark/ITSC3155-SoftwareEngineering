#1.  Class attribute (title of bank)
class bankAccountName:

    def __init__(self, name, balance, minimumBalance):
        self.name = name
        self.balance = balance
        self.minimumBalance = minimumBalance

#2.  Instance attributes (customer name, current balance)

#3.  Methods (deposit, withdraw, show cust. info)

    def deposit(self, depositAmount):
        self.balance += depositAmount
        assignment.accountDetails()

    def withdraw(self, withdrawAmount):
        self.balance -= withdrawAmount
        if self.balance < self.minimumBalance:
            self.balance += withdrawAmount
            print(f"Withdraw ${withdrawAmount} would leave account with less than the minimum balance requirement ${self.minimumBalance}")
        else:
            assignment.accountDetails()

    def accountDetails(self):
        print(f"{self.name} has ${self.balance} in their account.")
#4.  Add validation (no illegal transactions, ie. cannot withdraw so balance is negative)

assignment = bankAccountName("Holden Clark", 300, 100)

assignment.deposit(20)
assignment.withdraw(50)
assignment.withdraw(1000)


print("Thank you for using Bank of Holden")
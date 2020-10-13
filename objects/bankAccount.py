class Account:
    def __init__(self, owner, amount):
        self.owner = owner
        self.balance = amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print('Withdrawal Accepted')
            return amount
        else:
            print('Funds Unavailable!')
            return None

    def deposit(self, amount):
        self.balance += amount
        print('Deposit Accepted')

    def __str__(self):
        info = f'Account Owner:   {self.owner}'
        info += f'\nAccount Balance: ${self.balance}'
        return info


acc1 = Account('Jose', 100)
print(acc1)
print(acc1.owner)
print(acc1.balance)
acc1.deposit(50)
acc1.withdraw(75)
acc1.withdraw(500 )
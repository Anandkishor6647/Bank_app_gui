total_acc = []


class Account:
    def __init__(self, name, email, mob, password):
        self.name = name
        self.email = email
        self.mob = mob
        self.balance = 0
        self.account_num = 999800 + len(total_acc)
        self.password = password
        # total_acc.append(self)
        self.message = f"Hi {self.name} Your Account {self.account_num} has Successfully Created"

    def check_balance(self, ac_num):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.message = f"Rupees {amount} has Successfully Deposited"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.message = f"Rupees {amount} has Successfully Withdrawn"

        else:
            self.message = "No Sufficient Balance"

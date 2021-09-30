class BankAccount:

    all_accounts = []
    def __init__(self, amount, int_rate = 0.0025):
        self.amount = amount
        self.int_rate = int_rate
        self.balance = 0 + amount
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= amount
        return self

    def display_account_balance(self):
        print(f"Balance: ${self.balance}")
        print(f"Checking Acccount: {User.acct['Checking']}, Balance: ${self.balance}; Savings Acccount: {User.acct['Savings']}, Balance: ${self.balance}")

    def yield_interest(self):
        self.balance *= (1 + self.int_rate)
        return self

    @classmethod
    def all_account_info(cls):
        for account in cls.all_accounts:
            print(f"Balance Information: Your balance is ${account.balance}, Your Annual Interest Rate is {account.int_rate}")

class User:

    def __init__(self, name, email, amount):
        self.name = name
        self.email = email
        self.acct = {
            "Checking" : BankAccount(amount),
            "Savings" : BankAccount(amount)
        }

    def display_user_balance(self):
        print(f"Name: {self.name}, Account: 'Checking', Balance: ${self.acct['Checking'].balance}")
        print(f"Name: {self.name}, Account: 'Savings', Balance: ${self.acct['Savings'].balance}")

    def transfer_money(self, other_user, amount):
        self.acct['Checking'].balance -= amount
        other_user.acct['Checking'].balance += amount
        self.acct['Savings'].balance -= amount
        other_user.acct['Savings'].balance += amount
        return self

User1 = User("James Bond", "jb@email.com", 1000000)
User2 = User("John Wick", "jw@email.com", 5000000)
User3 = User("Jack Ryan", "jr@email.com", 250000)

User1.acct['Savings'].deposit(500000).withdraw(250000).yield_interest()
User1.display_user_balance()

User1.transfer_money(User2, 250000)
User2.display_user_balance()